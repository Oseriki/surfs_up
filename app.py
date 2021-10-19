# Add dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Add SQLAlchemy dependencies, which will help us access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import the Flask dependency 
from flask import Flask, jsonify

# Set Up the Database. This will allow access and query our SQLite database file.
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes e.g., tables.
Base = automap_base()

# Add the following code to reflect the database
Base.prepare(engine, reflect=True)

# With the database reflected, we can save our references to each table. 
# Again, they'll be the same references as the ones we wrote earlier in this module. 
# We'll create a variable for each of the classes so that we can reference them later.
# The two tables are Measurement and station. To see table names in jupyter notebook, run Base.classes.keys()
#Note, this not needed for fask
Measurement = Base.classes.measurement
Station = Base.classes.station

# Finally, create a session link from Python to our database with the following code:
session = Session(engine)

# Set up Flask. This will Create a New Flask App Instance
app = Flask(__name__)

# let's create our routes!
# Next, create a function called welcome(). 
# Whenever you make a route in Flask, you put the code you want in that specific route below @app.route(). 
@app.route('/')
def welcome():
    return(
    '''
    <strong>Welcome to the Climate Analysis</strong> API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

# Create the precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Create the stations Route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create the Monthly Temperature Route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create the Statistics Route
#Our last route will be to report on the minimum, average, and maximum temperatures. 
# However, this route is different from the previous ones in that we will have to provide 
# both a starting and ending date.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)