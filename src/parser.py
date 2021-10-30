import os
import json

class Parser:
    def __init__(self, packages_file):
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

        self.load()
        self.extract()

    def load(self):
        if (os.path.isfile(self.packages["path"]) == True):
            print("==> loading packages")
            self.packages["exists"] = True
            with open(self.packages["path"], 'r') as f:
                self.packages["content"] = json.load(f)
            print(" -- packages loaded")
        else:
            print("==> packages configuration file '{}' not found".format(self.packages["path"]))

    def extract(self):
        package_configuration = {}

        if (self.packages["exists"] == True):
            print("==> extracting packages")
            for package in self.packages["content"]["packages"]:
                for requirement in self.configurations["requirements"].keys():
                    package_configuration[requirement] = package[requirement]
                self.packages["packages"].append(package_configuration)
                print(" -- {} extracted".format(package_configuration["name"]))
            print(" -- packages extracted: {}".format(len(self.packages["packages"])))
    
