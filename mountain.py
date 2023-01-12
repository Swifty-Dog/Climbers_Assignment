class Mountain:

    def __init__(self,id,name,country,rank,height,prominence,range) -> None:
        self.id = id
        self.name = name
        self.country = country
        self.rank =rank
        self.height = height
        self.prominence = prominence
        self.range = range

    def height_difference(self):
        difference = self.height - self.prominence
        return difference

    def get_expeditions(self):
        pass
# mountain1 = Mountain("Momhil Sar",)

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    # def __repr__(self) -> str:
    #     return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))