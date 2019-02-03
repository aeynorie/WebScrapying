#! python3
import requests, sys, webbrowser, bs4

res = requests.get("http://www.nagoya-dome.co.jp/sp/eventcalen.php")
res.raise_for_status()
#soup = bs4.BeautifulSoup(res.text)
#print(res.encoding)
soup = bs4.BeautifulSoup(res.text.encode(res.encoding))

#ul = soup.select_one("#tabs-0 > table:nth-of-type(1) > tbody:nth-of-type(1) > tr:nth-of-type(1) > td:nth-of-type(1)")
tdList = soup.select("table > tbody > tr > td")
for td in tdList:
    if td != None:
        print(td)
#print(ul)