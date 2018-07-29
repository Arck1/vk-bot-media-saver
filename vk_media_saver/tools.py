import os.path
import inspect
import wget
import uuid
import zipfile
import time
import datetime


class MediaTools:
    """

    """
    def __init__(self, root_path: str = None):

        if root_path is None:
            root_path = os.path.join(os.path.dirname(__file__) or '.', 'data')

        if not os.path.exists(root_path):
            os.makedirs(root_path)

        self.root_path = os.path.join(root_path)

    @staticmethod
    def zip_files(src_path: str, zip_name: str = None, dest_path: str = None, timestamp: bool = False):

        assert os.path.isdir(src_path)

        src_path = src_path.rstrip(os.sep)

        if dest_path is None:
            dest_path = src_path

        assert os.path.isdir(dest_path)

        if zip_name is None:
            zip_name = os.path.basename(src_path)

        if zip_name is None or zip_name == '.' or len(zip_name) == 0:
            zip_name = str(uuid.uuid4())

        zip_name = zip_name.replace('.zip', '')

        if timestamp:
            zip_name = f'{MediaTools.generate_date_string()}_{zip_name}'

        zf = zipfile.ZipFile(os.path.join(dest_path, f"{zip_name}.zip"), "w")

        for dir_name, sub_dirs, files in os.walk(src_path):

            zf.write(dir_name)

            for filename in files:
                if filename != f"{zip_name}.zip":
                    zf.write(os.path.join(dir_name, filename))

        zf.close()

    @staticmethod
    def download(url: str, path: str, name: str = None, ext: str = None, timestamp: bool = False):
        working_directory = os.getcwd()
        if name is None:
            name = wget.filename_from_url(url)

        if name is None:
            name = str(uuid.uuid4())

        if timestamp:
            name = f'{MediaTools.generate_date_string()}_{name}'

        if not os.path.exists(path):
            os.makedirs(path)

        file_path = os.path.join(path, name)

        filename = wget.download(url, file_path)
        os.chdir(working_directory)

    @staticmethod
    def generate_date_string():
        today = datetime.datetime.now().isoformat(' ', 'seconds')
        name = str(today)
        name = name.replace(' ', '_').replace(':', '-')

        return name


