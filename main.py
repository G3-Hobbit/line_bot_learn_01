from linebot import LineBotApi
from linebot.models import TextSendMessage
import config

line_bot_api = LineBotApi(config.channel_access_token)

def main():
    messages = TextSendMessage(text='おはようございます\n御主人様❤')
    line_bot_api.push_message(config.user_id, messages=messages)

if __name__ == '__main__':
    main()

