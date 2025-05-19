from http.client import HTTPException

import requests
from image_recognition import song

def main():
    global res
    result = song()
    print(result)
    access_token = ""
    headers = {
        "Authorization" : f'Bearer ' + access_token
    }

    params = {
        "q" : result,
        "type" : "track",
        "limit" : 1
    }
    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params = params)
    track_uri = response.json()['tracks']['items'][0]['uri']
    print(track_uri)
    songToAdd = {
        "position" : 0,
        "uris" : [track_uri]
    }
    try:
        res = requests.post("https://api.spotify.com/v1/playlists/49zO31jJr2jjCjZdiIaJdO/tracks", headers=headers, json=songToAdd)
        res.raise_for_status()
    except HTTPException:
        print(res.json())

main()