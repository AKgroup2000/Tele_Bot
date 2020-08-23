from Auto_chat import Chatbot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
#cred = credentials.Certificate('/home/test/Downloads/just-49431-firebase-adminsdk-799ct-647b8e2815.json')
cred = credentials.Certificate('/home/test/Telegram/test.json')

firebase_admin.initialize_app(cred)
datab = firestore.client()

import time
old = []

Auto_chat=Chatbot("config.cfg")

def make_reply():
	reply = []
	usersref = datab.collection(u'orders')
	docs = usersref.stream()
	for doc in docs:
		#print('{} : {}'.format(doc.id,doc.to_dict()))
		print("\n")
		src = fetching(doc.to_dict())
		print("\n Source updated = ",src,"\n")
		print(src['address'])  #,"\t",src['Date'])
		#tem=src['address']
		#tem1=src['Name']
		if tem not in old: 
			Auto_chat.send_message(src, id1) #tem => src
			#Auto_chat.send_message(tem1, id1)
			print('Out =', tem)		#,'\t',tem1)
			old.append(tem)

	return reply

def fetching(dic1):
	utc_time = datetime.strptime(dict1['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
	keys=['userid','cleared_by_name','address','total_amount','created_at','status','map_geo_point','items']
	#dic2 = {x:dic1[x] for x in keys}
	#date = datetime.datetime.now()
	delay=datetime.datetime.now() - datetime.timedelta(hours=1)
	if delay < utc_time:
		dic2 = {x:dic1[x] for x in keys}
		return dic2

#id1=-448781380
id1=-452593796 # Test Group007
while True:
	
	update_id=None
	updates = Auto_chat.get_updates(offset=update_id)
	updates = updates["result"]
	print("\n * \n")
	if updates:
		print("\n ** \n")
		for item in updates:
			update_id = item["update_id"]
					
	reply = make_reply()
	print("\n *** \n")
	print("\n ODL Vla = ",old,"\n")
	time.sleep(2)



