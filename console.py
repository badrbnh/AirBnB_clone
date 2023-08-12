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
from models.base_model import BaseModel
from models import storage
import cmd
import re
from shlex import split

def parsing(arg):
    brack = re.search(r"\[(.*?)\]", arg)
    c_braces = re.search(r"\{(.*?)\}", arg)

    if c_braces is None:
        if brack is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[: brack.span()[0]])
            reslist = [i.strip(",") for i in lex]
            reslist.append(brack.group())
            return reslist
    else:
        lex = split(arg[: c_braces.span()[0]])
        reslist = [i.strip(",") for i in lex]
        reslist.append(c_braces.group())
        return reslist

class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class for the AirBnB clone project.
    """

    prompt = "(hbnb) "

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
        args = parsing(line)
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
        args = parsing(line)
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
        args = parsing(line)
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
        """ Prints all string representation of
all instances based or not on the class name.
Ex: $ all BaseModel or $ all"""
        args = parsing(line)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            class_ = globals()[class_name]
        except KeyError:
            print(f"** class doesn't exist **")
            return
        instances = storage.all().values()
        filtered_instances = [str(inst) for inst in instances
                              if isinstance(inst, class_)]
        print(filtered_instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id
by adding or updating attribute (save the change into the JSON file).
Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
        args = parsing(line)
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
                    atte_value = ''.join(args[3]).strip('""')
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


if __name__ == '__main__':
    """
    This block of code is executed only when the script is run directly,
    not when it's imported as a module.
    Creates an instance of HBNBCommand and starts the command loop.
    """
    HBNBCommand().cmdloop()