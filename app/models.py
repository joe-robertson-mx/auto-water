from .extensions import database

class Watered(database.Model):
    '''Model to hold the data for when the plant was last watered.'''

    __tablename__: str = 'watered_tab'

    id: database.Column = database.Column(database.Integer, primary_key=True, autoincrement=True)

    date_watered: database.Column = database.Column(database.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f'Watered(date_watered={self.date_watered})'


class Schedule(database.Model):
    '''Model to hold the values collected from the moisture sensors for a given plant.'''

    __tablename__: str = 'schedule_tab'

    id: database.Column = database.Column(database.Integer, primary_key=True, autoincrement=True)

    datetime: database.Column = database.Column(database.DateTime, nullable=False)
    water_level: database.Column = database.Column(database.Float, nullable=False)

    def __repr__(self) -> str:
        return f'Schedule(datetime={self.datetime})'
