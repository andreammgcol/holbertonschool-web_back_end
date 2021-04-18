#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User

k_words = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']


class DB:
    """DB class
    """

    def __init__(self):
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save the user to the database
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """That returns the first row found in the users table
        """
        user = self._session.query(User).filter_by(**kwargs).first()

        for i in kwargs.keys():
            if i not in k_words:
                raise InvalidRequestError

        if user:
            return user
        else:
            raise NoResultFound
            

    def update_user(self, user_id: int, **kwargs) -> None:
        """That takes as argument a required user_id integer
            and arbitrary keyword arguments, and returns None
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if key in k_words:
                setattr(user, key, value)
            else:
                raise ValueError
        self._session.commit()
