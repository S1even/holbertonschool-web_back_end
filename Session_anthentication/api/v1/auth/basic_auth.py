#!/usr/bin/env python3
"""
Module for Basic Authentication.
"""
import base64
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header
        for a Basic Authentication.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password.
        """
        if type(user_email) is not str or type(user_pwd) is not str:
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users or len(users) == 0:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overloads Auth and retrieves the User instance for a request.
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        b64_header = self.extract_base64_authorization_header(auth_header)
        if b64_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(b64_header)
        if decoded_header is None:
            return None

        email, password = self.extract_user_credentials(decoded_header)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
