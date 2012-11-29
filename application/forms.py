"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators


class BotForm(wtf.Form):
	bot_username = wtf.TextField('Username', validators=[validators.Required()])
	consumer_key = wtf.TextField('Consumer Key', validators=[validators.Required()])
	consumer_secret = wtf.TextField('Consumer Secret', validators=[validators.Required()])
	access_token = wtf.TextField('Access Token', validators=[validators.Required()])
	access_token_secret = wtf.TextField('Access Token Secret', validators=[validators.Required()])
	keywords = wtf.TextField('Keywords', validators=[validators.Required()])
