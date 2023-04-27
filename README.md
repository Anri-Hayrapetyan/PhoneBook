# PhoneBook

This is a console application for managing a phone book.

## Requirements

Python 3.x is required to run this program. There are no other dependencies.

## Usage

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the program using the command `python main.py`.
4. When prompted, enter the relative path to the txt file containing phone book records. The file should have the following structure:
   
    ```
    {name} {surname} {separator} {phoneNumber}
    ```
   
    For example:
    
    ```
    Edgar Danielyan - 0989598949
    Hovhannes Shitikyan - 0988598949
    Artak Hovhannisyan : 0925484988
    Nara Hovhannisyan : 092548487
    ```
    
5. Choose the sorting criteria (by name, surname, or phone number code) and the sorting order (ascending or descending).
6. The sorted phone book records will be displayed in the console, along with any validation messages for non-valid items in the records.
7. If there are any non-valid items, you will see messages like the following:

    ```
    Validations:
    line 1: phone number should be with 9 digits, the separator should be `:` or `-`.
    line 2: phone number should be with 9 digits.
    line 3: separator should be `:` or `-`.
    ```