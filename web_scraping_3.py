from bs4 import BeautifulSoup
import re
# re -> regular expression




# 1 - Changing attributes of a tag
# <option selected="" value="course-type">
with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    
tag = doc.find("option")
tag['value'] = 'new-course'
tag['selected'] = 'false'
# print(tag)


# 2 - Add an attribute to a tag and assign a value
tag['rating'] = '15'
# print(tag)


# 3 - Display all attributes of a tag
# print(tag.attrs)


# 4 - Find multiple tags
tags = doc.find_all(["p", "div", "li"])
# print(tags)


# 5 - Find tag with certain text
# Option tag having a certain text
# <option value="diploma">Diploma</option>
tag1 = doc.find_all(["option"], string="Diploma")
# print(tag1)


# 6 - Also find an attribute paired with a tag
# <option value="certificate">Certificate</option>
tag2 = doc.find_all(["option"], string="Certificate", value="certificate")
# print(tag2)


# 7 - Find different class names
tag3 = doc.find_all(class_ = 'btn-item')
# print(tag3)



# 8 - Find using regular expression (import re)
# Matching the Dollar Sign "$" and anything that comes after the dollar sign (\ used because $ sign is used)
# Eg: $100, $hello, etc.
tag4 = doc.find_all(string=re.compile("\$.*"))
# print(tag4)


# Make the above in a pretier format by removing spacing
for val in tag4:
    print(val.strip())
    


# 9 - Limit the number of results in a search
tag5= doc.find_all(string=re.compile("course.*"), limit=2)
print(tag5)



