from html import parser
import requests, random
from html.parser import HTMLParser

def return_rended_page(target_url, splash_api):
    try:
        rg = requests.get(splash_api,
                        params={
                            'url': target_url,
                            'wait': 10,
                            'timeout': 60
                        })
        rg.raise_for_status()
        return rg.text
    except requests.exceptions.RequestException as err:
        return "err"
    
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.backno = False
        self.backno_a = False
        self.backno_list = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h2" and "id" in attrs and attrs["id"] == "バックナンバー日付順":
            self.backno = True
        if self.backno and tag == "a":
            self.backno_a = True
    def handle_endtag(self, tag):
        if self.backno and tag == "ul":
            self.backno = False
    def handle_data(self, data):
        if self.backno_a:
            self.backno_list.append(data)
            self.backno_a = False

def extract_urls(rended_text, target_url):
    topic_dict = {}

    parser = MyHTMLParser()
    parser.feed(rended_text)
    parser.close()

    # todays process
    todays_title = random.choice(parser.backno_list)
    todays_index = parser.backno_list.index(todays_title)
    todays_url = "http://www.usupi.org/sysad/" + todays_title[4:7] + ".html"
    topic_dict["todays"] = {"title":todays_title, "url":todays_url}
    # previous process
    try:
        previous_title = parser.backno_list[todays_index+1]
        previous_url = "http://www.usupi.org/sysad/" + previous_title[4:7] + ".html"
    except IndexError:
        previous_title = "No topic. Link to main page."
        previous_url = target_url
    topic_dict["previous"] = {"title":previous_title, "url":previous_url}
    # next process
    try:
        next_title = parser.backno_list[todays_index-1]
        next_url = "http://www.usupi.org/sysad/" + next_title[4:7] + ".html"
    except IndexError:
        next_title = "No topic. Link to main page."
        next_url = target_url
    topic_dict["next"] = {"title":next_title, "url":next_url}
    return topic_dict