import requests
from bs4 import BeautifulSoup

# URL of the first website
url1 = "https://thehackernews.com/"

# URL of the second website
url2 = "https://cyware.com/cyber-security-news-articles"

# Send a request to the first website and get the response
response1 = requests.get(url1)

# Send a request to the second website and get the response
response2 = requests.get(url2)

# Parse the HTML content of the first website
soup1 = BeautifulSoup(response1.text, "html.parser")

# Parse the HTML content of the second website
soup2 = BeautifulSoup(response2.text, "html.parser")

# Extract the information you want from the parsed HTML content of the first website
# For example, you can use the find() method to find a specific HTML element
# and then extract its text or attributes
info1 = soup1.find('div', class_ = "clear home-right").text

# Extract the information you want from the parsed HTML content of the second website
# For example, you can use the find_all() method to find all the HTML elements
# with a specific tag or class, and then loop through the resulting list
# and extract the text or attributes of each element
info2 = []
for item in soup2.find_all("p", {"class": "article"}):
    info2.append(item.text)

# Combine the information from the two websites into a single string
combined_info = info1 + "\n" + "\n".join(info2)

# Save the combined information to an HTML file
with open("scraped_info.html", "w") as file:
    file.write(combined_info)
