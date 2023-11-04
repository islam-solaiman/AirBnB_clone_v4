#!/usr/bin/python3
"""
    Flask app to generate complete html page containing location/amenity
    dropdown menus and rental listings
"""

import uuid
from models import storage
from flask import Flask, render_template
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/3-hbnb')
def display_hbnb():
    """ Generates page with popdown menu of states or cities """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    cache_id = uuid.uuid4()
    return render_template('3-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """ Close database or file storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
