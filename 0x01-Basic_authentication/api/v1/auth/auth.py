#!/usr/bin/env python3
"""
the auth class
"""
from flask import request
from typing import List

class Auth:
    """
    class for auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require something
        """
        return False

    def authorization_header(self, request=None) -> None:
        """
        authorisation header
        """
        return None
    
    def current_user(self, request=None) -> None:
        """
        current user
        """
        return None

if __name__ == "__main__":
    a = Auth()
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.authorization_header())
    print(a.current_user())