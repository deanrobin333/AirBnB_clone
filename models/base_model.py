#!/usr/bin/python3
"""Defines a class BaseModel"""
import uuid
from datetime import datetime
import string


class BaseModel:
    """ Class that defines properties of base """
    models = []
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string represation of class details."""
        return f'BaseModel({self.id}, {self.__dict__})'

    def save(self):
        """Update public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.datetime.now()
        self.created_at = self.created_at
        BaseModel.models.append(self)

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance."""
        model_dict = {
            "id": self.id,
            "time created": self.created_at.isoformat(),
            "time updated": self.updated_at.isoformat()
        }

        return model_dict
