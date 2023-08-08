# AirBnB Clone
The goal of this project is to deploy on a server a simple copy of the [AirBnB website](https://www.airbnb.com/)
The complete web application is composed by:
- A command intepreter to manipulate data without a visual interface.
- A website (front-end) that shows the final product.
- A database or files that store data
- An API that provides communication interface between the front-end and your data

## Command Interpreter

This is the same as a Shell command line but limited to a specific use. In our case it should be able to manage the objects of our projects by:
- Create a new object i.e a new User or a new Place.
- Retrieve an object from a file, a database...
- Do operations on objects
- Update attributes of an object
- Destroy an object

## Usage
### In interactive mode

```bash
$ ./console.py
(hbnd) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnd)
(hbnd) quit
$
```

### In non interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
