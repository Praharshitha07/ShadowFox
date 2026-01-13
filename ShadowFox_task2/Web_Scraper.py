import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/events/python-events/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

event_list = soup.find("ul", class_="list-recent-events")
events = event_list.find_all("li")

print("\n===== UPCOMING PYTHON EVENTS =====\n")

for i, event in enumerate(events, start=1):
    title = event.find("h3").get_text(strip=True)
    location = event.find("span", class_="event-location").get_text(strip=True)
    date = event.find("time").get_text(" ", strip=True)

    print(f"Event {i}")
    print(f"Name     : {title}")
    print(f"Location : {location}")
    print(f"Date     : {date}")
    print("-" * 40)


