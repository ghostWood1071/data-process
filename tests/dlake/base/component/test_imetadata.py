from unittest import TestCase

from dlake.base.component.imetadata import IMetadata
from dlake.base.type.meta import MetaType


class TestIMetadata(TestCase):
    def test_init(self):
        meta = IMetadata.init('etl_ingestion_1', MetaType.LOCAL)
        print(meta.scenarios[0].extracts[0].__str__())
        print(meta.job_info.__str__())
