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
    """Retrieve song information upon being fed an track name"""
    pass



    def sp(self, irc, msg, args, song):
        """<artist> <song>

        The track name for which you need to draw out the information .
        """
        os.environ['SPOTIPY_CLIENT_ID'] = ''
        os.environ['SPOTIPY_CLIENT_SECRET'] = ''
        spotified = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        results = spotified.search(song)
        items = results['tracks']['items']
        if len(items) > 0:
            track = items[0]
            trackn = track['uri']
            track_info = spotified.track(trackn)
            track_artist = track['artists'][0]['name']
            track_name =track['name']
            track_url = track_info['external_urls']['spotify']
            re = utils.str.format('The song is %s by %s at %s with %s', track_name, track_artist, track_url, trackn)
            irc.reply(re)

        else:
            irc.error('Song not found')

    sp = wrap(sp, ['text'])

Class = Spotify
# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
