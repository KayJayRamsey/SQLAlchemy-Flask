from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect 

from flask import Flask, jsonify 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True) 
print(Base.classes.keys()) 
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine) 

app = Flask(__name__)

@app.route("/api/v1.0")
@app.route("/") 

def welcome():
   """List all available api routes."""
   return (
       f"Available Routes:<br/>"
       f"/api/v1.0/precipitation"
       f"<br/>"
       f"/api/v1.0/stations"
       f"<br/>"
       f"/api/v1.0/tobs"
       f"<br/>"
       f"/api/v1.0/<start>"
       f"<br/>"
       f"/api/v1.0/<start>/<end>"
   )

@app.route("/api/v1.0/precipitation")
def precipitation():

    session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    precipitation_12 = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= '2016-08-23').filter(Measurement.date <= '2017-08-23').order_by(Measurement.date).all()
    #precipitation_12

    precipitation_list = {date: prcp for date, prcp in results}

    return jsonify(precipitation_list) 