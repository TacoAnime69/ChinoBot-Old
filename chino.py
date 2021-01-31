import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import os
import time
import json

# Load Environment Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set CMD Prefix
bot = commands.Bot(command_prefix='$')

ROLES = ['cocoa', 'chino', 'rize', 'chiya', 'syaro',
         'maya', 'megu', 'aoyama', 'tippy', 'fuyu']


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def giveme(ctx, *args):
    # await ctx.send(args)
    if not len(args) > 0:
        await ctx.send('Please provide at least one character for a role. I.e. `$giveme chino`')
        return
    for role in args:
        if str(role).lower() not in ROLES:
            await ctx.send('ごめんなさい、{}がありません。\nSorry, {} does not exist as a role.'.format(role, role))
            continue
        roll_name = str(role[0]).capitalize() + str(role[1:]).lower() + ' Fan'
        member = ctx.message.author
        s_role = discord.utils.get(member.guild.roles, name=roll_name)
        await member.add_roles(s_role)
        await ctx.send('Added **{}** for {}'.format(roll_name, str(ctx.author)[:-5]))


@bot.command()
async def rmrole(ctx, *args):
    # await ctx.send(args)
    if not len(args) > 0:
        await ctx.send('Please provide at least one character for a role. I.e. `$rmrole chino`')
        return
    for role in args:
        if str(role).lower() not in ROLES:
            await ctx.send('ごめんなさい、{}がありません。\nSorry, {} does not exist as a role.'.format(role, role))
            continue
        roll_name = str(role[0]).capitalize() + str(role[1:]).lower() + ' Fan'
        member = ctx.message.author
        s_role = discord.utils.get(member.guild.roles, name=roll_name)
        try:
            await member.remove_roles(s_role)
            await ctx.send('Removed **{}** for {}'.format(roll_name, str(ctx.author)[:-5]))
        except discord.Forbidden:
            await ctx.send('Missing permissions')


# Text Commands
class TextComs(commands.Cog):
    """
    docstring
    """
    @commands.command()
    async def hello(self, ctx):
        name = str(ctx.author)[:-5]
        await ctx.send('こんにちは！{}さん (≧▽≦)/\nHello! {}~'.format(name, name))
    
    @commands.command()
    async def gm(self, ctx):
        name = str(ctx.author)[:-5]
        await ctx.send('おはようございます、{}さん (≧▽≦)/\nGood morning! {}~'.format(name, name))

    @commands.command()
    async def gn(self, ctx):
        name = str(ctx.author)[:-5]
        await ctx.send(
            'おやすみなさい, {}さん ／(^ × ^)＼\nGoodnight {}~'.format(name, name)
        )

    @commands.command()
    async def konata(self, ctx):
        await ctx.send('Sorry, I don\'t send pictures of ugly girls...')


