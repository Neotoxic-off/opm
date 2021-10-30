from src.parser import Parser
from src.downloader import Downloader

class Core:
    def __init__(self):
        self.sources = "packages.opm"
        self.parser = Parser(
            self.sources
        )
        self.downloader = Downloader(
            self.parser.packages["packages"]
        )

