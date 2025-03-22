from dlake.base.service.extract import Extract


class S3Extract(Extract):
    def __init__(self):
        super().__init__()

    def process(self):
        super().process()