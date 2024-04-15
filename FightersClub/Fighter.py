import random
from abc import ABC, abstractmethod
from .Decorators import random_using
from Exceptions import GetDataError


class Fighter(ABC):
    def __init__(self, age: int = None, name: str = None, fight_art: str = None):
        if type(age) is type(1):
            self.age = age
        else:
            raise GetDataError("Age")
        if type(name) is type("Name"):
            self.name = name
        else:
            raise GetDataError("Name")
        if type(fight_art) is type("Fight_art"):
            self.fight_art = fight_art
        else:
            raise GetDataError("Fight_art")
        self.hp = 100
        self.punch_power = random.randint(1, 20)
        self.healing_salve = 5

    @abstractmethod
    def punch_reaction(self, other):
        pass

    def _setPunchPower(self, a, b):
        self.punch_power = random.randint(a, b)

    def __str__(self):
        return f'Имя бойца - {self.name}\nВозраст бойца - {self.age}\nСтиль драки - {self.fight_art}\nКоличество здоровья - {self.hp}\nСила удара - {self.punch_power}'

    def __add__(self, other):
        self.hp += other
        return self

    def __sub__(self, other):
        self.hp -= other
        return self


class Healing:
    @random_using
    async def heal(self):
        healed_hp = 0
        if self.healing_salve > 0:
            if 40 < self.hp <= 80:
                healed_hp = min(100 - self.hp, random.randint(5, 40))
                self.hp += healed_hp
            elif 20 < self.hp <= 40:
                healed_hp = random.randint(5, 60)
                self.hp += healed_hp
            elif self.hp <= 20:
                healed_hp = min(100, self.hp + random.randint(5, 100))
                self.hp = healed_hp - self.hp
            if healed_hp != 0:
                self.healing_salve -= 1
        return healed_hp


class Boxer(Fighter, Healing):
    def __init__(self, age=18, name="Anonymous", fight_art="Box"):
        super().__init__(age=age, name=name, fight_art=fight_art)

    def punch_reaction(self, other):
        if random.randint(1, 1000) % 2 == 0:
            punch_name = "Right Hand Punch"
            self._setPunchPower(15, 25)
        else:
            punch_name = "Left Hand Punch"
            self._setPunchPower(30, 40)
        other = other - self.punch_power
        result = False
        if other.hp < 0:
            result = True
        return [result, punch_name]


class Karateka(Fighter, Healing):
    def __init__(self, age=18, name="Anonymous", fight_art="Karate"):
        super().__init__(age=age, name=name, fight_art=fight_art)

    def punch_reaction(self, other):
        if random.randint(1, 1000) % 3 == 0:
            punch_name = "Low kick"
            self._setPunchPower(30, 30)
        elif random.randint(1, 1000) % 3 == 1:
            punch_name = "High kick"
            self._setPunchPower(40, 40)
        else:
            punch_name = "Middle kick"
            self._setPunchPower(33, 38)
        other = other - self.punch_power
        result = False
        if other.hp <= 0:
            result = True
        return [result, punch_name]
