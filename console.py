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
        from models import classes_dict
        if all(line != key for key in classes_dict.keys()):
            print('** class doesn\'t exit **')
            return
        model = BaseModel()
        model.save()
        print(model.id)

    def do_show(self, line):
        """ show command"""
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

    def do_destroy(self, line):
        """ destroy command"""
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
        c: bool = True
        from models import storage
        for key in storage.all().keys():
            name, i = key.split('.')
            if name == class_name and i == identifier:
                storage.all().pop(key)
                storage.save()
                c = False
                break
        if c:
            print('** no instance found **')

    def do_all(self, line):
        """ all command"""
        from models import storage
        res = []
        if line:
            class_name, = line.split()
            from models import classes_dict
            if all(class_name != key for key in classes_dict.keys()):
                print('** class doesn\'t exit **')
                return
            for key, obj in storage.all().values():
                name, = key.split()
                if name == class_name:
                    res.append(str(obj))
        else:
            for obj in storage.all().values():
                res.append(str(obj))
        print(res)

    def do_update(self, line):
        """ update command"""
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
