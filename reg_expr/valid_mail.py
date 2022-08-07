import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

mail = "ap@gmail.com"

a = pattern.search(mail)

print(a)

password_pattern = re.compile("yomen")

password = "yomn"

b = password_pattern.match(password)

print(b)

