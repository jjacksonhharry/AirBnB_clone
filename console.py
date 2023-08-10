#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel


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

    def do_quit(self, arg):
        """
        Quits and exits the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exits on EOF (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """
        Ignore an empty input
        """
        pass

    # custom help commands
    def help_create(self):
        """
        Custom help command for create method
        """
        print("Creates an new instance of a class and saves it to JSON file")
        print("Usage: <create class_name>")

    def help_quit(self):
        """
        Custom Help guide for quit
        """
        print("Quits and exits the program")

    def help_EOF(self):
        """
        Custom help guide for EOF
        """
        print("Exits on EOF")
        print("Usage: ctrl+D")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
