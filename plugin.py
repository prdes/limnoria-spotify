###
# Copyright (c) 2020, mogad0n
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###
import spotipy
import os
import sys
from spotipy.oauth2 import SpotifyClientCredentials


from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Spotify')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class Spotify(callbacks.Plugin):
    """Retrieve Track information from Spotify using the Spotipy"""

    def sp(self, irc, msg, args, song):
        """<artist> <song>

        The track details for which the URL/trackID is desired.
        """
        clientID = self.registryValue('clientID')
        if not clientID:
            irc.error("The clientID is not set. Please set it via "
                      "'config plugins.spotify.clientID' and reload the plugin. "
                      "You can sign up for it from "
                      "https://developer.spotify.com/", Raise=True)

        clientSECRET = self.registryValue('clientSECRET')
        if not clientSECRET:
            irc.error("The clientSECRET is not set. Please set it via "
                      "'config plugins.spotify.clientSECRET' and reload the plugin. "
                      "You can sign up for it from "
                      "https://developer.spotify.com/", Raise=True)

        os.environ['SPOTIPY_CLIENT_ID'] = clientID
        os.environ['SPOTIPY_CLIENT_SECRET'] = clientSECRET

        spotified = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        results = spotified.search(song)
        items = results['tracks']['items']
        if len(items) > 0:
            track = items[0]
            track_uri = track['uri']
            track_artist = track['artists'][0]['name']
            track_album = track['album']['name']
            track_name =track['name']
            track_url = track['external_urls']['spotify']
            re = utils.str.format(' 🎶️ \x02\x0301,03SPOTIFY\x0f 🎶️ %s by %s from %s at %s and uri %s', track_name, track_artist, track_album, track_url, track_uri)
            irc.reply(re)
        else:
            irc.error('No Results')

    sp = wrap(sp, ['text'])

Class = Spotify
# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
