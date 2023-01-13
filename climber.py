import sqlite3
from datetime import date
class Climber:
    def __init__(self, id, first_name, last_name, nationality, date_of_birth) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth

    def get_age(self):
        today = date.today()
        self.date_of_birth = self.date_of_birth.split("-")
                                                        # if today month and day is lower than given value than the birthday hasnt reach yet
        age= today.year - int(self.date_of_birth[2]) - ((today.month, today.day) < (int(self.date_of_birth[1]), int(self.date_of_birth[0])))

        return age

    def get_expeditions(self):
        expedition_names = []
        expedition_id_list = []
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        name_query = "SELECT name FROM expeditions"
        c.execute(name_query)
        names = c.fetchall()
        for name in names:
            expedition_names.append(name)

        # return list van climber?? of alles?
        query = "SELECT expedition_id FROM expedition_climbers"
        c.execute(query)

        expeditions_id= c.fetchall()
        for expedition in expeditions_id:
            expedition= str(expedition)
            expedition= expedition.replace("(","").replace(")","").replace(",","").replace("","")
            expedition= int(expedition)
            expedition_id_list.append(expedition)

        for expedition_id in expedition_id_list:
            expedition_id = expedition_id - 1
            print(expedition_names[expedition_id])



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

