import threading
import requests
from bs4 import BeautifulSoup

url_list =["https://www.python.org/success-stories/how-hyperfinity-is-streamlining-its-serverless-architecture-with-snowflakes-snowpark-for-python/","https://www.python.org/success-stories/saving-the-world-with-open-data-and-python/","https://www.python.org/success-stories/python-to-help-meteorologists/"]

def fectch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} charecters from this {url}")
threads = []
for url in url_list:
    thread = threading.Thread(target=fectch_content,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("All Web Pages FEtched")