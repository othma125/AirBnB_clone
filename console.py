#!/usr/bin/python3
""" Module that contains class HBNBCommand """
from cmd import Cmd

from models import BaseModel


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
        if all(line != key for key in models.classes_dict.keys()):
            print('** class doesn\'t exit **')
            return
        model = BaseModel()
        model.save()
        print()

    def do_show(self, line):
        """ create command"""
        if not line:
            print('** class name missing **')
            return
        class_name, identifier = line.split()
        if all(class_name != key for key in models.classes_dict.keys()):
            print('** class doesn\'t exit **')
            return
        if not identifier:
            print('** instance id missing **')
            return
        print(line)
        c: bool = True
        for key, obj in models.storage.all().items():
            name, i = key.split('.')
            if name == class_name and i == identifier:
                print(obj)
                c = False
                break
        if c:
            print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
