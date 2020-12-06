import discord

client = discord.Client()
token = 'NzgzNzIzMDU4ODkxNDU2NTIy.X8e4-g.NsQzb4N5Y36OReBPL8hOjdKvmnU'

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('★𝗞𝗢𝗥𝗘𝗔 𝗦𝗘𝗥𝗩𝗘𝗥★')
    await client.change_presence(status=discord.Status.online, activity=game)

    
@client.event
async def on_message(message):
    if message.content.startswith("/출근"):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x80E12A)
                channel = ★전송될 채널 아이디★
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                #embed.set_image(url="")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("/퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0xFF0000)
                channel = ★전송될 채널 아이디★
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
                #embed.set_image(url="")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

client.run(token)
