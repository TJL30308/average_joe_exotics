# import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

from config import password

# create db connection
engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:5432/mad_data_db")

# print table names, debugging
print(engine.table_names())

# create base
Base = automap_base()
Base.prepare(engine, reflect=True)

# create references to each table
AC = Base.classes.Alcohol_Consumption
AP = Base.classes.Alcohol_Production
CO = Base.classes.Country
RW = Base.classes.Reviews
TD = Base.classes.Traffic_Related_Deaths

# setup Flask
app = Flask(__name__)

# Flask routes
@app.route("/")
def welcome():
    return (
        f"<h1>Mad Data API Routes</h1>"
        f"/api/v1.0/alcohol_consumption<br/>"
        f"/api/v1.0/alcohol_production<br/>"
        f"/api/v1.0/country<br/>"
        f"/api/v1.0/reviews<br/>"
        f"/api/v1.0/traffic_related_deaths"
    )

@app.route("/api/v1.0/alcohol_consumption")
def alcohol_consumption():
    
    session = Session(engine)

    results = session.query(AC.year).all()

    session.close()

    return results

@app.route("/api/v1.0/alcohol_production")
def alcohol_production():
    return "<h1>PLACEHOLDER TEXT</h1>"

@app.route("/api/v1.0/country")
def country():
    return "<h1>PLACEHOLDER TEXT</h1>"

@app.route("/api/v1.0/reviews")
def reviews():
    return "<h1>PLACEHOLDER TEXT</h1>"

@app.route("/api/v1.0/traffic_related_deaths")
def traffic_related_deaths():
    return "<h1>PLACEHOLDER TEXT</h1>"

if __name__ == '__main__':
    app.run(debug=True)