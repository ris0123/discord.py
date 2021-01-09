import discord
import datetime

TOKEN = 'Nzk3NTI3NTg3MDk0MDAzNzg0.X_nxcg.kJrMfQMYMzZNXURJEAcIcKtxGrM'

client = discord.Client()
pretime_dict = {}

@client.event
async def on_voice_state_update(before, after):
  print("ボイスチャンネルで変化がありました")

  if((before.voice.self_mute is not after.voice.self_mute) or (before.voice.self_deaf is not after.voice.self_deaf)):
    print("ボイスチャンネルでミュート設定の変更がありました")
    return

  if(before.voice_channel is None):
    pretime_dict[after.name] = datetime.datetime.now()
  elif(after.voice_channel is None):
    duration_time = pretime_dict[before.name] - datetime.datetime.now()
    duration_time_adjust = int(duration_time.total_seconds()) * -1

    reply_channel_name = "general"
    reply_channel = [channel for channel in before.server.channels if channel.name == reply_channel_name][0]
    reply_text = after.name + "　が　"+ before.voice_channel.name + "　から抜けました。　通話時間：" + str(duration_time_adjust) +"秒"

    await client.send_message(reply_channel ,reply_text)

client.run(TOKEN)#ボットのトークン
