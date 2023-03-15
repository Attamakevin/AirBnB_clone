#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """
    command interpreter class
    """
    prompt = "(hbnb)"
    File = None
    __clases = ['BaseModel', 'User', 'Place', 'State',
                'City', 'Amenity', 'Review']

    @classmethod
    def fetch_command(cls, command):
        commands = {"all": cls.do_all, "show": cls.do_show,
                    "destroy": cls.do_destroy, "update": cls.do_update,
                    "count": cls.do_count}
        if command in commands:
            return commands[command]
        else:
            return None

    def do_quit(self, line):

        """
         to exit the program
        """
        return True

    def do_EOF(self, line):

        """
        to exit the program
        """

        return True

    def empty_line(self):

        """
        commad do nothing when empty line is entered
        """

        pass

    def help_quit(self):

        """
        command to show quit help
        """

        print("quit command to exit the progam")

    def do_create(self, line):

        """creates a new instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        token = line.split()

        try:
            newInstance = eval(token[0])()
            newInstance.save()
            print(newInstance.id)
        except(NameError):
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        token = line.split()

        if len(token) == 0:
            print("** class name missing **")
            return
        if len(token) == 1:
            print("** instance id missing **")
            return
        try:
            eval(token[0])
        except(NameError):
            print("** class doesn't exist **")

        objDict = models.storage.all()
        keyId = token[0] + "." + token[1]

        try:
            value = objDict[keyId]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):

        """Deletes an instance based on the class name"""
        token = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return
        if token[1] == 0:
            print("** instance id missing **")

        try:
            eval(token[0])
        except NameError:
            print("** class doesn't exist **")
        objDict = models.storage.all()
        keyId = token[0] + "." + token[1]

        try:
            del objDict[keyId]
        except KeyError:
            print("** no instance found **")
        models.storage.save()

    def do_all(self, line):

        """ Prints string represention of all instances of a given class """

        if not line:
            print("** class name missing **")
            return

        token = line.split()

        if token[0] not in HBNBCommand.__clases:
            print("** class doesn't exist **")
        else:
            all_objs = models.storage.all()
            newList = []

            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                if ob_name == token[0]:
                    newList += [val.__str__()]
            print(newList)

    def do_update(self, line):

        """ Updates an instance based on the class name and id """

        if not line:
            print("** class name missing **")
            return

        token = line.split()

        if token[0] not in __Clases:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == token[0] and ob_id == token[1].strip('"'):
                    if len(token) == 2:
                        print("** attribute name missing **")
                    elif len(token) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, token[2], token[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
