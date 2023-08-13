#!/usr/bin/python3
import cmd
import re

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command intepreter for the application
    """
    prompt = '(hbnb) '

    def do_create(self, class_name):
        """
        Creates a new instance of a class and saves it
        and prints its id
        """
        if class_name == "":
            print("** class name missing **")
        else:
            try:
                instance = globals()[class_name]()
                print(instance.id)
                instance.save()
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based on class and id
        """
        if args == "":
            print("** class name missing **")
        else:
            args = args.split()
            name = args[0]
            if len(args) != 1:
                obj_id = args[1]
            else:
                obj_id = ""
            if name not in globals():
                print("** class doesn't exist **")
            elif obj_id == "":
                print("** instance id missing **")
            else:
                id_exists = False
                objects = storage.all()
                for key, obj in objects.items():
                    if obj_id == obj.id:
                        id_exists = True
                        print(obj)

                if id_exists is False:
                    print("** no instance found ** ")

    def do_destroy(self, args):
        """
        Deletes an instance based on class name and id
        """
        if args == "":
            print("** class name is missing **")
        else:
            args = args.split()
            name = args[0]
            if len(args) == 1:
                obj_id = ""
            else:
                obj_id = args[1]

            if name not in globals():
                print("** class doesn't exist **")
            elif obj_id == "":
                print("** instance id is missing **")
            else:
                id_exists = False
                objects = storage.all()

                for key, obj in objects.items():
                    if obj_id == obj.id:
                        id_exists = True
                        to_delete = key

                if id_exists is False:
                    print("** no instance found **")
                else:
                    del objects[to_delete]
                    storage.save()

    def do_all(self, args):
        """
        Prints all string representations of all instances
        based on or not the class name
        """
        object_list = []
        objects = storage.all()
        if args == "":
            for key, obj in objects.items():
                object_list.append(obj.__str__())
            print(object_list)
        elif args in globals():
            for key, obj in objects.items():
                class_name, obj_id = key.split('.')
                if args == class_name:
                    object_list.append(obj.__str__())
            print(object_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on class name and id
        """
        args = arg.split()

        if arg == "":
            print("** class name missing ***")
        else:
            args = arg.split()

            if args[0]:
                name = args[0]
                if name not in globals():
                    print("** class doesn't exist **")
                    return
            try:
                obj_id = args[1]
                objects = storage.all()
                id_exists = False
                for key, obj in objects.items():
                    if obj.id == obj_id:
                        id_exists = True
                        instance = obj
                if id_exists is False:
                    print("** no instance found **")
                    return
            except IndexError:
                print("** instance id missing **")
                return

            try:
                attribute_name = args[2]
            except IndexError:
                print("** attribute name missing **")
                return

            try:
                attribute_value = args[3]
            except IndexError:
                print("** value missing **")
                return

            try:
                attr_type = type(getattr(instance, attribute_name))
                # strip attribute value to remove unnecessary quotes
                attribute_value = attribute_value.strip('"')
                # cast the attribute value to its data type
                value = attr_type(attribute_value)
                setattr(instance, attribute_name, value)
            except AttributeError:
                if re.match(r'^\d+\.\d+$', attribute_value):
                    value = float(attribute_value)
                elif re.search(r'[a-zA-Z]', attribute_value):
                    value = str(attribute_value)
                elif re.search(r'\d', attribute_value):
                    value = attribute_value
                value = value.strip('"')
                setattr(instance, attribute_name, value)
            instance.save()

    def do_quit(self, arg):
        """
        Quits and exits the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exits on EOF (Ctrl+D)
        """
        print("")
        return True

    def emptyline(self):
        """
        Ignore an empty input
        """
        pass

    # custom help commands
    def help_show(self):
        """
        Help command for show method
        """
        print("Prints the string representation of an instance")
        print("Usage: show <class_name> <id>")

    def help_create(self):
        """
        Custom help command for create method
        """
        print("Creates an new instance of a class and saves it to JSON file")
        print("Usage: create <class_name>")

    def help_destroy(self):
        """
        Shows description od destroy command
        """
        print("Deletes an instance based on class name and id")
        print("Usage: destroy <class_name> <id>")

    def help_all(self):
        """
        Shows a description of all command
        """
        print("Prints all string representation based or not on class name")
        print("Usage: all / all <class_name>")

    def help_update(self):
        """
        Description of the update command
        """
        print("Updates an instance based on the class name and id")
        print('Usage: update <class name> <id> <attribute name> '
              '"<attribute value>"')

    def help_quit(self):
        """
        Custom Help guide for quit
        """
        print("Quit command to exit the program")
        print("")

    def help_EOF(self):
        """
        Custom help guide for EOF
        """
        print("Exits on EOF")
        print("Usage: ctrl+D")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
