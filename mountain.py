import sqlite3
class Mountain:
    def __init__(self,id,name,country,rank,height,prominence,range) -> None:
        self.id = id
        self.name = name
        self.country = country
        self.rank = int(rank) if rank else 0
        self.height = int(height)
        self.prominence = int(prominence)
        self.range = range

    def height_difference(self):
        difference = (self.height - self.prominence)
        return difference

    def get_expeditions(self):
        expedition_list = []
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        name_query = "SELECT name FROM expeditions"
        c.execute(name_query)
        expeditions = c.fetchall()
        for expedition in expeditions:
            expedition = str(expedition)
            expedition = expedition.replace(",","").replace("(","").replace(")","").replace("'","").replace("'","")
            expedition_list.append(expedition)

        # check id from mountain table --> return the id('s)
        # check id from expeditions --> return name from the id as index in a list from
        # the expedition_list
        return expedition_list

mountain1 = Mountain(1,"Momhil Sar" ,"Pakistan" ,64 ,7414 ,907 ,"Hispar Karakoram")

def main():
    print(mountain1.get_expeditions())
    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    # def __repr__(self) -> str:
    #     return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))

if __name__ == "__main__":
    main()