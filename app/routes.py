from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home');

@app.route('/artists')
def artists():

    artists =[
        {'author': {'artists': 'Tears'},
            'body': ''
        },
        {
            'author': {'artists': 'The Blasts'},
            'body': ''
        }
    ]
    return render_template('artists.html', title='Home', artists=artists);