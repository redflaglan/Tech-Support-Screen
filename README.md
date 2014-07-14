Tech-Support-Screen
===================

Install imagemagick, screen, fbida, and pip. Then use pip to install Flask.

Start a screen called tehpix with `screen -S tehpix`, and make it root using sudo su or login. (Disable root login in ssh's config and set a good password on the user you're using. security ain't no thing.)

Run generate.py to produce the initial set of images. Edit it to add more.

Run the web server in another screen (`screen -S webserver`) to be able to add new images easily. The password can be set by writing `SECRET = "something"` to config.py.
