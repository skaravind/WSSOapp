from background_task import background
from signup.data.send_email import *
import urllib
from bs4 import BeautifulSoup
import signup.data
from .models import UserDetails


@background(schedule=500)
def email():
    data = []
    for i in range(8):
        page = open("signup/data/Contaminated("+str(i)+")")
        soup = BeautifulSoup(page, "lxml")
        table = soup.find_all("tr")
        rows = []
        for item in table:
            elements = []
            for ele in item.find_all("td"):
                elements.append(ele.text)
            rows.append(elements)
        data.append(rows)
    users = UserDetails.objects
    for district in data:
        for row in district:
            try:
                users_matched = users.filter(Panchayat=row[4])
            except:
                pass
            for u in users_matched:
            	print('ALERT, sending email')
            	send_email(u.Email, 'Contamination Alert', 'The contaminant in hazardous quantity is '+row[7]+', at your panchayat '+row[4]+' and habitation '+row[6]+'. The permissible limit is '+row[8]+' while the current value is '+row[9]+'. Please be safe.')
            users_matched = []