def grab_url():
    import urlparse
    import requests
    from bs4 import BeautifulSoup as bs

    r = requests.get("http://hib.iiit-bh.ac.in/Hibiscus/Pub/nbDocList.php?client=iiit").text
    #r = requests.get("http://localhost/hib.html").text
    soup = bs(r)

    tr = soup.find_all("tr", class_ = "LOV")
    table = []

    for i in tr:
        td = i.find_all("td")

        for j in range(len(td)):
            td[j] = td[j].get_text()      #1:Date, 2:Title, 3:Posted by, 4:Attention

        url = i.find('a')
        if url is not None:
            url = url.get("href")
            par = urlparse.parse_qs(urlparse.urlparse(url).query)
            docid = par['docid']
            td.append(url)                  #5:url
            td.insert(0, docid[0])        #0:docid

            table.append(td)

    return table

if __name__ == "__main__":
    table = grab_url()
    print table
