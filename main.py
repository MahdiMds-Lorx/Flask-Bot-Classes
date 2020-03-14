from flask import Flask, request, jsonify
from requests import post
app = Flask(__name__)


import imghdr
import mimetypes
import os
from uuid import uuid4

from telegram import TelegramError

DEFAULT_MIME_TYPE = 'application/octet-stream'

def mydoc(document):
    with open('document', 'rb') as f:
        return f
class InputFile(object):
    """This object represents a Telegram InputFile.
    Attributes:
        input_file_content (:obj:`bytes`): The binaray content of the file to send.
        filename (:obj:`str`): Optional, Filename for the file to be sent.
        attach (:obj:`str`): Optional, attach id for sending multiple files.
    Args:
        obj (:obj:`File handler`): An open file descriptor.
        filename (:obj:`str`, optional): Filename for this InputFile.
        attach (:obj:`bool`, optional): Whether this should be send as one file or is part of a
            collection of files.
    Raises:
        TelegramError
    """

    def __init__(self, obj, filename=None, attach=None):
        self.filename = None
        self.input_file_content = obj.read()
        self.attach = 'attached' + uuid4().hex if attach else None

        if filename:
            self.filename = filename
        elif (hasattr(obj, 'name')
              and not isinstance(obj.name, int)  # py3
              and obj.name != '<fdopen>'):  # py2
            # on py2.7, pylint fails to understand this properly
            # pylint: disable=E1101
            self.filename = os.path.basename(obj.name)

        try:
            self.mimetype = self.is_image(self.input_file_content)
        except TelegramError:
            if self.filename:
                self.mimetype = mimetypes.guess_type(
                    self.filename)[0] or DEFAULT_MIME_TYPE
            else:
                self.mimetype = DEFAULT_MIME_TYPE
        if not self.filename:
            self.filename = self.mimetype.replace('/', '.')

    @property
    def field_tuple(self):
        return self.filename, self.input_file_content, self.mimetype

    @staticmethod
    def is_image(stream):
        """Check if the content file is an image by analyzing its headers.
        Args:
            stream (:obj:`str`): A str representing the content of a file.
        Returns:
            :obj:`str`: The str mime-type of an image.
        """
        image = imghdr.what(None, stream)
        if image:
            return 'image/%s' % image

        raise TelegramError('Could not parse file content')

    @staticmethod
    def is_file(obj):
        return hasattr(obj, 'read')

    def to_dict(self):
        if self.attach:
            return 'attach://' + self.attach



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
        u = f"{self.url}{method}
        res = post(u, data=kwargs)
        data = eval(res.text())
        return str(data)

    def send_message(self, chat_id, text, parse_mode='markdown', disable_web_page_preview=True, disable_notification=False, reply_to_message_id=None, reply_markup=None,schedule_date=None):
        try:
            u = self.call('sendMessage',chat_id=chat_id, text=text, parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, schedule_date=schedule_date ,reply_markup=reply_markup)
            
        except Exception as ex:
            return str(ex)
        
    def forward_message(self, chat_id, from_chat_id, message_ids, disable_notification=False , as_copy=False):
        try:
            if isinstance(message_ids, list):
                for msg_id in message_ids:
                    u = self.call('forwardMessage',chat_id=chat_id, from_chat_id=from_chat_id, message_id=msg_id, disable_notification=disable_notification , as_copy=as_copy)
            else:
                u = self.call('forwardMessage',chat_id=chat_id, from_chat_id=from_chat_id, message_id=msg_id, disable_notification=disable_notification,as_copy=as_copy)
        except Exception as ex:
            return str(ex)
        
    def send_photo(self , chat_id , photo , file_ref=None , caption=None , parse_mode = "markdown" , disable_notification=False , reply_to_message_id=None , schedule_time=None , reply_markup=None):
        try:
            u = self.call('sendPhoto' , chat_id=chat_id , photo = photo , file_ref=file_ref , caption=caption , parse_mode=parse_mode , disable_notification=disable_notification , reply_to_message_id=reply_to_message_id , reply_markup=reply_markup)
        except Exception as ex:
            return str(ex)
        
    def send_document(self , chat_id , document , file_ref=None , thumb=None , caption=None,parse_mode="markdown" , disable_notification=False , reply_to_message_id=None , schedule_date=None,reply_markup=None):
        try:
        mahdi = InputFile(mydoc(document))
            u = self.call('sendDocument' , chat_id=chat_id , document=mahdi , file_ref=file_ref , thumb=thumb , caption=caption , parse_mode=parse_mode , disable_notification=disable_notification , reply_to_message_id=reply_to_message_id , reply_markup=reply_markup , schedule_date=schedule_date)
        except Exception as ex:
            return str(ex)
        
    def set_chat_photo(chat_id , photo):
        try:
            u = self.call('setChatPhoto' , chat_id=chat_id , photo=photo)
        except Exception as ex:
            return str(ex)
    def delete_chat_photo(chat_id):
        try:
            u = self.call('deleteChatPhoto' , chat_id=chat_id)
        except Exception as ex:
            return str(ex)
    def get_chat(chat_id):
        try:
            return self.call('getChat' , chat_id=chat_id)
        except Exception as ex:
            return str(ex)
    def get_chat_members_count(chat_id):
        try:
            return self.call('getChatMembersCount' , chat_id=chat_id)
        except Exception as ex:
            return str(ex)
    def pin_message(chat_id , message_id , disable_notification=False):
        try:
            u = self.call('pinChatMessage' , chat_id = chat_id , message_id=message_id , disable_notification=disable_notification)
        except Exception as ex:
            return str(ex)
    def unpin_message(chat_id):
        try:
            u = self.call('unpinChatMessage' , chat_id=chat_id)
        except Exception as ex:
            return str(ex)
    def export_link(chat_id)
        try:
            return self.call('exportChatInviteLink' , chat_id=chat_id)
        except Exception as ex:
            return str(ex)
    def kick(chat_id , user_id , until_date=None):
        try:
            u = self.call('kickChatMember' , chat_id=chat_id , user_id=user_id , until_date=until_date)
        except Exception as ex:
            return str(ex)
    def unban(chat_id , user_id):
        try:
            u = self.call('unbanChatMember' , chat_id = chat_id ,user_id=user_id)
        except Exception as ex:
            return str(ex)
    def leave_chat(chat_id):
        try:
            self.call('leaveChat' , chat_id=chat_id)
        except Exception as ex:
            return str(ex)
    def edit_message(chat_id , message_id , text , parse_mode="markdown" , disable_web_page_preview=True , reply_markup=None):
        try:
            u = self.call('editMessageText' , chat_id=chat_id,message_id=message_id,text=text,parse_mode=parse_mode,disable_web_page_preview=disable_web_page_preview,reply_markup=reply_markup)
        except Exception as ex:
            return str(ex)
    def edit_message_caption(chat_id , message_id , caption , parse_mode="markdown"  , reply_markup=None):
        try:
            u = self.call('editMessageCaption' , chat_id=chat_id,message_id=message_id,caption=caption,parse_mode=parse_mode,reply_markup=reply_markup)
        except Exception as ex:
            return str(ex)
    def edit_message_keyboard(chat_id , message_id , reply_markup=None):
        try:
            u = self.call('editMessageReplyMarkup' , chat_id=chat_id,message_id=message_id,reply_markup=reply_markup)
        except Exception as ex:
            return str(ex)
    def send_action(chat_id , action):
        try:
            u = self.call('sendChatAction' , chat_id = chat_id , action=action)
        except Exception as ex:
            return str(ex)
@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method=="GET":
        return ""
    else:
        print(request.get_json(force=True))
        Message(str(request.get_json(force=True)))
        return ":)"







