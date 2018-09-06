
class ProgrammingLanguage:

    def __init__(self,name="", typing_type="static", reflection=False, year=0):
        self.name = name
        self.typing_type = typing_type
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing_type == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{self.name},{self.typing_type} typing, Reflection = {self.reflection}, first appeared in {self.year}".format(self=self)