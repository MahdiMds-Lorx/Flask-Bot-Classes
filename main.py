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

	def send_message(self, chat_id, text, parse_mode='markdown', disable_web_page_preview=True, disable_notification=False, reply_to_message_id=None, reply_markup=None,schedule_date=None):
		try:
			u = self.call('sendMessage',chat_id=chat_id, text=text, parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, schedule_date=schedule_date ,reply_markup=reply_markup)
		except:
			pass
		
	def forward_message(self, chat_id, from_chat_id, message_ids, disable_notification=False , as_copy=False):
		try:
			if isinstance(message_ids, list):
				for msg_id in message_ids:
					u = self.call('forwardMessage',chat_id=chat_id, from_chat_id=from_chat_id, message_id=msg_id, disable_notification=disable_notification , as_copy=as_copy)
			else:
				u = self.call('forwardMessage',chat_id=chat_id, from_chat_id=from_chat_id, message_id=msg_id, disable_notification=disable_notification,as_copy=as_copy)
		except:
			pass
		
	def send_photo(self , chat_id , photo , file_ref=None , caption=None , parse_mode = "markdown" , disable_notification=False , reply_to_message_id=None , schedule_time=None , reply_markup=None):
		try:
			u = self.call('sendPhoto' , chat_id=chat_id , photo = photo , file_ref=file_ref , caption=caption , parse_mode=parse_mode , disable_notification=disable_notification , reply_to_message_id=reply_to_message_id , reply_markup=reply_markup)
		except:
			pass
		
	def send_document(self , chat_id , document , file_ref=None , thumb=None , caption=None,parse_mode="markdown" , disable_notification=False , reply_to_message_id=None , schedule_date=None,reply_markup=None):
		try:
			u = self.call('sendDocument' , chat_id=chat_id , document=document , file_ref=file_ref , thumb=thumb , caption=caption , parse_mode=parse_mode , disable_notification=disable_notification , reply_to_message_id=reply_to_message_id , reply_markup=reply_markup , schedule_date=schedule_date)
		except:
			pass
		
	def set_chat_photo(chat_id , photo):
		try:
			u = self.call('setChatPhoto' , chat_id=chat_id , photo=photo)
		except:
			pass
	def delete_chat_photo(chat_id):
		try:
			u = self.call('deleteChatPhoto' , chat_id=chat_id)
		except:
			pass
	def get_chat(chat_id):
		try:
			return self.call('getChat' , chat_id=chat_id)
		except:
			pass
	def get_chat_members_count(chat_id):
		try:
			return self.call('getChatMembersCount' , chat_id=chat_id)
		except:
			pass
	def pin_message(chat_id , message_id , disable_notification=False):
		try:
			u = self.call('pinChatMessage' , chat_id = chat_id , message_id=message_id , disable_notification=disable_notification)
		except:
			pass
	def unpin_message(chat_id):
		try:
			u = self.call('unpinChatMessage' , chat_id=chat_id)
		except:
			pass
	def export_link(chat_id)
		try:
			return self.call('exportChatInviteLink' , chat_id=chat_id)
		except:
			pass
	def kick(chat_id , user_id , until_date=None):
		try:
			u = self.call('kickChatMember' , chat_id=chat_id , user_id=user_id , until_date=until_date)
		except:
			pass
	def unban(chat_id , user_id):
		try:
			u = self.call('unbanChatMember' , chat_id = chat_id ,user_id=user_id)
		except:
			pass
	def leave_chat(chat_id):
		try:
			self.call('leaveChat' , chat_id=chat_id)
		except:
			pass
	def edit_message(chat_id , message_id , text , parse_mode="markdown" , disable_web_page_preview=True , reply_markup=None):
		try:
			u = self.call('editMessageText' , chat_id=chat_id,message_id=message_id,text=text,parse_mode=parse_mode,disable_web_page_preview=disable_web_page_preview,reply_markup=reply_markup)
		except:
			pass
	def edit_message_caption(chat_id , message_id , caption , parse_mode="markdown"  , reply_markup=None):
		try:
			u = self.call('editMessageCaption' , chat_id=chat_id,message_id=message_id,caption=caption,parse_mode=parse_mode,reply_markup=reply_markup)
		except:
			pass
	def edit_message_keyboard(chat_id , message_id , reply_markup=None):
		try:
			u = self.call('editMessageReplyMarkup' , chat_id=chat_id,message_id=message_id,reply_markup=reply_markup)
		except:
			pass
	def send_action(chat_id , action):
		try:
			u = self.call('sendChatAction' , chat_id = chat_id , action=action)
		except:
			pass
@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method=="GET":
        return ""
    else:
        print(request.get_json(force=True))
        Message(str(request.get_json(force=True)))
        return ":)"







