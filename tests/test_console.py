#!/usr/bin/python3
""" Module for test console """

from io import StringIO
from unittest.mock import patch
from unittest import TestCase

from console import HBNBCommand


class TestConsole(TestCase):
    """ Suite to test console """

    def test_help_command(self) -> None:
        """ Test help command """
        output = " show command \n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("help show")
            self.assertEqual(out.getvalue(), output)
        output = " create command \n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("help create")
            self.assertEqual(out.getvalue(), output)
        output = " all command \n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("help all")
            self.assertEqual(out.getvalue(), output)
        output = " update command \n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("help update")
            self.assertEqual(out.getvalue(), output)
        output = " destroy command \n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(out.getvalue(), output)
        output = " count command \n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("help count")
            self.assertEqual(out.getvalue(), output)
        output = ""
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("quit")
            self.assertEqual(out.getvalue(), output)

    def test_error_messages(self) -> None:
        """ Test error commands """
        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("show")
            self.assertEqual(out.getvalue(), output)
        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("create")
            self.assertEqual(out.getvalue(), output)
        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("update")
            self.assertEqual(out.getvalue(), output)
        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(out.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("create my_class")
            self.assertEqual(out.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("show my_class")
            self.assertEqual(out.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("destroy my_class")
            self.assertEqual(out.getvalue(), output)
        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("update my_class")
            self.assertEqual(out.getvalue(), output)
        output = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("show User")
            self.assertEqual(out.getvalue(), output)
        output = "** instance id missing **\n"
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd("update User")
            self.assertEqual(out.getvalue(), output)
