from flask import Flask
from datetime import datetime, timedelta
from flask import render_template
from flask_migrate import Migrate
from .extensions import database
import re
from .testFile import testClass
from config import Config
from typing import Tuple

app = Flask(__name__)
app.config.from_object(Config)
database.init_app(app)
migrate = Migrate(app, database)


def graph_logic() -> Tuple[list, list]:
    '''function to return the Graph data for the watered graph on the index page.'''

    x = []
    y = []
    graph_length = current_app.config['GRAPH_LENGTH']
    start_date = datetime.today().date() - timedelta(days=graph_length)

    for i in range(graph_length):
        date = start_date + timedelta(days=i)
        x.append(date.strftime('%Y-%m-%d'))

        schedule = Schedule.query.filter(Schedule.datetime.cast(database.Date) == date).first()
        if schedule:
            y.append(schedule.water_level)
        else:
            y.append(0)
    return x, y

args: Dict[str, Any] = {
    'last_time_watered' : last_time_watered(selected_plant),
    'x_axis_dates'      : x,
    'graph_data'        : y,
}

@app.route("/")
def home():
    return render_template("home.html", **args)

@app.route("/test/", methods=['POST'])
def test():
    message = testClass()
    message.test_func('Wooo')
    return render_template("home.html")