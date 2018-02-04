import urllib
from bs4 import BeautifulSoup

def extractData():
	data = []
	for i in range(8):
		page = open("Contaminated("+str(i)+")")
		soup = BeautifulSoup(page, "lxml")
		table = soup.find_all("tr")
		rows = []
		for item in table:
			elements = []
			for ele in item.find_all("td"):
				elements.append(ele.text)
			rows.append(elements)
		data.append(rows)
	return data