# -*- coding: utf-8 -*-

headline_opening = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">'''

news_headline_opening = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333"><i>Blog posts</i></div></td></tr></table>'''

headline_difference = '''<br><br>'''
headline_closing = '''</div></td></tr></table>'''


def format_headlines(headlines, headlines_username_to_id, limit):
    profiles_link = 'https://tabulae.newsai.co/tables/{0}/{1}'
    if len(headlines):
        headlines_html = headline_opening + news_headline_opening
        count = 0

        for headline in headlines:
            if headline['FeedURL'].lower() in headlines_username_to_id:
                count += 1
                feed_data = headlines_username_to_id[
                    headline['FeedURL'].lower()]
                user_profile = profiles_link.format(
                    str(feed_data[0]), str(feed_data[1]))

                # If the name of the user is missing
                full_name = ''
                if 'FirstName' in feed_data[2] and 'LastName' in feed_data[2]:
                    full_name = feed_data[2][
                        'FirstName'] + ' ' + feed_data[2]['LastName']
                if full_name == '' or full_name == ' ':
                    full_name = 'an anonymous author'

                headlines_html += '<a class="pagerLink" href="' + headline['Url'] + \
                    '" target="_blank">' + \
                    headline['Title'] + '</a> by <a class="pagerLink" href="' + user_profile + \
                    '" target="_blank">' + full_name + '</a>'
                headlines_html += headline_difference

                if count == limit:
                    break

        # Checks how many times we actually added headline data
        if count > 0:
            return headlines_html + headline_closing
    return ''
