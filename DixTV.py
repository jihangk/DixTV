import discord
import asyncio
import random

client = discord.Client()


@client.event
async def on_ready():
    print("로그인")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='딕스TV 봇', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("/딕스"):
        await client.send_message(message.channel, "-- DixTV봇 명령어 --")
        await client.send_message(message.channel, "[촬영일정] 예정된 촬영 일정이 안내됩니다.")
        await client.send_message(message.channel, "[선공개] 현재 선공개 되어있는 영상을 확인하실 수 있습니다.")
        await client.send_message(message.channel, "[채널] 당일 촬영될 채널 및 방 비밀번호를 확인하실 수 있습니다.")
        await client.send_message(message.channel, "[주사위] 주사위를 굴려보세요! 일반적이지는 않을걸요?")
        await client.send_message(message.channel, "[판사님] [질문] 무엇이든 물어보세요! 지 맘대로 대답합니다 ^-^")
        await client.send_message(message.channel, "[돼지밥주기] [음식] 돼지에게 밥을 주세요! 조금 까다롭습니다.")
        await client.send_message(message.channel, "[돼지골라] [선택지1] [선택지2] 결정장애가 있으시다구요! 돼지에게 맡겨보세요! ㅎㅎ..")
        await client.send_message(message.channel, "[별자리운세] [별자리] 별자리로 운세를 봐드립니다!")

    if message.content.startswith("/별자리"):
        await client.send_message(message.channel, "별자리는 사람이 임의로 정한 것이며 천체는 당신 삶에 영향을 끼치지 않습니다.")

    if message.content.startswith("/촬영일정"):
        await client.send_message(message.channel, "2월 25일 (월) 밤 11시 - 런닝맨 히어로즈 Day 1")
        await client.send_message(message.channel, "2월 26일 (화) 밤 11시 - 런닝맨 히어로즈 Day 2")
        await client.send_message(message.channel, "")

    if message.content.startswith("/선공개"):
        await client.send_message(message.channel, "현재 선공개 되어있는 영상 링크입니다.")
        await client.send_message(message.channel, "https://youtu.be/kpzjgwul7Z0")

    if message.content.startswith("/채널"):
        await client.send_message(message.channel, "채널 : 24채널")
        await client.send_message(message.channel, "비밀번호 : [000000]")

    if message.content.startswith("/주사위"):
        roll = "<주사위결과>1 <주사위결과>2 <주사위결과>3 <주사위결과>4 <주사위결과>5 <주사위결과>6 <주사위결과>1 <주사위결과>2 <주사위결과>3 <주사위결과>4 <주사위결과>5 <주사위결과>6 <주사위결과>쨍그랑.. <주사위결과>빅보꿀꺽.."
        rollcoice = roll.split(" ")
        rollnumber = random.randint(1, len(rollcoice))
        rollresult = rollcoice[rollnumber-1]
        await client.send_message(message.channel, rollresult)

    if message.content.startswith("/판사님"):
        pansa = "<판사님>응~맞아~ <판사님>응~아니야~"
        pansacoice = pansa.split(" ")
        pansanumber = random.randint(1, len(pansacoice))
        pansaresult = pansacoice[pansanumber-1]
        await client.send_message(message.channel, pansaresult)

    if message.content.startswith("/돼지밥주기"):
        pig = "<돼지>엄청 <돼지>진짜 <돼지>세상에서제일 <돼지>더럽게 <돼지>환상적으로 <돼지>화려하게 <돼지>다방면으로"
        pigcoice = pig.split(" ")
        pignumber = random.randint(1, len(pigcoice))
        pigresult = pigcoice[pignumber-1]
        await client.send_message(message.channel, pigresult)

    if message.content.startswith("/돼지밥주기"):
        pigpig = "맛없다! 맛있다! 쓰레기같다! 더럽다! 완벽하다! 최악이다! 최고다! 빅보같다! 돼지같다!"
        pigpigcoice = pigpig.split(" ")
        pigpignumber = random.randint(1, len(pigpigcoice))
        pigpigresult = pigpigcoice[pigpignumber-1]
        await client.send_message(message.channel, pigpigresult)
        await client.send_message(message.channel, "꿀꿀~")

    if message.content.startswith("/돼지골라"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, "<돼지> 나의 선택은...")
        await client.send_message(message.channel, choiceresult)
        await client.send_message(message.channel, "마음에 들길 바래 꿀꿀~")


client.run('NTQ4MjE4MDc1MTU4NDEzMzEy.D1CHjg.xoNciaY74RviD46twfMXGgNV-aQ')
