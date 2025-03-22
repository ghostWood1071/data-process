import json

from dlake.base.component.imetadata import IMetadata
from dlake.base.model.meta_scenario import MetaScenario
from dlake.base.model.meta_history import HistoryMeta
from dlake.base.util.date import DateUtil
from dlake.base.util.logger import Logger

LOGGER = Logger.get_logger(__name__)
class LocalMetadata(IMetadata):
    history_path = "C:/Users/thinh/OneDrive/Desktop/datalab/data-process/history/history.json"
    def load_scenarios(self):
        with open('C:/Users/thinh/OneDrive/Desktop/datalab/data-process/scenario/etl_ingestion_1.json'.format(self.job_name), 'r') as file:
            data = json.load(file)
        metas = [x for x in data if x['status'] == True]
        for meta in metas:
            self.scenarios.append(MetaScenario(meta))
    
    def save_history(self, history):
        LOGGER.debug("history response from scenario: %s", history.__dict__)
        with open(self.history_path, mode = "r") as f:
            histories = json.load(f)
        if history.criteria_value:
            history.criteria_value = DateUtil.strftime(history.criteria_value, "%Y-%m-%d %H:%M:%S")
        histories.append(history.__dict__)
        with open(self.history_path, mode = "w") as f:
            f.write(json.dumps(histories))

    def get_latest_history(self, meta_extract, meta_load):
        with open(self.history_path, mode ="r") as f:
            histories:list[HistoryMeta] = [HistoryMeta(hist) for hist in json.load(f)]
        latest_date = DateUtil.min_date()
        for history in histories:
            if history.source_object == meta_extract.source_object and history.status == "SUCCESS":
                if history.criteria_value:
                    criteria_val = DateUtil.strptime(history.criteria_value, "%Y-%m-%d %H:%M:%S")
                    if criteria_val > latest_date:
                        latest_date = criteria_val
        return latest_date

