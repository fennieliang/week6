# -*- coding: utf-8 -*-
"""
Created on Fri Jul 2 16:03:37 2021

@author: fennieliang


"""
import webbrowser

# open an HTML file on my own (Windows) computer
# Display html tables

with open('example.html', 'w') as f: # writing an HTML file in my local disk
    f.write("<Content-Type: text/html>")
    f.write ("""
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <title>HTML Tutorial</title>
  <meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML, CSS, JavaScript">
  <meta name="author" content="Fennie Liang">

</head>

<body>
  
  <hr>
<table style="width:80%" align="center" border="1">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Mary</td>
    <td>Tomson</td>
    <td>50</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Tait</td>
    <td>80</td>
  </tr>
</table>

</body>
</html>
""")
  
f.close()


# open an HTML file on my own (Windows) computer
url = "file:///Users/fennieliang/Documents/GitHub/python/lesson04/example.html"
webbrowser.open_new(url)

# open a public URL, in this case, the webbrowser docs
#url = "http://google.com"
#webbrowser.open_new(url)

