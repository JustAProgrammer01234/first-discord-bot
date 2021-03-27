import discord

person = discord.Client()

@person.event
async def on_ready():
    print(f'Hello, {person}')

@person.event
async def on_message(message):
    if message.author == person.user:
        return
    if message.content.startswith('$'):
        if message.content == '$':
            await message.channel.send("What are you going to say?")

        elif message.content.replace(' ','') == '$fuckyou':
            await message.channel.send(f"Fuck you, {message.author}")

        elif message.content.replace(' ','') == '$help':
            await message.channel.send("```just say hello.... (Note that Im case sensitive and don't forget to put a dollar sign at the start of your message!)\nor say jojo\nor say fuck you```")

        elif message.content.replace(' ','') == '$hello':
            await message.channel.send('Hello!')

        elif message.content.replace(' ','') == '$jojo':
            await message.channel.send('Golden Wind!')

        else:
            await message.channel.send('Uh what..')


person.run('ODI1Mjg0Mjk2ODc2ODgzOTc5.YF7r5Q.Hox33BBnhsHAHeUeMr8mGLat4yo')