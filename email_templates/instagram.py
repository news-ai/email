# -*- coding: utf-8 -*-

ig_opening = '''<tr>
    <td class="cols-wrapper" style="padding-left:12px;padding-right:12px">
        <!--[if mso]>
  <table border="0" width="576" cellpadding="0" cellspacing="0" style="width: 576px;">
  <tr><td width="192" style="width: 192px;" valign="top"><![endif]-->'''

ig_headline_opening = '''<table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px"><tr><td class="container-padding content" align="left" style="padding-left:12px;padding-right:24px;padding-top:6px;padding-bottom:6px;background-color:#ffffff"><div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333"><i>Instagram posts</i></div></td></tr></table>'''

ig_closing = '''<!--[if mso]></td></tr></table><![endif]-->
    </td>
</tr>'''

single_ig_post = '''<table width="192" border="0" cellpadding="0" cellspacing="0" align="left" class="force-row" style="width: 192px;">
    <tr>
        <td class="col" valign="top" style="padding-left:12px;padding-right:12px;padding-top:18px;padding-bottom:12px">
            <table border="0" cellpadding="0" cellspacing="0" class="img-wrapper">
                <tr>
                    <td style="padding-bottom:18px"><a class="pagerLink" href="{0}" target="_blank"><img src="{1}" border="0" width="168" height="auto" hspace="0" vspace="0" style="max-width:100%;" class="image"></a></td>
                </tr>
            </table>
            <table border="0" cellpadding="0" cellspacing="0">
                <tr>
                    <td class="subtitle" style="font-family:Helvetica, Arial, sans-serif;font-size:16px;line-height:22px;font-weight:600;color:#2469A0;padding-bottom:6px"><a class="pagerLink" href="{2}" target="_blank">@{3}</a></td>
                </tr>
            </table>
            <br>
        </td>
    </tr>
</table>
<!--[if mso]></td><td width="192" style="width: 192px;" valign="top"><![endif]-->'''


def format_instagram_posts(instagram_posts, instagram_username_to_id, limit):
    if len(instagram_posts) > 0:
        profiles_link = 'https://tabulae.newsai.co/tables/{0}/{1}'
        all_html = ''
        count = 0
        for instagram_post in instagram_posts:
            instagram_link = ''
            if instagram_post['InstagramUsername'] in instagram_username_to_id:
                instagram_link = instagram_username_to_id[
                    instagram_post['InstagramUsername']]
                instagram_link = profiles_link.format(
                    instagram_link[1], instagram_link[0])

            if instagram_link != '':
                count += 1
                all_html += single_ig_post.format(instagram_post['InstagramLink'], instagram_post['InstagramImage'], instagram_link, instagram_post['InstagramUsername'])

                if count == limit:
                    break

        if all_html != '':
            return (count, ig_opening + ig_headline_opening + all_html + ig_closing)
    return (0, '')
