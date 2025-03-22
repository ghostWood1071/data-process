from dlake.base.type.compress import CompressType
from dlake.base.component.compress.zip import ZipCompress


class ICompress():
    def __init__(self): pass

    def compress(self, input_path, output_path): pass

    def decompress(self, input_path, output_path): pass

    @staticmethod
    def init(compress_type: CompressType):
        match compress_type:
            case CompressType.ZIP:
                return ZipCompress()
            case _:
                return ICompress()

