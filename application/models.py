"""
models.py

App Engine datastore models

"""


from google.appengine.ext import db


class BotModel(db.Model):
	"""Twitter Bot Model"""
	bot_username = db.StringProperty(required=True)
	consumer_key = db.StringProperty(required=True)
	consumer_secret = db.StringProperty(required=True)
	access_token = db.StringProperty(required=True)
	access_token_secret = db.StringProperty(required=True)
	keywords = db.ListProperty(str, required=True)
	activated = db.BooleanProperty(default=False)
	timestamp = db.DateTimeProperty(auto_now_add=True)
