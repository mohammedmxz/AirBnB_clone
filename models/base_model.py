#!/usr/bin/python3
"""BaseModel module defines all common attributes/methods
for the AirBnB Project.
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel():
    """BaseModel class defines all common attributes/methods
    for the AirBnB Project.
    """
    def __init__(self, *args, **kwargs):
        """Initializes an instance of BaseModel.

        Arguments:
            *args (tuple): Receives arguments from instance initialization.
            **kwargs (dictionary): Receives arguments as key-value pairs.

        Comments:
            Creates an ID and is updated with the time and date it was created
            or updated, along with any other instance attribute.
        """
        if kwargs:
            # Added the variables because they are compulsory attributes
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for arg in kwargs:
                if arg == "created_at":
                    # Change variable name from 'value' to 'va' for brevity
                    va = datetime.strptime(kwargs[arg], '%Y-%m-%dT%H:%M:%S.%f')
                    # Change effect in setattr
                    # setattr(self, arg, va)
                    self.created_at = va
                elif arg == "updated_at":
                    # Change variable name from 'value' to 'va' for brevity
                    va = datetime.strptime(kwargs[arg], '%Y-%m-%dT%H:%M:%S.%f')
                    # Change effect in setattr
                    # setattr(self, arg, va)
                    self.updated_at = va
                elif arg != "__class__":
                    setattr(self, arg, kwargs[arg])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Official representation of a human-readable string
        for an object.

        Returns:
            String representing the object.
        """
        s_name = type(self).__name__
        s_id = self.id
        s_dict = str(self.__dict__)
        return "[{}] ({}) {}".format(s_name, s_id, s_dict)
        # Original return line below
        # return "[{}] ({}) {}".format(type(self).__name__
        # , self.id, str(self.__dict__))

    def save(self):
        """Sets updated time on the detail of the object
        Persist the date into the JSON file.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns:
            Dictionary - Representation of the Object to be
            serializable with JSON.
        """
        base_dictionary = {}
        for item in self.__dict__:
            base_dictionary[item] = self.__dict__[item]
        base_dictionary["__class__"] = type(self).__name__
        # base_dictionary["created_at"] = datetime.now().isoformat()
        base_dictionary["created_at"] = self.created_at.isoformat()
        # base_dictionary["updated_at"] = datetime.now().isoformat()
        base_dictionary["updated_at"] = self.updated_at.isoformat()
        return base_dictionary

