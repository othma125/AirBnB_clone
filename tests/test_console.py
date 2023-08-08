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
