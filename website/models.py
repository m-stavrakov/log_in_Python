# when i porting from a folder use .
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

# db.Model a layout or a blueprint for an object that will be stored in the database
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func.now() gets the current date and time
    # how to associate different info with different users, setting a relationship between Note and User classes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #tells us which note was made by which user

class User(db.Model, UserMixin):
    # defining the columns
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False) #150 is the max length for the string, unique means that no user can have the same email
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')