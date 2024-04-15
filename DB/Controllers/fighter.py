from sqlalchemy import ScalarResult
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError

from DB.Models import FighterModel
from DB.Models.Fighter import FighterModel
from DB.connection import get_db_sessionmaker


class fighter_controller:
    async def create_fighter(name: str, age: int, fight_art: str,
                             db_sessionmaker: async_sessionmaker = get_db_sessionmaker()):
        try:
            async with db_sessionmaker.begin() as session:
                # Проверяем, существует ли боец с данным именем
                existing_fighter = await fighter_controller.get_fighter_by_name(fighter_name=name)
                if existing_fighter is None:
                    fighter = FighterModel(name=name, age=age, fight_art=fight_art)
                    session.add(fighter)
                    await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def get_fighter_by_name(fighter_name: str,
                                  db_sessionmaker: async_sessionmaker = get_db_sessionmaker()) -> FighterModel:
        try:
            async with db_sessionmaker.begin() as session:
                result = await session.execute(select(FighterModel).filter_by(name=fighter_name))
                return result.scalar_one_or_none()  # возвращает None, если ничего не найдено
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    async def get_all_fighters(db_sessionmaker: async_sessionmaker = get_db_sessionmaker()) -> ScalarResult[
        FighterModel]:
        async with db_sessionmaker.begin() as session:
            result = await session.scalars(select(FighterModel))
            return result

    async def update_fighter_wins(fighter_name: str, db_sessionmaker: async_sessionmaker = get_db_sessionmaker()):
        async with db_sessionmaker.begin() as session:
            fighter = await session.scalar(select(FighterModel).where(FighterModel.name == fighter_name))
            if fighter:
                fighter.wins += 1
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

    async def update_fighter_fights(fighter_name: str, db_sessionmaker: async_sessionmaker = get_db_sessionmaker()):
        async with db_sessionmaker.begin() as session:
            fighter = await session.scalar(select(FighterModel).where(FighterModel.name == fighter_name))
            if fighter:
                fighter.fights += 1
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

    async def delete_fighter(fighter_id: int, db_sessionmaker: async_sessionmaker = get_db_sessionmaker()):
        async with db_sessionmaker.begin() as session:
            fighter = await session.get(FighterModel, fighter_id)
            if fighter:
                await session.delete(fighter)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
