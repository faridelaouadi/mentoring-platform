import os

from flask import Flask, render_template, request

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://buuhbogioluhpv:1bc683148bb4b606d690a466dd885d977b1a9b03dd36a91c316221bdd04d1d36@ec2-79-125-126-205.eu-west-1.compute.amazonaws.com:5432/d9pljc2v09nhs6"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

def main():
  # Create tables based on each table definition in `models`
  db.create_all()
  db.session.commit()
  print("tables were created")
if __name__ == "__main__":
  # Allows for command line interaction with Flask application
  with app.app_context():
      main()
