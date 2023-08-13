import uuid
import os
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.city import City
import console


class TestConsole(unittest.TestCase):
    def setUp(self):
        """ Create file at the beginning of every test"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Delete created file after every test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_module_doc(self):
        """ Test for module documentation"""
        self.assertIsNotNone(console.__doc__)

    def test_class_doc(self):
        """ Test for class documentation"""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_method_docs(self):
        """Test all methods in ``console`` for docs"""
        methods = [
            HBNBCommand.do_EOF,
            HBNBCommand.do_quit,
            HBNBCommand.do_create,
            HBNBCommand.do_show,
            HBNBCommand.do_destroy,
            HBNBCommand.do_all,
            HBNBCommand.do_update,
            HBNBCommand.default,
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def test_quit(self):
        """ Test quit method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        """ Test EOF method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_empty_line(self):
        """ Test empty_line method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_help_create(self):
        """ Test help_create method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_show(self):
        """ Test help_show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_destroy(self):
        """ Test help_destroy method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_all(self):
        """ Test help_all method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_update(self):
        """ Test help_update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_create_with_valid_class_name_BaseModel(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_User(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Place(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_State(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_City(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Amenity(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Review(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_without_class_name(self):
        """ Test create without class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_with_invalid_class_name(self):
        """ Test create with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_with_valid_class_and_id(self):
        """ Test show with valid class and id"""
        test_inst = User()
        test_inst.save()
        cmd = f"show User {test_inst.id}"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst.id})", output)
            self.assertIn("created_at", output)
            self.assertIn("updated_at", output)
            self.assertIn("id", output)
            self.assertNotIn("__class__", output)
            self.assertFalse(output.startswith('["'))
            self.assertFalse(output.endswith('"]'))

    def test_show_without_class_name(self):
        """ Test show without class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_with_invalid_class_name(self):
        """ Test show with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_without_instance_id(self):
        """ Test show without instance id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_with_invalid_instance_id(self):
        """ Test show with invalid instance id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_valid_class_and_id(self):
        """ Test destroy with valid class and id"""
        test_inst = User()
        test_inst.save()
        cmd = f"destroy User {test_inst.id}"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            HBNBCommand().onecmd(f"show User {test_inst.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_missing_class_name(self):
        """ Test destroy with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_with_nonexistent_class(self):
        """ Test destroy with nonexistent class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_with_missing_id(self):
        """ Test destroy with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_with_nonexistent_instance(self):
        """ Test destroy with nonexistent instance"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all_with_valid_class(self):
        """ Test ``all`` with valid class"""
        test_inst1 = User()
        test_inst1.save()
        test_inst2 = User()
        test_inst2.save()
        test_inst3 = City()
        test_inst2.save()
        test_inst4 = Place()
        test_inst4.save()
        test_inst5 = Place()
        test_inst5.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst1.id})", output)
            self.assertIn(f"[User] ({test_inst2.id})", output)
            self.assertNotIn(f"[Place]", output)
            self.assertNotIn(f"[Basemodel]", output)
            self.assertNotIn(f"[City]", output)
            self.assertTrue(output.startswith('["'))
            self.assertTrue(output.endswith('"]'))

    def test_all_with_noexistent_class(self):
        """ Test ``all`` with noexistent class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_with_class(self):
        """ Test ``update`` with a class"""
        test_inst = User()
        test_inst.save()
        cmd = f"update User {test_inst.id} __class__ 'not allowed'"
        self.assertNotEqual(test_inst.__class__, "not allowed")

    def test_update_with_missing_class_name(self):
        """ Test ``update`` with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_with_nonexistent_class(self):
        """ Test ``update`` with invalid class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_with_missing_id(self):
        """ Test ``update`` with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_with_missing_attribute_name(self):
        """ Test ``update`` with attribut name"""
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {test_inst.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_update_with_missing_attribute_value(self):
        """ Test ``update`` with attribut value"""
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {test_inst.id} name")
            output = f.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_update_with_many_input(self):
        """ Test ``update`` multiple input"""
        test_inst = User()
        test_inst.save()
        cmd1 = f"update User {test_inst.id} name 'malibu smith' "
        cmd2 = f"age 30 height 1.7"
        HBNBCommand().onecmd(cmd1 + cmd2)
        self.assertFalse(hasattr(test_inst, "age"))
        self.assertFalse(hasattr(test_inst, "height"))

    def test_all_with_valid_class2(self):
        """ Test ``all`` with valid class"""
        test_inst1 = User()
        test_inst1.save()
        test_inst2 = User()
        test_inst2.save()
        test_inst3 = City()
        test_inst2.save()
        test_inst4 = Place()
        test_inst4.save()
        test_inst5 = Place()
        test_inst5.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst1.id})", output)
            self.assertIn(f"[User] ({test_inst2.id})", output)
            self.assertNotIn(f"[Place]", output)
            self.assertNotIn(f"[Basemodel]", output)
            self.assertNotIn(f"[City]", output)
            self.assertTrue(output.startswith('["'))
            self.assertTrue(output.endswith('"]'))

    def test_all_with_empty_class2(self):
        """ Test ``all`` with empty class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_all_with_noexistent_class2(self):
        """ Test ``all`` with invalid class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.all()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_count_with_nonexistent_class(self):
        """ Test ``count`` with invalid class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_count_with_valid_class(self):
        """ Test ``count`` with valid class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "0")

    def test_count_with_valid_class1(self):
        """ Test ``count`` with valid class"""
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

    def test_count_with_valid_class2(self):
        """ Test ``count`` with valid class"""
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "0")

    def test_count_with_valid_class3(self):
        """ Test ``count`` with valid class"""
        test_inst = User()
        test_inst.save()
        test_inst = Place()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

    def test_show_with_valid_class_and_id2(self):
        """ Test ``show`` with valid class and id"""
        test_inst = User()
        test_inst.save()
        cmd = f"User.show({test_inst.id})"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst.id})", output)
            self.assertIn("created_at", output)
            self.assertIn("updated_at", output)
            self.assertIn("id", output)
            self.assertNotIn("__class__", output)
            self.assertFalse(output.startswith('["'))
            self.assertFalse(output.endswith('"]'))

    def test_show_with_invalid_class_name2(self):
        """ Test ``show`` with invalid class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_without_instance_id2(self):
        """ Test ``show`` without id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_with_invalid_instance_id2(self):
        """ Test ``show`` with invalid id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(121212)")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_valid_class_and_id2(self):
        """ Test ``destroy`` with valid class and id"""
        test_inst = User()
        test_inst.save()
        cmd = f"User.destroy({test_inst.id})"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            HBNBCommand().onecmd(f"show User {test_inst.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_nonexistent_class2(self):
        """ Test ``destory`` with invalid class"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_with_missing_id2(self):
        """ Test ``destroy`` with missing id"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_with_nonexistent_instance2(self):
        """ Test ``destory`` with invalid instance"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(121212)")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
