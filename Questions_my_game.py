import discord
list_player = []
spisok_slov = dict()

def add_lst(message_id, message_content):
    message_content_now = message_content.split(' ')
    message_content_now = message_content_now[1:]
    message_content = ' '.join(message_content_now)
    spisok_slov[message_id] = message_content

