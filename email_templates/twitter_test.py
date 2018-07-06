# -*- coding: utf-8 -*-

twitter_opening = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:12px;padding-bottom:12px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">'''
twitter_single_post = '''{0} by <a class="pagerLink" href="https://tabulae.newsai.co/tables/{1}/{2}" target="_blank">@{3}</a>'''
twitter_difference = '''<br><br>'''
twitter_closing = '''</div></td></tr></table>'''


def format_twitter_posts(twitter_posts, twitter_username_to_id):
    if len(twitter_posts):
        twitter = twitter_opening
        count = 0

        for twitter_post in twitter_posts:
            if twitter_post['Username'].lower() in twitter_username_to_id:
                count += 1
                twitter_data = twitter_username_to_id[
                    twitter_post['Username'].lower()]

                # Properly encode them so they don't screw up in the email
                contact_id = str(twitter_data[0]).encode('utf-8')
                list_id = str(twitter_data[1]).encode('utf-8')
                text = twitter_post['Text'].encode('utf-8')
                username = twitter_post['Username'].encode('utf-8')

                twitter += twitter_single_post.format(
                    text, list_id, contact_id, username)
                twitter += twitter_difference
        # Checks how many times we actually added twitter data
        if count > 0:
            return twitter + twitter_closing
    return ''
