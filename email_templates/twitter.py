# -*- coding: utf-8 -*-

twitter_opening = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">'''

new_twitter_opening = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333"><i>Tweets</i></div></td></tr></table>'''

twitter_difference = '''<br><br>'''
twitter_closing = '''</div></td></tr></table>'''


def format_twitter_posts(twitter_posts, twitter_username_to_id, limit):
    if len(twitter_posts):
        twitter = twitter_opening + new_twitter_opening
        count = 0

        for twitter_post in twitter_posts:
            if twitter_post['Username'].lower() in twitter_username_to_id:
                count += 1
                twitter_data = twitter_username_to_id[
                    twitter_post['Username'].lower()]
                twitter += twitter_post['Text'] + ' by <a class="pagerLink" href="https://tabulae.newsai.co/tables/' + str(
                    twitter_data[1]) + '/' + str(twitter_data[0]) + '" target="_blank">@' + twitter_post['Username'] + '</a>'
                twitter += twitter_difference

                if count == limit:
                    break

        # Checks how many times we actually added twitter data
        if count > 0:
            return twitter + twitter_closing
    return ''
