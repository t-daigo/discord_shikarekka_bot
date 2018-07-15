import random
import discord
import asyncio
import csv


def parse_meigen():
    '''
    名言を整形する
    '''
    with open('source/meigen.txt', 'r', encoding='utf-8') as f:
        line = f.readlines()
        line = [l.replace('\\r\\n', '\n') for l in line]
        return line


def parse_reply():
    '''
    リプライ一覧を取得してランダムに一つ返す
    '''
    with open('source/reply.txt', 'r', encoding='utf-8') as f:
        line = f.readlines()
        return random.choice(line)


async def random_meigen(client, message):
    '''
    ランダムな迷言を投稿
    '''
    await client.send_message(message.channel, random.choice(parse_meigen()))


async def random_reply(client, message):
    '''
    ランダムなリプライを返す
    '''
    s = '{} ' + parse_reply()
    await client.send_message(message.channel, s.format(message.author.mention))


async def help(client, message):
    '''
    今ある機能一覧
    '''
    func_list = {
        '名言、 迷言': 'ランダムな迷言を表示します',
        'help、 ヘルプ': '機能一覧を表示します',
        'それ以外': 'ランダムなリプライを返します'
    }

    for k in func_list:
        await client.send_message(message.channel, k + '...' + func_list[k])
