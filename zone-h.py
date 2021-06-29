import requests
import re
from bs4 import BeautifulSoup
cookie = {
	"ZHE" : "",
	"PHPSESSID" : ""
}
notiferz=[]
print('Grab Some Notiferz (From 1st 10 pages).....')
for n in range(10):
 usr = requests.get('https://zone-h.org/archive/published=0/page='+str(n+1), cookies=cookie).content
 if 'If you often get this captcha when gathering data' in usr.decode('utf-8'):
  input('Please Go to https://zone-h.org/archive/published=0 And Verify the captcha then press entre ....')
  usr = requests.get('https://zone-h.org/archive/published=0/page='+str(n+1), cookies=cookie).content
 soup = BeautifulSoup(usr, 'html.parser')
 amir=soup.findAll('a')
 for i in range(len(amir)):
  if '/archive/notifier=' in str(amir[i]):
    vv=str(amir[i]).replace('<a href="/archive/notifier=','')
    notif=''
    for j in range(len(vv)-1):
    	if not(vv[j]+vv[j+1]=='">'):
    		notif=notif+vv[j]
    	else:
    		break
    if notif not in notiferz :
    	notiferz.append(notif)
    	open('notiferz.txt','a+').write(notif+'\n')
print('Total Notiferz Grabbed : '+str(len(notiferz)))
sitez=[]
for i in range(len(notiferz)):
 print('Grabbing Sites From : '+str(notiferz[i]))
 for j in range(50):
  verif = requests.get('http://www.zone-h.org/archive/notifier='+str(notiferz[i])+'/page='+str(j+1), cookies=cookie).content
  if 'If you often get this captcha when gathering data' in verif.decode('utf-8'):
   input('Please Go to https://zone-h.org/archive/published=0 And Verify the captcha then press entre ....')
   verif = requests.get('http://www.zone-h.org/archive/notifier='+str(notiferz[i])+'/page='+str(j+1), cookies=cookie).content
  soup = BeautifulSoup(verif, 'html.parser')
  amir=soup.findAll("td", {"class": "defacepages"})
  if '<strong>0</strong>' in str(amir[0]):
  	break
  else:
   verif=verif.decode('utf-8')
   king = re.findall('<td>(.*)\n							</td>',verif)
   for oo in king:
    newurl='http://'+str(oo.split('/')[0])
    if str(newurl) not in sitez :
   	 sitez.append(newurl)
   	 #open(str(notiferz[i])+'.txt','a+').write(newurl+'\n')
   	 open('allsites.txt','a+').write(newurl+'\n')
   	 print(newurl)