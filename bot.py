import discord
from discord.ext import commands, tasks
import time
import os
from random import choice

client = commands.Bot(command_prefix='?')

status= ["Servers Building", "Communities Growing"]

#-----------------------------------------------------------------------------------------------------------------------------------#
#                                                          Client Events                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------#

@client.event
async def on_ready():
    #set status of the bot
    await client.change_presence(status = discord.Status.online)
    
    # set activity of the bot
    change_status.start()
    await client.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name= "Servers Building"))
    
    print("{0.user} is ready!".format(client))

global owner
global headmod
global mod
global chat_mod
global mute
global lvl60
global lvl50
global lvl35    
global lvl25
global lvl15
global lvl05
global member
global bots

#-----------------------------------------------------------------------------------------------------------------------------------#
#                                                          General Cmds                                                             #
#-----------------------------------------------------------------------------------------------------------------------------------#

#1. Return Latency of bot
@client.command()
async def ping(ctx):
    await ctx.send("{0} ms".format(round(client.latency * 1000)))

#2. Hello command
@client.command()
async def hello(ctx):
    #print this message
    await ctx.send('Hey {0}! Wassup?'.format(ctx.author.mention))

#3. Purge command
@client.command()
async def clear(ctx, amount = 5):
    #remove the 'amount' number  of messages from the channel along with the command itself
    await ctx.channel.purge(limit = amount + 1)


#-----------------------------------------------------------------------------------------------------------------------------------#
#                                                           Bot Build                                                               #
#-----------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------- Rule Module--------------------------------------------------------------#

