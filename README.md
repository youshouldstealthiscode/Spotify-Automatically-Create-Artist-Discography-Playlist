# Spotify-Automatically-Create-Artist-Discography-Playlist

chatGPT prompt/program description:

write a program that uses the official spotify API. reference the documentation at https://developer.spotify.com/documentation/web-api/reference/* to gather all releases by and including a specific artist-- including all forms of releases e.g. albums, EPs, singles, featured on, any spotify item that includes the artist in any way, etc.-- and creates a playlist titled "<artist's name> + < Discography>". make sure the releases are ordered chronologically by release date. if multiple items are released in the same year, sub-order them in the playlist chronologically by upload date. if there are singles that are also found in the album, remove the singles from the playlist and keep the album. make sure the albums are all internally ordered properly by track number on the album.

------------------------------------------------------------------------------------------------

To create a program that uses the official Spotify API and accomplishes the requested tasks, you need to register your app on the Spotify Developer Dashboard to get the necessary client_id and client_secret.

Here is a Python script using the spotipy library, which is a Python library for the Spotify Web API. You can install it using:

pip install spotipy

------------------------------------------------------------------------------------------------

Replace <your_client_id> and <your_client_secret> with the appropriate values from your registered Spotify Developer application.

This script will prompt you to enter the name of the artist, then it will create a playlist named "<artist's name> Discography" containing all of their releases, including albums, singles, compilations, and tracks they were featured on, in chronological order as specified.

Please note that the Spotify API has rate limits. If you encounter errors, you might want to implement error handling and retries with exponential backoff.
