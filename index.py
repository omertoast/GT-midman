import discord
from discord.ext import commands
from random import randint
import os
import psutil
import time
import pandas as pd
import asyncio
from discord.ext.commands.cooldowns import BucketType

TOKEN = "NjM3MzgwODQ3ODg4MjM2NTk2.XbNVbg.1Y8VcCCcIL0mSQ34XGNcHhnfub0"
client = commands.Bot(command_prefix = "!")

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def pass_change():
    pass_change.door_pass = str(randint(999,9999))
    f = open("sifre.ahk","r",encoding = 'utf-8')
    lines = f.readlines()
    lines[0] = "pass = {}\n".format(pass_change.door_pass)
    f.close()
    f = open("sifre.ahk","w",encoding = 'utf-8')
    f.writelines(lines)
    f.close()
    return os.startfile("sifre.ahk")

def remove_tag(string):
    string_list = list(string)
    string_list.remove("@")
    string_list.remove("<")
    string_list.remove(">")
    if "!" in string_list:
        string_list.remove("!")
        return "".join(string_list)

    else:
        return "".join(string_list)

bot = commands.Bot(...)

@client.event
async def on_ready():
    print("Discord Bot is ready.")
    bot.GT_guild = client.get_guild(632552291832037381)
    bot.midman_room_t_mention = "<#637765948987801611>"
    bot.midman_room_t = client.get_channel(637765948987801611)
    bot.invite_room_t = client.get_channel(632552291832037385)
    bot.costumer_role = bot.GT_guild.get_role(637594581998895114)
    bot.status = "np" #startingGT,crashed,np
    bot.in_trade = "False" #true,false,siradaki
    bot.action = False
    bot.pass_rights = True
    bot.stage = 0
    bot.satici_iptal = 0
    bot.alici_iptal = 0
    bot.iptal_process = False

    if checkIfProcessRunning('growtopia'):
        print('Yes a growtopia was running')
        print("GT Bot is ready.")
    else:
        print('No growtopia process was running')
        #start_GT()
        bot.status = "startingGT"
        os.startfile(r'D:\Users\omrto\AppData\Local\Growtopia\Growtopia.exe')
        await asyncio.sleep(5)
        os.startfile("startGT.ahk")
        await asyncio.sleep(15)
        bot.status = "np"
        print("GT Bot is ready.")

    bot.istekList = pd.DataFrame(columns= ["COSTUMER1_ID","COSTUMER2_ID"])
    bot.siraList = pd.DataFrame(columns= ["COSTUMER1_ID","COSTUMER2_ID"])

@client.event
async def on_message(message):
    if message.content == "YOU DID IT YOU CRAZY BASTARD":
        await message.channel.send(":sunglasses:")
    await client.process_commands(message)

@client.command()
#@commands.cooldown(1, 10.00 , BucketType.member)
async def istek(ctx,message1):
    if ctx.channel != bot.invite_room_t:
        await ctx.send("Aracılık isteği için {} odasına gidiniz.".format(bot.invite_room_t.mention))
        return
    if bot.status == "startingGT":
        costumer_2 = message1
        await ctx.send("Growtopia başlatılıyor, lütfen bekleyiniz.")
        return

    costumer_1 = "<@" + str(ctx.author.id) + ">"
    costumer_2 = message1
    costumer_2_id = int(remove_tag(costumer_2))
    costumer_1_m = ctx.author
    costumer_1_id = costumer_1_m.id

    if costumer_1_id == costumer_2_id:
        await ctx.send("Kendi kendine istek gönderemezsin")
        
    elif costumer_1_id != costumer_2_id:    
        new_istek = {"COSTUMER1_ID": costumer_1_id,"COSTUMER2_ID": costumer_2_id}
        bot.istekList = bot.istekList.append(new_istek, ignore_index = True)
        await ctx.send("{} Size bir aracılık isteği gönderdi. Kabul etmek için `!kabul`, reddetmek için `!red` yazın. {}".format(costumer_1,costumer_2))
        await asyncio.sleep(10)
        bot.istekList = bot.istekList[bot.istekList.COSTUMER1_ID != costumer_1_id]

@client.command()
async def onaylıyorum(ctx):
    if(ctx.author.id == bot.satici_id or ctx.author.id == bot.alici_id):
        


