#!C:\Users\nickm\AppData\Local\Programs\Python\Python310\python.exe

print("Content-type: text/html\n")

#!C:\Python310\python.exe

import cgi, cgitb

form = cgi.FieldStorage()

firstname = form.getvalue("firstName")
lastname = form.getvalue("lastName")
schoolname = form.getvalue("school")

school = "<h2>School: {}</h2>"
firstName = "<h2>First Name: {}</h2>"
lastName = "<h2>Last Name: {}</h2>"

print(school.format(schoolname))
print(firstName.format(firstname))
print(lastName.format(lastname))

