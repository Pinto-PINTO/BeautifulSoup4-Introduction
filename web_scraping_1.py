from bs4 import BeautifulSoup

# 1 - Reading Html File
# Open index.html in read format and parse the html file.
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# 2 - Prints with indentation
# print(doc.prettify())


# 3 - Find the first tag with the specified tag name
tag = doc.title
tag2 = doc.b
# print(tag)
# print(tag2)


# 4 - String inside the tag
# print(tag.string)


# 5 - Modify string inside of a tag
tag.string = "Menuka Pinto's Title"
# print(tag)
# print(doc.prettify())


# 6 - Find all occurances of a tag
tags = doc.find_all("p")
# print(tags)


# 7 - Find content within a nested tag (index = 0) [First p tag]
tag0 = doc.find_all("p")[1]
tag0_string = tag0.find_all("b")[0]
print(tag0_string)
print(tag0_string.string)




