from heyoo import WhatsApp
import constants
    
def send(receiver,res):
  ws_message=WhatsApp(constants.FACEBOOK_TOKEN,constants.NUMBER_IDENTIFIER)
  ws_message.send_message(res,receiver)