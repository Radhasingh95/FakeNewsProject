# After installing with pip install psycopg2
import psycopg2 as pg

#TODO write script to use scrapped data from webScrapper.py and add it as a row to TRAIN, USERINPUT and STAT tables

# Create a connection with PostgreSQL
conn = pg2.connect(database='FNDB', user='postgres',password='password')

# Pass in a PostgreSQL query as a string
cur.execute("SELECT * FROM TRAIN")

"""
DO NOT TRY TO USE THIS, IT IS STILL INCOMPLETE AND LACKS DEPENDENCIES
"""