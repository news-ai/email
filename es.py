# -*- coding: utf-8 -*-
# Stdlib imports
import json
import os

# Third-party app imports
import moment
import certifi
from elasticsearch import Elasticsearch, helpers

# Elasticsearch
ELASTICSEARCH_USER = os.environ['NEWSAI_ELASTICSEARCH_USER']
ELASTICSEARCH_PASSWORD = os.environ['NEWSAI_ELASTICSEARCH_PASSWORD']

# Elasticsearch setup
es = Elasticsearch(
    ['https://search1.newsai.org'],
    http_auth=(ELASTICSEARCH_USER, ELASTICSEARCH_PASSWORD),
    port=443,
    use_ssl=True,
    verify_certs=True,
    ca_certs=certifi.where(),
)


def get_active_email_users():
    query = {
        'size': 5000,
        'from': 0,
        'query': {
            'bool': {
                'must': [{
                    'term': {
                        'data.IsActive': True
                    }
                },  {
                    'term': {
                        'data.GetDailyEmails': True
                    }
                }]
            }
        }
    }

    res = es.search(index='users', doc_type='user', body=query)
    return res


def get_media_lists_for_user(created_by):
    query = {
        'size': 5000,
        'from': 0,
        'query': {
            'bool': {
                'must': [{
                    'term': {
                        'data.CreatedBy': created_by
                    }
                },  {
                    'term': {
                        'data.Archived': False
                    }
                }]
            }
        }
    }

    res = es.search(index='lists', doc_type='list', body=query)
    return res


def get_contacts_from_list_id(list_id):
    query = {
        'size': 5000,
        'from': 0,
        'query': {
            'bool': {
                'must': [{
                    'term': {
                        'data.ListId': list_id
                    }
                },  {
                    'term': {
                        'data.IsDeleted': False
                    }
                }]
            }
        }
    }

    res = es.search(index='contacts', doc_type='contact', body=query)
    return res


def get_emails_from_user_id(user_id):
    date_from = moment.now().locale("US/Eastern").timezone("Europe/London").subtract(days=1).replace(
        hours=0, minutes=0, seconds=0).format('YYYY-MM-DDTHH:mm:ss')
    date_to = moment.now().locale(
        "US/Eastern").timezone("Europe/London").format('YYYY-MM-DDTHH:mm:ss')

    query = {
        'size': 5000,
        'from': 0,
        'sort': [{
            'data.Created': {
                'order': 'desc',
                'mode': 'avg'
            }
        }],
        'query': {
            'bool': {
                'must': [{
                    'term': {
                        'data.CreatedBy': user_id
                    }
                },  {
                    'term': {
                        'data.IsSent': True
                    }
                },  {
                    'range': {
                        'data.Created': {
                            'from': date_from,
                            'to': date_to
                        }
                    }
                }]
            }
        }
    }

    res = es.search(index='emails1', doc_type='email', body=query)
    return res


def get_feeds_from_list_id(list_id):
    query = {
        'size': 5000,
        'from': 0,
        'query': {
            'bool': {
                'must': [{
                    'term': {
                        'data.ListId': list_id
                    }
                },  {
                    'term': {
                        'data.ValidFeed': True
                    }
                }]
            }
        }
    }

    res = es.search(index='rssfeeds', doc_type='feed', body=query)
    return res


def get_users():
    # Get all the users in Es
    # Perhaps have filters to see if they are active users or not.
    users = get_active_email_users()
    users_hits = users['hits']['hits']

    users_data = []
    for user in users_hits:
        new_user = user['_source']['data']
        users_data.append(new_user)

    return users_data


def users_to_lists():
    # Create a mapping from users to media lists
    # Here we go through each user and query datastore for all their lists
    users = get_users()
    user_to_media_list = {}

    for user in users:
        lists = get_media_lists_for_user(user['Id'])
        list_hits = lists['hits']['hits']
        media_lists = []
        for media_list in list_hits:
            new_media_list = media_list['_source']['data']
            media_lists.append(new_media_list)
        user_to_media_list[user['Id']] = [user, media_lists]

    return user_to_media_list


def get_contact_details_from_contact_id(contact_id):
    try:
        res = es.get(index='contacts', doc_type='contact', id=str(contact_id))
        return res['_source'] and res['_source']['data']
    except Exception, e:
        return {}
    return {}


def clean_contact(res):
    social_profiles = {}

    # Get the Twitter and Instagram usernames for this particular social
    # profile
    if res['_source'] and res['_source']['data'] and res['_source']['data']['Twitter']:
        social_profiles['Twitter'] = res['_source'][
            'data']['Twitter'].lower()
        # Add some social information
        social_profiles['ListId'] = res['_source'][
            'data']['ListId']
        social_profiles['Id'] = res['_source'][
            'data']['Id']

    if res['_source'] and res['_source']['data'] and res['_source']['data']['Instagram']:
        social_profiles['Instagram'] = res['_source'][
            'data']['Instagram'].lower()
        # Add some social information
        social_profiles['ListId'] = res['_source'][
            'data']['ListId']
        social_profiles['Id'] = res['_source'][
            'data']['Id']

    return social_profiles


def get_social_posts_for_last_day(contacts, feeds):
    # Get all the social posts from the last day for a particular list
    # A list will be a set of contacts and feeds
    date_from = moment.now().subtract(days=1).replace(
        hours=6, minutes=0, seconds=0).format('YYYY-MM-DDTHH:mm:ss')
    date_to = moment.now().format('YYYY-MM-DDTHH:mm:ss')

    # This might have to be paginated someday. Currently will only load
    # latest 500, but some lists might have a much larger social count.
    # Can do some kind of intelligent querying to also sort by other things
    # as well.
    query = {
        'size': 5000,
        'from': 0,
        'min_score': 0.05,
        'sort': [{
            'data.CreatedAt': {
                'order': 'desc',
                'mode': 'avg'
            }
        }],
        'query': {
            'bool': {
                'must': [{
                    'range': {
                        'data.CreatedAt': {
                            'from': date_from,
                            'to': date_to
                        }
                    }
                }],
                'should': [],
            }
        }
    }

    for contact in contacts:
        if 'Twitter' in contact:
            query['query']['bool']['should'].append({
                'term': {
                    'data.Username': contact['Twitter']
                }
            })

        if 'Instagram' in contact:
            query['query']['bool']['should'].append({
                'term': {
                    'data.InstagramUsername': contact['Instagram']
                }
            })

    for feed in feeds:
        query['query']['bool']['should'].append({
            'term': {
                'data.FeedURL': feed['_source']['data']['FeedURL']
            }
        })

    # Search elasticsearch with this particular query
    res = es.search(index='feeds', doc_type='feed', body=query)

    # If there are results then we return them
    if res['hits']['total'] > 0:
        return res['hits']['hits']
    return {}


def get_contacts_social_profiles(media_list):
    # Loop through contacts and get all of their social profiles from
    # elasticsearch
    contacts = get_contacts_from_list_id(media_list['Id'])
    contacts = contacts['hits']['hits']
    social_posts = []
    for contact in contacts:
        social_post = clean_contact(contact)
        if social_post:
            social_posts.append(social_post)
    return social_posts
