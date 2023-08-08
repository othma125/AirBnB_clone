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
