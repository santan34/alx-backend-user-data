#!/usr/bin/env python3
"""create a model in sqlalchemy"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

base = declarative_base()


class User(base):
    """
    creates a table tablename 'users'
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
