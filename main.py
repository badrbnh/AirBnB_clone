def do_all(self, line):
        """ Prints all string representation of
all instances based or not on the class name.
Ex: $ all BaseModel or $ all"""
        args = line.split()
        if not args:
            print(f"** class doesn't exist **")
            return
        class_name = args[0]
        try:
            class_ = globals()[class_name]
        except Exception:
            print(f"** class doesn't exist **")
            return
        instances = storage.all().values()
        filtered_instances = [str(inst) for inst in instances
                              if isinstance(inst, class_)]
        print(filtered_instances)