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
- `api/users/password-reset` (POST)
  - email
  Sends uid and token for password reset.
- `api/users/password-reset-confirm` (POST)
  - uid
  - token
  - new_password1
  - new_password2
  Sets new password using info from reset.
- `api/user/password-change` (POST)
  - new_password1
  - new_password2
  - old_password
  Sets new password.
- `api/users/` (GET)
  Returns list of all users
- `api/users/<int:pk>` (GET, PUT, DELETE)
Returns user witch matches primary key
## Registration
- `api/auth/registration` (POST)
  - username
  - password1
  - password2
  - email
  Returns "email sent" if successful. Email verification is required
- `api/users/resend-email` (POST)
  - email
  Resends verification email.
