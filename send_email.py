# -*- coding: utf-8 -*-
# Stdlib imports
import datetime

# Third-party app imports
import urllib2 as urllib
import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail, Personalization

# Imports from app
from es import get_contact_details_from_contact_id
from email_templates.headline import format_headline, format_footer
from email_templates.news_headlines import format_headlines
from email_templates.email import format_emails
from email_templates.instagram import format_instagram_posts
from email_templates.twitter import format_twitter_posts
from email_templates.category_headline import format_category_headline
from email_templates.construct_email import construct_email
from email_templates.fallbacks import no_lists, no_social_posts
from email_templates.general import format_count

# Initialize Sendgrid
SENDGRID_API_KEY = ''
SENDGRID_SENDER = 'NewsAI Daily <hello@newsai.co>'
sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)


def send_sendgrid_email(email, html):
    # Setup when to send the email
    now = datetime.datetime.now()
    today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)

    # Set the subject
    subject = "Your Daily NewsAI update"
    to_email = Email(email)
    content = Content("text/html", html)
    mail = Mail(
        Email(SENDGRID_SENDER, "NewsAI"), subject, to_email, content)
    mail.personalizations[0].set_send_at(int(today8am.strftime("%s")))
    mail.personalizations[0].add_bcc(Email("dropbox@abhiagarwal.com"))
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except urllib.HTTPError as e:
        print e
    return


def email_user_daily_feed(user, media_lists, posts, emails):
    all_html = ''
    counts = []
    for media_list in media_lists:
        if str(media_list['Id']) in posts:
            social_posts = posts[str(media_list['Id'])][0]
            contacts = posts[str(media_list['Id'])][1]
            feeds = posts[str(media_list['Id'])][2]

            twitter_username_to_id = {}
            instagram_username_to_id = {}
            headlines_feedurl_to_id = {}

            for contact in contacts:
                if 'Twitter' in contact:
                    twitter_username_to_id[contact['Twitter'].lower()] = (
                        contact['Id'], contact['ListId'])
                if 'Instagram' in contact:
                    instagram_username_to_id[contact['Instagram'].lower()] = (
                        contact['Id'], contact['ListId'])

            for feed in feeds:
                single_contact = get_contact_details_from_contact_id(
                    feed['_source']['data']['ContactId'])
                headlines_feedurl_to_id[
                    feed['_source']['data']['FeedURL'].lower()] = (feed['_source']['data']['ListId'], feed['_source']['data']['ContactId'], single_contact)

            twitter_posts = social_posts[0]
            instagram_posts = social_posts[1]
            headlines = social_posts[2]
            social_count = social_posts[3]

            if len(twitter_posts) > 0 or len(instagram_posts) > 0 or len(headlines) > 0:
                headline = media_list['Name']
                list_headline_html = format_headline(
                    media_list['Id'], headline, social_count)
                instagram_html = format_instagram_posts(
                    instagram_posts, instagram_username_to_id, 3)
                twitter_html = format_twitter_posts(
                    twitter_posts, twitter_username_to_id, 3)
                headline_html = format_headlines(
                    headlines, headlines_feedurl_to_id, 3)
                list_footer_html = format_footer()

                if twitter_html != '' or instagram_html[0] > 0 or headline_html != '':
                    counts.append(social_count)
                    html_email_format = list_headline_html + \
                        instagram_html[1] + twitter_html + \
                        headline_html + list_footer_html
                    all_html += html_email_format

    if all_html != '':
        # If the users has lists to share
        if len(counts) > 0:
            all_html += format_count(counts)
            all_html = format_category_headline('Social') + all_html

        # if len(emails[0]) > 0:
        #     email_html = format_category_headline('Email Analytics')
        #     email_format = format_emails(emails, 3)
        #     if email_format != '':
        #         email_html += email_format
        #         all_html = email_html + all_html

        final_html = construct_email(all_html)
        send_sendgrid_email(user['Email'], final_html)
        return

    # If the user has no lists
    if len(media_lists) == 0:
        print 'No media lists'
        final_html = construct_email(no_lists())
        send_sendgrid_email(user['Email'], final_html)
        return

    # # If the user genuinely has no social posts today
    final_html = construct_email(no_social_posts())
    send_sendgrid_email(user['Email'], final_html)
    return
