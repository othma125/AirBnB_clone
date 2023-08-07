#!/usr/bin/python3
""" Module that contains class HBNBCommand """
from cmd import Cmd


class HBNBCommand(Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command"""
        return True

    def do_quit(self, line):
        """quit command"""
        return self.do_EOF()

    def do_create(self, line):
        """create command"""
        if not line:
            print("** class name missing **")
            return
        from models import classes_dict

        if line not in classes_dict:
            print("** class doesn't exit **")
            return
        model = classes_dict[line]()
        print(model.id)

    def do_show(self, line):
        """show command"""
        if not line:
            print("** class name missing **")
            return
        print(line.split())
        # here
        line_split = line.split()
        class_name = line_split[0] if len(line_split) > 0 else None
        identifier = line_split[1] if len(line_split) > 1 else None
        
        if not class_name:
            print("** class name missing **")
            return
        
        if not identifier:
            print("** instance id missing **")
            return
        

        from models import classes_dict

        if class_name not in classes_dict:
            print("** class doesn't exit **")
            return
        
        c: bool = True
        from models import storage

        for key, my_dict in storage.all().items():
            name, i = key.split(".")
            if name == class_name and i == identifier:
                class_name = my_dict["__class__"]
                print(classes_dict[class_name](**my_dict).__str__())
                c = False
                break
        if c:
            print("** no instance found **")

    def do_destroy(self, line):
        """destroy command"""
        if not line:
            print("** class name missing **")
            return
        class_name, identifier = line.split()
        from models import classes_dict

        if all(class_name != key for key in classes_dict.keys()):
            print("** class doesn't exit **")
            return
        if not identifier:
            print("** instance id missing **")
            return
        c: bool = True
        from models import storage

        for key in storage.all().keys():
            name, i = key.split(".")
            if name == class_name and i == identifier:
                storage.all().pop(key)
                storage.save()
                c = False
                break
        if c:
            print("** no instance found **")

    def do_all(self, line):
        """all command"""
        from models import storage, classes_dict

        res = []
        if line:
            (class_name,) = line.split()
            if all(class_name != key for key in classes_dict.keys()):
                print("** class doesn't exit **")
                return
            for key, my_dict in storage.all().items():
                (name,) = key.split(".")
                if name == class_name:
                    res.append(classes_dict[class_name](**my_dict).__str__())
        else:
            for my_dict in storage.all().values():
                class_name = my_dict["__class__"]
                res.append(classes_dict[class_name](**my_dict).__str__())
        print(res)

    def do_update(self, line):
        """update command"""
        if not line:
            print("** class name missing **")
            return
        class_name, identifier, att_name, value = line.split()
        from models import classes_dict

        if all(class_name != key for key in classes_dict.keys()):
            print("** class doesn't exit **")
            return
        if not identifier:
            print("** instance id missing **")
            return
        if not att_name:
            print("** attribute name missing **")
            return
        if not value:
            print("** value missing **")
            return
        c: bool = True
        value = value.stri
        from models import storage

        for key, my_dict in storage.all().items():
            name, i = key.split(".")
            if name == class_name and i == identifier:
                obj = classes_dict[class_name](**my_dict)
                setattr(obj, att_name, value.strip('"'))
                obj.save()
                c = False
                break
        if c:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
