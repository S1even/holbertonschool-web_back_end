#!/usr/bin/env python3
"""
Module to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template class for all authentication systems.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Now supports '*' at the end of excluded paths.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path_with_slash = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:

            if excluded_path.endswith('*'):

                prefix = excluded_path[:-1]

                if path.startswith(prefix):
                    return False

            elif path_with_slash == excluded_path or path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request.
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user from a request.
        """
        return None
