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

"""def kick_gt(k_member1):
    k_member1 = k_member1.upper()
    f = open("kick.ahk","r",encoding = 'utf-8')
    lines = f.readlines()
    lines[0] = "ControlSend,, {{Enter}}{{NumpadDiv}}KICK {}{{Enter}},ahk_exe Growtopia.exe".format(k_member1)
    f.close()
    f = open("kick.ahk","w",encoding = 'utf-8')
    f.writelines(lines)
    f.close()
    return os.startfile("kick.ahk")"""


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
    bot.stage = 0
    bot.satici_iptal = 0
    bot.alici_iptal = 0
    bot.iptal_process = False
    bot.satici_geri = 0
    bot.alici_geri = 0
    bot.alici_onay = 0
    bot.satici_onay = 0

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
async def kick(ctx, member1):
    if(bot.stage == 1 and ctx.author.id != bot.satici_id):
        await ctx.send("**Aracılığın bu aşamasında sadece satıcı kickleyebilir**  " + ctx.author.mention)
        return

    if(bot.stage == 2 and ctx.author.id != bot.alici_id):
        await ctx.send("**Aracılığın bu aşamasında sadece alıcı kickleyebilir**  " + ctx.author.mention)
        return

    if(bot.action == True):
        await ctx.send("**Bot şuan hareket halinde, az sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    bot.action = True
    member1 = member1.upper()
    f = open("kick.ahk","r",encoding = 'utf-8')
    lines = f.readlines()
    lines[0] = "ControlSend,, {{Enter}}{{NumpadDiv}}KICK {}{{Enter}},ahk_exe Growtopia.exe".format(member1)
    f.close()
    f = open("kick.ahk","w",encoding = 'utf-8')
    f.writelines(lines)
    f.close()
    os.startfile("kick.ahk")
    await asyncio.sleep(2)
    await ctx.send("**Oyuncu kicklenmiştir, eğer oyuncu hala kicklenmemişse ismi doğru yazdığınızdan emin olup tekrar deneyin**  " + ctx.author.mention)
    bot.action = False

@client.command()
async def onaylamak(ctx):
    #await sex.invoke(ctx)
    """if(bot.siraList.empty == True):
        return"""

    bot.siradaki = bot.siraList.head(1)
    print(bot.siradaki)
    bot.pot_satici_id = int(bot.siradaki["COSTUMER1_ID"].values)
    bot.pot_alici_id = int(bot.siradaki["COSTUMER2_ID"].values)
    
    bot.pot_satici = client.get_member(bot.pot_satici_id)
    bot.pot_alici = client.get_member(bot.pot_satici_id)

    await bot.midman_room_t.send("**Sıranız geldi! Aracılığa başlamak için `!kabul` yazabilirsiniz  {} - {}**".format(bot.pot_satici.mention, bot.pot_alici.mention))

@client.command()
async def onay(ctx):
    if(bot.iptal_process == True):
        await ctx.send("**İptal sürecindeyken aracılık işlemi onaylanamaz**  " + ctx.author.mention)

    if ctx.channel != bot.midman_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin {}**"  .format(bot.midman_room_t, ctx.author.mention))
        return
    
    if bot.stage == 1:
        if ctx.author.id == bot.satici_id:
            bot.satici_onay = 1
            if(bot.alici_onay == 0):
                await ctx.send("**Satıcı, DL'yi dropladığını onayladı, eminseniz `!onay` yazarak ikinci aşamaya geçebilirsiniz**  " + bot.satici_men)
                return

        elif ctx.author.id == bot.alici_id:
            bot.alici_onay = 1
            if(bot.satici_onay == 0):
                await ctx.send("**Alıcı, DL'nin droplandığını onayladı, işleme devam etmek istiyorsanız `!onay` yazarak ikinci aşamaya geçebilirsiniz**  " + bot.alici_men)
                return
        
        if(DL_check() != "none"):
            await bot.midman_room_t.send("**Aşama** :two: ")
            bot.stage = 2
            bot.alici_onay = 0
            bot.satici_onay = 0
    
    elif(bot.stage == 2):
        if ctx.author.id == bot.satici_id:
            bot.satici_onay = 1
            if(bot.alici_onay == 0):
                await ctx.send("**Satıcı, paranın geldiğini onayladı, aracılık işlemini tamamlamak için `!onay` yazabilirsiniz**  " + bot.alici_men)
                return
        
        elif ctx.author.id == bot.alici_id:
            bot.alici_onay = 1
            if(bot.satici_onay == 0):
                await ctx.send("**Alıcı, parayı gönderdiğini onayladı, paranın geldiğinden emin olduktan sonra `!onay` yazarak aracılık işlemini tamamlayabilirsiniz**  " + bot.satici_men)
                return
        
        bot.stage = 3
        bot.action = True
        pass_change()
        await asyncio.sleep(5)
        bot.action = False
        await bot.alici_DM.send(pass_change.door_pass)
        await ctx.send("**Aracılık işlemi tamamlandı, eğer botun bulunduğu alanda birisi varsa `!kick (Kullacının ismi)` komutuyla oyuncuyu kickleyip, `!drop` komutuyla DL'nizi alabilirsiniz**")
        
        await asyncio.sleep(240)
        await bot.satici_mem.remove_roles(bot.costumer_role)
        await bot.alici_mem.remove_roles(bot.costumer_role)
    
@client.command()
async def iptal(ctx):
    if(bot.iptal_process == True):
        await ctx.send("**Aracılık işlemi zaten iptal ediliyor**  " + user.mention)
        return

    if ctx.channel != bot.midman_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin {}**"  .format(bot.midman_room_t, ctx.author.mention))
        return

    if bot.status == "startingGT":
        await ctx.send("**Growtopia başlatılıyor, lütfen bekleyiniz**  " + user.mention)
        return

    if bot.in_trade == "False":
        await ctx.send("**Şuanda herhangi bir aracılık işlemi bulunmamaktadır**  " + user.mention)
        return

    if bot.stage == 1:
        if ctx.author.id == bot.satici_id:
            bot.satici_iptal = 1
            if(bot.alici_iptal == 0):
                await ctx.send("**Satıcı, aracılık işleminin iptalini talep etti, bu işlemi onaylamak için `!iptal` yazabilirsiniz**  " + bot.alici_men)
                return

        elif ctx.author.id == bot.alici_id:
            bot.alici_iptal = 1
            if(bot.satici_iptal == 0):
                await ctx.send("**Alıcı, aracılık işleminin iptalini talep etti, bu işlemi onaylamak için `!iptal` yazabilirsiniz**  " + bot.satici_men)
                return

            bot.iptal_process = True
            bot.action = True
            if(DL_check() != "none"):
                os.startfile("drop.ahk")
                await asyncio.sleep(10)
                bot.action = False
                await ctx.send("**Aracılık işlemi iptal edilmiştir ve bot DL'yi worlde droplamıştır. 4 dakika içinde satıcının DL'sini __growtopiatc1__ worldünden almaz ise DL'leri yeni aracılık yapanlar alacaktır**  " + bot.satici_men)
                await asyncio.sleep(240)
                bot.action = False
                bot.stage = 0
                bot.satici_iptal = 0
                bot.alici_iptal = 0
                bot.iptal_process = False
                bot.satici_geri = 0
                bot.alici_geri = 0
                bot.alici_onay = 0
                bot.satici_onay = 0
                bot.in_trade = "False"
            
            elif(DL_check() == "none"):
                await ctx.send("**Aracılık işlemi iptal edilmiştir**  {} - {}".format(bot.satici_men, bot.alici_men))
        
        else:
            await ctx.send("**Bu komutu kullanmaya gücün yetmiyor**  " + ctx.author.mention)
            return

@client.command()
async def sex(ctx):
    await bot.midman_room_t.send("safa")


@client.command()
async def kabul(ctx,costumer_1: discord.Member):
    if ctx.channel != bot.invite_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin  {}**".format(bot.invite_room_t.mention, ctx.author.mention))
        return

    if bot.status == "startingGT":
        await ctx.send("**Growtopia başlatılıyor, lütfen bekleyiniz** " + user.mention)
        return

    costumer_2_id = ctx.author.id
    if True in bot.istekList["COSTUMER1_ID"].isin([costumer_1.id]).values:
        ananinki = bot.istekList.loc[bot.istekList["COSTUMER1_ID"] == costumer_1.id]

        if True in ananinki["COSTUMER2_ID"].isin([costumer_2_id]).values:
            ananinki2 = ananinki.loc[ananinki["COSTUMER2_ID"] == costumer_2_id]
            if bot.in_trade == "True":
                #new_sira = bot.istekList[bot.istekList.COSTUMER2_ID == costumer_2_id]
                bot.siraList.append(ananinki2, ignore_index = True)
                #siradaki = bot.siraList.head(1)
                await ctx.send("**Aracılık isteğiniz sıraya alınmıştır** :notepad_spiral:  " + ctx.author.mention)
            
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
                await ctx.send("**Aracılık işlemi başlatıldı**  {} :tools: {}.\n{}**'na giderek aracılık işleminizi sürdürebilirsiniz**".format(bot.satici_men,bot.alici_men,bot.midman_room_t_mention))
                
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
                await bot.midman_room_t.send("**Aşama** :one:: Satıcı, GrowtopiaTC1 worldüne gidip DM'den aldığı şifreyi kullanarak botun yanına giderek aracılık yapılacak DL miktarını alıcının gözü önünde droplasın. Alıcı istediği miktarın droplandığından emin olduktan sonra `!onay` yazarak 2. aşamaya geçebilirsiniz** ")
                bot.action = True
                pass_change()
                await asyncio.sleep(5)
                bot.action = False
                await bot.satici_DM.send(pass_change.door_pass)
                bot.stage = 1
        else:
            await ctx.send("**Etiketlediğiniz kullanıcının size herhangi bir isteği bulunmamaktadır**  " + ctx.author.mention)
    else:
        await ctx.send("**Hakkınızda herhangi bir istek bulunmamaktadır**  "+ ctx.author.mention )

@client.command()
async def yenisifre(ctx):   
    user = ctx.author

    if(bot.iptal_process == True and ctx.author.id != bot.satici_id):
        await ctx.send("**İptal sürecindeyken şifreyi sadece satıcı değiştirebilir**  " + user.mention)
        return

    if ctx.channel != bot.midman_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin  {}**".format(bot.midman_room_t, ctx.author.mention))
        return

    if bot.status == "startingGT":
        await ctx.send("**Growtopia başlatılıyor, lütfen bekleyiniz**  " + user.mention)
        return

    if bot.in_trade == "False":
        await ctx.send("**Şuanda herhangi bir aracılık işlemi bulunmamaktadır**  " + user.mention)
        return

    if bot.stage == 1 or bot.stage == 2:
        if ctx.author.id == bot.satici_id:
            if bot.action == False:
                bot.action = True
                pass_change()
                await asyncio.sleep(5)
                bot.action = False
                await bot.satici_DM.send(pass_change.door_pass)

            elif bot.action == True:
                await ctx.send("**Bot şuanda hareket halinde, lütfen az sonra tekrar deneyiniz**  " + user.mention)
        else:
            await ctx.send("**Aracılığın bu aşamasında şifreyi sadece satıcı değiştirebilir**  " + user.mention)
        
    elif bot.stage == 3:
        if ctx.author.id == bot.alici_id:
            if bot.action == False:
                bot.action = True
                pass_change()
                await asyncio.sleep(5)
                bot.action = False
                await bot.satici_DM.send(pass_change.door_pass)

            elif bot.action == True:
                await ctx.send("**Bot şuanda hareket halinde, az sonra tekrar deneyiniz**  " + user.mention)
        else:
            await ctx.send("**Aracılığın bu aşamasında şifreyi sadece alıcı değiştirebilir**  " + user.mention)   

@client.command()
async def drop(ctx):
    user = ctx.author
    if ctx.channel != bot.midman_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin**  {}".format(bot.midman_room_t.mention,ctx.author.mention))
        return

    if bot.in_trade == "False":
        await ctx.send("**Şuanda herhangi bir aracılık işlemi bulunmamaktadır**  " + user.mention)
        return

    if bot.status == "startingGT":
        await ctx.send("**Growtopia başlatılıyor, lütfen daha sonra tekrar deneyiniz**  " + user.mention)
        return

    if(bot.iptal_process == True and ctx.author.id != bot.satici_id):
        await ctx.send("**İptal sürecindeyken DL'yi sadece satıcı geri alabilir**  " + user.mention)
        return
    
    if(bot.action != False):
            await ctx.send("**Bot şuanda hareket halinde, az sonra tekrar deneyiniz**  " + user.mention)
            bot.alici_geri = 0
            bot.satici_geri = 0
            return

    if bot.stage == 1:

        if user.id == bot.satici_id:
            bot.action = True
            os.startfile("dropcheck.ahk")
            await asyncio.sleep(2)
            serialDL_f = open("serialDL.txt","r")
            serialWL_f = open("serialWL.txt","r")
            serialDL = serialDL_f.read()
            serialWL = serialWL_f.read()
            print(serialWL)
            print(serialDL)
            if(str(serialDL) == "0" and str(serialWL) == "0"):
                await ctx.send("**Botta herhangi bir DL veya WL bulunmamakta**  ")
                bot.action = False
                serialDL_f.close()
                serialWL_f.close()
                return

            bot.satici_geri = 1
            if(bot.alici_geri == 0):
                await ctx.send("**Satıcı, botun DL'yi geri droplamasını talep etti, bu işlemi onaylamak için `!drop` yazabilirsiniz**  " + bot.satici_men)
                bot.action = False
                return

        elif user.id == bot.alici_id:
            bot.action = True
            os.startfile("dropcheck.ahk")
            await asyncio.sleep(2)
            serialDL_f = open("serialDL.txt","r")
            serialWL_f = open("serialWL.txt","r")
            serialDL = serialDL_f.read()
            serialWL = serialWL_f.read()
            print(serialWL)
            print(serialDL)
            if(serialDL == "0" and serialWL == "0"):
                await ctx.send("**Botta herhangi bir DL veya WL bulunmamakta**  ")
                bot.action = False
                serialDL_f.close()
                serialWL_f.close()
                return

            bot.alici_geri = 1
            if(bot.satici_geri == 0):
                await ctx.send("**Alıcı, botun DL'yi geri droplamasını talep etti, bu işlemi onaylamak için `!drop` yazabilirsiniz**  " + bot.alici_men)
                bot.action = False
                return

        else:
            await ctx.send("**Aracılık işleminde bulunmadığınız için bu komutu kullanma yetkisine sahip değilsiniz**  " + user.mention)
            return

        os.startfile("drop.ahk")
        await asyncio.sleep(10)
        bot.action = False
        await ctx.send("**Bot DL'yi başarıyla geri dropladı**  {} - {}".format(bot.satici_men, bot.alici_men))
        bot.satici_geri = 0
        bot.alici_geri = 0
        serialDL_f.close()
        serialWL_f.close()

    elif bot.stage == 2:
        await ctx.send("**Aracılığın bu aşamasında DL'yi geri alamazsın, eğer aracılık işlemine devam etmek istemiyorsan `!iptal` komutunu kullanabilirsin**  " + user.mention)
        return

    elif bot.stage == 3:
        if(ctx.author.id != bot.alici_id):
            await ctx.send("**Aracılığın bu aşamasında DL'yi sadece alıcı alabilir**  " + ctx.author.mention)
            return
        
        if(bot.action != False):
            await ctx.send("**Bot şuanda hareket halinde, az sonra tekrar deneyiniz**  " + user.mention)
            return

        bot.action = True
        os.startfile("drop.ahk")
        await asyncio.sleep(10)
        bot.action = False

        await ctx.send("**Bot DL'yi dropladı**  " + ctx.author.mention)

client.run(TOKEN)