цвет_фона = "#54aec7"
название_страницы = "резюме"
заголовок_1 = "Мой сайт портфолио"
заголовок_2 = "Мои контакты"
заголовок_3 = "Я в интернете"
ссылка_вк = '"https://vk.com/id260089130"' 
ссылка_githab = '"https://github.com/pupokbomzha/013"'

print("<!DOCTIPE>")

print("<html>")

print("<head>")
print('<title>',название_страницы, '</title>')
print("</head>")

print('<body style="background-color:', цвет_фона, '">')
print("<h1>", заголовок_1, "</h1>")
print("<div>")
print("<h2>", заголовок_2, "</h2>")
print("<div>")
print("<h3>", заголовок_3, "</h3>")
print("<ul>")
print('<li><a href=', ссылка_вк, '>Я в ВК</a></li>')
print('<li><a href=', ссылка_githab, '>Moй репозиторий</a></li>')
print("</ul>")
print("</div>")
print("</div>")
print("</body>")

print("</html>")

