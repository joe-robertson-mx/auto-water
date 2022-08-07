import string
from sensors import sensors

class testClass():
    def __init__(self) -> None:
        pass

    def test_func (self, logmsg: string):
        database_uri: str = 'postgresql+psycopg2://test:test@db/test'
        test_sensor: sensors.TestSensor = sensors.TestSensor(database_uri)
        test_sensor.read_moisture()