# API endpoints
## Basic
- `api/auth/login` (POST)
  - username
  - email
  - password
  Returns token key
- `api/auth/logout` (POST)
  Calls Django logout method and deletes the Token object
  assigned to the current User object.
- `api/auth/password/reset` (POST)
  - email
  Sends uid and token for password reset.
- `api/auth/password/reset/confirm/` (POST)
  - uid
  - token
  - new_password1
  - new_password2
  Sets new password using info from reset.
- `api/auth/password/change` (POST)
  - new_password1
  - new_password2
  - old_password
  Sets new password. By default requires old one.
- `api/auth/user` (GET, PUT, PATCH)
  - username
  - first_name
  - last_name
  Returns pk, username, email, first_name, last_name
- `api/auth/token/verify` (POST)
  - token
  Returns an empty JSON object if token is valid and not expired.
- `api/auth/token/refresh` (POST)
  NOT USED (Only with JWT)
  `REST_USE_JWT = True` to use.
## Registration
- `api/auth/registration` (POST)
  - username
  - password1
  - password2
  - email
  By default email verification is no required, but email is set as not verified.
- `api/auth/registration/verify-email` (POST)
  - key
  Verifies email.
- `api/auth/registration/resend-email` (POST)
  - email
  Resends verification email.
