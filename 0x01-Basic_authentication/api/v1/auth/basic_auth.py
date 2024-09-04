#!/usr/bin/env python3
"""
the basic auth class
"""

from .auth import Auth
import base64
from typing import TypeVar

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
        
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """split the decoded string:"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not type(decoded_base64_authorization_header) == type("words"):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None 
        username, password = decoded_base64_authorization_header.split(":")
        return username, password
    

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        get user object from auth
        """
        if user_email is None or user_pwd is None:
            return None
        if type(user_email) == type(user_pwd) and type(user_pwd) != type("ji"):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]
    
def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
