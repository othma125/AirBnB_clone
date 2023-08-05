#!/usr/bin/python3
""" Module that contains class HBNBCommand """
from cmd import Cmd


class HBNBCommand(Cmd):
    """ HBNBCommand class """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ EOF command"""
        return True

    def do_quit(self, line):
        """ quit command"""
        return self.do_EOF(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
