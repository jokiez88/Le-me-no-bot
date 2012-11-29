"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template, flash, url_for, redirect

from models import BotModel
from decorators import login_required, admin_required
from forms import BotForm


def home():
    return redirect(url_for('list_bots'))


def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities"""
    return 'Hello %s' % username

@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

def list_bots():
    """List all bots"""
    bots = BotModel.all()
    form = BotForm()
    if form.validate_on_submit():
        keywords = form.keywords.data.split(',')
        bot = BotModel(
            bot_username=form.bot_username.data,
            consumer_key=form.consumer_key.data,
            consumer_secret=form.consumer_secret.data,
            access_token=form.access_token.data,
            access_token_secret=form.access_token_secret.data,
            keywords=keywords
        )
        try:
            bot.put()
            bot_id = bot.key().id()
            flash(u'Bot %s successfully saved.' % bot.bot_username, 'success')
            return redirect(url_for('list_bots'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_bots'))
    return render_template('list_bots.html', bots=bots, form=form)


def delete_bot(bot_id):
    """Delete an bot object"""
    bot = BotModel.get_by_id(bot_id)
    try:
        bot.delete()
        flash(u'Bot %s successfully deleted.' % bot.bot_username, 'success')
        return redirect(url_for('list_bots'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_bots'))

def activate_bot(bot_id):
    """Activate an bot object"""
    bot = BotModel.get_by_id(bot_id)
    try:
        keywords = bot.keywords
        
        flash(u'Bot %s successfully activated.' % bot.bot_username, 'success')
        return redirect(url_for('list_bots'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_bots'))
