
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

