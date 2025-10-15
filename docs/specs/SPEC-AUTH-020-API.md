---
id: SPEC-AUTH-020-API
feature_id: FEAT-AUTH-020
status: Draft
last_updated: 2025-10-15
---

# Spec — QR Login API
- Endpoint: `POST /v1/auth/qr/exchange`
- Input: `device_code`, `nonce`
- Output: `access_token` (short-lived), `refresh_token` (ROTATE)
- Security: OIDC, PKCE, signed QR payload.
