from telethon import TelegramClient, events
from decouple import config

# Reemplaza 'tu_api_id', 'tu_api_hash', y 'tu_bot_token' en el archivo .env
api_id = config('API_ID')
api_hash = config('API_HASH')
bot_token = config('BOT_TOKEN')

client = TelegramClient('get_file_id_bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handler(event):
    if event.photo:
        file_id = event.message.media.photo.id
        print(f'File ID: {file_id}')
        await event.reply(f'File ID: {file_id}')

async def main():
    print("Bot está corriendo... Envía una imagen al bot para obtener el File ID.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
