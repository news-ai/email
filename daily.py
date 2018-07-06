# -*- coding: utf-8 -*-
# Local app imports
import es
import analysis
import send_email


def media_lists_to_social_posts(media_lists):
    media_list_to_best_social_posts = {}

    # Loop through all the lists for a particular user
    for media_list in media_lists:
        # Get all the social profiles & feeds for a particular list
        print 'Processing list', media_list['Id']
        contacts = es.get_contacts_social_profiles(media_list)
        if len(contacts) > 0:
            feeds = es.get_feeds_from_list_id(media_list['Id'])
            feeds = feeds['hits']['hits']
            if len(contacts) > 0 or len(feeds) > 0:
                # Has all the social posts for a particular list
                social_posts = es.get_social_posts_for_last_day(
                    contacts, feeds)

                # Now we have all the social posts for a particular list
                # (hopefully)
                if len(social_posts) > 0:
                    posts = analysis.find_best_posts(social_posts)
                    media_list_to_best_social_posts[
                        str(media_list['Id'])] = (posts, contacts, feeds)

    return media_list_to_best_social_posts


def get_email_analytics(user):
    emails = es.get_emails_from_user_id(user)
    analysis_emails = analysis.find_best_email(emails)

    contact_id_to_contact_details = {}
    for email in analysis_emails:
        if 'ContactId' in email and email['ContactId']:
            contact_id_to_contact_details[email['ContactId']] = es.get_contact_details_from_contact_id(email['ContactId'])

    return (analysis_emails, contact_id_to_contact_details)


def process():
    # Get the mapping of user id -> list
    users_to_media_lists = es.users_to_lists()
    # user_id = 5749563331706880
    # Go through each user id
    for user_id in users_to_media_lists.keys():
        print 'Processing user', user_id
        user = users_to_media_lists[user_id][0]
        media_lists = users_to_media_lists[user_id][1]
        # If the user has media lists
        if len(media_lists) > 0:
            # Process all the media lists for a particular user
            print user['Email']
            media_lists_to_best_social_posts = media_lists_to_social_posts(
                media_lists)
            email_analytics = get_email_analytics(user['Id'])
            send_email.email_user_daily_feed(
                user, media_lists, media_lists_to_best_social_posts, email_analytics)

process()
