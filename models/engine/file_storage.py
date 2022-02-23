#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from json.decoder import JSONDecodeError
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """Deletes object from storage dictionary"""
        if obj is not None:
            uid = obj.__class__.__name__ + '.' + obj.id
            FileStorage.__objects.pop(uid)
        else:
            pass

    def save(self):
        """Saves storage dictionary to file"""
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def close(self):
        """reloads the all data"""
        self.reload()
