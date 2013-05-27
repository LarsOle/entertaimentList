import xml.dom.minidom as dom

class XMLFileOperations:

    def __init__(self, parent=None):
        super(XMLFileOperations, self).__init__()

    def readXMLFile(self, fileName, tagName, tagList):
        xmlDocument = dom.parse("databases/" + fileName)
        animeList = []
        nodelist = xmlDocument.getElementsByTagName(tagName)
        for node in nodelist:
            tempAnimeList = []
            for i in range(0, len(tagList)):
               tempNode = node.getElementsByTagName(tagList[i])
               tempAnimeList.append(tempNode[0].firstChild.nodeValue)
            animeList.append(tempAnimeList)
        return animeList

    def writeXMLFile(self, databaseName, fileName, tagName, tagList, animeList):
        doc = dom.Document()
        rootTag = databaseName 
      
        root = doc.createElement(rootTag)
        doc.appendChild(root)

        for anime in animeList:
           tagItem = doc.createElement(tagName)
           for i in range(0, len(tagList)) :
               tempElement = doc.createElement(tagList[i])
               textElement = doc.createTextNode(anime[i])
               tempElement.appendChild(textElement)
               tagItem.appendChild(tempElement)
           root.appendChild(tagItem)
        xmlString = doc.toprettyxml(indent='\t')
        xmlFile = open("databases/" + fileName, "wt") 
        xmlFile.write(xmlString)
        xmlFile.close()
