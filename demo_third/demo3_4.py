from urllib.request import urlopen

url = "https://kivihal.me/itp.html" # Address of the website
f = urlopen(url) #open the website
content = f.read().decode("utf-8") # This reads the website into variable

index_h1 = content.find("<h1>")
index_end_h1 = content.index("</h1>")
print(content[(index_h1+4):index_end_h1])
