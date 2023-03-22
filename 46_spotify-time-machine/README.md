
# Spotify Time Machine

This app was created as coursework for day 46 of Angela Yu's 100 Days of Code Class. It is a simple command line program that prompts the user to enter a date (from 1990-01-01 onwards) and creates a Spotify playlist containing that week's Billboard Hot 100. It currently only searches by the song title which sometimes leads to Spotify picking the wrong song. I will work on fixing that in the future.

To run this program on your machine, you will need to have access to the Spotify API. After creating an app in the API, you will have to set four environment variables or insert in your code:
1) SPOTIPY_CLIENT_ID: your Spotify app's ID
2) SPOTIPY_CLIENT_SECRET: your Spotify app's secret
3) SPOTIPY_REDIRECT_URI: Needs to be the same as the redirect URI you specify in your app's settings
4) SPOTIFY_USER: Your spotify username

The code runs as of 3/22/23, but it seems like Spotify is changing their API access quite frequently. I wrote about 200 lines of code that used previous iterations of Spotify API authorization flows before I found the working one.