
x = 'Diazonic' # AIO-Username
y= 'bb69d720de4446128cbbf7bcae1531a4' #AIO-Key

from Adafruit_IO import Client, Feed
aio = Client(x,y)

from telegram.ext import Updater, CommandHandler,MessageHandler, Filters 

def lightoff(bot,update):
    data = aio.send('light', 0)
    rdata = aio.receive('light').value
    chat_id = bot.message.chat_id
    bot.message.reply_text('Request processing')
    update.bot.sendPhoto(chat_id=chat_id, photo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ8jpdHR_pFaoP2Vudl7k-46mSK7I3shuCvFw&usqp=CAU", caption="Light off")
    
def lighton(bot,update):
    data = aio.send('light', 1)
    rdata = aio.receive('light').value
    chat_id = bot.message.chat_id
    bot.message.reply_text('Request Processing')
    update.bot.sendPhoto(chat_id=chat_id, photo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRgKuBghXuR_IjPXnRu9o2znn0O_avidTs-ig&usqp=CAU", caption="Light on")

def acon(bot,update):
    data = aio.send('ac', 1)
    rdata = aio.receive('ac').value
    chat_id = bot.message.chat_id
    bot.message.reply_text('Request processing- AC ON')
    

def acoff(bot,update):
    data = aio.send('ac', 0)
    rdata = aio.receive('ac').value
    chat_id = bot.message.chat_id
    bot.message.reply_text('Request processing- AC OFF')

def tempe(bot,update):
    #data = aio.send('', 1)
    rdata = aio.receive('temp').value
    chat_id = bot.message.chat_id
    bot.message.reply_text(f'The temperature is {rdata} °C')
    
def chooser(bot,update):
          chat_id = bot.message.chat_id
            
          a = bot.message.text

          data1 = aio.receive_previous('light')

          if a == "Light on" or a =="Light ON" or a =="Light On" or a == "LIGHT ON" or a =="light on" and data1 == 0:
                { 
                       lighton(bot,update)
                }
          elif a == "Light off" or a =="Light OFF" or a =="Light Off" or a == "LIGHT OFF" or a =="light off" and data1 == 1:
                {
                        lightoff(bot,update)
                }
          elif a == "AC off":
                {
                        acoff(bot,update)
                }
          elif a == "AC on":
                {
                        acon(bot,update)
                }
          elif a == "what is the temperature" or a =="temp":
                {
                        tempe(bot,update)
                }
          else:
                {
                        bot.message.reply_text('Invalid Text')
                }

def main():
  BOT_TOKEN= '1399670762:AAFaWQo6_Gmx754-9mzwxiLdwg8xRGfC3Fw'
  u = Updater(BOT_TOKEN, use_context=True)
  dp = u.dispatcher
  dp.add_handler(MessageHandler(Filters.text, chooser))
  u.start_polling()
  u.idle()
    
if __name__ == '__main__':
    main()
