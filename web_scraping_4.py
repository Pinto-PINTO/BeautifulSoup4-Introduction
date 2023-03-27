from bs4 import BeautifulSoup
import re

# 1 - Save Modified HTML Code
with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# Find all input tags where the attribute type is equal to "text "  
tags = doc.find_all("input", type="text")

# Modify each placeholder in each tag
for tag in tags:
    tag['placeholder'] = "Updated placeholder!"
    

# Save these changes in a new HTML file
# Create new file "changed.html"
# Into it write the string of the doc - This means write all of doc's html 
# Doc contains the altered HTML code after running the above modifications
with open("changed.html", "w") as file:
    file.write(str(doc))

