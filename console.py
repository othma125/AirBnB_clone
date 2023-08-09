#!/usr/bin/python3
""" Module that contains class HBNBCommand """
from cmd import Cmd
from json import loads
from re import fullmatch, search


def extract_args(string: str):
    """ handle command that contains dictionary format """
    match = search(r'\((.*?)\)', string)
    if not match:
        return []
    args = match.group(1)
    # If there's a '{', extract everything between '{' and '}'
    if '{' in args:
        curly_braces_content = search(r'\{(.*?)\}', args)
        if curly_braces_content:
            args = args.replace(curly_braces_content.group(0), '').split(',')
            args = [arg.strip() for arg in args if arg.strip()]
            args.append(curly_braces_content.group(0))
        else:
            args = args.split(',')
    else:
        args = args.split(',')
    return [arg.strip() for arg in args if arg.strip()]


class HBNBCommand(Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    # def precmd(self, line):
    #     print(line)
    #     return Cmd.precmd(self, line)

    def do_EOF(self, line):
        """EOF command"""
        return True

    def do_quit(self, line):
        """ quit command """
        return True

    def do_exit(self, line):
        """ exit command """
        return True

    def emptyline(self):
        """Ignore empty line"""
        pass

    def do_create(self, line):
        """ create command """
        if not line:
            print("** class name missing **")
            return
        from models import classes_dict
        if line not in classes_dict:
            print("** class doesn't exist **")
            return
        model = classes_dict[line]()
        model.save()
        print(model.id)

    def do_show(self, line):
        """ show command """
        if not line:
            print("** class name missing **")
            return
        line_split = line.split()
        class_name = line_split[0] if len(line_split) > 0 else None
        identifier = line_split[1] if len(line_split) > 1 else None
        if not class_name:
            print("** class name missing **")
            return
        from models import classes_dict
        if all(class_name != key for key in classes_dict.keys()):
            print("** class doesn't exist **")
            return
        if not identifier:
            print("** instance id missing **")
            return
        c: bool = True
        from models import storage
        for my_dict in storage.all().values():
            if my_dict['__class__'] == class_name \
                    and my_dict['id'] == identifier.strip("'\""):
                class_name = my_dict["__class__"]
                obj = classes_dict[class_name](**my_dict)
                print(str(obj))
                c = False
                break
        if c:
            print("** no instance found **")

    def do_all(self, line):
        """ all command """
        from models import storage, classes_dict
        res = []
        if line:
            line = line.split()[0]
            if all(line != key for key in classes_dict.keys()):
                print("** class doesn't exist **")
                return
            for key, my_dict in storage.all().items():
                class_name, _ = key.split('.')
                if my_dict['__class__'] == line:
                    obj = classes_dict[line](**my_dict)
                    res.append(str(obj))
        else:
            for key, my_dict in storage.all().items():
                class_name, _ = key.split('.')
                obj = classes_dict[class_name](**my_dict)
                res.append(str(obj))
        print(res)

    def do_destroy(self, line):
        """ destroy command """
        if not line:
            print("** class name missing **")
            return
        line_split = line.split()
        class_name = line_split[0] if len(line_split) > 0 else None
        identifier = line_split[1] if len(line_split) > 1 else None
        from models import classes_dict
        if all(class_name != key for key in classes_dict.keys()):
            print("** class doesn't exist **")
            return
        if not identifier:
            print("** instance id missing **")
            return
        c: bool = True
        from models import storage
        for key, my_dict in storage.all().items():
            if my_dict['__class__'] == class_name \
                    and my_dict['id'] == identifier.strip("'\""):
                storage.all().pop(key)
                storage.save()
                c = False
                break
        if c:
            print("** no instance found **")

    def do_update(self, line):
        """ update command """
        if not line:
            print("** class name missing **")
            return
        line_split = line.split()
        n: int = len(line_split)
        class_name = line_split[0] if n > 0 else None
        from models import classes_dict
        if all(class_name != key for key in classes_dict.keys()):
            print("** class doesn't exist **")
            return
        identifier = line_split[1] if n > 1 else None
        if not identifier:
            print("** instance id missing **")
            return
        if n > 3:
            att_name = line_split[2]
            value = line_split[3]
            if not att_name:
                print("** attribute name missing **")
                return
            if not value:
                print("** value missing **")
                return
            c: bool = True
            from models import storage
            for key, my_dict in storage.all().items():
                name, i = key.split(".")
                if name == class_name and i == identifier.strip('\'"'):
                    obj = classes_dict[class_name](**my_dict)
                    setattr(obj, att_name.strip('\'"'), value.strip('\'"'))
                    obj.save()
                    c = False
                    break
            if c:
                print("** no instance found **")
        else:
            try:
                dct: dict = loads(line_split[2])
            except ValueError:
                print("** value missing **")
            else:
                c: bool = True
                from models import storage
                for key, my_dict in storage.all().items():
                    name, i = key.split(".")
                    if name == class_name and i == identifier.strip('\'"'):
                        obj = classes_dict[class_name](**my_dict)
                        for att_name, value in dct.items():
                            setattr(obj, att_name.strip('\'"'), value.strip('\'"'))
                        obj.save()
                        c = False
                        break
                if c:
                    print("** no instance found **")

    def do_count(self, line):
        """ count command """
        from models import storage, classes_dict
        count = 0
        if line:
            line = line.split()[0]
            if all(line != key for key in classes_dict.keys()):
                print("** class doesn't exit **")
                return
            for key, my_dict in storage.all().items():
                class_name, _ = key.split('.')
                if my_dict['__class__'] == line:
                    count += 1
        else:
            count = len(storage.all())
        print(count)

    def default(self, line):
        """
        handle invalid commands and
        special commands like <class name>.<command>()
        """
        match = fullmatch(r"[A-Za-z]+\.[A-Za-z]+\(.*?\)", line)
        if match:
            split_line = line.split('.')
            from models import classes_dict
            if any(split_line[0] == key for key in classes_dict.keys()):
                parsed = split_line[1].split("(")
                parsed[1] = parsed[1].strip(")")
                args = parsed[1].split(",")
                args = [arg.strip() for arg in args]
                if len(args) >= 3:
                    temp = args[2]
                    args = [arg.strip('"') for arg in args[:2]]
                    args.append(temp)
                else:
                    args = [arg.strip('"') for arg in args]
                commands = {"all": HBNBCommand.do_all,
                            "show": HBNBCommand.do_show,
                            "destroy": HBNBCommand.do_destroy,
                            "update": HBNBCommand.do_update,
                            "count": HBNBCommand.do_count}
                c: bool = True
                for key, command in commands.items():
                    if key == parsed[0]:
                        if key == 'update':
                            reconstructed_args = extract_args(split_line[1])
                            print(reconstructed_args)
                        else:
                            reconstructed_args = args.copy()
                        reconstructed_args.insert(0, split_line[0])
                        command(self, " ".join(reconstructed_args))
                        c = False
                        break
                if c:
                    print(f"*** Unknown syntax: {line}")
            else:
                print("** class doesn't exist **")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
