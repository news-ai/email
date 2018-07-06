# -*- coding: utf-8 -*-

header = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1"> <!-- So that mobile will display zoomed in -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- enable media queries for windows phone 8 -->
  <meta name="format-detection" content="telephone=no"> <!-- disable auto telephone linking in iOS -->
  <title>NewsAI Daily Update</title>
  
  <style type="text/css">
body {
  margin: 0;
  padding: 0;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
table {
  border-spacing: 0;
}
table td {
  border-collapse: collapse;
}
.ExternalClass {
  width: 100%;
}
.ExternalClass,
.ExternalClass p,
.ExternalClass span,
.ExternalClass font,
.ExternalClass td,
.ExternalClass div {
  line-height: 100%;
}
.ReadMsgBody {
  width: 100%;
  background-color: #ebebeb;
}
table {
  mso-table-lspace: 0pt;
  mso-table-rspace: 0pt;
}
img {
  -ms-interpolation-mode: bicubic;
}
.yshortcuts a {
  border-bottom: none !important;
}
@media screen and (max-width: 599px) {
  .force-row,
  .container {
    width: 100% !important;
    max-width: 100% !important;
  }
}
@media screen and (max-width: 400px) {
  .container-padding {
    padding-left: 12px !important;
    padding-right: 12px !important;
  }
}
.ios-footer a {
  color: #aaaaaa !important;
  text-decoration: underline;
}
@media screen and (max-width: 599px) {
  .col {
    width: 100% !important;
    border-top: 1px solid #eee;
    padding-bottom: 0 !important;
  }
  .cols-wrapper {
    padding-top: 18px;
  }
  .img-wrapper {
    float: right;
    max-width: 40% !important;
    height: auto !important;
    margin-left: 12px;
  }
  .subtitle {
    margin-top: 0 !important;
  }
}
@media screen and (max-width: 400px) {
  .cols-wrapper {
    padding-left: 0 !important;
    padding-right: 0 !important;
  }
  .content-wrapper {
    padding-left: 12px !important;
    padding-right: 12px !important;
  }
}
.pagerLink {
    text-decoration: none !important;
}
.btn, .btn:link, .btn:visited {
  border-radius: 0.3em;
  border-style: solid;
  border-width: 1px;
  color: #111;
  display: inline-block;
  font-family: avenir, helvetica, arial, sans-serif;
  letter-spacing: 0.15em;
  margin-bottom: 0.5em;
  padding: 1em 0.75em;
  text-decoration: none;
  text-transform: uppercase;
  -webkit-transition: color 0.4s, background-color 0.4s, border 0.4s;
  transition: color 0.4s, background-color 0.4s, border 0.4s; }

.btn:hover, .btn:focus {
  color: #7FDBFF;
  border: 1px solid #7FDBFF;
  -webkit-transition: background-color 0.3s, color 0.3s, border 0.3s;
  transition: background-color 0.3s, color 0.3s, border 0.3s; }

.btn:active {
  color: #0074D9;
  border: 1px solid #0074D9;
  -webkit-transition: background-color 0.3s, color 0.3s, border 0.3s;
  transition: background-color 0.3s, color 0.3s, border 0.3s; }

/* 

  Sizes 
  
  Small  = .btn--s
  Medium = .btn--m
  Large  = .btn--l

  Code:
  <a href="#" class="btn btn--s">
  <a href="#" class="btn btn--m">
  <a href="#" class="btn btn--l">

*/
.btn--s {
  font-size: 12px; }

.btn--m {
  font-size: 14px; }

.btn--l {
  font-size: 20px;
  border-radius: 0.25em !important; }

/* 

  Layout utility for responsive buttons 

  Code:
  <a href="#" class="btn btn--full">

*/
.btn--full, .btn--full:link {
  border-radius: 0.25em;
  display: block;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  width: 100%; }

/*

  Skins

  * Black & White
  * Grays
  * Colors

  Code:
  <a href="#" class="btn btn--black">
  <a href="#" class="btn btn--white">
  <a href="#" class="btn btn--gray">
  <a href="#" class="btn btn--gray-dark">
  <a href="#" class="btn btn--gray-border">
  <a href="#" class="btn btn--blue">

*/
/* BLACK & WHITE */
.btn--black, .btn--black:link, .btn--black:visited {
  color: #fff;
  background-color: #000; }

.btn--black:hover, .btn--black:focus {
  color: #fff;
  background-color: #777;
  border-color: #777; }

.btn--black:active {
  color: #fff;
  background-color: #999;
  border-color: #999; }

.btn--black:hover, .btn--black:focus {
  background-color: #444; }

.btn--black {
  background-color: #000; }

.btn--gray:link, .btn--gray:visited {
  background-color: #f0f0f0;
  border-color: #f0f0f0;
  color: #555; }

.btn--gray:hover, .btn--gray:focus {
  background-color: #ddd;
  border-color: #ddd;
  color: #444; }

.btn--gray:active {
  background-color: #ccc;
  border-color: #ccc;
  color: #444; }

.btn--gray-border:link, .btn--gray-border:visited {
  background-color: #fff;
  border-color: #555;
  border-width: 2px;
  color: #555; }

.btn--gray-border:hover, .btn--gray-border:focus {
  background-color: #fff;
  border-color: #ddd;
  color: #777; }

.btn--gray-border:active {
  background-color: #ccc;
  border-color: #ccc;
  color: #444; }

.btn--gray-dark:link, .btn--gray-dark:visited {
  background-color: #555;
  color: #eee; }

.btn--gray-dark:hover, .btn--gray-dark:focus {
  background-color: #333;
  border-color: #333;
  color: #eee; }

.btn--gray-dark:active {
  background-color: #777;
  border-color: #777;
  color: #eee; }

/* BLUES */
.btn--blue:link, .btn--blue:visited {
  color: #fff;
  background-color: #0074D9; }

.btn--blue:hover, .btn--blue:focus {
  color: #fff !important;
  background-color: #0063aa;
  border-color: #0063aa; }

.btn--blue:active {
  color: #fff;
  background-color: #001F3F;
  border-color: #001F3F; }

/* Keep it mobile-first and responsive */
@media screen and (min-width: 32em) {
  .btn--full {
    max-width: 16em !important; } }
</style>
</head>

<body style="margin:0; padding:0;" bgcolor="#F0F0F0" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">

<!-- 100% background wrapper (grey background) -->
<table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" bgcolor="#F0F0F0">
  <tr>
    <td align="center" valign="top" bgcolor="#F0F0F0" style="background-color: #F0F0F0;">

      <br>

      <!-- 600px container (white background) -->
      <table border="0" width="600" cellpadding="0" cellspacing="0" class="container" style="width:600px;max-width:600px">
        <tr>
          <td class="container-padding header" align="left" style="font-family:Helvetica, Arial, sans-serif;font-size:24px;font-weight:bold;padding-bottom:12px;color:#DF4726;padding-left:24px;padding-right:24px">
            Your daily NewsAI update
          </td>
        </tr>
        <tr>
          <td class="content" align="left" style="padding-top:12px;padding-bottom:12px;background-color:#ffffff">
'''

footer = '''</td>
        </tr>
        <tr>
          <td class="container-padding footer-text" style="font-family:Helvetica, Arial, sans-serif;font-size:12px;line-height:16px;color:#aaaaaa;padding-left:24px;padding-right:24px" align="center">
          <p><a href="https://tabulae.newsai.co/settings" style="font-size: 14px;"><font color="#000000">Unsubscribe</font></a></p>
            <p><a href="https://newsai.org/" style="font-size: 16px;"><font color="#000000">NewsAI</font></a></p>
          </td>
        </tr>
      </table>
<!--/600px container -->
    </td>
  </tr>
</table>
<!--/100% background wrapper-->

</body>
</html>
'''


def construct_email(middle_html):
    return header + middle_html + footer
