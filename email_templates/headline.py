# -*- coding: utf-8 -*-

headline = '''<table width="600" border="0" cellpadding="0" cellspacing="0" class="force-row" style="width: 600px;">
    <tr>
        <td class="content-wrapper" style="padding-left:24px;padding-right:24px">
            <br>
            <div class="title" style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;color:#374550"><a class="pagerLink" href="https://tabulae.newsai.co/tables/{0}" target="_blank">{1}</a></div>
        </td>
    </tr>
'''

count_sentence = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">Your list has {0} Instagram posts, {1} Twitter posts, and {2} blog posts.</div></td></tr></table>'''

footer = '''</table>'''


def format_headline(list_id, list_name, count):
    return headline.format(list_id, list_name)
    # return headline.format(list_id, list_name) + count_sentence.format(count[0], count[1], count[2])


def format_footer():
    return footer
