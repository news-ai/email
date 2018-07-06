category_headline = '''<table width="600" border="0" cellpadding="0" cellspacing="0" class="force-row" style="width: 600px;">
    <tr>
        <td class="content-wrapper" style="padding-left:24px;padding-right:24px">
            <br>
            <div class="title" style="font-family:Helvetica, Arial, sans-serif;font-size:24px;font-weight:600;color:#374550">{0}</div>
        </td>
    </tr>
'''


def format_category_headline(category):
    return category_headline.format(category)
