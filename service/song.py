import spotipy
import flask

song_api = flask.url_for("songs")

@song_api.route("")
def get_songs():
    return []