from dlake.base.component.imetadata import IMetadata
from dlake.core.session.job import JobSession
from dlake.base.type.usecase import USType
from dlake.base.util.logger import Logger
from dlake.base.model.meta_history import HistoryMeta

LOGGER = Logger.get_logger("UseCase")

class UseCase():
    metadata: IMetadata

    def __init__(self, metadata: IMetadata):
        self.metadata = metadata
        self.responses =  HistoryMeta()

    def process(self):
        pass

    @staticmethod
    def init(session: JobSession):
        LOGGER.info("[init] Use Case Type = %s, env = %s", session.type,session.env.name)
        metadata = IMetadata.init(session=session)
        match session.type:
            case USType.INGESTION:
                LOGGER.info("[init] Initalization IngestionUseCaseImpl")
                from dlake.usecase.impl.us_ingestion import IngestionUseCaseImpl
                return IngestionUseCaseImpl(metadata=metadata)
            case USType.WAREHOUSING:
                LOGGER.info("[init] Initalization IngestionUseCaseImpl")
            case USType.LANDING:
                LOGGER.info("[init] Initalization IngestionUseCaseImpl")
            case USType.ENCRYPTION:
                LOGGER.info("[init] Initalization IngestionUseCaseImpl")
            case USType.DECRYPTION:
                LOGGER.info("[init] Initalization IngestionUseCaseImpl")
            case USType.SOURCING:
                LOGGER.info("[init] Initalization IngestionUseCaseImpl")
            case _:
                raise Exception("[process] Dont support US type = %s",session.type)




