#!/usr/bin/python3
'''
    Define class DBStorage
'''
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
#from models import classes
import models


class DBStorage:
    '''
        Links the MySQL database
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            Initializes the database storage engine
        '''
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, host, db), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''
            Returns dictionary of all of type class or all of all types if cls == None
                key = <class-name>.<object-id>
                value = object
        '''
        result = {}
        if cls != None:
            for instance in __session.query(cls):
                key = "{}.{}".(cls, instance.id)
                result[key] = instance
        else:
            for c in models.classes: 

    def new(self, obj):
        '''
            Add obj to current database session
        '''

    def save(self):
        '''
            Commits all changes to the current database session
        '''

    def delete(self, obj=None):
        '''
            Deletes obj from current database session if obj != None
        '''

    def reload(self):
        '''
            Creates all tables in database and creates session
        '''
        Base.metadata.create_all(engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
            expire_on_commit=False))
        __session = Session()
