#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage by class"""
        if cls is None or cls == "":
            return FileStorage.__objects
        else:
            temp = {}
            for k, v in FileStorage.__objects.items():
                if cls.__name__ == k.split('.')[0]:
                    temp[k] = v
            return temp

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.engine.available_class import FileUtil

        classes = FileUtil.my_Classes
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete object from __objects f its inside"""
        if obj is None:
            return
        else:
            objKey = f"{obj.__class__.__name__}.{obj.id}"
            if objKey in FileStorage.__objects:
                del FileStorage.__objects[objKey]
                self.save()

    def close(self):
        """deserializing the JSON file to objects"""
        self.reload()
