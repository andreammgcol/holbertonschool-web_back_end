#!/usr/bin/env python3
""" SessionDBAuth class
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from os import getenv
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class inherits from SessionExpAuth
    """

    def create_session(self, user_id=None):
        """ that creates and stores new instance of UserSession
        """
        if user_id:
            session_id = super().create_session(user_id)
            user = UserSession(user_id=user_id, session_id=session_id)
            user.save()
            UserSession.save_to_file()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """ that returns the User ID by requesting UserSession
            in the database based on session_id
        """
        if not session_id:
            return None
        UserSession.load_from_file()
        users = UserSession.search({'session_id': session_id})
        for user in users:
            delta = timedelta(seconds=self.session_duration)
            if user.created_at + delta < datetime.now():
                return None
            return user.user_id

    def destroy_session(self, request=None):
        """ that destroys the UserSession based on the Session ID
            from the request cookie
        """
        if request:
            session_id = self.session_cookie(request)
            if not session_id:
                return False
            if not self.user_id_for_session_id(session_id):
                return False
            users = UserSession.search({'session_id': session_id})
            for user in users:
                user.remove()
                UserSession.save_to_file()
                return True
        return False
