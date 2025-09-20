from parser import findLinks
from counter import findData
username = "enter the username"
destinationpath = "enter the destination path"
linksFileName = "enter the links file name"
dataFileName = "enter the data file name"

findLinks(linksFileName,username,destinationpath)
findData(linksFileName,dataFileName,destinationpath)

