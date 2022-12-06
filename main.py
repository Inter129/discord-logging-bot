from dhooks import Webhook
import discord
import config as cf


intents = discord.Intents.all()

client = discord.Client(intents=intents)
bot = discord.Bot(intents=intents)

hook = Webhook(cf.webhurl)


@bot.event
async def on_ready():
    print(f'{bot.user}({bot.user.id})으로 로그인 되었습니다.')


@bot.event
async def on_message(message):
    if message.author.id != cf.webid:
        hook.send(f"{message.author}({message.author.id}) : {message.content}")


bot.run(cf.token)
