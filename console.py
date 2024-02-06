#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

CLASSES = {
    "BaseModel": BaseModel,
    "User": User
}

"""This is the console module"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            if arg in CLASSES:
                cls = CLASSES[arg]
                instance = cls()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            if args[0] in CLASSES:
                cls = CLASSES[args[0]]
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                instances = storage.all()
                key = args[0] + "." + args[1]
                if key in instances:
                    print(instances[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            if args[0] in CLASSES:
                cls = CLASSES[args[0]]
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                instances = storage.all()
                key = args[0] + "." + args[1]
                if key in instances:
                    del instances[key]
                    storage.save()
                else:
                    print("** instance doesn't exist **")
            else:
                print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all instances"""
        args = arg.split()
        instances = storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            try:
                if args[0] in CLASSES:
                    cls = CLASSES[args[0]]
                    print([str(instance)
                           for instance in
                           instances.values() if isinstance(instance, cls)])
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            if args[0] in CLASSES:
                cls = CLASSES[args[0]]
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                instances = storage.all()
                key = args[0] + "." + args[1]
                if key in instances:
                    if len(args) < 3:
                        print("** attribute name missing **")
                        return
                    if len(args) < 4:
                        print("** value missing **")
                        return
                    instance = instances[key]
                    attr_name = args[2]
                    attr_value = args[3]
                    setattr(instance, attr_name, attr_value)
                    instance.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
