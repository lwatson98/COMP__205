from flask import render_template
from app import app


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
@app.route('/new_artist')
def Newartists():

    warning =[
        {'body': 'Under Construction'}
    ]

    return render_template('new_artist.html', title="Home", warning=warning);