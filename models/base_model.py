#!/usr/bin/python3

"""
class base model is the building block from which other class inherits
"""

from uuid import uuid4
from datetime import datetime
import models
from models import storage


class BaseModel:

    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):

        """
        initializes the base model
        """
        dateTime = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(kwargs[key], dateTime)
                    setattr(self, key, val)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):

        """
        string representation of the class attribute
        """
        clsname = self.__class__.__name__

        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):

        """
        method to update class instance
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):

        """
        Method to return dictionary.
        """
        name = self.__class__.__name__
        New_dict = self.__dict__.copy()
        New_dict.update(__class__=name, created_at=self.created_at.isoformat())
        New_dict.update(updated_at=self.updated_at.isoformat())

        return New_dict
