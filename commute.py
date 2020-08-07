import discord

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('★표시될 게임이름★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/출근"):
        try:
            # 1명일시 'or message.author.id == ★유저id★' 삭제 / 이상 일시 'or message.author.id == ★유저id★'추가
            if message.author.id == ★유저id★ or message.author.id == ★유저id★:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0x80E12A)
                channel = ★전송될 채널 아이디★
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                embed.set_image(url="★이미지 url★")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("/퇴근"):
        try:
            author = message.guild.get_member(int(message.author.id))
            embed = discord.Embed(color=0xFF0000)
            channel = ★전송될 채널 아이디★
            embed.set_author(name=author, icon_url=message.author.avatar_url)
            embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
            embed.set_image(url="★이미지 url★")
            await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

client.run('★봇 토큰★')
