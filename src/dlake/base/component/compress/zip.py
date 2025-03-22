from dlake.base.component.icompress import ICompress


class ZipCompress(ICompress):
    def __init__(self):
        super().__init__()

    def compress(self, input_path, output_path):
        super().compress(input_path, output_path)

    def decompress(self, input_path, output_path):
        super().decompress(input_path, output_path)
