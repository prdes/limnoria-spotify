# limnoria-spotify

Retrieve Song information from Spotify



### Dependencies

This requires a reasonably current version of Limnoria to run

It relies on [Spotipy](https://spotipy.readthedocs.io/en/2.14.0/) and the dependencies can be can be installed using

`pip3 install -r requirements.txt`



### Setting up clientID and clientSECRET

1. Obtain your credentials from their [Developer Portal](https://developer.spotify.com/documentation/web-api/)
2. Set the clientID and clientSECRET using

`@config plugins.spotify.clientID "<insert your clientID here>"`

`@config plugins.spotify.clientSECRET "<insert your ClienSECRET here>"`

3. Reload the plugin. 

### Usage

`@sp Radiohead Creep`

`@sp dynatron pulse power`