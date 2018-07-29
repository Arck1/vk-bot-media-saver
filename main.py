import argparse
import os

from vk_media_saver.saver import MediaSaver

if __name__ == '__main__':
    # loading params from params.json with login, pass, token, etc
    # json_params = open("params.json").read()
    # params = json.loads(json_params)
    # vk_session = vk_api.VkApi(params["login"], params["password"])
    # vk_session = vk_api.VkApi(token=params["token"])

    # vk_session.auth()  # auth for login, pass session
    # vk = vk_session.get_api()

    # args_parser = argparse.ArgumentParser(description='')
    # args_parser.add_argument('--login', '-l', type=str, dest='login', help='vk login',
    #                          default=params["login"])
    # args_parser.add_argument('--password', '-p', type=str, dest='password', help='vk password',
    #                          default=params["password"])
    # args_parser.add_argument('--wait', '-w', type=float, dest='wait', help='Timeout',
    #                          default=5)
    # parsed_args = args_parser.parse_args()
    media_saver = MediaSaver()
    print(media_saver.generate_date_string())
    media_saver.download(
        'https://psv4.userapi.com/c6035/u16000205/docs/6b45a2423ad0/puppy2.gif?extra=2rXhQoZ'
        '-8739QgZoELbIKUX8b6FuPgpRmy2JwLgQEKiYgj26mXQmD6ckibdaAgd'
        '-03Kvyc62pA6IB5TFkotbnHL9M7lZfO91ZmJKL5I1cD6G0DUYDBRa9j_FHCvw9wGZK10-Sbg95e0', '.\\media\\', datatime=True)
