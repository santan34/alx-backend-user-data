#!/usr/bin/env python3
"""
the auth class
"""
from flask import request
from typing import List
import fnmatch


class Auth:
    """
    class for auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require something
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded in excluded_paths:
            if fnmatch.fnmatch(
                    path, excluded) or fnmatch.fnmatch(
                    f'{path}/', excluded):
                return False
        return True

    def authorization_header(self, request=None) -> None:
        """
        authorisation header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> None:
        """
        current user
        """
        return None


if __name__ == "__main__":
    a = Auth()
    print(a.require_auth(None, None))
    print(a.require_auth(None, []))
    print(a.require_auth("/api/v1/status/", []))
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
    print(a.require_auth("/api/v1/users",
          ["/api/v1/status/", "/api/v1/stats"]))
