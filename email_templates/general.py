# -*- coding: utf-8 -*-

count_sentence = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">Since yesterday there's been {0} new Instagram posts, {1} new Twitter posts, and {2} new blog posts for your lists.<br><br><a href="https://tabulae.newsai.co/" class="btn btn--full btn--gray">Check them out!</a></div></td></tr></table>'''


def format_count(counts):
    instagram_posts = 0
    twitter_posts = 0
    blog_posts = 0

    for count in counts:
        instagram_posts += count[0]
        twitter_posts += count[1]
        blog_posts += count[2]

    return count_sentence.format(instagram_posts, twitter_posts, blog_posts)
