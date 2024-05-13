import discord

from settings import *
import dev.instruction as Instruction

from discord.ext import commands
import google.generativeai as ai
import random
import time
from dev.errorhandler import ErrorHandler

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='>', intents=intents)

ai.configure(api_key=AI_KEY)
model = ai.GenerativeModel(
    model_name=Instruction.model_name, 
    generation_config=Instruction.generation_config,
    safety_settings=Instruction.safety_settings,
    system_instruction=Instruction.system_instruction
)

chat = model.start_chat(history=[])

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('meu Irmão pela a Janela', type=3))
    print(f'Nome do Bot: {client.user.name}')
    print(f'Ping do Bot: {client.latency}')

def generateContent(ctx:commands.Context):
    try:
        user = f'{ctx.author} ({ctx.author.global_name}) falou:'
        response = chat.send_message(user+ctx.content).text
        length = len(response)
        if length <= 2000:
            return ctx.reply(response)
        else:
            text_parts = [response[i:i+2000] for i in range(0,length,2000)]
            for i in text_parts: ctx.reply(i)
            return text_parts[len(text_parts)]
    except Exception as e:
        return ctx.send(embed=ErrorHandler(e).embed())

@client.event
async def on_message(ctx: commands.Context):
    if ctx.author.bot:
        return
    
    if client.user in ctx.mentions:
        async with ctx.channel.typing():
            await generateContent(ctx)
    await client.process_commands(ctx)

@client.command()
async def repetir(ctx: commands.Context, arg):
    await ctx.reply(f'{arg}')  

@client.command()
async def ping(ctx: commands.Context):
    await ctx.reply(f'Ping = {client.latency}')  

@client.command()
async def miau(ctx: commands.Context):
    miaus = ""
    for i in range(random.randint(1, 100)):
        miaus += "miau "
    await ctx.send(miaus)

@client.command()
async def ajuda(ctx: commands.Context):
    embed = discord.Embed(title="Painel de Ajuda", description=f'opa {ctx.author.mention}, sou Jubscleudo. O melhor bot de entreterimento do discord! se você precisar de alguma ajuda para saber os comandos, aqui está a lista deles.', color=0xFFFFFF)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/924485124635119666/1131834286832615544/image.png?ex=66372652&is=6635d4d2&hm=a2d93858e1b2672740049fe2438d3cf88ae149d55235da7e9dde80fd3e2f751a&=&format=webp&quality=lossless")
    embed.add_field(name="repetir [texto]", value="Autoexplicativo", inline=True)
    embed.add_field(name="miau", value="este é um comando para me fazer miar.", inline=True)
    embed.add_field(name="calvicemode", value="com esse comando você pode me calvar <:(", inline=True)
    embed.add_field(name="miojo", value="com este comando você pode invocar o Miguel Miojeiro para poder apreciar um delicioso miojo 😋", inline=True)
    embed.add_field(name="dados [número]", value="Role um dado, lembre de especificar o número de lados!", inline=True)
    embed.add_field(name="ping", value="Veja o ping do Bot!", inline=True)
    embed.add_field(name="@Jubscleudo", value="Me Marque para Perguntar Algo!", inline=True)
    embed.set_author(name="GuineaPigUuhh", 
                     url="https://github.com/GuineaPigUuhh",
                     icon_url="https://avatars.githubusercontent.com/u/93527295?s=400&u=f05f46740b146732f2121e2acba51edb0bc6a8f5&v=4"
                     )
    await ctx.reply(embed=embed)

@client.command()
async def calvicemode(ctx: commands.Context):
    embed = discord.Embed(description="Por que você fez isso? to todo tortinho calvinho 😭.", color=0xFFDCAE)
    embed.set_image(url="https://media.discordapp.net/attachments/888062092928774154/1118693038349369354/3510c5f4c7b34b3933548d49f8c4091e.png?ex=66377654&is=663624d4&hm=df641103115f741a5eec35640009f8c5491ef9104451af6e7997d0584d8bdbee&=&format=webp&quality=lossless")
    await ctx.reply(embed=embed)

@client.command()
async def assassinar(ctx: commands.Context, user: discord.User):
    embed = discord.Embed(description=f'PIU PIU!!! {user.mention} FOI ASSASSINADO(A)!!!!', color=0xBF2C2C)
    embed.set_image(url="https://media.discordapp.net/attachments/888062092928774154/1116449666523992185/image.png?ex=66373607&is=6635e487&hm=234e35b48c1ef7504ffea113a4a5a21e5358451e15896b700c9c4029b382749f&=&format=webp&quality=lossless")
    await ctx.reply(embed=embed)

@client.command()
async def miojo(ctx: commands.Context):
    embed = discord.Embed(title="MIOJO!!!",description='graças a mim e ao Miguel Miojeiro você agora pode ter miojo!!!!!!!!', color=0xFFEF66)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1052999558881361930/1126730636674203658/image.png?ex=66370a2d&is=6635b8ad&hm=6996cfc95a537fc8c0719be20fc912072092cf771db66d57692fbe81ef3bef7d&=&format=webp&quality=lossless")
    embed.set_image(url="https://media.discordapp.net/attachments/1126651992966701128/1126729494812708884/miguel_miojeiro.png?ex=6637091d&is=6635b79d&hm=2a51759c1ac50364c9e9cf5e8f7a93009ce31729bd4f56782a2e8526727ae1bd&=&format=webp&quality=lossless&width=1200&height=676")
    await ctx.reply(embed=embed)

@client.command()
async def dados(ctx: commands.Context, arg):
    await ctx.reply("Dados, dados! olha os dados!!!")
    time.sleep(3)
    await ctx.reply(f'🎲 - {random.randint(1, int(arg))}')

@client.command()
async def error(ctx: commands.Context):
    try:
        raise Exception('isso é apenas um Erro de Teste, não fique assustado!')
    except Exception as e:
        await ctx.send(embed=ErrorHandler(e).embed())

@client.command()
async def src(ctx: commands.Context):
    await ctx.reply('https://github.com/GuineaPigUuhh/JubscleudoBot')  

client.run(KEY)

"""
@client.command()
async def template(ctx: commands.Context, arg):
    await ctx.reply(f'{arg}')  
"""