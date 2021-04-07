#!/usr/bin/env python3
""" SessionExpAuth class
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ class SessionExpAuth that inherits from SessionAuth
    """

    def __init__(self):
        """Initialize
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Session ID by calling super()
        """
        session_id = super().create_session(user_id)
        if session_id:
            SessionAuth.user_id_by_session_id[session_id] = {
                'user_id': user_id, 'created_at': datetime.now()}
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """ that return user_id from the session dictionary
        """
        if not session_id:
            return None
        dictionary = SessionExpAuth.user_id_by_session_id.get(session_id)
        if not dictionary:
            return None
        if self.session_duration <= 0:
            return dictionary['user_id']
        if 'created_at' not in dictionary:
            return None
        delta = timedelta(seconds=self.session_duration)
        if dictionary['created_at'] + delta < datetime.now():
            return None
        return dictionary['user_id']
