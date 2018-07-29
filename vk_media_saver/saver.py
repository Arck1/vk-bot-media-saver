import os.path
from collections import deque
import vk_api
from vk_media_saver.tools import MediaTools
from message_parser.parser import CommandModule


class MediaSaver(CommandModule):
    """

    """

    def __init__(self, vk: vk_api.VkApi):
        super().__init__()
        self.commands = {}
        self.vk = vk

    @staticmethod
    def get_all_attachments_list(items: list):
        answer = []
        q = deque()
        q.append(items[0])
        while len(q) > 0:
            elem = q.popleft()
            if 'attachments' in elem:
                answer += elem['attachments']
                # answer.append(elem['attachments'])
            if 'fwd_messages' in elem:
                for m in elem['fwd_messages']:
                    q.append(m)
        return answer

    @staticmethod
    def download_files(files_list: list, dist_path: str = None):

        if dist_path is None:
            dist_path = os.path.join('.', 'media', MediaTools.generate_date_string())

        for file in files_list:
            file_type = file['type']
            if file_type == 'doc':
                MediaTools.download(file[file_type]['url'], dist_path, file[file_type]['title'])
            elif file_type == 'photo':
                photo_url = MediaSaver.get_better_photo_link(file[file_type])
                if photo_url is not None:
                    MediaTools.download(photo_url, dist_path)
            elif file_type == 'link':
                if not os.path.exists(dist_path):
                    os.makedirs(dist_path)
                with open(os.path.join(dist_path, 'links.txt'), 'a') as links_file:
                    links_file.write(f"{file[file_type]['url']}{os.linesep}")


    @staticmethod
    def get_better_photo_link(file):
        atr = list(filter(lambda f: f.startswith('photo_'), file.keys()))
        return file[atr[-1]] if len(atr) > 0 else None

