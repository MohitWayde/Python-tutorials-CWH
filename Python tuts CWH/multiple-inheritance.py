# 16-11-2020
# multiple inheritance
# write first charater of class name in capital letter
class programmer:
    def __init__(self):
        no_of_leaves = 10
    def programmer_accept(self, aname, alanguage, asalary):
        self.name = aname
        self.language = alanguage
        self.salary = asalary
    def programmer_display(self):   
        print(f"the name is {self.name}, known languages are {self.language} and salary is {self.salary}")
class player:
    def __init__(self):
        no_of_games = 5
    def player_accept(self, aname, agame, ayears):
        self.name = aname
        self.game = agame
        self.years = ayears
    def player_display(self):   
        print(f"the name is {self.name}, known games are {self.game} and experience of playing is {self.years}")
        
class cool_programmer(programmer, player):
    pass

object1 = cool_programmer()
object1.programmer_accept("amar","python","15000")
object1.programmer_display()
object2 = cool_programmer()
object2.player_accept("sham" , ["cricket","football"], 3)
object2.player_display()

    
