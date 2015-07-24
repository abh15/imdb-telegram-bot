
#requires python-telegram-bot,install using-
#pip python-telegram-bot
__author__ = 'MirSpur'

import telegram
import imdb


def main():
    token = "your telegram bot token here"
    bot = telegram.Bot(token)  # Telegram Bot Authorization Token
    ia = imdb.IMDb() # by default access the web.

    global LAST_UPDATE_ID
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id  # Get lastest update

    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID):
            text = update.message.text
            chat_id = update.message.chat.id
            update_id = update.update_id
            if LAST_UPDATE_ID < update_id:
                if text:
                    try:
                    	bot.sendMessage(chat_id=chat_id, text=nome+"\nIMdb rating:"+str(ret))

                        LAST_UPDATE_ID = update_id

                    except:
                        pass



if __name__ == '__main__':
    main()
