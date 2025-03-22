from dlake.base.model.meta_load import LoadMeta
from dlake.base.util.str import StrUtil


class Load:

    def __init__(self, dataframe, load_meta: LoadMeta):
        self.df = dataframe
        self.load_meta = load_meta

    def process(self): pass

    def get_path(self):
        path = ""
        if not StrUtil.isblank(self.load_meta.target_zone):
            path += self.load_meta.target_zone + "/"
        if not StrUtil.isblank(self.load_meta.target_database):
            path += self.load_meta.target_database + "/"
        if not StrUtil.isblank(self.load_meta.target_schema):
            path += self.load_meta.target_schema + "/"
        if not StrUtil.isblank(self.load_meta.target_object):
            path += self.load_meta.target_object
        return path
