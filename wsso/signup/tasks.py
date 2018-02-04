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
            	measures=" "
            	if str(row[7])=='Arsenic':
            		measures = "Install arsenic removal systems – either centralized or domestic – and ensure the appropriate disposal of the removed arsenic."
            	if str(row[7])=='Fluoride':
            		measures = "Finding safer local sources of water with lesser or no fluoride. In many fluoride affected places, there is a nearby source of water which is free from fluoride."
            	if str(row[7])=='Salinity':
            		measures = "The palatability of water with a total dissolved solids TDS level of less than about 600 mg per L is generally considered to be good."
            	if str(row[7])=='Iron':
            		measures = "Water containing dissolved iron concentrations less than 2 mg per L may be treated using polyphosphate addition."
            	if str(row[7])=='Nitrate':
            		measures = "There is no simple way to remove all nitrates from your water. Finding and correcting the source of nitrate contamination is the best course of action."
            	send_email(u.Email, "Contamination Alert", "The contaminant in hazardous quantity is "+row[7]+", at your panchayat "+row[4]+" and habitation "+row[6]+". The permissible limit is "+row[8]+" while the current value is "+row[9]+". Please be safe. Safety Measures: " + measures + ".")
            users_matched = []