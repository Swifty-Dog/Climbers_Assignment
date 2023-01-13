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
        climbers_list = []
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT * FROM expedition_climbers WHERE expedition_id=?"
        val = (self.id),
        c.execute(query,val)
        results = c.fetchall
        print(results)
        # query = "SELECT * FROM climbers"
        # cursor.execute(query)
        # climbers = cursor.fetchall()
        # for x in climbers:
        #     climbers_list.append(x)
        #
        # return climbers_list

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
        date = self.date
        #current in table is YYYY-MM-DD
        #options YYYY-MM-DD // DD-MM-YYYY // MM-DD-YYYY
        # %d %m %Y
        date = str(date)
        date = date.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
        year, month, day = date.split("-")
        if format == "1":
        #prints it in DD-MM-YYYY
            return f"{day}-{month}-{year}"
        #print it in MM-DD-YYYY
        if format == "2":
            return f"{month}-{day}-{year}"
        #print is in YYYY-MM-DD
        if format == "3":
            return f"{year}-{month}-{day}"

    def convert_duration(self, format):
        # given format  is by user which will choose what format it will become tp
        duration = self.duration
        duration = duration.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "").replace("[","").replace("]","")
        duration = duration.split("H")
        hours = int(duration[0])
        minutes = int(duration[1])
        #prints the duration in days
        if format == "1":
            minutes_to_day = minutes / 3600
            hours_to_day = hours / 24
            total_day = hours_to_day + minutes_to_day
            return total_day
        #prints the duration in hours
        elif format =="2":
            minutes_to_hours = minutes / 60
            total_hours = round(hours + minutes_to_hours)
            return total_hours
        #prints the duration in minutes
        elif format == "3":
            hours_to_minutes = hours * 60
            total_minutes = round(hours_to_minutes + minutes)
            return total_minutes

        return "Invalid Format"
exp = Expedition(2, "The journey of Momhil Sar",2 ,"Pakistan", "1965-08-18", "Indonesia", "24H48", True )

def main():
    print(exp.get_mountain())

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    # def __repr__(self) -> str:
    #     return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))

if __name__=="__main__":
    main()