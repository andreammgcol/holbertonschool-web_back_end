#!/usr/bin/env python3
"""
Create a class SessionAuth
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """SessionAuth class that inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method that creates a Session ID for a user_id
        """
        if isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """method that returns a User ID based on a Session ID
        """
        if isinstance(session_id, str):
            return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """method that returns a User instance based on a cookie value
        """
        user = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user)

    def destroy_session(self, request=None):
        """method that deletes the user session/logout
        """
        if request:
            session_id = self.session_cookie(request)
            if not session_id:
                return False
            if not self.user_id_for_session_id(session_id):
                return False
            self.user_id_by_session_id.pop(session_id)
            return True
