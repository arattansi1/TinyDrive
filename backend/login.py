from urllib import request
import jwt
from social_core.backends.oauth import BaseOAuth2


class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('picture', 'picture')
    ]

    def authorization_url(self):
        return 'https://' + self.setting('DOMAIN') + '/authorize'

    def access_token_url(self):
        return 'https://' + self.setting('DOMAIN') + '/oauth/token'

    def get_user_id(self, details, response):
        """Return current user id."""
        return details['username']

    def get_user_details(self, response):
        # Obtain JWT and the keys to validate the signature
        id_token = response.get('id_token')
        issuer = 'https://' + self.setting('DOMAIN') + '/'
        audience = self.setting('KEY')  # CLIENT_ID

        payload = jwt.decode(id_token, self.setting('SOCIAL_AUTH_AUTH0_SECRET'), algorithms=['HS256'], audience=audience, issuer=issuer)
        first_name = payload.pop('name', None)
        payload['first_name'] = payload.pop('given_name', first_name)
        payload['last_name'] = payload.pop('family_name', None)
        payload['username'] = payload.pop('sub')

        return payload

