#!/usr/bin/python3
"""
console.py

This module contains the entry point of
the command interpreter for the AirBnB clone project.
The HBNBCommand class defines the command interpreter,
which allows users to interact with the project's objects.

Usage:
python3 console.py

"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
from models.place import Place
from models.review import Review
import re
from models.state import State
from models import storage
from shlex import split
from models.user import User


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[: brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[: curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class for the AirBnB clone project.
    """

    prompt = "(hbnb) "

    def default(self, line):
        """ default behaviour for cmd module when input """
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", line)
        if match is not None:
            arg_list = [line[:match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                cmd = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if cmd[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], cmd[1])
                    return arg_dict[cmd[0]](call)
        print("*** Unknown syntax: {}".format(line))

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctrl-D command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Handles the emptylines."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance_class = globals()[args[0]]
            new_instance = new_instance_class()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_ = globals()[class_name]
        except Exception:
            print(f"** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        try:
            data = storage.all().get(key)
            if data is None:
                print("** no instance found **")
            else:
                print(data)
        except Exception:
            pass

    def do_destroy(self, line):
        """Deletes an instance based on
        the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_ = globals()[class_name]
        except Exception:
            print(f"** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        try:
            data_key = storage.all().get(key)
            if data_key is None:
                print("** no instance found **")
                return
            else:
                data = storage.all()
                del data[key]
                storage.save()
        except Exception:
            pass

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = parse(line)

        if len(args) > 0:
            class_name = args[0]
            try:
                class_ = globals()[class_name]
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            class_name = None

        objl = []

        for obj in storage.all().values():
            if class_name is None or isinstance(obj, class_):
                objl.append(obj.__str__())

        print(objl)

    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = parse(line)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
        args = parse(line)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_ = globals()[class_name]
        except Exception:
            print(f"** class doesn't exist **")
            return
        if len(args) > 1:
            key = f"{class_name}.{args[1]}"
            all_objs = storage.all()

            if key not in all_objs:
                print("** no instance found **")
                return
            obj = all_objs[key]
            if len(args) > 2:
                if len(args) > 3:
                    attr_name = args[2]
                    atte_value = "".join(args[3]).strip('""')
                    setattr(obj, attr_name, atte_value)
                    obj.save()
                else:
                    print("** value missing **")
                    return
            else:
                print("** attribute name missing **")
                return
        else:
            print("** instance id missing **")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
