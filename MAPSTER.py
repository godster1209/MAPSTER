import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Made by Godster")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("메이플망겜"):
        await message.channel.send("인정")

    if message.content.startswith("/1"):
        embed = discord.Embed(title="토드의 모든것", url="https://m.blog.naver.com/PostView.nhn?blogId=cap1_&logNo=221332045845&proxyReferer=https:%2F%2Fwww.google.com%2F", description="토드 정리", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.author.guild_permissions.administrator == True:
        if message.content.startswith("/테스트"):
            channel = message.content[5:23]
            msg = message.content[24:]
            await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("-1"):
       ## pic = message.content.split("1_1.png")[1]
        await message.channel.send(file=discord.File("1_1.png"))

    if message.content.startswith("-3"):
        await message.channel.send(file=discord.File("1_3.png"))

    if message.content.startswith("-4"):
        await message.channel.send(file=discord.File("1_4.png"))

    #if message.content.startswith("-u"):
    #    Text = ""
    #    learn = message.content.split(" ")
    #    vrsize = len(learn)  # 배열크기
    #    vrsize = int(vrsize)
    #    for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
    #        Text = Text + " " + learn[i]
    #    encText = Text
    #   await message.channel.send(encText)

    









client.run("NzA5NDU2NTE5MzUxMTA3Njk0.XrmMHA.T7ol4H87bINh6zncMYXS2e9XVV4")