@client.command()
async def staff_roles(ctx):
    guild= ctx.message.guild
   
    #staff server perms all set
    admin_perms= discord.role.Permissions(administrator= True, manage_guild= True, mention_everyone= True, view_guild_insights= True, view_audit_log= True, connect= True, speak= True, stream= True, priority_speaker= True, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    head_mod_perms= discord.role.Permissions(manage_channels= True, manage_roles= True, manage_permissions= True, manage_emojis= True, view_audit_log= True,  manage_webhooks= True, manage_nicknames= True, manage_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, use_voice_activation= True, priority_speaker= False, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    mod_perms= discord.role.Permissions(manage_channels= True, manage_emojis= True, manage_webhooks= True, create_instant_invite= True, change_nickname= True, manage_nicknames= True, ban_members= True, kick_members= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, manage_messages= True, read_message_history= True, send_tts_messages= True, connect= True, speak= True, stream= True, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    chat_mod_perms= discord.role.Permissions(create_instant_invite= True, change_nickname= True, ban_members= True, kick_members= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, manage_messages= True, read_message_history= True, send_tts_messages= True, connect= True, speak= True, stream= True, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)

    #roles color hex
    headmodhex= "aab2f0"
    modhex= "93ff9e"
    chatmodhex= "702cec"

    #staff roles created
    global owner
    owner= await guild.create_role(name= "Owner", permissions= admin_perms, hoist= True, mentionable= False, color= discord.Color.dark_red())
    global headmod
    headmod= await guild.create_role(name= "Head Mod", permissions= head_mod_perms, mentionable= True, hoist= True, color= discord.Color(int(f"0x{headmodhex}", 16)))
    global mod
    mod= await guild.create_role(name= "Moderator", permissions= mod_perms, mentionable= True, hoist= True, color= discord.Color(int(f"0x{modhex}", 16)))
    global chat_mod
    chat_mod= await guild.create_role(name= "Chat Moderator", permissions= chat_mod_perms, mentionable= False, hoist= True, color= discord.Color(int(f"0x{chatmodhex}", 16)))

    embd = discord.Embed(title= "Staff Roles Created", description="", color = discord.Color.blue())   
    await ctx.send(embed= embd)

@client.command()
async def level_roles(ctx):
    guild= ctx.message.guild
    
    #lvl roles color hex
    lvl60hex= "89efff"
    lvl50hex= "ffdb50"
    lvl35hex= "b2ff7e"
    lvl25hex= "337099"
    lvl15hex= "b674ff"
    lvl05hex= "89efff"

    #roles created
    global lvl60
    lvl60= await guild.create_role(name= "Level 60", hoist= True, mentionable= False, color= discord.Color(int(f"0x{lvl60hex}", 16)))
    global lvl50
    lvl50= await guild.create_role(name= "Level 50", hoist= True, mentionable= False, color= discord.Color(int(f"0x{lvl50hex}", 16)))
    global lvl35
    lvl35= await guild.create_role(name= "Level 35", hoist= True, mentionable= False, color= discord.Color(int(f"0x{lvl35hex}", 16)))
    global lvl25
    lvl25= await guild.create_role(name= "Level 25", hoist= True, mentionable= False, color= discord.Color(int(f"0x{lvl25hex}", 16)))
    global lvl15
    lvl15= await guild.create_role(name= "Level 15", hoist= True, mentionable= False, color= discord.Color(int(f"0x{lvl15hex}", 16)))
    global lvl05
    lvl05= await guild.create_role(name= "Level 05", hoist= False, mentionable= False, color= discord.Color(int(f"0x{lvl05hex}", 16)))

    embd = discord.Embed(title= "Level Roles Created", description="", color = discord.Color.blue())   
    await ctx.send(embed= embd)

@client.command()
async def member_roles(ctx):
    guild= ctx.message.guild

    #member perms all set
    muted_perms= discord.role.Permissions(view_channel= False, send_messages= False, read_message_history= False, add_reactions= False, speak= False, stream= False, request_to_speak= False, create_instant_invite= False)
    member_perms= discord.role.Permissions(view_channel= True, create_instant_invite= True, send_messages= True, add_reactions= True, read_message_history= True, connect= True, speak= True, use_voice_activation= True, request_to_speak= True)
    
    #member roles created
    await guild.create_role(name= "Rule Offender", permissions= muted_perms, mentionable= False, hoist= False)
    global mute
    mute= await guild.create_role(name= "Muted", permissions= muted_perms, mentionable= False, hoist= False)
    global member
    member= await guild.create_role(name= "Member", permissions= member_perms, mentionable= False, hoist= False, color= discord.Color.dark_gold())
    global bots
    bots= await guild.create_role(name= "Bots", hoist= True, mentionable= False)
    await guild.create_role(name= "No XP", hoist= False, mentionable= False)


    embd = discord.Embed(title= "Member Roles Created", description="", color = discord.Color.blue())   
    await ctx.send(embed= embd)

@client.command()
async def culture(ctx):
    guild= ctx.message.guild

    #cultural roles created    
    await guild.create_role(name= "Movie Buff", mentionable= False)
    await guild.create_role(name= "Book Geek", mentionable= False)
    await guild.create_role(name= "Podcast", hoist= True, mentionable= False)
    await guild.create_role(name= "Anime Lover", hoist= False, mentionable= False)
    await guild.create_role(name= "Sports Enthusiast", mentionable= False)
    await guild.create_role(name= "Finance Enthusiast", hoist= True, mentionable= False)
    await guild.create_role(name= "Artist", hoist= True, mentionable= False)
    await guild.create_role(name= "Coder", hoist= True, mentionable= False)
    await guild.create_role(name= "Gamer", hoist= True, mentionable= False)
    await guild.create_role(name= "Pure Science", hoist= False, mentionable= False)

    embd = discord.Embed(title= "Culture Roles Created", description="", color = discord.Color.blue())   
    await ctx.send(embed= embd)

@client.command()
async def all_roles(ctx):
    
    #staff roles created
    await ctx.invoke(client.get_command('staff_roles'))

    #level roles created
    await ctx.invoke(client.get_command('level_roles'))

    #member roles created
    await ctx.invoke(client.get_command('member_roles'))
    
    #culture roles created
    await ctx.invoke(client.get_command('culture'))


#---------------------------------------------------------Welcome Category----------------------------------------------------------#

@client.command()
async def welcome(ctx):
    guild = ctx.message.guild

    #category made
    category = await guild.create_category("Welcome", overwrites=None, reason=None)
    
    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(member, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)   #view_channel= True
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    
    embd = discord.Embed(title= "Wecome Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channel created with synced-perms
    welcome= await guild.create_text_channel("welcome", overwrites= None, category= category, sync_permissions= True)
    rules= await guild.create_text_channel("rules", overwrites= None, category= category, sync_permissions= True)
    updates= await guild.create_text_channel("server-updates", overwrites= None, category= category, sync_permissions= True)
    announce= await guild.create_text_channel("announcements", overwrites= None, category= category, sync_permissions= True)
    await guild.create_text_channel("self-roles", overwrites= None, category= category, sync_permissions= True)
    await guild.create_voice_channel(f"Member Count: {guild.member_count}", overwrites=None, category=category, sync_permissions= True)

    await welcome.send('Take all permissions from **everyone** except for Read Message History | Use Voice Activations from server settings\n Create a permanent invite link **of welcome channel**')
    await rules.send('Make it a rules channel.')
    await updates.send('Make it an Announcement channel channel.')
    await announce.send('Make it an Announcement channel. | Give {0} All permissions except last 2 | Give {1} Permissions to add reactions'.format(headmod.mention, member.mention))

    embd = discord.Embed(title= "Welcome Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#---------------------------------------------------------Youtube Category----------------------------------------------------------#

@client.command()
async def youtube(ctx):
    guild = ctx.message.guild

    #category made
    category = await guild.create_category("YT Stats & Notif", overwrites=None, reason=None)
    
    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(member, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)   #view_channel= True
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    
    embd = discord.Embed(title= "Youtube Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channel created with synced-perms
    video= await guild.create_text_channel("Videos", overwrites= None, category= category, sync_permissions= True)
    await guild.create_text_channel("LiveStream", overwrites= None, category= category, sync_permissions= True)
    await guild.create_voice_channel("Subscribers", overwrites=None, category=category, sync_permissions= True)
    await guild.create_voice_channel("Views", overwrites=None, category=category, sync_permissions= True)
    await guild.create_voice_channel("Videos", overwrites=None, category=category, sync_permissions= True)

    await video.send('Make both announcement channels.')
    embd = discord.Embed(title= "Youtube Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#---------------------------------------------------------General Category----------------------------------------------------------#

@client.command()
async def general(ctx):
    guild= ctx.message.guild
    
    #category made
    category= await guild.create_category("Discussion Zone", overwrites= None, reason= None)

    #lev60 -> embed_links
    #lvl50 -> attach_files
    #lvl25 -> use_external_emptes
    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= True, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= True, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mute, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    await category.set_permissions(lvl60, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= True, attach_files= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)      #view_channel #send_messages= True add_reactions= True #use_external_emojis= True #speak= True
    await category.set_permissions(lvl50, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)     #view_channel #send_messages= True add_reactions= True #use_external_emojis= True #speak= True
    await category.set_permissions(lvl35, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)    #view_channel #send_messages= True add_reactions= True #use_external_emojis= True #speak= True
    await category.set_permissions(lvl25, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)    #view_channel #send_messages= True add_reactions= True #use_external_emojis= True #speak= True
    await category.set_permissions(lvl15, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)   #view_channel #send_messages= True add_reactions= True #speak= True
    await category.set_permissions(lvl05, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)   #view_channel #send_messages= True add_reactions= True #speak= True
    await category.set_permissions(member, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)  #view_channel #send_messages= True add_reactions= True #speak= True
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)

    embd = discord.Embed(title= "Discussion Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    
    #channels created with synced-perms
    await guild.create_text_channel("general-chat", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("book-discussion", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("movie-discussion", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("sports-discussion", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("gaming-discussion", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("anime-discussion", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("pictures", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("memes", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("fan-art", overwrites= None, category= category, reason= None, sync_permissions= True)

    embd = discord.Embed(title= "Discussion Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#---------------------------------------------------------Voice Category-------------------------------------------------------------#

@client.command()
async def voice(ctx):
    guild= ctx.message.guild
    
    #category made
    category= await guild.create_category("Voice Channel", overwrites= None, reason= None)

    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= True, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= True, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mute, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    await category.set_permissions(lvl60, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= True, attach_files= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)      #view_channel #send_messages= True add_reactions= True #use_external_emojis= True #speak= True
    await category.set_permissions(lvl50, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)     #view_channel #send_messages= True add_reactions= True #use_external_emojis= True #speak= True
    await category.set_permissions(member, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)  #view_channel #send_messages= True add_reactions= True #speak= True
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)

    embd = discord.Embed(title= "VC's perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channels created with synced-perms
    await guild.create_text_channel("no-mic-chat", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_voice_channel("General", overwrites= None, category= category, reason= None, sync_permissions= True, user_limit= 60)
    await guild.create_voice_channel("Book discussion", overwrites= None, category= category, reason= None, sync_permissions= True, user_limit= 30)
    await guild.create_voice_channel("Movie discussion", overwrites= None, category= category, reason= None, sync_permissions= True, user_limit= 30)
    await guild.create_voice_channel("Sports discussion", overwrites= None, category= category, reason= None, sync_permissions= True, user_limit= 30)
    await guild.create_voice_channel("Gaming discussion", overwrites= None, category= category, reason= None, sync_permissions= True, user_limit= 30)
    await guild.create_voice_channel("Duo", overwrites= None, category = category, reason= None, sync_permissions= True, user_limit= 2)
    await guild.create_voice_channel("Trio", overwrites= None, category = category, reason= None, sync_permissions= True, user_limit= 3)
    await guild.create_voice_channel("Squad", overwrites= None, category = category, reason= None, sync_permissions= True, user_limit= 4)
    await guild.create_voice_channel("Penta", overwrites= None, category = category, reason= None, sync_permissions= True, user_limit= 5)
    await guild.create_voice_channel("Deca", overwrites= None, category = category, reason= None, sync_permissions= True, user_limit= 10)
    # await guild.create_text_channel("Level 35", overwrites= None, category= category, reason= None)
    
    embd = discord.Embed(title= "VC Category setup Successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#-----------------------------------------------------Miscellaneous Category---------------------------------------------------------#

@client.command()
async def misc(ctx):
    guild= ctx.message.guild

    #category made
    category= await guild.create_category("Miscellaneous", overwrites= None, reason= None)
    
    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= True, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= True, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mute, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    await category.set_permissions(member, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= False, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)  #view_channel= True #send_messages= True add_reactions= True #speak= True
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)

    embd = discord.Embed(title= "Miscellaneous Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channels created with synced-perms
    level= await guild.create_text_channel("level-up", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("check-your-rank-here", overwrites= None, category= category, reason= None, sync_permissions= True)
    dank= await guild.create_text_channel("dank-memer", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("chess", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("casino", overwrites= None, category= category, reason= None, sync_permissions= True)

    await level.send('Take message perms from {0}'.format(member.mention))  
    await dank.send('Disable rob and heist command')
    embd = discord.Embed(title= "Miscellaneous Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#------------------------------------------------------Contact Category---------------------------------------------------------------#

@client.command()
async def contact_staff(ctx):
    guild = ctx.message.guild

    #category created
    category = await guild.create_category("Contact Staff", overwrites=None, reason=None)
    
    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= True, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mute, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    await category.set_permissions(member, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= True, stream= False, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)  #view_channel #send_messages= True add_reactions= True #speak= True
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    
    embd = discord.Embed(title= "Contact Staff Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channel created with synced perms  
    await guild.create_text_channel("help", overwrites= None, category= category, reason= None, sync_permissions= True)
    suggest= await guild.create_text_channel("suggestions", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("complaints", overwrites= None, category= category, reason= None, sync_permissions= True)
    query= await guild.create_text_channel("serious-query", overwrites= None, category= category, reason= None, sync_permissions= True)

    await suggest.send('Give Read Message History to {0}'.format(member.mention))
    await query.send('Give Read Message History to {0}'.format(member.mention))
    
    embd = discord.Embed(title= "Contact Staff Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#-------------------------------------------------------Music Category----------------------------------------------------------------#

@client.command()
async def music(ctx):
    guild= ctx.message.guild

    #category made
    category= await guild.create_category("Music", overwrites= None, reason= None)
    
    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= True, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= True, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mute, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    await category.set_permissions(member, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, embed_links= False, attach_files= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, stream= False, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)  #view_channel= True #send_messages= True add_reactions= True #speak= True
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)

    embd = discord.Embed(title= "Music Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channels created with synced-perms
    await guild.create_text_channel("rythm-commands", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("groovy-commands", overwrites= None, category= category, reason= None, sync_permissions= True)
    jockie= await guild.create_text_channel("jockie-commands", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_voice_channel("Rythm VC", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_voice_channel("Groovy VC", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_voice_channel("Jockie VC", overwrites= None, category= category, reason= None, sync_permissions= True)
    
    await jockie.send('Give perms to only special roles')

    embd = discord.Embed(title= "Music Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#------------------------------------------------------Boosters Category---------------------------------------------------------------#

@client.command()
async def booster_area(ctx):
    guild = ctx.message.guild
    
    #category made
    every_member_owerwrites= {guild.default_role : discord.PermissionOverwrite(view_channel= False), member : discord.PermissionOverwrite(view_channel= False)}
    category = await guild.create_category("Booster Area", overwrites= every_member_owerwrites, reason=None)

    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= True, manage_permissions= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False   , use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mute, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    await category.set_permissions(member, view_channel= False, send_messages= False)
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)

    embd = discord.Embed(title= "Booster Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channels made
    perks= await guild.create_text_channel("booster-perks", overwrites= None, category= category, reason= None)
    boostchat= await guild.create_text_channel("booster-chat", overwrites= None, category= category, reason= None)
    await guild.create_text_channel("custom-colors", overwrites= None, category= category, reason= None)
    await guild.create_voice_channel("Boosters VC", overwrites= None, category= category, reason= None)

    await boostchat.send('Setup Booster perms after the build')
    await perks.send('Take send message perms from **Mods** from booster-perks & custom-colors')

    embd = discord.Embed(title= "Booster Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#-------------------------------------------------------Muted Category----------------------------------------------------------------#

@client.command()
async def muted(ctx):
    guild= ctx.message.guild
    
    #category created
    everyone_owerwrites= {guild.default_role : discord.PermissionOverwrite(view_channel= False)}
    category= await guild.create_category("Muted Jail", overwrites= everyone_owerwrites, reason= None)

    #category pers all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= True, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(mute, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= False, priority_speaker= False, use_voice_activation= True, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    await category.set_permissions(member, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, embed_links= False, attach_files= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    
    embd = discord.Embed(title= "Muted Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channel created with synced perms
    await guild.create_text_channel("muted-instructions", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_text_channel("muted-confessions", overwrites= None, category= category, reason= None, sync_permissions= True)
    await guild.create_voice_channel("Confessions VC", overwrites= None, category= category, reason= None, sync_permissions= True)

    embd = discord.Embed(title= "Muted Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#--------------------------------------------------------Staff Category---------------------------------------------------------------#

@client.command()
async def staff_chat(ctx):
    guild = ctx.message.guild
    
    #category made
    everyone_owerwrites= {guild.default_role : discord.PermissionOverwrite(view_channel= False)}
    category = await guild.create_category("Staff Chat", overwrites= everyone_owerwrites, reason=None)
    
    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(chat_mod, view_channel= True, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= False, embed_links= False, attach_files= False, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= True)
    await category.set_permissions(member, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    await category.set_permissions(bots, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= False, send_messages= False, embed_links= False, attach_files= False, add_reactions= False, use_external_emojis= False, mention_everyone= False, manage_messages= False, read_message_history= False, send_tts_messages= False, use_slash_commands= False, connect= False, speak= False, stream= False, priority_speaker= False, use_voice_activation= False, mute_members= False, deafen_members= False, move_members= False, request_to_speak= False)
    
    embd = discord.Embed(title= "Staff Category perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channel created with synced-perms
    await guild.create_text_channel("community-updates", overwrites= None, category= category, reason= None)
    await guild.create_text_channel("admins", overwrites= None, category= category, reason= None)
    await guild.create_text_channel("mod-chat", overwrites= None, category= category, sync_permissions= True)
    await guild.create_text_channel("bot-setup", overwrites= None, category= category, sync_permissions= True)
    await guild.create_text_channel("bot-commands", overwrites= None, category= category, sync_permissions= True)
    await guild.create_text_channel("no-mic-chat", overwrites= None, category= category, sync_permissions= True)
    await guild.create_voice_channel("Meeting VC", overwrites= None, category= category, sync_permissions= True)

    embd = discord.Embed(title= "Staff Category setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#---------------------------------------------------------Logs Category---------------------------------------------------------------#

@client.command()
async def logs(ctx):
    guild = ctx.message.guild
    
    #category made
    everyone_owerwrites= {guild.default_role : discord.PermissionOverwrite(view_channel= False)}
    category = await guild.create_category("Logs", overwrites= everyone_owerwrites, reason=None)
    
    #category perms all set
    await category.set_permissions(headmod,view_channel= True, manage_channels= True, manage_permissions= True, manage_webhooks= True, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= True, use_slash_commands= True, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    await category.set_permissions(mod, view_channel= False, manage_channels= False, manage_permissions= False, manage_webhooks= False, create_instant_invite= True, send_messages= True, embed_links= True, attach_files= True, add_reactions= True, use_external_emojis= True, mention_everyone= False, manage_messages= False, read_message_history= True, send_tts_messages= False, use_slash_commands= False, connect= True, speak= True, stream= True, priority_speaker= False, use_voice_activation= True, mute_members= True, deafen_members= True, move_members= True, request_to_speak= True)
    
    embd = discord.Embed(title= "Log perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channel created with synced-perms
    await guild.create_text_channel("welcome logs", overwrites= None, category= category, reason= None)
    await guild.create_text_channel("joiners-leavers", overwrites= None, category= category, reason= None)
    await guild.create_text_channel("probot-logs", overwrites= None, category= category, sync_permissions= True)
    await guild.create_text_channel("dyno-logs", overwrites= None, category= category, sync_permissions= True)
    await guild.create_text_channel("carl-bot-logs  ", overwrites= None, category= category, sync_permissions= True)
    await guild.create_text_channel("message", overwrites= None, category= category, sync_permissions= True)

    embd = discord.Embed(title= "Logs setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#------------------------------------------------------Ticket Logs Category-----------------------------------------------------------#

@client.command()
async def ticket_logs(ctx):
    guild = ctx.message.guild

    #category made
    every_member_owerwrites= {guild.default_role : discord.PermissionOverwrite(view_channel= False)}
    category = await guild.create_category("Ticket Logs", overwrites= every_member_owerwrites, reason=None)
    
    #category perms all set
    
    embd = discord.Embed(title= "Ticket-Log perms all set", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

    #channel created with synced-perms
    await guild.create_text_channel("open-close-logs", overwrites= None, category= category, reason= None)
    await guild.create_text_channel("transcript-logs", overwrites= None, category= category, reason= None)

    embd = discord.Embed(title= "Ticket-Log setup successful", description="", color = discord.Color.green())
    await ctx.send(embed= embd)

#-----------------------------------------------------------------------------------------------------------------------------------#
#                                                         Delete Module                                                             #
#-----------------------------------------------------------------------------------------------------------------------------------#

@client.command(help='delete all channels from the server')
async def deleteallch(ctx):
    guild= ctx.message.guild

    for channel in guild.channels:
        await channel.delete()

@client.command(help='delete all roles from the server')            #doesn't work
async def deleterole(ctx):
    guild= ctx.message.guild
    allroles= await guild.fetch_roles()

    for role in allroles:
        if role.id != guild.default_role.id:
            await role.delete()
        else:
            continue

#-----------------------------------------------------------------------------------------------------------------------------------#
#                                                  Customized Category Builds                                                       #
#-----------------------------------------------------------------------------------------------------------------------------------#


    
#-----------------------------------------------------------------------------------------------------------------------------------#
#                                                  Customized Server Builds                                                         #
#-----------------------------------------------------------------------------------------------------------------------------------#

#testing tempelate command
@client.command()
async def tempelato(ctx):   
    
    #starting embed
    embd = discord.Embed(title= "Starting the build process", description="", color = discord.Color.red())
    embd.set_image(url= "https://cdn.discordapp.com/attachments/848848402447466527/850072386036301864/professor_build_start.jpeg")
    await ctx.send(embed= embd)
    
    # channels
    await ctx.invoke(client.get_command('all_roles'))
    await ctx.invoke(client.get_command('welcome'))
    await ctx.invoke(client.get_command('general'))
    await ctx.invoke(client.get_command('voice'))
    await ctx.invoke(client.get_command('misc'))
    await ctx.invoke(client.get_command('music'))
    await ctx.invoke(client.get_command('contact_staff'))
    await ctx.invoke(client.get_command('booster_area'))
    await ctx.invoke(client.get_command('muted'))
    await ctx.invoke(client.get_command('staff_chat'))
    await ctx.invoke(client.get_command('logs'))
    await ctx.invoke(client.get_command('ticket_logs'))

    time.sleep(2)
    #ending embed
    embd = discord.Embed(title= "Server Build is successfull as per the chosen tempelate", description="", color = discord.Color.red())
    embd.set_image(url= "https://cdn.discordapp.com/attachments/848848402447466527/850072390368755792/professor_the_builder.jpg")
    await ctx.send(embed= embd)


#-----------------------------------------------------------------------------------------------------------------------------------#
#                                                              Tasks                                                                #
#-----------------------------------------------------------------------------------------------------------------------------------#

@tasks.loop(seconds= 30)
async def change_status():
    await client.change_presence(activity= discord.Activity(type= discord.ActivityType.watching, name= choice(status)))

#-----------------------------------------------------------------------------------------------------------------------------------#
#                                                            Misc Cmds                                                              #
#-----------------------------------------------------------------------------------------------------------------------------------#

# bot-token
client.run(os.environ['BOT_TOKEN'])


#----------------------------------------------------------------------------------------------------------------------------_#

# overwrites = {
#     guild.default_role: discord.PermissionOverwrite(read_messages=False),
#     guild.me: discord.PermissionOverwrite(read_messages=True)
# }

# channel = await guild.create_text_channel('secret', overwrites=overwrites)
