from flask import render_template, flash, redirect
from app import app
from app.forms import NewArtistForm


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

