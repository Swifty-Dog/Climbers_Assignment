import sqlite3


class Expedition:
    def __init__(self, id, name, mountain_id, start, date, country, duration, success) -> None:
        self.id = id
        self.name = name
        self.mountain = mountain_id
        self.start = start
        self.date = date
        self.country = country
        self.duration = duration
        self.success = success

    def add_climber(self, climber):
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "INSERT OR IGNORE INTO expedition_climbers VALUES (?, ?)"
        #dit stukje moet in het MENU
        #climber is gegeven aan door de user
        val = (climber, self.id)
        c.execute(query, val)
        conn.commit()
        conn.close()

# prints a None on the end cuz of print(x) statement
    def get_climbers(self):
        conn = sqlite3.connect("climbersapp.db")
        cursor = conn.cursor()
        query = "SELECT * FROM climbers"
        cursor.execute(query)
        climbers = cursor.fetchall()
        for x in climbers:
            print(x)

    def get_mountain(self):
        mountain_list = []
        id_mountain_list = []
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        name_query = "SELECT name FROM mountains"
        c.execute(name_query)
        mountains = c.fetchall()
        for mountain in mountains:
            mountain = str(mountain)
            mountain = mountain.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
            mountain_list.append(mountain)

        id_query = "SELECT id FROM mountains"
        c.execute(id_query)
        id_mountain = c.fetchall()
        for id in id_mountain:
            id = str(id)
            id = id.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
            id = int(id)
            id_mountain_list.append(id)

        for id in id_mountain_list:
            id = id - 1
            return mountain_list[id]

    def convert_date(self,format):
        # gives format by user which will choose what format it will become to
        conn = sqlite3.connect("climbersapp.db")
        cursor = conn.cursor()
        query = "SELECT date FROM expeditions WHERE ?"
        val = str(self.id)
        cursor.execute(query,val)
        dates = cursor.fetchone()
        #current in table is YYYY-MM-DD
        #options YYYY-MM-DD // DD-MM-YYYY // MM-DD-YYYY
        # %d %m %Y
        for date in dates:
            date = str(date)
            date = date.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
            year, month, day = date.split("-")
            if format == "1":
            #prints it in DD-MM-YYYY
                print(f"{day}-{month}-{year}")
            #print it in MM-DD-YYYY
            if format == "2":
                print(f"{month}-{day}-{year}")
            #print is in YYYY-MM-DD
            if format == "3":
                print(f"{year}-{month}-{day}")


    def convert_duration(self, format):
        # given format  is by user which will choose what format it will become to
        conn = sqlite3.connect("climbersapp.db")
        cursor = conn.cursor()
        query = "SELECT duration FROM expeditions WHERE id=?"
        val = str(self.id)
        cursor.execute(query, val)
        duration = cursor.fetchall()
        duration = str(duration)
        duration = duration.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "").replace("[","").replace("]","")
        duration = duration.replace("H"," ")
        duration = duration.split(" ")
        hours = int(duration[0])
        minutes = int(duration[1])
        #prints the duration in days
        if format == "1":
            minutes_to_day = minutes / 3600
            hours_to_day = hours / 24
            total_day = hours_to_day + minutes_to_day
            print(f"The duration in days is: {total_day}")

        #prints the duration in hours
        if format =="2":
            minutes_to_hours = minutes / 60
            total_hours = hours + minutes_to_hours
            print(f"The duration in hours is: {total_hours}")

        #prints the duration in minutes
        if format == "3":
            hours_to_minutes = hours * 60
            total_minutes = hours_to_minutes + minutes
            print(f"The duration in minutes is: {total_minutes}")

exp = Expedition(4, "The journey of Momhil Sar",1 ,"Pakistan", "1965-08-18", "Indonesia", "24H48", True )

def main():
    exp.convert_duration("1")

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    # def __repr__(self) -> str:
    #     return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))

if __name__=="__main__":
    main()