@client.command()
async def iptal(ctx):
    if(bot.iptal_process == False):
        if(ctx.author.id == bot.satici_id or ctx.author.id == bot.alici_id):
            if(ctx.author.id == bot.satici_id):
                if(bot.alici_iptal == 0):
                    await ctx.send("Satıcı bu aracılık işlemini iptal etmek istiyor, eğer siz de iptal etmek istiyorsanız !iptal yazarak iptal edebilirsiniz " + bot.alici_men)
                    bot.satici_iptal = 1
                else:
                    if(bot.stage == 1):
                        bot.iptal_process = True
                        bot.action = True
                        os.startfile("drop.ahk")
                        await asyncio.sleep(10)
                        bot.action = False
                        await ctx.send("Aracılık işlemi iptal edilmiştir ve bot DL'yi worlde droplamıştır. 4 dakika içinde satıcının DL'sini growtopiatc1 worldünden alması gerekir, aksi taktirde DL'leri yeni aracılık yapanlar alacaktır " + bot.satici_men)
                        await asyncio.sleep(240000)
                        bot.pass_rights = True
                        bot.stage = 0
                        bot.satici_iptal = 0
                        bot.alici_iptal = 0
                        bot.iptal_process = False
                        bot.in_trade = "False"
            else:
                if(bot.satici_iptal == 0):
                    await ctx.send("Alıcı bu aracılık işlemini iptal etmek istiyor, eğer siz de iptal etmek istiyorsanız !iptal yazarak iptal edebilirsiniz " + bot.satici_men)
                    bot.alici_iptal = 1
                
                else:
                    if(bot.stage == 1):
                        bot.iptal_process = True
                        bot.action = True
                        os.startfile("drop.ahk")
                        await asyncio.sleep(10)
                        bot.action = False
                        await ctx.send("Aracılık işlemi iptal edilmiştir ve bot DL'yi worlde droplamıştır. 4 dakika içinde satıcının DL'sini growtopiatc1 worldünden alması gerekir, aksi taktirde DL'leri yeni aracılık yapanlar alacaktır " + bot.satici_men)
                        await asyncio.sleep(240000)
                        bot.pass_rights = True
                        bot.stage = 0
                        bot.satici_iptal = 0
                        bot.alici_iptal = 0
                        bot.iptal_process = False
                        bot.in_trade = "False"
        else:
            await ctx.send("Bu komutu kullanmaya gücün yetmiyor")
    
    else:
        await ctx.send("Ard arda iptal edemezsin")

@client.command()
async def sex(ctx):
    async def aracilik():
        ctx.send("hi")
    
    bot.task = asyncio.ensure_future(aracilik())

@client.command()
async def kabul(ctx,costumer_1: discord.Member):
    if bot.status == "startingGT":
        await ctx.send("Growtopia başlatılıyor, lütfen bekleyiniz.")
        return

    costumer_2_id = ctx.author.id
    if True in bot.istekList["COSTUMER1_ID"].isin([costumer_1.id]).values:
        ananinki = bot.istekList.loc[bot.istekList["COSTUMER1_ID"] == costumer_1.id]

        if True in ananinki["COSTUMER2_ID"].isin([costumer_2_id]).values:
            ananinki2 = ananinki.loc[ananinki["COSTUMER2_ID"] == costumer_2_id]
            if bot.in_trade == "True":
                new_sira = bot.istekList[bot.istekList.COSTUMER2_ID == costumer_2_id]
                bot.siraList.append(new_sira, ignore_index = True)
                siradaki = bot.siraList.tail(1)
                await ctx.send("Aracılık isteğiniz sıraya alınmıştır :notepad_spiral:")
            
            elif bot.in_trade == "False":
                bot.in_trade = "True"
                bot.aktifList = ananinki2
                bot.satici_id = int(ananinki2["COSTUMER1_ID"].values)
                bot.alici_id = int(ananinki2["COSTUMER2_ID"].values)
                bot.satici_men = "<@" + str(bot.satici_id) + ">"
                bot.alici_men = "<@" + str(bot.alici_id) + ">"
                bot.satici_mem = bot.GT_guild.get_member(bot.satici_id)
                bot.alici_mem = bot.GT_guild.get_member(bot.alici_id)
                await bot.satici_mem.create_dm()
                await bot.alici_mem.create_dm()
                bot.satici_DM = bot.satici_mem.dm_channel
                bot.alici_DM = bot.alici_mem.dm_channel
                await ctx.send("Aracılık işlemi başlatıldı {} :tools: {}.\n{}'na giderek aracılık işleminizi sürdürebilirsiniz.".format(bot.satici_men,bot.alici_men,bot.midman_room_t_mention))
                
                if checkIfProcessRunning('growtopia'):
                    print('Yes a growtopia was running')
                else:
                    await bot.midman_room_t.send("Bot oyuna giriyor, lütfen bekleyiniz.")
                    print('No growtopia process was running')
                    #start_GT()
                    bot.status = "startingGT"
                    os.startfile(r'D:\Users\omrto\AppData\Local\Growtopia\Growtopia.exe')
                    await asyncio.sleep(5)
                    os.startfile("startGT.ahk")
                    await asyncio.sleep(15)
                    bot.status = "np"

                await bot.satici_mem.add_roles(bot.costumer_role)
                await bot.alici_mem.add_roles(bot.costumer_role)
                await bot.midman_room_t.send("__**Satıcının Yapması Gerekenler**__\n**MAVIBALINA87** worldündeki şifreli kapının şifresi DM'den size iletilmiştir, __**güvenliğiniz için bu şifreyi kimse ile paylaşmayın**__. Şifreli kapıdan geçtikten ve __alıcının worldde sizi gördüğünden emin olduktan sonra__ takas edeceğiniz miktarı botun üstüne droplayınız. Eğer DM özelliğiniz sadece arkadaşlarınıza açıksa veya şifrenin size ulaştığından emin değilseniz DM'inizi herkese açtıktan sonra bu yazı kanalına `!yeni-şifre` yazarak DM'den yeni şifrenizi alabilirsiniz. `!iptal` yazarak aracılık sürecini iptal edebilirsiniz.\n \n__**Alıcının Yapması Gerekenler**__\n__Satıcının satın alıcağınız miktarı botun üstüne dropladığından emin olduktan sonra__ bu yazı kanalına `!onaylıyorum` yazarak satın alma işlemine devam edebilirsiniz. Eğer satıcının satın alacağınız miktarı dropladığından emin değilseniz `!geri` yazarak botun takas edeceğiniz miktarı geri vermesini sağlayabilirsiniz, satıcının takas edeceğeniz miktarı geri dropladığına emin olduktan sonra `!onaylıyorum` yazarak işleme devam edebilir veya aracılık işleminin devam etmesini istemiyorsanız `!iptal` yazarak aracılık sürecini iptal edebilirsiniz.")
                bot.action = True
                pass_change()
                await asyncio.sleep(5)
                bot.action = False
                await bot.satici_DM.send(pass_change.door_pass)
                bot.pass_rights = True
                bot.stage = 1
        else:
            await ctx.send("Etiketlediğiniz kullanıcının size herhangi bir isteği bulunmamaktadır " + ctx.author.mention)
    else:
        await ctx.send("Hakkınızda herhangi bir istek bulunmamaktadır.")
    
    """async def myTaskGenerator():
        asyncio.ensure_future(aracilik())

    bot.loop = asyncio.get_event_loop()
    bot.loop.run_until_complete(myTaskGenerator())
    print("ok")
    bot.loop.close()
    bot.task = asyncio.create_task(kabul())"""

