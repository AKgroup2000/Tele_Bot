from Auto_chat import Chatbot

Auto_chat=Chatbot("config.cfg")

def make_reply(msg):
    reply = None
    if msg is not None:
    	if msg=='Mobile':
    		reply="Mobile Details"

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
            Auto_chat.send_message(reply, from_)


