from pyrogram import Client, filters

app = Client('my_account')

def getStatus():
  file = open('./settings/status.txt', 'r')
  return file.readline()

def setStatus(arg):
  file = open('./settings/status.txt', 'w')
  file.write(arg)
  file.close()

async def isOn_func(_, __, ___):
  return getStatus() == 'on'
isOn = filters.create(isOn_func)

@app.on_message(filters.text & filters.private & ~filters.me & filters.regex('سلام') & isOn)
def reply_handler(client, message):
  message.reply_text('😐🖐🏻')

@app.on_message(filters.me & filters.command('on'))
def bot_on_handler(client, message):
  setStatus('on')
  message.reply_text('i\'m on now')

@app.on_message(filters.me & filters.command('off'))
def bot_on_handler(client, message):
  setStatus('off')
  message.reply_text('i\'m off now')

@app.on_message(filters.me & filters.command('status'))
def bot_on_handler(client, message):
  status = getStatus()
  message.reply_text(f'i\'m {status}')

app.run()
