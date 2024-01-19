from pyperclip3 import copy
from sys import stdin
print("Enter list of URLs: \n(Press Ctrl+d twice aftering entering all urls)")
text = stdin.read()
urls = [url for url in text.split("\n")]
new_text = ""

ex_url = urls[0]
first_occurence = ex_url.find("/", 7)

print("")
for i in range(len(urls)):
    urls[i] = str(urls[i])[first_occurence:].lstrip("/").rstrip("/").replace("-", " ")

for url in urls:
    new_text += url+"\n"

new_text = new_text.rstrip("\n")
print(new_text)
copy(new_text)
print(f"All {len(urls)} urls copied to clipboard")
