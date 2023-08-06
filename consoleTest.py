#!/usr/bin/python3
""" Module that contains class HBNBCommand """
from cmd import Cmd

from models import BaseModel
from typing import Callable


class HBNBCommand(Cmd):
    """ HBNBCommand class """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ EOF command"""
        return True

    def do_quit(self, line):
        """ quit command"""
        return self.do_EOF(line)

    def do_create(self, line):
        """ create command"""
        if not line:
            print('** class name missing **')
            return
        from models import classes_dict
        if all(line != key for key in classes_dict.keys()):
            print('** class doesn\'t exit **')
            return
        model = BaseModel()
        model.save()
        print(model.id)

    def do_show(self, line):
        """ create command"""
        if not line:
            print('** class name missing **')
            return
        class_name, identifier = line.split()
        from models import classes_dict
        if all(class_name != key for key in classes_dict.keys()):
            print('** class doesn\'t exit **')
            return
        if not identifier:
            print('** instance id missing **')
            return
        print(line)
        c: bool = True
        from models import storage
        for key, obj in storage.all().items():
            name, i = key.split('.')
            if name == class_name and i == identifier:
                print(obj)
                c = False
                break
        if c:
            print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
