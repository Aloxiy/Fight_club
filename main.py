from FightersClub import Boxer
from FightersClub import Karateka
from FightersClub import Octagon
from DB.Controllers import fighter_controller
import asyncio


async def main():
    fighter1 = Boxer(name="Cvetkov", age=45)
    await fighter_controller.create_fighter(name="Cvetkov", age=45, fight_art="Box")
    fighter2 = Karateka(name="Musaev", age=41)
    await fighter_controller.create_fighter(name="Musaev", age=41, fight_art="Karateka")
    Kletka = Octagon(fighter1, fighter2)
    await Kletka.fight()


asyncio.run(main())
