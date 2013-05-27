import urllib.request
import xml.dom.minidom as dom
from bs4 import BeautifulSoup

class FetchInformation:
    
    def __init__(self,labels, username, password, parent=None):
        super(FetchInformation, self).__init__()

        self.labels = labels 
        self.passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()

        self.passman.add_password(None, 'http://myanimelist.net/api/anime/search.xml?q=bleach', username, password)
        self.auth_handler = urllib.request.HTTPBasicAuthHandler(self.passman)
        self.opener = urllib.request.build_opener(self.auth_handler)
        urllib.request.install_opener(self.opener)
         
    def fetchInformation(self):
        self.newList = []

        self.websiteData = urllib.request.urlopen('http://myanimelist.net/api/anime/search.xml?q=' + urllib.parse.quote_plus(self.labels[1]))
        soup = BeautifulSoup(self.websiteData.read())
        self.xmlDocument = dom.parseString(soup.decode('UTF-8'))
      
        self.entryList = self.xmlDocument.getElementsByTagName("entry")
        for entry in self.entryList:
            tempEntry = entry.getElementsByTagName("title")
            tempEntry2 = entry.getElementsByTagName("english")
            if tempEntry[0].firstChild.nodeValue.strip() == self.labels[1].strip() or tempEntry2[0].firstChild.nodeValue.strip == self.labels[1].strip():
             
                self.image = entry.getElementsByTagName("image")
                urllib.request.urlretrieve(self.image[0].firstChild.nodeValue, "pictures/" + urllib.parse.quote_plus(self.labels[1] + ".jpg"))
                self.newList.append("pictures/" + urllib.parse.quote_plus(self.labels[1] + ".jpg"))
                        
                self.newList.append(self.labels[1])
                self.newList.append(self.labels[2]) 
                self.newList.append(self.labels[3])

                self.episodes = entry.getElementsByTagName("episodes")
                self.newList.append(self.episodes[0].firstChild.nodeValue)

                self.status = entry.getElementsByTagName("status")
                self.newList.append(self.status[0].firstChild.nodeValue)

                self.airring = entry.getElementsByTagName("start_date")
                self.newList.append(self.airring[0].firstChild.nodeValue)

                self.type = entry.getElementsByTagName("type")
                self.newList.append(self.type[0].firstChild.nodeValue)
                
                self.rating = entry.getElementsByTagName("score")
                self.newList.append(self.rating[0].firstChild.nodeValue)

                self.newList.append(self.labels[9])
                break

        if not self.newList:
                self.image = self.entryList[0].getElementsByTagName("image")
                urllib.request.urlretrieve(self.image[0].firstChild.nodeValue, "pictures/" + urllib.parse.quote_plus(self.labels[1] + ".jpg"))
                self.newList.append("pictures/" + urllib.parse.quote_plus(self.labels[1] + ".jpg"))
                        
                self.newList.append(self.labels[1])
                self.newList.append(self.labels[2]) 
                self.newList.append(self.labels[3])

                self.episodes = self.entryList[0].getElementsByTagName("episodes")
                self.newList.append(self.episodes[0].firstChild.nodeValue)

                self.status = self.entryList[0].getElementsByTagName("status")
                self.newList.append(self.status[0].firstChild.nodeValue)

                self.airring = self.entryList[0].getElementsByTagName("start_date")
                self.newList.append(self.airring[0].firstChild.nodeValue)

                self.type = self.entryList[0].getElementsByTagName("type")
                self.newList.append(self.type[0].firstChild.nodeValue)
                
                self.rating = self.entryList[0].getElementsByTagName("score")
                self.newList.append(self.rating[0].firstChild.nodeValue)

                self.newList.append(self.labels[9])
        return self.newList
