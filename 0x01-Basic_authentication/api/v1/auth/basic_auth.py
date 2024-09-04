#!/usr/bin/env python3
"""
the basic auth class
"""

from .auth import Auth

class BasicAuth(Auth):
    """
    class for basic auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        get the base64 header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != type("abab"):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.replace('Basic ', '')

if __name__ == "__main__":
    a = BasicAuth()
    print(a.extract_base64_authorization_header(None))
    print(a.extract_base64_authorization_header(89))
    print(a.extract_base64_authorization_header("Holberton School"))
    print(a.extract_base64_authorization_header("Basic Holberton"))
    print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
    print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
    print(a.extract_base64_authorization_header("Basic1234"))


    
    