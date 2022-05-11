# Playist-creator-for-Spotify
A Python script that scrapes the Billboard Top 100 for a given date and creates a Spotify playlist with the available songs.

Instructions:
Create a free Spotify account and open the developer dashboard
create a new app
Set the environmanent variables SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET using your Spotify id and secret
Set http://example.com as Redirect URI in the created Spotify app
Run the script
Click AGREE to give your app the required rights to access your account
Copy the entire URL from the browser and paste it into your Python prompt
Once you completed the steps above you can run the script as often as you like creating playlists for any given date. Make sure to use the correct format (YYYY-MM-DD) when entering the date. Songs not available in your country will be skipped automatically.
