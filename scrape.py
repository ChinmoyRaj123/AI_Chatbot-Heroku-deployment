import requests
from bs4 import BeautifulSoup as soup
# input = "nearby park"

def google_response(text):
    if ("near") in text:
        x = near(text)
        a="\n".join(x)
        return(a)
    elif ("nearby") in text:
        x = near(text)
        a="\n".join(x)
        return(a)
    elif ("now") in text:
        x= now(text)
        return(x)
    elif ("when") in text:
        x= now(text)
        return(x)
    elif ("who") in text:
        x= who(text)
        return(x)
    elif ("what") in text:
        x= who(text)
        return(x)
    elif ("where") in text:
        x= where(text)
        return(x)
    else:
        return("Please ask another question.")

# //near me
def near(text):
    raw_url='https://www.google.com/search?q='+text
    url = requests.get(raw_url)
    page = soup(url.content, 'html.parser')
    results= page.find_all('div', class_="X7NTVe")
    ans=[]
    for i in results:
        name = i.find('div', attrs={'class':'BNeawe deIvCb AP7Wnd'}).text
        ans.append(name)
    return(ans)

# // time now
def now(text):
    raw_url='https://www.google.com/search?q='+text
    url = requests.get(raw_url)
    page = soup(url.content, 'html.parser')
    results= page.find('div', id="main")
    name = results.find('div', attrs={'class':'ZINbbc xpd O9g5cc uUPGi'})
    ans = name.find_all('div', attrs={'class':'BNeawe iBp4i AP7Wnd'})[1].text
    return(ans)

# // who and what
def who(text):
    raw_url='https://www.google.com/search?q='+text
    url = requests.get(raw_url)
    page = soup(url.content, 'html.parser')
    results= page.find('div', id='main')
    name = results.find('div', attrs={'class':'ZINbbc xpd O9g5cc uUPGi'})
    try:
        first = name.find_all('div', attrs={'class':'BNeawe s3v9rd AP7Wnd'})[1].text
        last = name.find_all('div', attrs={'class':'BNeawe s3v9rd AP7Wnd'})[2].text
        first= first.split("...")[0]
        return(first+"\n"+last)
    except:
        first = name.find_all('div', attrs={'class':'BNeawe s3v9rd AP7Wnd'})[1].text
        first= first.split("...")[0]
        return(first)


# //where is this
def where(text):
    raw_url='https://www.google.com/search?q='+text
    url = requests.get(raw_url)
    page = soup(url.content, 'html.parser')
    try:
        results= page.find('div', id='main')
        name = results.find('div', attrs={'class':'ZINbbc xpd O9g5cc uUPGi'})
        ans = name.find_all('div', attrs={'class':'BNeawe iBp4i AP7Wnd'})[1].text
        return(ans)
    except:
        results= page.find('div', class_='ZINbbc xpd O9g5cc uUPGi')
        name = results.find('a').get('href')
        a = name.split(",",2)[2]
        b = a.split("&")[0]
        ans = b.replace("+"," ")
        return(ans)
