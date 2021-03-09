#Import Dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

######################################################
# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
connection = engine.connect()
connection