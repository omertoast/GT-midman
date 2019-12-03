import discord
from discord.ext import commands
from random import randint
import os
import time
import pandas as pd
import asyncio
from discord.ext.commands.cooldowns import BucketType

TOKEN = "NjM3MzgwODQ3ODg4MjM2NTk2.XbNVbg.1Y8VcCCcIL0mSQ34XGNcHhnfub0"
client = commands.Bot(command_prefix = "!")

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
    bot.seks_room_t = client.get_channel(650002582395420741)
    bot.costumer_role = bot.GT_guild.get_role(637594581998895114)
    bot.total_trade = 0
    bot.status = "np" #startingGT,crashed,np,service
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
    bot.pot_alici_iptal = 0
    bot.pot_satici_iptal = 0
    bot.satici_id = 0
    bot.alici_id = 0
    bot.satici_men = 0
    bot.alici_men = 0
    bot.satici_mem = 0
    bot.alici_mem = 0
    bot.satici_DM = 0
    bot.alici_DM = 0

    bot.istekList = pd.DataFrame(columns= ["COSTUMER1_ID","COSTUMER2_ID"])
    bot.siraList = pd.DataFrame(columns= ["COSTUMER1_ID","COSTUMER2_ID"])

    while True:
        if bot.status == "service":
            await asyncio.sleep(5)

        else:
            if bot.action == True:
                await asyncio.sleep(5)

            else:
                os.startfile("drop2.ahk")
                await asyncio.sleep(2)
                mod_control_f = open("mod_control.txt","r")
                mod_control = mod_control_f.read()
                if(str(mod_control) == "0"):
                    await asyncio.sleep(5)

                elif(str(mod_control) == "1"):
                    await bot.midman_room_t.send("bakımdayızfeıwuapnefwu")
                    os.startfile("formod.ahk")
                    bot.status = "service"
                    if bot.in_trade == True:
                        await bot.satici_DM.send("**Bot bakıma girdi açılınca haber veririz  **" + bot.satici_men)
                        await bot.alici_DM.send("**Bot bakıma girdi açılınca haber veririz  **" + bot.alici_men)
        

@client.event
async def on_message(message):
    if message.content == "YOU DID IT YOU CRAZY BASTARD":
        await message.channel.send(":sunglasses:")
    await client.process_commands(message)

@client.command()
async def yoket(ctx):
    if ctx.channel != bot.seks_room_t:
        return
    
    if bot.action == True:
        ctx.send("hareket halinde bekle")
        return
    
    await bot.satici_mem.remove_roles(bot.costumer_role)
    await bot.alici_mem.remove_roles(bot.costumer_role)
    bot.stage = 0
    bot.satici_iptal = 0
    bot.alici_iptal = 0
    bot.iptal_process = False
    bot.satici_geri = 0
    bot.alici_geri = 0
    bot.alici_onay = 0
    bot.satici_onay = 0
    bot.pot_alici_iptal = 0
    bot.pot_satici_iptal = 0
    bot.satici_id = 0
    bot.alici_id = 0
    bot.satici_men = 0
    bot.alici_men = 0
    bot.satici_mem = 0
    bot.alici_mem = 0
    bot.satici_DM = 0
    bot.alici_DM = 0

    if(bot.siraList.empty == True):
        print("boş kardeşim")
        bot.in_trade = "False"
        return

    bot.in_trade = "siradaki"
    while(bot.in_trade == "siradaki"):
        if bot.status == "service":
            await asyncio.sleep(5)

        else:
            if(bot.siraList.empty == True):
                print("boş kardeşim")
                bot.in_trade = "False"
                break
            
            else:
                bot.siradaki = bot.siraList.head(1)
                print(bot.siradaki)
                bot.pot_satici_id = int(bot.siradaki["COSTUMER1_ID"].values)
                bot.pot_alici_id = int(bot.siradaki["COSTUMER2_ID"].values)

                print(bot.pot_alici_id)
                print(bot.pot_satici_id)

                bot.pot_satici = bot.GT_guild.get_member(bot.pot_satici_id)
                bot.pot_alici = bot.GT_guild.get_member(bot.pot_alici_id)

                await bot.invite_room_t.send("**Sıranız geldi! Aracılığa başlamak için 30 saniye içinde `!kabul` yazabilirsiniz  {} - {}**".format(bot.pot_satici.mention, bot.pot_alici.mention))
                await asyncio.sleep(30)
                bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != bot.pot_satici_id]

