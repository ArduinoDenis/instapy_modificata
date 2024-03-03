import random
from instapy import InstaPy
from instapy import smart_run

# Login credentials
insta_username = ''  # Insert your Instagram username
insta_password = ''  # Insert your Instagram password

# Hashtags that will prevent interactions with photos
dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']

# List of friends to avoid interaction with
friends = ['list of friends I do not want to interact with']

# Hashtags related to your content
like_tag_list = ['travel', 'trip', 'journey', 'beach', 'city', 'travelphotography',
                 'photography', 'travelgram', 'nature', 'wanderlust', 'photooftheday',
                 'instatravel', 'love', 'instagood', 'adventure', 'explore', 'sydney',
                 'ocean', 'traveling', 'landscape', 'holiday', 'summer']

# Users with similar content
accounts = ['USER1', 'USER2', 'USER3', 'USER4', 'USER5', 'USER6']  # Replace with users similar to yours

# Get a session
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  want_check_browser=False)

with smart_run(session):
    # Settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=15000)
    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)

    # Sleep rules
    session.set_action_delays(enabled=True,
                              like=30,
                              comment=29,
                              follow=71,
                              unfollow=28,
                              story=10,
                              randomize=True, random_range_from=70, random_range_to=140)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # Activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)

    session.unfollow_users(amount=random.randint(75, 150),
                           InstapyFollowed=(True, "all"), style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501)

    """ Joining Engagement Pods...
    """
    photo_comments = ['Nice photo! @{}',
                      'I really like your profile! @{}',
                      'Really great content! :thumbsup:',
                      'Just incredible :open_mouth:',
                      'What trick did you use to frame the shot @{}?',
                      'Love your posts @{}',
                      'This looks awesome @{}',
                      'Getting inspired by you. Keep up the good work! @{}',
                      ':raised_hands: Yes!',
                      'I can feel your passion for real! @{} :muscle:']

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(photo_comments, media='Photo')
    session.join_pods(topic='travel')
