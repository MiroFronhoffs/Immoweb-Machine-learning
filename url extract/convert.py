import json

with open("page_urls.json", "r") as file:
    dic_page_urls = json.load(file)


urls_list = []
for values in dic_page_urls.values():
    for value in values:
        print(value)
        urls_list.append(value)
print(type(urls_list))

# Save the URLs to a JSON file
with open("url_list.json", "w") as f:
    json.dump(urls_list, f)