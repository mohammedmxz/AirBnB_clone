# AirBnB Clone Project

## Description of the Project

This project is a simplified clone of the AirBnB platform, focusing on creating a command-line interface (CLI) for managing and interacting with various objects like Users, Places, Reviews, and more. The primary goal is to build a robust and functional command interpreter that allows users to perform CRUD (Create, Read, Update, Delete) operations on these objects.

## Command Interpreter

The command interpreter is a command-line interface that enables users to interact with and manage the AirBnB clone. It allows users to perform various operations, such as creating and managing user accounts, adding places, writing reviews, and more.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/mohammedmxz/AirBnB_clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AirBnB_clone
    ```

3. Run the command interpreter:

    ```bash
    ./console.py
    ```

### How to Use the Command Interpreter

The command interpreter provides a set of commands for managing objects. Here are some key commands and their descriptions:

- `create`: Create a new instance of a specified class.
- `show`: Display details of a specific instance.
- `destroy`: Delete a specified instance.
- `all`: Display all instances or all instances of a specific class.
- `update`: Update the attributes of a specified instance.

Use the `help` command to get more information about each command.

### Examples

1. **Create a User:**

    ```bash
    (hbnb) create User
    ```

2. **Show details of a Place:**

    ```bash
    (hbnb) show Place <place_id>
    ```

3. **Display all Reviews:**

    ```bash
    (hbnb) all Review
    ```

4. **Update a User's attribute:**

    ```bash
    (hbnb) update User <user_id> first_name "John"
    ```

5. **Delete a Place:**

    ```bash
    (hbnb) destroy Place <place_id>
    ```

These are just a few examples, and there are more commands and functionalities available in the command interpreter. Explore the `help` command and the documentation for a comprehensive list of features and usage.
