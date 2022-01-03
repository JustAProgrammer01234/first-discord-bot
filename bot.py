import discord

person = discord.Client()

def help_message():
    with open('help.txt','r') as f:
        return f.read()

@person.event
async def on_ready():
    print(f'Hello, {person.user}')

@person.event
async def on_message(message):
    if message.author == person.user:
        return
    if message.content.startswith('$'):
        if message.content == '$':
            await message.channel.send("What are you going to say?")

        elif message.content.replace(' ','').lower() == '$fuckyou':
            await message.channel.send(f"Fuck you, {message.author}")

        elif message.content.replace(' ','').lower() == '$help':
            await message.channel.send(help_message())

        elif message.content.replace(' ','').lower() == '$hello' or message.content.replace(' ','').lower() == '$hi':
            await message.channel.send('Hello!')

        elif message.content.replace(' ','').lower() == '$jojo':
            await message.channel.send('Golden Wind!')

        else:
            await message.channel.send('Uh what..')


person.run('token')
