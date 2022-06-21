# API endpoints
## Basic
- `api/users/login` (POST)
  - username
  - email
  - password
  Returns token key
- `api/users/logout` (POST)
  Calls Django logout method and deletes the Token object
  assigned to the current User object.
- `api/users/password/reset` (POST)  (NOT IMPLEMENTED)
  - email
  Sends uid and token for password reset.
- `api/users/password/reset/confirm/` (POST) (NOT IMPLEMENTED)
  - uid
  - token
  - new_password1
  - new_password2
  Sets new password using info from reset.
- `api/auth/password/change` (POST) (NOT IMPLEMENTED)
  - new_password1
  - new_password2
  - old_password
  Sets new password.
- `api/users/` (GET)
  Returns list of all users
- `api/users/<int:pk>` (GET, PUT, DELETE)
Returns user witch matches primary key
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
- `api/users/resend-email` (POST)
  - email
  Resends verification email.
