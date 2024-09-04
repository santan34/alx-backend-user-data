#!/usr/bin/env python3
"""
the auth class
"""
from flask import request

class Auth:
   '''
   i dont know for 
   ''' 
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require something
        """
        returns False

    def authorization_header(self, request=None) -> str:
        """
        authorisation header
        """
        returns None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user
        """
        returns None

if __neme__ == "__main__":
    a = Auth()
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.authorization_header())
    print(a.current_user())