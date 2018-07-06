email_opening = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">'''

email_analytics_opening = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333"><i>{0}</i></div></td></tr></table>'''

email_difference = '''<br>'''
email_closing = '''</div></td></tr></table>'''

def format_emails(emails, limit):
    profiles_link = 'https://tabulae.newsai.co/tables/{0}/{1}'
    # How many emails scheduled
    # How many emails were sent
    # Best responding pitches

    all_emails = emails[0]
    contacts = emails[1]

    emails_html = email_opening + email_analytics_opening.format('Overview')
    emails_html += '<p>You created {0} emails yesterday.</p>'.format(len(all_emails))

    emails_html += email_analytics_opening.format('Best responding pitches')

    count = 0
    for email in all_emails:
        count += 1

        if email['ContactId'] in contacts and contacts[email['ContactId']]:
            print contacts[email['ContactId']]['FirstName']

        if count == limit:
            break

    return emails_html + email_closing
