from datetime import datetime
from app import db




class Artist(db.Model):
    Artistid = db.Column(db.Integer, primary_key=True)
    Artistname = db.Column(db.String(64), index=True, unique=True)
    genre = db.Column(db.String(120), index=True, unique=True)
    gig = db.Column(db.String(120), index=True, unique=True)
    body = db.Column(db.String(140))




class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Eventname = db.Column(db.String(140))
    time= db.Column(db.DateTime, index=True, default=datetime.utcnow)
    Event_id = db.Column(db.Integer, db.ForeignKey('Artist.Artistid'))




class ArtisttoEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ArtistID = db.Column(db.String, db.ForeignKey('Artist.Artistid'))
    EventID = db.Column(db.String, db.ForeignKey('Event.id'))
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Venue(db.Model):
    Venuename = db.Column(db.String(140))
    currentPerformer = db.Column(db.String(140))
    EventID = db.Column(db.String, db.ForeignKey('Event.EventID'))



