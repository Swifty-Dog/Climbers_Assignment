import sqlite3
import json

class Climber:
    def __init__(self, ID, first_name, last_name, nationality, date_of_birth) -> None:
        self.id = ID
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth

    def test(self):
        return f"{self.first_name} {self.last_name}"

def main():
    pass

# Representation method
# This will format the output in the correct order
# Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
# def __repr__(self) -> str:
#     return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))

if __name__ == "__main__":
    main()