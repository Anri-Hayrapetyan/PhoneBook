class Record:
    def __init__(self, name, surname, separator, phone_number, index):
        self.name = name
        self.surname = surname
        self.separator = separator
        self.phone_number = phone_number
        self.index = index
        self.validation_message = ""

    def __str__(self):
        return f"{self.name} {self.surname} {self.separator} {self.phone_number}"

    def validate(self):
        self.validation_message = validate_record(self)

def validate_record(record):
    validation_message = ""
    if not record.name:
        validation_message += f"name is missing. "
    if not record.surname:
        validation_message += f"surname is missing. "
    if len(record.phone_number) != 9:
        validation_message += f"phone number should be with 9 digits. "
    if not record.phone_number.isdigit():
        validation_message += f"phone number should contain only digits. "
    if record.separator not in [":", "-"]:
        validation_message += f"the separator should be `:` or `-`."
    return validation_message

class PhoneBook:
    def __init__(self, file_path):
        self.records = []
        self.read_records(file_path)

    def read_records(self, file_path):
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                for index, line in enumerate(lines, start=1):
                    parts = line.strip().rsplit(" ", 2)
                    if len(parts) != 3:
                        raise InvalidDataException(f"Invalid data in line {index}")
                    name_parts = parts[0].rsplit(" ", 1)
                    separator = parts[1][0]
                    phone_number = parts[2]
                    record = Record(name_parts[0], name_parts[1] if len(name_parts) > 1 else "", separator, phone_number, index)
                    record.validate()
                    self.records.append(record)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            exit(1)
        except InvalidDataException as e:
            print(str(e))
            exit(1)

    def sort_records(self, key_function, reverse=False):
        self.records = sorted(self.records, key=key_function, reverse=reverse)

    def display_records(self):
        print('\nFile Structure')
        for record in self.records:
            print(record)

    def display_validations(self):
        print("\nValidations:")
        for record in self.records:
            if record.validation_message:
                print(f"line {record.index}: {record.validation_message}")

def get_key_function(criteria):
    return lambda record: {
        "surname": (record.surname or "\uffff", record.name),
        "name": (record.name, record.surname),
        "phonenumbercode": (record.phone_number[:3], record.name, record.surname)
    }.get(criteria.lower())

def start():
    file_path = input("Enter the file path: ")
    phone_book = PhoneBook(file_path)

    order = ""
    while order.lower() not in("ascending", "descending"):
        order = input("Please choose an ordering to sort: \"Ascending\" or \"Descending\": ")

    criteria = ""
    while criteria.lower() not in ("name", "surname", "phonenumbercode"):
        criteria = input("Please choose criteria: \"Name\", \"Surname\" or \"PhoneNumberCode\": ")

    reverse = True if order.lower() == "descending" else False
    key_function = get_key_function(criteria)
    phone_book.sort_records(key_function, reverse)
    phone_book.display_records()
    phone_book.display_validations()

if __name__ == "__main__":
    start()
