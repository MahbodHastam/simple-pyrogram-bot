from pyrogram import Client, filters
from pyrogram.errors import InternalServerError
from functions import *
from filters import *

app = Client('my_account')

@app.on_message(filters.text & filters.private & ~filters.me & filters.regex('سلام') & isOn)
def reply_handler(client, message):
  message.reply_text('😐🖐🏻')

@app.on_message(filters.me & filters.command('on'))
def bot_on_handler(client, message):
  setStatus('on')
  message.reply_text('i\'m on now')

@app.on_message(filters.me & filters.command('off'))
def bot_off_handler(client, message):
  setStatus('off')
  message.reply_text('i\'m off now')

@app.on_message(filters.me & filters.command('status'))
def bot_status_handler(client, message):
  status = getStatus()
  message.reply_text(f'i\'m {status}')

@app.on_message(filters.me & filters.command('setid') & isOn)
def setid_handler(client, message):
  try:
    createFile('./settings/send_message_to_friend/id.txt', message.command[1])
    message.reply_text('Set your message by `/setmsg MESSAGE`')
  except InternalServerError as e:
    message.reply_text('Failed❗️\nCheck your logs.')
    createFile('logs.txt', e)

@app.on_message(filters.me & filters.command('setmsg') & isOn)
def setmsg_handler(client, message):
  try:
    createFile('./settings/send_message_to_friend/message.txt', message.command[1])
    message.reply_text('Send by `/send`')
  except InternalServerError as e:
    message.reply_text('Failed❗️\nCheck your logs.')
    createFile('logs.txt', e)

@app.on_message(filters.me & filters.command('send') & isOn)
def send_handler(client, message):
  try:
    app.send_message(openFile('./settings/send_message_to_friend/id.txt'), openFile('./settings/send_message_to_friend/message.txt'))
    message.reply_text('Message sent.')
  except InternalServerError as e:
    message.reply_text('Failed❗️\nCheck your logs.')
    createFile('logs.txt', e)

app.run()
