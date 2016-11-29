# bert
Bert exports recorded talks

## changelog
* 23/11/2016 - initial commit of new Bert project.  Playlists can be opened from .json and saved to .json.  Playlist items can be moved up and down within their playlist.
* 26/11/2016 - Playlist items can be added and edited.  Main menu and keyboard shortcuts added.
* 27/11/2016 - Playlists can be uploaded to a remote directory via ftp.
* 28/11/2016 - Missing assets are indicated to the user in the playlist view and edit talk view.
* 29/11/2016 - Renamed media directories to more obvious names.  Remote directories are created if necessary on upload.

## installation
* Mutagen is required: pip install mutagen
* Edit the ftp connection details in the file bert_ftp_sample.py and then save the file as bert_ftp.py
