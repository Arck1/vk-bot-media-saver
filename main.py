import argparse
import os
import vk_api
import json
import yaml
from vk_api.longpoll import VkLongPoll, VkEventType, Event

from vk_media_saver.saver import MediaSaver

def message_handler(event: Event):
    print(event.attachments.items())
    msg = vk.messages.getById(message_ids=event.message_id)
    files_list = media_saver.get_all_attachments_list(msg['items'])
    media_saver.download_files(files_list)


def main():
    # vk.messages.send(peer_id=params["admin_id"], message="starting vk bot")
    longpoll = VkLongPoll(vk_session)

    global running
    global process_list
    try:
        running = True

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message_handler(event)

    except InterruptedError:
        running = False

if __name__ == '__main__':
    # loading params from params.json with login, pass, token, etc
    with open("params.yaml") as stream:
        params = yaml.load(stream)

    args_parser = argparse.ArgumentParser(
        description='Bot for downloading files from attachments and packing them into one archive')
    args_parser.add_argument('--login', '-l', type=str, dest='login', help='vk login',
                             default=params['vk']["login"])
    args_parser.add_argument('--password', '-p', type=str, dest='password', help='vk password',
                             default=params['vk']["password"])
    parsed_args = args_parser.parse_args()

    # vk_session = vk_api.VkApi(parsed_args.login, parsed_args.password)
    vk_session = vk_api.VkApi(token=params['vk']["token"]) # if use vk_token comment auth() line

    # vk_session.auth()  # auth for login, pass session
    vk = vk_session.get_api()

    # vk.messages.send(peer_id=params['vk']['admin_id'], message="new app start")
    media_saver = MediaSaver(vk)
    main()