@client.command()
#@commands.cooldown(1, 10.00 , BucketType.member)
async def istek(ctx,costumer_2: discord.Member):
    if bot.status == "service":
        ctx.send("**Bot şuanda bakımda, lütfen daha sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if ctx.channel != bot.invite_room_t:
        await ctx.send("**Aracılık isteği göndermek için {} odasına gidiniz.".format(bot.invite_room_t.mention))
        return

    costumer_1 = "<@" + str(ctx.author.id) + ">"
    costumer_2_id = costumer_2.id
    costumer_2_mention = "<@" + str(costumer_2_id) + ">"
    costumer_1_m = ctx.author
    costumer_1_id = costumer_1_m.id

    if costumer_1_id == costumer_2_id:
        await ctx.send("**Kendi kendine istek gönderemezsin**  " + ctx.author.mention)
        return
    
    """if costumer_1_id == bot.satici_id or costumer_1_id == bot.alici_id:
        await ctx.send("**Aracılık işlemindeyken istek gönderemezsin**  " + ctx.author.mention)
        return

    if costumer_2_id == bot.satici_id or costumer_2_id == bot.alici_id:
        await ctx.send("**İstek gönderdiğiniz kişi halihazırda bir aracılık işleminde**  " + ctx.author.mention)
        return"""

    new_istek = {"COSTUMER1_ID": costumer_1_id,"COSTUMER2_ID": costumer_2_id}
    bot.istekList = bot.istekList.append(new_istek, ignore_index = True)
    await ctx.send("**{} Size bir aracılık isteği gönderdi. Kabul etmek için 30 saniye içinde `!kabul @{}`, reddetmek için `!red @{}` yazabilirsin**  {}".format(costumer_1,costumer_1_m, costumer_1_m, costumer_2.mention))
    await asyncio.sleep(30)
    bot.istekList = bot.istekList[bot.istekList.COSTUMER1_ID != costumer_1_id]

@client.command()
async def kick(ctx, member1):
    if bot.status == "service":
        ctx.send("**Bot şuanda bakımda, lütfen daha sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if(bot.iptal_process == True and ctx.author.id == bot.satici_id):
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

    if(bot.action == True):
        await ctx.send("**Bot şuan hareket halinde, az sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if(bot.stage == 1 and ctx.author.id != bot.satici_id):
        await ctx.send("**Aracılığın bu aşamasında sadece satıcı kickleyebilir**  " + ctx.author.mention)
        return

    if(bot.stage == 2 and ctx.author.id != bot.alici_id):
        await ctx.send("**Aracılığın bu aşamasında sadece alıcı kickleyebilir**  " + ctx.author.mention)
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
async def onay(ctx):
    if bot.status == "service":
        ctx.send("**Bot şuanda bakımda, lütfen daha sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if ctx.channel != bot.midman_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin {}**"  .format(bot.midman_room_t, ctx.author.mention))
        return

    if(bot.action == True):
        await ctx.send("**Bot şuan hareket halinde, az sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if(bot.iptal_process == True):
        await ctx.send("**İptal sürecindeyken aracılık işlemi onaylanamaz**  " + ctx.author.mention)

    bot.action = True
    os.startfile("dropcheck.ahk")
    await asyncio.sleep(2)
    serialDL_f = open("serialDL.txt","r")
    serialWL_f = open("serialWL.txt","r")
    serialDL = serialDL_f.read()
    serialWL = serialWL_f.read()
    bot.action = False
    if(str(serialDL) == "0" and str(serialWL) == "0"):
        await ctx.send("**Botta herhangi bir DL veya WL bulunmuyor**  " + ctx.author.mention)
        bot.action = False
        return

    if bot.stage == 1:
        if ctx.author.id == bot.satici_id:
            bot.satici_onay = 1
            if(bot.alici_onay == 0):
                await ctx.send("**Satıcı, DL'yi dropladığını onayladı, eminseniz `!onay` yazarak ikinci aşamaya geçebilirsiniz**  " + bot.alici_men)
                return

        elif ctx.author.id == bot.alici_id:
            bot.alici_onay = 1
            if(bot.satici_onay == 0):
                await ctx.send("**Alıcı, DL'nin droplandığını onayladı, işleme devam etmek istiyorsanız `!onay` yazarak ikinci aşamaya geçebilirsiniz**  " + bot.alici_men)
                return

        bot.action = False
        bot.stage = 2
        await bot.midman_room_t.send("**Aşama :two:: Alıcı, satıcının verdiği kart numarasına parayı atacak. Satıcı parasının hesabına geldiğinden emin olduktan sonra `!onay` yazarak aracılık işlemni tamamlayabilirsiniz. Eğer bir sorun çıkar ise `!iptal` yazarak aracılık işlemini iptal edebilirsiniz**  {} **-** {}".format(bot.satici_men, bot.alici_men))
        bot.satici_onay = 0
        bot.alici_onay = 0 

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
        
        bot.action = True
        pass_change()
        await asyncio.sleep(5)
        await bot.alici_DM.send(pass_change.door_pass)
        os.startfile("kasa.ahk")
        await asyncio.sleep(6)
        bot.action = False
        bot.stage = 3
        await ctx.send("**Aracılık işlemi tamamlandı, 4 dakika içinde eğer botun bulunduğu alanda birisi varsa `!kick (Kullacının ismi)` komutuyla oyuncuyu kickleyip, `!drop` komutuyla DL'nizi alabilirsiniz**")
        
        """
        while i < 240:
            await asyncio.sleep(5)
            if bot.action == True:
                await asyncio.sleep(5)
                i += 10
            else:
                bot.action = True
                os.startfile("dropcheck.ahk")
                await asyncio.sleep(2)
                serialDL_f = open("serialDL.txt","r")
                serialWL_f = open("serialWL.txt","r")
                serialDL = serialDL_f.read()
                serialWL = serialWL_f.read()
                if(str(serialDL) == "0" and str(serialWL) == "0"):

                else:
            """


        await asyncio.sleep(240)
        await bot.satici_mem.remove_roles(bot.costumer_role)
        await bot.alici_mem.remove_roles(bot.costumer_role)
        bot.stage = 0
        bot.satici_iptal = 0
        bot.alici_iptal = 0
        bot.iptal_process = False
        bot.satici_geri = 0
        bot.alici_geri = 0
        bot.alici_onay = 0
        bot.satici_onay = 0
        bot.pot_alici_iptal = 0
        bot.pot_satici_iptal = 0
        bot.satici_id = 0
        bot.alici_id = 0
        bot.satici_men = 0
        bot.alici_men = 0
        bot.satici_mem = 0
        bot.alici_mem = 0
        bot.satici_DM = 0
        bot.alici_DM = 0

        if(bot.siraList.empty == True):
            print("boş kardeşim")
            bot.in_trade = "False"
            return

        bot.in_trade = "siradaki"
        while(bot.in_trade == "siradaki"):
            if bot.status == "service":
                await asyncio.sleep(5)

            else:
                if(bot.siraList.empty == True):
                    print("boş kardeşim")
                    bot.in_trade = "False"
                    break
                
                else:
                    bot.siradaki = bot.siraList.head(1)
                    print(bot.siradaki)
                    bot.pot_satici_id = int(bot.siradaki["COSTUMER1_ID"].values)
                    bot.pot_alici_id = int(bot.siradaki["COSTUMER2_ID"].values)

                    print(bot.pot_alici_id)
                    print(bot.pot_satici_id)

                    bot.pot_satici = bot.GT_guild.get_member(bot.pot_satici_id)
                    bot.pot_alici = bot.GT_guild.get_member(bot.pot_alici_id)

                    await bot.invite_room_t.send("**Sıranız geldi! Aracılığa başlamak için 30 saniye içinde `!kabul` yazabilirsiniz  {} - {}**".format(bot.pot_satici.mention, bot.pot_alici.mention))
                    await asyncio.sleep(30)
                    bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != bot.pot_satici_id]

@client.command()
async def get(ctx):
    if bot.status == "service":
        await ctx.send("**Bot şuanda bakımda, lütfen daha sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if bot.action == "True":
        await ctx.send("**Bot şuan hareket halinde, az sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    bot.action = True
    await ctx.send("**Miktar başarıyla alındı**  " + ctx.author.mention)
    os.startfile("get.ahk")
    await asyncio.sleep(2)
    bot.action = False

@client.command()
async def iptal(ctx):
    if bot.status == "service":
        ctx.send("**Bot şuanda bakımda, lütfen daha sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if(bot.iptal_process == True):
        await ctx.send("**Aracılık işlemi zaten iptal ediliyor**  " + ctx.author.mention)
        return

    if ctx.channel != bot.midman_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin {}**"  .format(bot.midman_room_t, ctx.author.mention))
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
        os.startfile("dropcheck.ahk")
        await asyncio.sleep(2)
        serialDL_f = open("serialDL.txt","r")
        serialWL_f = open("serialWL.txt","r")
        serialDL = serialDL_f.read()
        serialWL = serialWL_f.read()
        if(str(serialDL) == "0" and str(serialWL) == "0"):
            await ctx.send("**Aracılık işlemi iptal edildi**  " + ctx.author.mention)
            await bot.satici_mem.remove_roles(bot.costumer_role)
            await bot.alici_mem.remove_roles(bot.costumer_role)
            bot.stage = 0
            bot.satici_iptal = 0
            bot.alici_iptal = 0
            bot.iptal_process = False
            bot.satici_geri = 0
            bot.alici_geri = 0
            bot.alici_onay = 0
            bot.satici_onay = 0
            bot.pot_alici_iptal = 0
            bot.pot_satici_iptal = 0
            bot.satici_id = 0
            bot.alici_id = 0
            bot.satici_men = 0
            bot.alici_men = 0
            bot.satici_mem = 0
            bot.alici_mem = 0
            bot.satici_DM = 0
            bot.alici_DM = 0
                
        else:
            await ctx.send("**Aracılık işlemi iptal edilmiştir. 4 dakika içinde botun yanında biri var ise `!kick (Kullacının ismi)` komutuyla oyuncuyu kickleyip, `!drop` komutuyla DL'nizi geri alabilirsin  **  " + bot.satici_men)
            
            await asyncio.sleep(240)
            await bot.satici_mem.remove_roles(bot.costumer_role)
            await bot.alici_mem.remove_roles(bot.costumer_role)
            bot.stage = 0
            bot.satici_iptal = 0
            bot.alici_iptal = 0
            bot.iptal_process = False
            bot.satici_geri = 0
            bot.alici_geri = 0
            bot.alici_onay = 0
            bot.satici_onay = 0
            bot.pot_alici_iptal = 0
            bot.pot_satici_iptal = 0
            bot.satici_id = 0
            bot.alici_id = 0
            bot.satici_men = 0
            bot.alici_men = 0
            bot.satici_mem = 0
            bot.alici_mem = 0
            bot.satici_DM = 0
            bot.alici_DM = 0
    
    elif(bot.stage == 2):
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
        os.startfile("dropcheck.ahk")
        await asyncio.sleep(2)
        serialDL_f = open("serialDL.txt","r")
        serialWL_f = open("serialWL.txt","r")
        serialDL = serialDL_f.read()
        serialWL = serialWL_f.read()
        if(str(serialDL) == "0" and str(serialWL) == "0"):
            await ctx.send("**Aracılık işlemi iptal edildi**  " + ctx.author.mention)
            await bot.satici_mem.remove_roles(bot.costumer_role)
            await bot.alici_mem.remove_roles(bot.costumer_role)
            bot.stage = 0
            bot.satici_iptal = 0
            bot.alici_iptal = 0
            bot.iptal_process = False
            bot.satici_geri = 0
            bot.alici_geri = 0
            bot.alici_onay = 0
            bot.satici_onay = 0
            bot.pot_alici_iptal = 0
            bot.pot_satici_iptal = 0
            bot.satici_id = 0
            bot.alici_id = 0
            bot.satici_men = 0
            bot.alici_men = 0
            bot.satici_mem = 0
            bot.alici_mem = 0
            bot.satici_DM = 0
            bot.alici_DM = 0

        else:
            await bot.satici_DM.send("**Aracılık işlemi iptal edilmiştir ve güvenliğiniz için DL'ye el konulmuştur. Herhangi bir yetkili müsait olunca durumla ilgilenecektir**  " + bot.satici_men)
            await bot.alici_DM.send("**Aracılık işlemi iptal edilmiştir ve güvenliğiniz için DL'ye el konulmuştur. Herhangi bir yetkili müsait olunca durumla ilgilenecektir**  " + bot.alici_men)
            await bot.satici_mem.remove_roles(bot.costumer_role)
            await bot.alici_mem.remove_roles(bot.costumer_role)
            bot.stage = 0
            bot.satici_iptal = 0
            bot.alici_iptal = 0
            bot.iptal_process = False
            bot.satici_geri = 0
            bot.alici_geri = 0
            bot.alici_onay = 0
            bot.satici_onay = 0
            bot.pot_alici_iptal = 0
            bot.pot_satici_iptal = 0
            bot.satici_id = 0
            bot.alici_id = 0
            bot.satici_men = 0
            bot.alici_men = 0
            bot.satici_mem = 0
            bot.alici_mem = 0
            bot.satici_DM = 0
            bot.alici_DM = 0

            if(str(serialDL) == "1" and str(serialWL) == "0"):
                os.startfile("yedek_kasa_DL.ahk")
                await asyncio.sleep(5)

            elif(str(serialDL) == "0" and str(serialWL) == "1"):
                os.startfile("yedek_kasa_WL.ahk")
                await asyncio.sleep(5)

            elif(str(serialDL) == "1" and str(serialWL) == "1"):
                os.startfile("yedek_kasa_DL.ahk")
                await asyncio.sleep(5)
                os.startfile("yedek_kasa_WL.ahk")
                await asyncio.sleep(5)


    if(bot.siraList.empty == True):
        print("boş kardeşim")
        bot.in_trade = "False"
        return

    bot.in_trade = "siradaki"
    while(bot.in_trade == "siradaki"):
        if bot.status == "service":
            await asyncio.sleep(5)

        else:
            if(bot.siraList.empty == True):
                print("boş kardeşim")
                bot.in_trade = "False"
                break
            
            else:
                bot.siradaki = bot.siraList.head(1)
                print(bot.siradaki)
                bot.pot_satici_id = int(bot.siradaki["COSTUMER1_ID"].values)
                bot.pot_alici_id = int(bot.siradaki["COSTUMER2_ID"].values)

                print(bot.pot_alici_id)
                print(bot.pot_satici_id)

                bot.pot_satici = bot.GT_guild.get_member(bot.pot_satici_id)
                bot.pot_alici = bot.GT_guild.get_member(bot.pot_alici_id)

                await bot.invite_room_t.send("**Sıranız geldi! Aracılığa başlamak için 30 saniye içinde `!kabul` yazabilirsiniz  {} - {}**".format(bot.pot_satici.mention, bot.pot_alici.mention))
                await asyncio.sleep(30)
                bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != bot.pot_satici_id]

@client.command()
async def komutlar(ctx):
    ctx.send("**!istek:** Satıcıysanız, `!istek @KullanıcıAdı` şeklinde alıcıyı etiketleyerek aracılık isteğinizi gönderebilirsiniz.\n**!kabul:** Gönderilen aracılık isteğini `!kabul @KullanıcıAdı` şeklinde aracılık isteğini kabul edebilirsiniz.\n**!yenisifre:** Şifreli kapının şifresini değiştirir.\n**!drop** Bottaki DL'yi geri droplar\n**!onay:** ARACILIK İŞLEMİNİ ONAYLAR VE OH BE BİTTİ DERSİNİZ PARANIZ CEBİNİZDE KALIR\n" + ctx.author.mention)

@client.command()
async def sıra(ctx):
    if(bot.siraList.empty == True):
        await ctx.send("**Sırada herhangi biri bulunmamaktadır**  " + ctx.author.mention)
        return

    sikis = 0

    if True in bot.siraList["COSTUMER1_ID"].isin([ctx.author.id]).values:
        sonuc = bot.siraList[bot.siraList["COSTUMER1_ID"] == ctx.author.id].index.values.astype(int)[0] + 1
        sikisdf = bot.siraList.loc[bot.siraList['COSTUMER1_ID'] == ctx.author.id]
        sira_satici = int(sikisdf["COSTUMER1_ID"].values)
        sira_alici = int(sikisdf["COSTUMER2_ID"].values)
        await ctx.send("**Sıranız: " + str(sonuc) + "** <@" + str(sira_satici)  + ">" + "** - **" + "<@" + str(sira_alici) + ">")
        sikis = 1

    if True in bot.siraList["COSTUMER2_ID"].isin([ctx.author.id]).values:
        sonuc = bot.siraList[bot.siraList["COSTUMER2_ID"] == ctx.author.id].index.values.astype(int)[0] + 1
        sikisdf = bot.siraList.loc[bot.siraList['COSTUMER2_ID'] == ctx.author.id]
        sira_satici = int(sikisdf["COSTUMER1_ID"].values)
        sira_alici = int(sikisdf["COSTUMER2_ID"].values)
        await ctx.send("**Sıranız: " + str(sonuc) + "** | **" + "**Satıcı: **" + "** <@" + str(sira_satici)  + ">" + "** - **" + " **Alıcı: **" + "<@" + str(sira_alici) + ">")
        sikis = 1

    if sikis == 0:
        await ctx.send(":x: **Sırada değilsiniz**  " + ctx.author.mention)
        return

@client.command()
async def kabul(ctx,costumer_1: discord.Member = None):
    if bot.status == "service":
        ctx.send("**Bot şuanda bakımda, lütfen daha sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if ctx.channel != bot.invite_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin  {}**".format(bot.invite_room_t.mention, ctx.author.mention))
        return
    
    if bot.in_trade == "siradaki":      
        if ctx.author.id == bot.pot_satici_id:
            bot.pot_satici_iptal = 1
            if(bot.pot_alici_iptal == 0):
                await ctx.send("**Satıcı, aracılık isteğini kabul etti, siz de kabul etmek için `!kabul` yazabilirsiniz**  " + bot.pot_alici.mention)
                return

        elif ctx.author.id == bot.pot_alici_id:
            bot.pot_alici_iptal = 1
            if(bot.pot_satici_iptal == 0):
                await ctx.send("**Alıcı, aracılık isteğini kabul etti, siz de kabul etmek için `!kabul` yazabilirsiniz**  " + bot.pot_satici.mention)
                return

        bot.in_trade = "True"
        bot.stage = 1
        bot.satici_id = bot.pot_satici_id
        bot.alici_id = bot.pot_alici_id
        bot.total_trade += 1
        trade_no = bot.total_trade
        bot.satici_men = "<@" + str(bot.satici_id) + ">"
        bot.alici_men = "<@" + str(bot.alici_id) + ">"
        bot.satici_mem = bot.GT_guild.get_member(bot.satici_id)
        bot.alici_mem = bot.GT_guild.get_member(bot.alici_id)
        await bot.satici_mem.create_dm()
        await bot.alici_mem.create_dm()
        bot.satici_DM = bot.satici_mem.dm_channel
        bot.alici_DM = bot.alici_mem.dm_channel

    else:
        costumer_2_id = ctx.author.id
        if True in bot.istekList["COSTUMER1_ID"].isin([costumer_1.id]).values:
            ananinki = bot.istekList.loc[bot.istekList["COSTUMER1_ID"] == costumer_1.id]
            print("sex")
        
        else:
            await ctx.send("**Hakkınızda herhangi bir istek bulunmamaktadır**  "+ ctx.author.mention)
            return

        if True in ananinki["COSTUMER2_ID"].isin([costumer_2_id]).values:
            ananinki2 = ananinki.loc[ananinki["COSTUMER2_ID"] == costumer_2_id]
        else:
            await ctx.send("**Etiketlediğiniz kullanıcının size herhangi bir isteği bulunmamaktadır**  " + ctx.author.mention)
            return

        if bot.in_trade == "True":
            print(ananinki2)
            satici_kaldir = int(ananinki2["COSTUMER1_ID"].values)
            alici_kaldir = int(ananinki2["COSTUMER2_ID"].values)
            
            if True in bot.siraList["COSTUMER1_ID"].isin([satici_kaldir]).values:
                print("polis")
                bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != satici_kaldir]

            if True in bot.siraList["COSTUMER2_ID"].isin([satici_kaldir]).values:
                print("polis1")
                bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != satici_kaldir]

            if True in bot.siraList["COSTUMER1_ID"].isin([alici_kaldir]).values:
                print("polis2")
                bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != alici_kaldir]

            if True in bot.siraList["COSTUMER2_ID"].isin([alici_kaldir]).values:
                print("polis3")
                bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != alici_kaldir]

            bot.siraList = bot.siraList.append(ananinki2, ignore_index = True)
            await ctx.send("**Aracılık isteğiniz sıraya alınmıştır** :notepad_spiral:  " + ctx.author.mention)
            return

        bot.in_trade = "True"
        bot.stage = 1
        bot.aktifList = ananinki2
        bot.satici_id = int(ananinki2["COSTUMER1_ID"].values)
        bot.alici_id = int(ananinki2["COSTUMER2_ID"].values)
        bot.total_trade += 1
        trade_no = bot.total_trade
        bot.satici_men = "<@" + str(bot.satici_id) + ">"
        bot.alici_men = "<@" + str(bot.alici_id) + ">"
        bot.satici_mem = bot.GT_guild.get_member(bot.satici_id)
        bot.alici_mem = bot.GT_guild.get_member(bot.alici_id)
        await bot.satici_mem.create_dm()
        await bot.alici_mem.create_dm()
        bot.satici_DM = bot.satici_mem.dm_channel
        bot.alici_DM = bot.alici_mem.dm_channel

    await ctx.send("**Aracılık işlemi başlatıldı**  {} :tools: {}.\n{}**'na giderek aracılık işleminizi sürdürebilirsiniz**".format(bot.satici_men,bot.alici_men,bot.midman_room_t_mention))

    await bot.satici_mem.add_roles(bot.costumer_role)
    await bot.alici_mem.add_roles(bot.costumer_role)
    await bot.midman_room_t.send("**Aşama :one:: Satıcı, GrowtopiaTC1 worldüne gidip DM'den aldığı şifreyi kullanarak botun yanına giderek aracılık yapılacak DL miktarını alıcının gözü önünde droplasın. Alıcı istediği miktarın droplandığından emin olduktan sonra `!onay` yazarak 2. aşamaya geçebilirsiniz**  {} **-** {}".format(bot.satici_men, bot.alici_men))
    bot.action = True
    pass_change()
    await asyncio.sleep(5)
    bot.action = False
    await bot.satici_DM.send(pass_change.door_pass)

    await asyncio.sleep(180)
    
    while True:
        if bot.total_trade != trade_no:
            return

        if bot.action == True:
            await asyncio.sleep(5)
        else:
            bot.action = True
            os.startfile("dropcheck.ahk")
            await asyncio.sleep(2)
            serialDL_f = open("serialDL.txt","r")
            serialWL_f = open("serialWL.txt","r")
            serialDL = serialDL_f.read()
            serialWL = serialWL_f.read()
            if(str(serialDL) == "0" and str(serialWL) == "0"):
                await bot.midman_room_t.send("**1 dakika içerisinde bota DL koymazsanız aracılık işleminiz iptal olacaktır**  {} - {}".format(bot.alici_men, bot.satici_men))
                bot.action = False
                break
            
            else:
                bot.action = False
                break
    
    await asyncio.sleep(60)

    while True:
        if bot.total_trade != trade_no:
            return

        if bot.action == True:
            await asyncio.sleep(5)
        else:
            bot.action = True
            os.startfile("dropcheck.ahk")
            await asyncio.sleep(2)
            serialDL_f = open("serialDL.txt","r")
            serialWL_f = open("serialWL.txt","r")
            serialDL = serialDL_f.read()
            serialWL = serialWL_f.read()
            if(str(serialDL) == "0" and str(serialWL) == "0"):
                await bot.alici_DM.send("**Aracılık işleminiz 4 dakika içerisinde herhangi bir DL koymadığınız için iptal olmuştur**  " + bot.alici_men)
                await bot.satici_DM.send("**Aracılık işleminiz 4 dakika içerisinde herhangi bir DL koymadığınız için iptal olmuştur**  " + bot.satici_men)
                await bot.satici_mem.remove_roles(bot.costumer_role)
                await bot.alici_mem.remove_roles(bot.costumer_role)
                bot.stage = 0
                bot.satici_iptal = 0
                bot.alici_iptal = 0
                bot.iptal_process = False
                bot.satici_geri = 0
                bot.alici_geri = 0
                bot.alici_onay = 0
                bot.satici_onay = 0
                bot.pot_alici_iptal = 0
                bot.pot_satici_iptal = 0
                bot.satici_id = 0
                bot.alici_id = 0
                bot.satici_men = 0
                bot.alici_men = 0
                bot.satici_mem = 0
                bot.alici_mem = 0
                bot.satici_DM = 0
                bot.alici_DM = 0
                bot.action = False
                if(bot.siraList.empty == True):
                    print("boş kardeşim")
                    bot.in_trade = "False"
                    return

                bot.in_trade = "siradaki"
                while(bot.in_trade == "siradaki"):
                    if bot.status == "service":
                        await asyncio.sleep(5)

                    else:
                        if(bot.siraList.empty == True):
                            print("boş kardeşim")
                            bot.in_trade = "False"
                            break
                        
                        else:
                            bot.siradaki = bot.siraList.head(1)
                            print(bot.siradaki)
                            bot.pot_satici_id = int(bot.siradaki["COSTUMER1_ID"].values)
                            bot.pot_alici_id = int(bot.siradaki["COSTUMER2_ID"].values)

                            print(bot.pot_alici_id)
                            print(bot.pot_satici_id)

                            bot.pot_satici = bot.GT_guild.get_member(bot.pot_satici_id)
                            bot.pot_alici = bot.GT_guild.get_member(bot.pot_alici_id)

                            await bot.invite_room_t.send("**Sıranız geldi! Aracılığa başlamak için 30 saniye içinde `!kabul` yazabilirsiniz  {} - {}**".format(bot.pot_satici.mention, bot.pot_alici.mention))
                            await asyncio.sleep(30)
                            bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != bot.pot_satici_id]
            
            else:
                bot.action = False
                break
    
    await asyncio.sleep(5)
    print("biz burdayizzz")
    if bot.total_trade != trade_no:
        return
    
    await bot.midman_room_t.send("**Aracılık işleminizi 2 dakika içinde bitirmezseniz, aracılık işlemi sonlandırılacaktır  {} - {}**".format(bot.satici_men, bot.alici_men))

    if bot.total_trade != trade_no:
        return
    
    while True:
        if bot.action == True:
            await asyncio.sleep(5)
        else:
            bot.action = True
            os.startfile("dropcheck.ahk")
            await asyncio.sleep(2)
            serialDL_f = open("serialDL.txt","r")
            serialWL_f = open("serialWL.txt","r")
            serialDL = serialDL_f.read()
            serialWL = serialWL_f.read()
            if(str(serialDL) == "0" and str(serialWL) == "0"):
                await bot.satici_DM.send("**Aracılık işleminizi 8 dakika içinde bitirmediğinizden dolayı aracılık işlemi sonlandırılmıştır**  " + bot.satici_men)
                await bot.alici_DM.send("**Aracılık işleminizi 8 dakika içinde bitirmediğinizden dolayı aracılık işlemi sonlandırılmıştır**  " + bot.alici_men)
                await bot.satici_mem.remove_roles(bot.costumer_role)
                await bot.alici_mem.remove_roles(bot.costumer_role)
                bot.stage = 0
                bot.satici_iptal = 0
                bot.alici_iptal = 0
                bot.iptal_process = False
                bot.satici_geri = 0
                bot.alici_geri = 0
                bot.alici_onay = 0
                bot.satici_onay = 0
                bot.pot_alici_iptal = 0
                bot.pot_satici_iptal = 0
                bot.satici_id = 0
                bot.alici_id = 0
                bot.satici_men = 0
                bot.alici_men = 0
                bot.satici_mem = 0
                bot.alici_mem = 0
                bot.satici_DM = 0
                bot.alici_DM = 0
            
            else:
                await bot.satici_DM.send("**Aracılık işleminizi 8 dakika içinde bitirmediğinizden dolayı DL'nize el konulmuştur. Yetkili birisi müsait olduğunda sizinle iletişime geçip DL'nizi iade edecektir**  " + bot.satici_men)
                await bot.alici_DM.send("**Aracılık işleminizi 8 dakika içinde bitirmediğinizden dolayı aracılık işlemi sonlandırılmıştır**  " + bot.alici_men)
                await bot.satici_mem.remove_roles(bot.costumer_role)
                await bot.alici_mem.remove_roles(bot.costumer_role)
                bot.stage = 0
                bot.satici_iptal = 0
                bot.alici_iptal = 0
                bot.iptal_process = False
                bot.satici_geri = 0
                bot.alici_geri = 0
                bot.alici_onay = 0
                bot.satici_onay = 0
                bot.pot_alici_iptal = 0
                bot.pot_satici_iptal = 0
                bot.satici_id = 0
                bot.alici_id = 0
                bot.satici_men = 0
                bot.alici_men = 0
                bot.satici_mem = 0
                bot.alici_mem = 0
                bot.satici_DM = 0
                bot.alici_DM = 0
                
                if(str(serialDL) == "1" and str(serialWL) == "0"):
                    os.startfile("yedek_kasa_DL.ahk")
                    await asyncio.sleep(5)

                elif(str(serialDL) == "0" and str(serialWL) == "1"):
                    os.startfile("yedek_kasa_WL.ahk")
                    await asyncio.sleep(5)

                elif(str(serialDL) == "1" and str(serialWL) == "1"):
                    os.startfile("yedek_kasa_DL.ahk")
                    await asyncio.sleep(5)
                    os.startfile("yedek_kasa_WL.ahk")
                    await asyncio.sleep(5)

            if(bot.siraList.empty == True):
                print("boş kardeşim")
                bot.in_trade = "False"
                return

            bot.in_trade = "siradaki"
            while(bot.in_trade == "siradaki"):
                if bot.status == "service":
                    await asyncio.sleep(5)

                else:
                    if(bot.siraList.empty == True):
                        print("boş kardeşim")
                        bot.in_trade = "False"
                        break
                    
                    else:
                        bot.siradaki = bot.siraList.head(1)
                        print(bot.siradaki)
                        bot.pot_satici_id = int(bot.siradaki["COSTUMER1_ID"].values)
                        bot.pot_alici_id = int(bot.siradaki["COSTUMER2_ID"].values)

                        print(bot.pot_alici_id)
                        print(bot.pot_satici_id)

                        bot.pot_satici = bot.GT_guild.get_member(bot.pot_satici_id)
                        bot.pot_alici = bot.GT_guild.get_member(bot.pot_alici_id)

                        await bot.invite_room_t.send("**Sıranız geldi! Aracılığa başlamak için 30 saniye içinde `!kabul` yazabilirsiniz  {} - {}**".format(bot.pot_satici.mention, bot.pot_alici.mention))
                        await asyncio.sleep(30)
                        bot.siraList = bot.siraList[bot.siraList.COSTUMER1_ID != bot.pot_satici_id]


@client.command()
async def yenisifre(ctx):   
    user = ctx.author

    if bot.status == "service":
        ctx.send("**Bot şuanda bakımda, lütfen daha sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if(bot.iptal_process == True and ctx.author.id != bot.satici_id):
        await ctx.send("**İptal sürecindeyken şifreyi sadece satıcı değiştirebilir**  " + user.mention)
        return

    if ctx.channel != bot.midman_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin  {}**".format(bot.midman_room_t, ctx.author.mention))
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

    if bot.status == "service":
        ctx.send("**Bot şuanda bakımda, lütfen daha sonra tekrar deneyiniz**  " + ctx.author.mention)
        return

    if ctx.channel != bot.midman_room_t:
        await ctx.send("**Bu komutu sadece {} kanalında kullanabilirsin**  {}".format(bot.midman_room_t.mention,ctx.author.mention))
        return

    if bot.in_trade == "False":
        await ctx.send("**Şuanda herhangi bir aracılık işlemi bulunmamaktadır**  " + user.mention)
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
            if(serialDL == "0" and serialWL == "0"):
                await ctx.send("**Botta herhangi bir DL veya WL bulunmuyor**  ")
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