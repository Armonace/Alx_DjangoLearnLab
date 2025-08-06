
# Django Role-Based Access Control

## Groups and Permissions Setup

### Groups:
- **Viewers**: can view articles.
- **Editors**: can view, create, and edit articles.
- **Admins**: full control (view, create, edit, delete).

### Custom Permissions:
Defined in `Article` model:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

### Testing Permissions:
- Use Django Admin to create users and assign them to groups.
- Login as each user and test if views are restricted based on their permissions.
- Protected views use `@permission_required` decorators.

# LibraryProject - Security Setup

## Security Measures Implemented

- **DEBUG=False**: Prevents sensitive error details from leaking.
- **Cookie Security**: Ensures CSRF and session cookies are only sent via HTTPS.
- **XSS & Content Type Protections**: Uses security headers to block malicious scripts.
- **CSRF Protection**: All forms include `{% csrf_token %}`.
- **SQL Injection Prevention**: Queries use Django ORM; no raw SQL.
- **Content Security Policy (CSP)**: Configured to only allow scripts/styles from same origin.
- **X-Frame-Options**: Prevents clickjacking by blocking iframe embedding.

## Testing

- Tested forms to confirm CSRF tokens are present.
- Input fields validated to reject script injections.
- Database queries checked for safe use of parameters.
