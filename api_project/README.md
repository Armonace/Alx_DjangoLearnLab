Authentication: Token-based via rest_framework.authentication.TokenAuthentication

Token login: Send POST to /api-token-auth/ with username & password

Permissions: Default is IsAuthenticated, ensuring only logged-in users can access resources