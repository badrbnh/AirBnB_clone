#!/usr/bin/python3
""" Define Hbnb Console """
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


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
    HBNBCommand class is a simple command-line interpreter that inherits
    from cmd.Cmd. It provides a basic shell for interacting with the program.
    """

    prompt = "(hbnb) "
    _classes = {
        "BaseModel": BaseModel,
    }

    def emptyline(self):
        """
        Handles an empty line.
        This method is called when the user enters an empty line.
        Returns: True to continue the command loop.
        """
        pass

    def do_EOF(self, args):
        """
        Handles the End of File (EOF) command.
        This method is called when Ctrl+D is pressed.
        Returns: True to exit the command loop.
        """
        print(" ")
        return True

    def do_quit(self, args):
        """
        Handles the 'quit' command.
        This method is called when the user enters 'quit' in the shell.
        Returns: True to exit the command loop.
        """
        return True

    def do_create(self, args):
        """
        Create a new instance of a given class and save it to storage.
        Args:
            args (str): Class name
        """
        arg_list = parsing(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand._classes:
            print("** class doesn't exist **")
        else:
            new_inst = HBNBCommand._classes[arg_list[0]]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, args):
        """
        Display the string representation of a class instance.
        Args:
            args (str): Class name and instance ID
        """
        args_tokens = parsing(args)
        all_objects = storage.all()

        if not args_tokens:
            print("** class name missing **")
        elif args_tokens[0] not in HBNBCommand._classes:
            print("** class doesn't exist **")
        elif len(args_tokens) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(args_tokens[0], args_tokens[1])
            if instance_key in all_objects:
                print(all_objects[instance_key])
            else:
                print("** no instance found **")


if __name__ == "__main__":
    """
    This block of code is executed only when the script is run directly,
    not when it's imported as a module.
    Creates an instance of HBNBCommand and starts the command loop.
    """
    HBNBCommand().cmdloop()
