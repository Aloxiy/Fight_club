class FightEnd(Exception):
    def __init__(self, fighter_hitting, fighter_defending):
        message = f"Бой закончился"
        super().__init__(message)
        self.extra_info = [fighter_hitting, fighter_defending]


