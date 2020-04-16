from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client, get_tracker_conf
from django.utils.deconstruct import deconstructible

@deconstructible
class FDFSStorage(Storage):
    """fast dfs文件存储类"""
    def __init__(self, option=None):
        if not option:
            self.option = settings.CUSTOM_STORAGE_OPTIONS
        else:
            self.option = option

    def _open(self, name, mode='rb'):
        '''打开文件时使用'''
        pass

    def _save(self, name, content):
        """
        在FastDFS中保存文件
        :param name: 传入的文件名
        :param content: 文件内容
        :return: 保存到数据库中的FastDFS的文件名
        """
        client_conf_obj = get_tracker_conf(self.option.get('CLIENT_CONF'))
        client = Fdfs_client(client_conf_obj)
        ret = client.upload_by_buffer(content.read())
        if ret.get("Status") != "Upload successed.":
            raise Exception("upload file failed")
        file_name = ret.get("Remote file_id")

        # file_name为bytes类型，只能返回str类型，不然会报错
        return file_name.decode()

    def exists(self, name):
        '''Django判断文件名是否可用'''
        return False

    def url(self, name):
        '''返回访问文件的url路径'''
        return self.option.get('BASE_URL') + name



