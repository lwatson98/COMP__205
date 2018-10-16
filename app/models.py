from datetime import datetime
from app import db




class Artist(db.Model):
    Artistid = db.Column(db.Integer, primary_key=True)
    Artistname = db.Column(db.String(64), index=True, unique=True)
    genre = db.Column(db.String(120), index=True, unique=True)
    gig = db.Column(db.String(120), index=True, unique=True)
    body = db.Column(db.String(140))
    events = db.relationship('ArtisttoEvent', back_populates='artist')




class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Eventname = db.Column(db.String(140))
    time= db.Column(db.DateTime, index=True, default=datetime.utcnow)
    VenueID = db.Column(db.Integer, db.ForeignKey('venue.id'))
    artist =db.relationship('Event', back_populates='events')





class ArtisttoEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ArtistID = db.Column(db.String, db.ForeignKey('artist.Artistname'))
    EventID = db.Column(db.String, db.ForeignKey('event.Eventname'))
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    artist=db.relationship('Artist', back_populates='events')
    event =db.relationship('Event', back_populates='artists')


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    address = db.Column(db.String(140))
    events = db.relationship('Event', backref='venue')






