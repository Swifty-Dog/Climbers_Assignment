import sqlite3
import json
from datetime import datetime,date
class Climber:
    def __init__(self, ID, first_name, last_name, nationality, date_of_birth) -> None:
        self.id = ID
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth

    def get_age(self):
        today = date.today()
        self.date_of_birth = self.date_of_birth.split("-")
        age= today.year - int(self.date_of_birth[2]) - ((today.month, today.day) < (int(self.date_of_birth[1]), int(self.date_of_birth[0])))

        return age

    def get_expeditions(self):
        expedition_list = []
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        c.execute("SELECT name FROM expeditions WHERE success = true AND id = ?", (self.id,))
        expeditions = c.fetchall()
        for expedition in expeditions:
            expedition_list.append(expedition)
        conn.commit()
        return expedition_list

        # conn = sqlite3.connect("climbersapp.db")
        # cursor = conn.cursor()
        # query = "SELECT * FROM expeditions WHERE climber_id = ? AND success = 1 "
        # val = self.id
        # cursor.execute(query, val)
        # expeditions = cursor.fetchall()
        # conn.close()
        # return expeditions


climb1 = Climber(931,"Burr", "Danahar","Malawi","06-12-1907")


def main():
    print(climb1.get_expeditions())


# Representation method
# This will format the output in the correct order
# Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
# def __repr__(self) -> str:
#     return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))

if __name__ == "__main__":
    main()

