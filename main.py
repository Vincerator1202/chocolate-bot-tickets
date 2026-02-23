import discord
from discord.commands import Option
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
AUTO_ROLE = int(os.getenv("AUTO_ROLE"))
ANNOUNCEMENT_CHANNEL = int(os.getenv("ANNOUNCEMENT_CHANNEL"))




user_messages = {}

intents = discord.Intents.default()
intents.message_content = True  # für on_message nötig
intents.members = True

bot = discord.Bot(
    intents=intents,
    debug_guilds=[1464742301044707464, 1364024225312276571]
)


@bot.event
async def on_ready():
    print(f"{bot.user} ist online!")

    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Larpix sein neues Video!"
        )
    )


@bot.slash_command(description="Grüße einen User!")
async def greet(ctx, user: Option(discord.Member, "Der User den du grüßen möchtest")):
    embed = discord.Embed(
        title="👋 Begrüßung",
        description=f"Hallo {user.mention}!",
        color=discord.Color.green()
    )
    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
    await ctx.respond(embed=embed)


@bot.slash_command(description="Lass den Bot eine Nachricht senden!")
async def say(
    ctx,
    text: Option(str, "Der Text den der Bot senden soll"),
    channel: Option(discord.TextChannel)
):
    embed = discord.Embed(
        title="📢 Nachricht",
        description=text,
        color=discord.Color.blue()
    )
    await channel.send(embed=embed)
    await ctx.respond("Nachricht gesendet!", ephemeral=True)


@bot.slash_command(description="Zeigt Informationen an!")
async def info(
    ctx,
    alter: Option(int, "Das Alter", min_value=1, max_value=99),
    user: Option(discord.Member, "Gib einen User an!", default=None),
    hobbys: Option(str, "Die Hobbys (z.B. Fußball, Zocken)", default="Nicht angegeben"),
    lieblingsfarbe: Option(str, "Die Lieblingsfarbe", default="Nicht angegeben"),
    lieblingsspiel: Option(str, "Das Lieblingsspiel", default="Nicht angegeben")
):
    if user is None:
        user = ctx.author
    embed = discord.Embed(title="ℹ️ User Info", color=discord.Color.purple())
    embed.add_field(name="👤 User", value=user.mention, inline=False)
    embed.add_field(name="🎂 Alter", value=alter, inline=True)
    embed.add_field(name="🎮 Lieblingsspiel", value=lieblingsspiel, inline=True)
    embed.add_field(name="🎨 Lieblingsfarbe", value=lieblingsfarbe, inline=True)
    embed.add_field(name="⚽ Hobbys", value=hobbys, inline=False)
    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
    await ctx.respond(embed=embed)


@bot.slash_command(description="Zeigt dein Profil an!")
async def profil(
    ctx,
    user: Option(discord.Member, "Welcher User?", default=None)
):
    if user is None:
        user = ctx.author
    embed = discord.Embed(title="👤 Profil", color=discord.Color.gold())
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Account erstellt", value=user.created_at.strftime("%d.%m.%Y"), inline=False)
    embed.add_field(name="Server beigetreten", value=user.joined_at.strftime("%d.%m.%Y"), inline=False)
    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
    embed.set_footer(text=f"Angefragt von {ctx.author}")
    await ctx.respond(embed=embed)


@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(WELCOME_CHANNEL)
    if channel is None:
        return

    embed = discord.Embed(
        title="🎉 Willkommen!",
        description=f"Hey {member.mention}, schön dass du da bist!",
        color=discord.Color.green()
    )

    embed.add_field(name="Mitglieder", value=f"Du bist Mitglied Nr. {member.guild.member_count}")
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
    embed.set_footer(text=f"Server: {member.guild.name}")

    rolle = member.guild.get_role(AUTO_ROLE)
    if rolle:
        await member.add_roles(rolle)

    await channel.send(embed=embed)



if TOKEN is None:
    print("❌ Token nicht gefunden! Bitte überprüfe deine .env Datei.")
    exit()



@bot.slash_command()

async def ankündigung(
    ctx,
    text: Option(str, "Die Ankündigung die der Bot senden soll!"),
    channel: Option(discord.TextChannel)
):
    embed = discord.Embed(
        title="📢 Ankündigung",
        description=text,
        color=discord.Color.red()
    )

    await channel.send(embed=embed)
    await ctx.respond("Ankündigung gesendet!", ephemeral=True)


bot.load_extension("cogs.greet")



bot.run(TOKEN)
