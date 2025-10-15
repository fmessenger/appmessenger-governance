#!/usr/bin/env python3
import csv, sys, re, os, json

SCHEMA = ["Epic_ID","Use_Case_ID","Feature_ID","Spec_ID","ADR_ID","C4_ID","DPIA_ID","Status","Priority","Phase","Sprint","Build_Order","Owner","Risk_Level","Decision_Summary","Last_Updated","Comments","DPIA_Status","External_Compliance","KPI","Acceptance_Criteria","Monetization_Tag","Tags","Domain","Data_Type","Infra_Cost_Class"]

strict = os.environ.get("STRICT","0") == "1"
backlog_path = "backlog/backlog.csv"
errors = []
warnings = []

def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)

# Header check
with open(backlog_path,newline="") as f:
    r = csv.reader(f)
    header = next(r)
    if header != SCHEMA:
        err(f"Header order mismatch. Expected 26 columns: {SCHEMA}")

    rows = list(r)

if not rows:
    warn("Backlog has no rows.")

# Row checks
for i,row in enumerate(rows, start=2):
    rec = dict(zip(SCHEMA,row + [""]*(len(SCHEMA)-len(row))))
    ctx = f"row {i} ({rec.get('Feature_ID','?')})"

    # Required chain
    if not rec["Feature_ID"]: err(f"{ctx}: Feature_ID is required")
    if not rec["Spec_ID"]: err(f"{ctx}: Spec_ID is required")
    if not rec["Epic_ID"]: warn(f"{ctx}: Epic_ID missing")
    if not rec["Use_Case_ID"]: warn(f"{ctx}: Use_Case_ID missing")

    # DPIA gate
    domain = (rec["Domain"] or "").lower()
    dtype = (rec["Data_Type"] or "").lower()
    touches_personal = any(k in domain for k in ["auth","person","identity","user"]) or any(k in dtype for k in ["personal","usage","identifier","location"])
    if touches_personal:
        if not rec["DPIA_ID"]:
            (err if strict else warn)(f"{ctx}: DPIA_ID required for personal/usage data features")
        if (rec["DPIA_Status"] or "").lower() != "approved":
            (err if strict else warn)(f"{ctx}: DPIA_Status must be Approved for personal/usage data features")

    # Priority validity
    if rec["Priority"] and rec["Priority"] not in {"P0","P1","P2","P3"}:
        warn(f"{ctx}: Priority should be one of P0/P1/P2/P3")

state = "fail" if errors else "pass"
report = {"state": state, "errors": errors, "warnings": warnings}
print(json.dumps(report, indent=2))

if errors:
    sys.exit(1)
