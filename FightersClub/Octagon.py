import random
from .Decorators import time_of_function
from .Fighter import Fighter
from Exceptions import FightEnd
from DB.Controllers import fighter_controller
import asyncio


class Octagon:
    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.controller = fighter_controller

    async def punch(self, fighter_hitting, fighter_defending):
        result = fighter_hitting.punch_reaction(fighter_defending)
        print(
            f"{fighter_hitting.name} нанёс {fighter_defending.name} {fighter_hitting.punch_power} урона, сделав {result[1]}")
        if result[0]:
            await asyncio.sleep(1)
            raise FightEnd(fighter_hitting, fighter_defending)

    @time_of_function
    async def fight(self):
        await self.controller.update_fighter_fights(self.fighter1.name)
        await self.controller.update_fighter_fights(self.fighter2.name)
        round_n = 1
        while True:
            print(f"           Раунд {round_n}")
            await asyncio.sleep(1)
            print(f"{self.fighter1.name} - {self.fighter1.hp} {self.fighter2.name} - {self.fighter2.hp}")
            await asyncio.sleep(1)
            try:
                punch_task = []
                if random.randint(1, 1000) <= 500:
                    punch_task.append(asyncio.create_task(self.punch(self.fighter1, self.fighter2)))
                else:
                    punch_task.append(asyncio.create_task(self.punch(self.fighter2, self.fighter1)))
                await asyncio.gather(*punch_task)
            except FightEnd as e:
                await self.controller.update_fighter_wins(e.extra_info[0].name)
                print(
                    f"             Бой зевершен         \nБоец {e.extra_info[0].name} победил, у него осталось {e.extra_info[0].hp} здоровья")
                print('Бой длился', end=' ')
                break
            heal_task = [asyncio.create_task(self.fighter1.heal()), asyncio.create_task(self.fighter2.heal())]
            await asyncio.gather(*heal_task)
            for i, fighter in enumerate([self.fighter1, self.fighter2]):
                if heal_task[i].result() != 0:
                    await asyncio.sleep(1)
                    print(f'Боец {fighter.name} востановил себе {heal_task[i].result()} здоровья')
            round_n += 1
            await asyncio.sleep(1)
