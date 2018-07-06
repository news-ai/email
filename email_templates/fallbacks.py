# -*- coding: utf-8 -*-

headline = '''
<table width="600" border="0" cellpadding="0" cellspacing="0" class="force-row" style="width: 600px;">
    <tr>
        <td class="content-wrapper" style="padding-left:24px;padding-right:24px">
            <br>
            <div class="title" style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;color:#374550">{0}</div>
        </td>
    </tr>
'''

response = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">{0}</div></td></tr></table>'''

footer = '''</table>'''


def no_lists():
    return headline.format('You have no lists!') + response.format('To start getting social data login to our platform <a href="https://tabulae.newsai.co/" target="_blank">here</a>!') + footer


def no_social_posts():
    return headline.format('You have no social updates!') + response.format('Add more social contacts on our <a href="https://tabulae.newsai.co/" target="_blank">platform</a>!') + footer
