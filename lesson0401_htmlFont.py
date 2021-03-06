# -*- coding: utf-8 -*-
"""
Created on Fri Jul 2 16:03:37 2021

@author: fennieliang

Display a html page
"""
import webbrowser
# open an HTML file on my own (Windows) computer

from lesson_04_class import FileOperate as fo

name = 'example.html'
path = '/Users/fennieliang/Documents/GitHub/python/week07'
string = """<Content-Type: text/html>
 
<!DOCTYPE html>
<html lang="en">
<head>
  <title>HTML Tutorial</title>
  <meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML, CSS, JavaScript">
  <meta name="author" content="Fennie Liang">

</head>

<body>
  <h1 style="color:red">Heading 1</h1>
  <h2>Heading 2</h2>
  <h3 style="color:blue">Heading h3</h3>
  <h4>Heading h4</h4>
  <h5>Heading 5</h5>
  <h6>Heading 6</h6>
  <p>
    Our first <b>HTML</b>, <mark>lesson</mark>, --- <a href="https://sites.google.com/site/fennieliang/"><ins>Fennie Liang</ins></a>.
  </p>

  <p> 
    <del>cross line</del>
  </p>

  <p>
    This <br> is    a paragraph <br> with <br> line     breaks <!-- 這裹的註解文字不會出現在網頁中 -->
  </p>

  <p style="color:green">
    Add green colour to this paragraph.
  </p>

  <p>bullet points:</p>
  <ul>
    <li>Lesson 1</li>
    <li>Lesson 2</li>
    <li>Lesson 3</li>
  </ul>
<p>Auto numbered list:</p>
  <ol>
    <li>Taiwan </li>
    <li>America </li>
    <li>United Kingdom </li>
    <li>France</li>
  </ol>

</body>
</html>
"""
fo.create(path, name, string)

# open an HTML file on my own (Windows) computer, change the path to suit yours
url = "file:///Users/fennieliang/Documents/GitHub/python/week07/example.html"

webbrowser.open_new(url)


