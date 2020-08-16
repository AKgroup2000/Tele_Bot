from Auto_chat import Chatbot
from firebase import firebase
firebase = firebase.FirebaseApplication("https://just-49431.firebaseio.com/", None)
res=firebase.get('/just-49431/data/First_table','')
print(res)
reply=[]
'''for a in res:
	#print(a)
	b= firebase.get('/just-49431/data/First_table','{}'.format(a))
	print(b['Email'])'''
Auto_chat=Chatbot("config.cfg")
app=2
def make_reply(msg):
	reply = []
	if msg is not None:
		print(msg, "\t", type(msg))
		if msg == '/Mobile':
			for a in res:
				print("a = ",a)
				b= firebase.get('/just-49431/data/First_table','{}'.format(a))
				print("\n",b,"\t",type(b['Email']),"\n")
				tem=str(b['Email'])
				print(type(tem))
				reply.append(tem)
			print(reply)

		else:
			reply = "Welcome Telegram Chatbot"
	return reply

update_id = None
while True:
	updates = Auto_chat.get_updates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id = item["update_id"]
			try:
				message = str(item["message"]["text"])
			except:
				message = None
			from_ = item["message"]["from"]["id"]
			reply = make_reply(message)
			index=0
			for a in res:
				Auto_chat.send_message(reply[index], from_)
				index+=1
