import pandas
from pandas import read_csv, DataFrame
import sqlite3
import os
from os import path

conn = sqlite3.connect('buddymove_holidayiq.csv')

curs = conn.cursor()
