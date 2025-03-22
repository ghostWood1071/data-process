from dlake.base.type.env import ENV


class IConnector:
    uri: str
    host: str
    port: int
    user: str
    password: str
    dbname: str
    driver: str
    env: ENV


    def __init__(self, uri: str = None, host: str = None, port: int = 0, user: str = None, password: str = None,
                 dbname: str = None, driver: str = None, env: ENV = ENV.DEV):
        self.uri = uri
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.driver = driver
        self.env = env
        self.conn = None

    def connect(self): pass

    def select(self, table_name: str, condition: dict, limit: int = None): pass

    def select_one(self, table_name: str,  condition: dict): pass

    def update(self, table_name: str, data: dict, condition: dict): pass

    def delete(self, table_name: str, condition: dict): pass

    def insert(self, table_name: str, obj: dict): pass

    def execute(self, sql: str): pass

    def close(self): pass
