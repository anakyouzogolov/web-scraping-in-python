from bs4 import BeautifulSoup

with open("index.html") as html_file:
    soup = BeautifulSoup(html_file, features="html.parser")


# get all html content
# print(soup.prettify())

#get value tag (title value)
# print(soup.title.string)

# get parent's tag
# print(soup.title.parent.name)

# get class name of tag element like p 
# print(soup.p["class"])

# get all elements with tag name
# paragraphs = soup.find_all("p")
# print(paragraphs)

# find tag element with id
# print(soup.find(id="link2"))

#get tag value with id
# print(soup.find(id="link2").string)

# extracting all text from a page
# print(soup.get_text())

# get attrbs of a tag element
# print(soup.p.attrs) # list all attrbs ofp element

# edit , add , remove a tag's attrbs

# edit
# soup.p["id"] = "new_id"
# print(soup.p)

# remove 
# del soup.p["id"]
# print(soup.p)

# edit a string in place, but you can replace one string with another , using replace_with()

# soup.p.string.replace_with("hola mundo !!")
# print(soup.p)