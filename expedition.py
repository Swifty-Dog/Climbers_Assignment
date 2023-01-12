class Expedition:

    def __init__(self, id, name, mountain, start, date, country, duration, success) -> None:
        self.id = id
        self.name = name
        self.mountain = mountain
        self.start = start
        self.start = start
        self.date = date
        self.country = country
        self.duration = duration
        self.succes = success

    def add_climber(self, climber):
        conn = sqlite3.connect("expeditions.db")
        c = conn.cursor()
        query = "INSERT INTO expedition_climbers (expedition_id, climber_id) VALUES (?,?)"
        val = self.id, climber.id
        c.execute(query, val)
        conn.commit()
        conn.close()
    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    # def __repr__(self) -> str:
    #     return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))