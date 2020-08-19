from Auto_chat import Chatbot
from firebase import firebase
old =[]
firebase = firebase.FirebaseApplication("https://just-49431.firebaseio.com/", None)
res=firebase.get('just-49431/data/First_table','')
print(res)

Auto_chat=Chatbot("config.cfg")

def upgrage_db(db):
	old = db


def make_reply():
	reply = []
	
	for a in res:
		print("a = ",a)
		b= firebase.get('/just-49431/data/First_table','{}'.format(a))
		print("\n",b,"\t",type(b['Email']),"\n")
		tem=str(b['Email'])
		print(type(tem))
		reply.append(tem)
	print(reply)

	
	return reply

def start():
	update_id=None
	updates = Auto_chat.get_updates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id = item["update_id"]
				
id1=-448781380  # Which is the chat id for the GROUP
while True:
	start()
	reply = make_reply()
	index=0

	for a in res:
		if reply[index] not in old: 
			Auto_chat.send_message(reply[index], id1)
			upgrage_db(reply)
		index+=1
