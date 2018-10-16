from flask import render_template, flash, redirect
from app import app,db

from app.forms import NewArtistForm
from app.models import *

from app.forms import LoginForm



@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home');

@app.route('/artists')
def artists():

    artists =[
        {'band': {'name': 'Tears'},
            'body': ''
        },
        {
            'band': {'name': 'The Blasts'},
            'body': ''
        }
    ]
    return render_template('artists.html', title='Home', artists=artists);
@app.route('/Tears')
def Tears():

    info ={'bandname':'Tears','hometown':'Ithaca', 'body': 'Tears is an Upstate NY, hard rockin, boogie band assembled by bassist, Jeff Howell, formerly of Foghat, The Outlaws and Savoy Brown, to name a few.'}


    return render_template('Tears.html', title="Home", info=info);


@app.route('/new_artist', methods=['GET', 'POST'])
def Newartists():

    form = NewArtistForm()
    if form.validate_on_submit():
        information = {}

        information['bandname']=form.username.data
        information['hometown'] = form.hometown.data
        information['body']=form.description.data
        return render_template('Tears.html', title="Home", info=information);





    return render_template('new_artist.html', title="Home", form=form);


# @app.route('/new_artist', methods=['GET', 'POST'])
# def Newartists():
#
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return render_template('new_artist.html', title="Home", form=form);
#     return render_template('new_artist.html', title="Home", form=form);
@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")
   # clear all data from all tables
   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()

   a1= Artist(Artistname="The Tears",genre="Rock",gig="Ithaca Theater",body="Just Rocking and Jamming")
   db.session.add(a1)

   a2 = Artist(Artistname="The Blasts", genre="Punk", gig="Ithaca Gorges", body="Rocking like a Hurricane")
   db.session.add(a2)
   a3 = Artist(Artistname="Feed the Fire", genre="Reggae", gig="Busy Bee Market", body="We Jammin and we Hope you like Jammmin to")
   db.session.add(a3)
   v1 = Venue(Venuename="College Bagel Steppers", currentPerformer="The Tears")
   db.session.add(v1)
   v2 = Venue(Venuename="Ins and Outs of Mind", currentPerformer="The Blasts")
   db.session.add(v2)
   e1 = Event(Eventname="Ithaca Theater")
   db.session.add(e1)
   e2 = Event(Eventname="Ithaca Gorges")
   db.session.add(e2)
   db.session.commit()

   a2e1 = ArtisttoEvent(artist=a1, event=e1)
   a2e2 = ArtisttoEvent(artist=a2, event=e2)


