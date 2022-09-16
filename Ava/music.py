import json
import spotipy
import webbrowser
import Ava
  
user_name = '313q77fmtlbbgqa7i6kqcxi5dxau'
clientID = '44b5bec613d646af8e9cba7307fd8074'
clientSecret = '32c5debc177644289032a8ed00b1636a'
redirect_uri = 'http://google.com/callback'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
  
# To print the JSON response from 
# browser in a readable format.
# optional can be removed

def play_music():
    Ava.speak("What song would you like to listen to?")
    search_song = Ava.TakeCommand().lower()
    results = spotifyObject.search(search_song, 1, 0, "track")
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)
    Ava.speak("Here is your song, you can listen to it on your browser")
    Ava.speak("Enjoy your music, loggging out now")
