from wiki.pokemon import Pokemon

class Pika(Pokemon):
    no = 25
    breed_population = 0
    pass
    def __init__(self, name, lv = 5):
        super().__init__(name, lv)
        self.skill = '전기충격' , 25
    def walk(self):
        return '뚜벅 뚜벅'
class Meta(Pokemon):
    no = 132
    breed_population = 0
    pass

p1 = Pika('피카츄')
m1 = Meta('메타몽')
# print(p1.name, p1.attack())
# print(m1.name, m1.no, m1.skill)
# print(pokemon.breed_population)

class Child(Pika, Meta):
    pass
class Brother(Meta, Pika):
    pass

c1 = Child('피타몽')
b1 = Brother('메카츄')
print(b1.name)
print(b1.skill)