from twython import Twython
import random


class Bot:
    """ The twitter bot class """
    def __init__(self, bot):
        self.twython_obj = Twython(app_key=bot.consumer_key,
                                   app_secret=bot.consumer_secret,
                                   oauth_token=bot.access_token,
                                   oauth_token_secret=bot.access_token_secret)
        self.keywords = bot.keywords
        self.source_user_ids = bot.source_user_ids
        self.source_followers_ids = bot.source_followers_ids
        self.followers_ids = bot.followers_ids


    def get_source_user_ids(self):
        """ Get some users to initiate the twitter bot for the given keywords"""
        source_user_ids = []
        for keyword in self.keywords:
            # get a list of user objects by searching for the keyword
            userlist = self.twython_obj.searchUsers(q=keyword)
            # select 3 random user objects
            random_list = random.sample(userlist, 3)
            # store the screen_name of the 5 users in a list
            ids = [user['id'] for user in random_list]
            #add screen_names to the list of our tweet sources
            source_user_ids = source_user_ids + ids

        for keyword in self.keywords:
            # get a list of recent tweets
            tweetlist = self.twython_obj.search(q=keyword, result_type="recent", lang='en')['results']
            # select 7 random tweets
            random_list = random.sample(tweetlist, 7)
            # store screen_names of users who made the tweets
            ids = [tweet['from_user_id'] for tweet in random_list]
            #add screen_names to the list of our tweet sources
            source_user_ids = source_user_ids + ids

        self.source_user_ids = source_user_ids

        return source_user_ids

    def get_source_followers_ids(self):
        """ Returns a list of all followers of the users in source_users"""
        source_followers_ids = []
        for source_user_id in self.source_user_ids:
            follower_ids = self.twython_obj.getFollowersIDs(user_id=source_user_id)['ids']
            source_followers_ids = source_followers_ids + follower_ids

        self.source_followers_ids = source_followers_ids

        return source_followers_ids

    def find_and_follow(self):
        """ Find users to follow and follow them """
        # Randomly select one keyword from the list of keywords
        keyword = random.choice(self.keywords)
        # Seacrh for tweets with that keyword
        tweets = self.twython_obj.search(q=keyword, result_type="recent", lang='en')['results']

        done_following = False
        while not done_following:
            # Randomly select a tweet
            tweet = random.choice(tweets)
            user_id = tweet['from_user_id']
            if user_id not in self.source_user_ids and user_id not in self.source_followers_ids:
                self.twython_obj.createFriendship(user_id=user_id)
                done_following = True

        return done_following

    def get_follwers(self):
        """ Returns a list of ids of all followers of the bot """
        followers_ids = self.twython_obj.getFollowersIDs(user_id=user_id)['ids']
        self.followers_ids = followers
        return followers_ids

    def copy_and_tweet(self):
        """ Copy a tweet and tweet it """
        

    

