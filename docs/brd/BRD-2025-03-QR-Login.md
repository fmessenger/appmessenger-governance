---
id: BRD-2025-03-QR-Login
feature_id: FEAT-AUTH-020
spec_id: SPEC-AUTH-020-API
adr_id: ADR-010
c4_id: C4-AUTH-020
dpia_id: DPIA-003
status: Draft
last_updated: 2025-10-15
---

# BRD — QR Login
Problem: Allow desktop login by scanning a QR from a signed-in phone.

Goals:
- 95% success under 5 seconds.
- No message content stored on servers; metadata only.

Options:
- A) Keycloak OIDC device-code + QR bridge
- B) Custom QR API

Decision: A) for speed and reuse.
