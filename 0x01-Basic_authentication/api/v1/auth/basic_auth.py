#!/usr/bin/env python3
"""
the basic auth class
"""

from .auth import Auth
import base64

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
        
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        decode a base6 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != type("abab"):
            return None
        try:
            res = base64.b64decode(base64_authorization_header)
            return res.decode('utf-8')
        except:
            return None
