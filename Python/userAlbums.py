

def make_album(artist_name, album_name, numberOfTracks=''):
    album = {'artist': artist_name, 'album': album_name}
    if numberOfTracks:
        album['tracks'] = str(numberOfTracks)
    return album

while True:
    print ''
    print ''
    print "Let's make a dictionary out of an album!"
    print "Type 'q' at any time to quit."
    artist = str(raw_input('Type in the artist: '))
    if artist == 'q':
        break
    print ''
    album = str(raw_input('Type in the album: '))
    if album == 'q':
        break
    print ''
    print make_album(artist, album)
    