@bot.command()
async def about(ctx, args):
    with open('characters.json') as f:
        data = json.load(f)

    if args not in data:
        await ctx.send('Sorry, I don\'t know that one ｡ﾟ･ (>﹏<) ･ﾟ｡')
        return
    # c_color = hex(int(data[args]['color'], 16))
    c_color = 0xffd6e7

    embed = discord.Embed(
        title=data[args]['title'],
        url=data[args]['url'],
        color=c_color)
    embed.set_author(name="About")
    embed.set_thumbnail(url=data[args]['thmb'])
    embed.add_field(name="name-kanji",
                    value=data[args]['name-kanji'], inline=True)
    embed.add_field(name="name-rōmaji",
                    value=data[args]['name-roman'], inline=True)
    embed.add_field(name="Gender", value=data[args]['gender'], inline=True)
    embed.add_field(name="Age", value=data[args]['age'], inline=True)
    embed.add_field(name="Birthday", value=data[args]['bday'], inline=True)
    embed.add_field(name="Hair color",
                    value=data[args]['haircolor'], inline=True)
    embed.add_field(name="Eye color",
                    value=data[args]['eyecolor'], inline=True)
    embed.add_field(name="Height", value=data[args]['height'], inline=True)
    embed.add_field(name="Blood type", value=data[args]['blood'], inline=True)
    embed.add_field(name="Appearance",
                    value=data[args]['appear'], inline=False)
    embed.add_field(name="Personality",
                    value=data[args]['Personality'], inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def hentai(ctx, args):
    # name = args.display_name
    user = await bot.fetch_user(args[3:-1])
    name = user.display_name
    if (name == str(bot.user)[:-5]):
        await ctx.send('no')
        return
    await ctx.send('{}、ヘンタイ…\n{}, you pervert...'.format(name, name))
    await ctx.send(file=discord.File('hentai.jpg'))


# VC Commands
class VCC(commands.Cog):
    """cog desc"""
    @commands.command()
    async def sing(self, ctx, args):
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(
            discord.FFmpegPCMAudio('chino.wav'),
            after=lambda e: print('done', e)
        )
        while vc.is_playing():
            time.sleep(1)
        time.sleep(2)
        await vc.disconnect()

    @commands.command()
    async def vcraid(self, ctx):
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('coom.ogg'),
                after=lambda e: print('done', e))
        while vc.is_playing():
            time.sleep(1)
        time.sleep(2)
        await vc.disconnect()

    @commands.command()
    async def vcjoin(self, ctx):
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        files = os.listdir('Audio')
        choice = random.choice(files)
        time.sleep(1)
        vc.play(discord.FFmpegPCMAudio(os.path.join('Audio', choice)),
                after=lambda e: print('done', e))
        while vc.is_playing():
            time.sleep(1)
        time.sleep(2)
        await vc.disconnect()

    @commands.command()
    async def vconii(self, ctx):
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        time.sleep(1)
        vc.play(discord.FFmpegPCMAudio('chino_oniichan.ogg'),
                after=lambda e: print('done', e))
        while vc.is_playing():
            time.sleep(1)
        time.sleep(2)
        await vc.disconnect()


# Images Commands
class ImageGenerator(commands.Cog):
    """Category Documentation"""

    @commands.command()
    async def coffee(self, ctx):
        await ctx.send(file=discord.File('coffee.png'))

    @commands.command()
    async def greentea(self, ctx):
        await ctx.send(file=discord.File('greentea.png'))

    @commands.command()
    async def chino(self, ctx):
        path = os.path.join('Pictures', 'chino')
        files = os.listdir(path)
        choice = random.choice(files)
        await ctx.send(file=discord.File(os.path.join(path, choice)))

    @commands.command()
    async def cocoa(self, ctx):
        path = os.path.join('Pictures', 'cocoa')
        files = os.listdir(path)
        choice = random.choice(files)
        await ctx.send(file=discord.File(os.path.join(path, choice)))

    @commands.command()
    async def rize(self, ctx):
        path = os.path.join('Pictures', 'rize')
        files = os.listdir(path)
        choice = random.choice(files)
        await ctx.send(file=discord.File(os.path.join(path, choice)))

    @commands.command()
    async def chiya(self, ctx):
        path = os.path.join('Pictures', 'chiya')
        files = os.listdir(path)
        choice = random.choice(files)
        await ctx.send(file=discord.File(os.path.join(path, choice)))

    @commands.command()
    async def syaro(self, ctx):
        path = os.path.join('Pictures', 'syaro')
        files = os.listdir(path)
        choice = random.choice(files)
        await ctx.send(file=discord.File(os.path.join(path, choice)))

    @commands.command()
    async def maya(self, ctx):
        path = os.path.join('Pictures', 'maya')
        files = os.listdir(path)
        choice = random.choice(files)
        await ctx.send(file=discord.File(os.path.join(path, choice)))

    @commands.command()
    async def megu(self, ctx):
        path = os.path.join('Pictures', 'megu')
        files = os.listdir(path)
        choice = random.choice(files)
        await ctx.send(file=discord.File(os.path.join(path, choice)))

    @commands.command()
    async def tippy(self, ctx):
        path = os.path.join('Pictures', 'tippy')
        files = os.listdir(path)
        choice = random.choice(files)
        await ctx.send(file=discord.File(os.path.join(path, choice)))


# Run bot
bot.add_cog(VCC())
bot.add_cog(ImageGenerator())
bot.add_cog(TextComs())
# bot.add_cog(ServComs())

bot.run(TOKEN)
