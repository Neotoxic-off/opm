import subprocess

class Downloader:
    def __init__(self, packages):
        self.packages = packages
    
        self.download()

    def download(self): 
        if (len(self.packages) > 0):
            for i in self.packages:
                print("==> downloading {}".format(i["name"]))
                child = subprocess.Popen(
                    "{} {}".format(i["method"], i["source"]),
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    shell = True,
                    universal_newlines = True
                )
                result = child.communicate()
                print(" -- downloaded")
                print("==> building {}".format(i["name"]))
                child = subprocess.Popen(
                    "{}".format(i["build"]),
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    shell = True,
                    universal_newlines = True
                )
                result = child.communicate()
