import os
import json

class Parser:
    def __init__(self, logs, packages_file):
        self.packages = {
            "exists" : False,
            "path" : packages_file,
            "content" : None,
            "packages" : []
        }
        self.configurations = {
            "requirements" : {
                "name" : "name",
                "method" : "method",
                "source" : "source",
                "build" : "build"
            },
            "found" : False
        }
        self.logs = logs

        self.load()
        self.extract()

    def load(self):
        if (os.path.isfile(self.packages["path"]) == True):
            self.logs.action("loading packages")
            self.packages["exists"] = True
            with open(self.packages["path"], 'r') as f:
                self.packages["content"] = json.load(f)
            self.logs.success("packages loaded")
        else:
            self.logs.error("packages configuration file '{}' not found".format(self.packages["path"]))

    def extract(self):
        package_configuration = {}

        if (self.packages["exists"] == True):
            self.logs.action("extracting packages")
            for package in self.packages["content"]["packages"]:
                for requirement in self.configurations["requirements"].keys():
                    package_configuration[requirement] = package[requirement]
                self.packages["packages"].append(package_configuration)
                self.logs.success("{} extracted".format(package_configuration["name"]))
            self.logs.success("packages extracted: {}".format(len(self.packages["packages"])))
    
