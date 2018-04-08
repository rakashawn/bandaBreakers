import pytumblr

# AuthenticateS via OAuth, copy from https://api.tumblr.com/console/calls/user/info
client = pytumblr.TumblrRestClient(
  'your_consumer_key',
  'your_consumer_secret',
  'your_token',
  'your_token_secret'
)

client.create_photo(
'your_account_username', 
state=“published”, 
tags=[“raspberrypi”, “picamera”], 
data=“fotos/animateMe.gif"
)
print("uploaded")