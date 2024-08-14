#!/usr/bin/python3
# base_mode.py

import uuid
from datetime import datetime, timezone
import models


class BaseModel():
    """ Class that defines properties of base """
    def __init__(self, *args, **kwargs):
        """ Creates new instances of Base """
        if not kwargs:
            self.id = str(uuid.uuid4())
            # datetime.utcnow() has been depracated
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = self.created_at
            '''Add the new when created object'''
            models.storage.new(self)
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                '''created_at and updated_at are strings in this dictionary,
                but inside BaseModel instance is working with datetime object.
                You have to convert these strings into datetime object.

                - Allows us to create a BaseModel from another BaseModel
                by it calling the "to_dict()" method. Eg
                bm1 = BaseModel()
                bm2 = BaseModel(**bm1.to_dict())
                '''
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns a string represation of class details.

        Returns:
            str: class details
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance.

        Returns:
            dict: key/value pairs.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
