import discord
import asyncio
import random
import sys
import os
import botFunction.functions as f

client = discord.Client()

func_list = {
    '名言': f.random_meigen,
    '迷言': f.random_meigen,
    '武器': f.random_splat_buki,
    'ブキ': f.random_splat_buki,
    'help': f.help,
    'ヘルプ': f.help
}


@client.event
async def on_ready():
    '''
    起動時に呼ばれるメソッド
    '''
    print('-----Logged in info-----')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')


@client.event
async def on_message(message):
    '''
    特定のメッセージを受け取って処理する\n
    今はメンションを送るとランダムに名言を返す
    '''
    try:
        if client.user.id in message.content:
            for k in func_list:
                if k in str(message.content):
                    await func_list[k](client, message)
                    break
            else:
                await f.random_reply(client, message)
    except:
        print(sys.exc_info())

client.run(os.environ.get('ENV_VAR_DISCORD_ID'))
