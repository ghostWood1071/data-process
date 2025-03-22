import json

from dlake.base.component.imetadata import IMetadata
from dlake.base.model.meta_job import MetaJob
from dlake.base.model.meta_scenario import MetaScenario


class DynamoMetadata(IMetadata):

    def load_scenarios(self):
        with open('C:/Users/hvsinh/Projects/data-platform/data-metadata/scenario/{}.json'.format(self.job_name), 'r') as file:
            data = json.load(file)
        metas = [x for x in data if x['status'] == True]
        for meta in metas:
            self.scenarios.append(MetaScenario(meta))
