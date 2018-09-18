from flask import render_template, flash, redirect
from app import app
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

    info =[
        {'body': 'Tears is an Upstate NY, hard rockin, boogie band assembled by bassist, Jeff Howell, formerly of Foghat, The Outlaws and Savoy Brown, to name a few.'}
    ]

    return render_template('Tears.html', title="Home", info=info);
@app.route('/new_artist', methods=['GET', 'POST'])
def Newartists():

    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return render_template('new_artist.html', title="Home", form=form);
    return render_template('new_artist.html', title="Home", form=form);