@client.command()
async def yenisifre(ctx):   
    user = ctx.author
    if ctx.channel == bot.midman_room_t:
        if bot.status == "startingGT":
            await ctx.send("Growtopia başlatılıyor, lütfen bekleyiniz.")
            return

        if bot.in_trade == "False":
            await ctx.send("Şuanda herhangi bir aracılık işlemi bulunmamaktadır " + user.mention)
            return

        if bot.pass_rights == True:
            if ctx.author.id == bot.satici_id:
                if bot.action == False: 
                    bot.action = True
                    pass_change()
                    await asyncio.sleep(5)
                    bot.action = False
                    await bot.satici_DM.send(pass_change.door_pass)

                elif bot.action == True:
                    await ctx.send("Bot şuanda hareket halinde, lütfen az sonra tekrar deneyiniz" + user.mention)
            else:
                await ctx.send("Aracılığın bu aşamasında şifreyi sadece satıcı değiştirebilir " + user.mention)
            
        elif bot.pass_rights == False:
            if ctx.author.id == bot.alici_id:
                if bot.action == False:
                    bot.action = True
                    pass_change()
                    await asyncio.sleep(5)
                    bot.action = False
                    await bot.satici_DM.send(pass_change.door_pass)

                elif bot.action == True:
                    await ctx.send("Bot şuanda hareket halinde, az sonra tekrar deneyiniz " + user.mention)
            else:
                await ctx.send("Aracılığın bu aşamasında şifreyi sadece alıcı değiştirebilir " + user.mention)
    else:
        await ctx.send("Bu komutu bu kanalda kullanamazsınız.")     

@client.command()
async def geri(ctx):
    user = ctx.author
    if ctx.channel == bot.midman_room_t:

        if bot.in_trade == "False":
            await ctx.send("Şuanda herhangi bir aracılık işlemi bulunmamaktadır " + user.mention)
            return

        if bot.status == "startingGT":
            await ctx.send("Growtopia başlatılıyor, lütfen daha sonra tekrar deneyiniz." + user.mention)
            return

        if bot.stage == 1:

            if user.id == bot.satici_id or user.id == bot.alici_id:
                
                if bot.action == False:
                    bot.stage = 0
                    bot.action = True
                    os.startfile("drop.ahk")
                    await asyncio.sleep(10)
                    print("sex")
                    bot.action = False

                else:
                    await ctx.send("Bot şuanda hareket halinde, az sonra tekrar deneyiniz " + user.mention)
            else:
                await ctx.send("Aracılık işleminde bulunmadığınız için bu komutu kullanma yetkisine sahip değilsiniz." + user.mention)
        
        elif bot.stage == 0:
            await ctx.send("ana skm işte anla şuan yapamıyosun" + user.mention)
    else:
        await ctx.send("Bu komutu bu kanalda kullanamazsınız.")

@client.command()
async def red(ctx):
    if bot.status == "startingGT":
        await ctx.send("Growtopia başlatılıyor, lütfen bekleyiniz.")
        return

    if str(ctx.author.id) == str(costumer_2_id):
        return await ctx.send("Aracılık isteğiniz reddedildi :rolling_eyes: {}".format(costumer_1))
            
    elif str(ctx.author.id) != str(costumer_2_id):
        return await ctx.send("Siktir git sıranı bekle\nhttps://i.hizliresim.com/7BL86Y.png")

client.run(TOKEN)