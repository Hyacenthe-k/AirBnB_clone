#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to JSON and deserializes to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes JSON file to __objects."""
        classes = {
            "BaseModel": BaseModel,
            "User": User
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    cls_name = v.get("__class__")
                    if cls_name in classes:
                        FileStorage.__objects[k] = classes[cls_name](**v)
        except (FileNotFoundError, IOError):
            pass
