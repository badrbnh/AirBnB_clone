#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import cmd
import re
from shlex import split

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def parser(arg):
        brack = re.search(r"\[(.*?)/]", arg)
        c_braces = re.search(r"\{(.*?\}", arg)

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

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Ctrl-D command to exit the program"""
        print("")
        return True
    
    def emptyline(self):
       
        pass
    
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
Ex: $ create BaseModel"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance_class =  globals()[args[0]]
            new_instance = new_instance_class()
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")
            return
    
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return 
        class_name = args[0] 
        try:
            class_ = globals()[class_name]
        except:
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
        except:
            pass
 
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
Ex: $ destroy BaseModel 1234-1234-1234."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return 
        class_name = args[0] 
        try:
            class_ = globals()[class_name]
        except:
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
            else:
                data = storage.all()
                del data[key]
                storage.save()
        except:
            pass
               
    def do_all(self, line):
        """Prints all string representation of instances."""
        args = line.split()
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
        filtered_instances = [str(inst) for inst in instances if isinstance(inst, class_)]
        print(filtered_instances)


        
    
    
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()