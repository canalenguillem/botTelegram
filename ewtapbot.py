from telethon import TelegramClient, events, Button
from decouple import config

api_id = config('API_ID')
api_hash = config('API_HASH')
bot_token = config('BOT_TOKEN')
web_app_url = config('WEB_APP_URL')

client = TelegramClient('tap_to_earn_bot', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        '¡Bienvenido al bot Tap to Earn! Toca el botón a continuación para abrir la app.',
        buttons=[
            [Button.web_app('Lanzar App', web_app_url)]
        ]
    )
    raise events.StopPropagation

async def main():
    await client.start(bot_token=bot_token)
    print("Bot está corriendo...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
