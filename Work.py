import discord
from discord.ext import commands
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('검은사막 모바일')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
@commands.has_permissions(manage_messages=True)
async def on_message(message):
    if message.content.startswith("/출근"):
        try:
            author = message.guild.get_member(int(message.author.id))
            embed = discord.Embed(color=0x80E12A)
            channel = 740543419079983133
            embed.set_author(name=author, icon_url=message.author.avatar_url)
            embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
            embed.set_footer(text=str(date.year) + "/" + str(date.month) + "/" + str(date.day))
            await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("/퇴근"):
        try:
            author = message.guild.get_member(int(message.author.id))
            embed = discord.Embed(color=0xFF0000)
            channel = 740543419079983133
            embed.set_author(name=author, icon_url=message.author.avatar_url)
            embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
            embed.set_image(url="https://cdn.discordapp.com/attachments/713667320232280086/740542160742383676/Webp.net-resizeimage.gif")
            await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

client.run('NzQwNTQyNjc0NzU4NTMzMTcw.XyqiHA.Dy3ln1ffJQ0WDgok9OJLuMdsuvA')