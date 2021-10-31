from src.logs import Logs

from src.parser import Parser
from src.downloader import Downloader

class Core:
    def __init__(self):
        self.sources = "packages.opm"
        self.logs = Logs()
        self.parser = Parser(
            self.logs,
            self.sources
        )
        self.downloader = Downloader(
            self.logs,
            self.parser.packages["packages"]
        )

