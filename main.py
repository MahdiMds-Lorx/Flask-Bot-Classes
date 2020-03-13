from flask import Flask, request, jsonify

app = Flask(__name__)

class Message:
	def __init__(self, update):
		update =eval(update)
		self.userid = update['message']['from']['id']
		self.is_bot = update['message']['from']['is_bot']
		self.first_name = update['message']['from']['first_name']
		self.username = update['message']['from']['username']
		self.language_code = update['message']['from']['language_code']
		self.username = update['message']['from']['username']
		self.chatid = update['message']['chat']['id']
		self.chatname = update['message']['chat']['first_name']
		self.chatusername = update['message']['chat']['username']
		self.chattype = update['message']['chat']['type']
		self.date = update['message']['date']
		self.text = update['message']['text']
		self.message_id = update['message']['message_id']
		print( self.message_id, self.userid, self.is_bot, self.first_name, self.username, self.language_code, self.username, self.chatid, self.chatname, self.chatusername, self.chattype, self.date, self.text)

class Bot:
	def __init__(self, token):
		self.url = f"https://api.telegram.org/bot{token}/"

	def call(method, **kwargs):
		ar = ""
		n = len(kwargs.keys())
		i = 0
		for en,key,val in zip(kwargs.keys(), kwargs.values()):
			i+=1
			if i == n:
				ar +=f"{key}={val}"
			else:
				ar +=f"{key}={val}&"
		u = f"{self.url}{method}?{ar}"
		return u 

	def send_message(self, chat_id, text, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
		u = self.call('sendmessage',chat_id=chat_id, text=text, parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

	def forward_message(self, chat_id, from_chat_id, message_id, disable_notification);
		u = self.call('forwardmessage',chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id, disable_notification=disable_notification)

	

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method=="GET":
        return ""

    else:
    	
        print(request.get_json(force=True))
        Message(str(request.get_json(force=True)))
        return ":)"







