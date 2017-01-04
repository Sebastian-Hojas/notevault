import os

class ConfigManager:
    def __init__(self, path, dryrun, verbose):
        self.path = path
        self.dryrun = dryrun
        self.verbose = verbose
        self.config = []
        try:
            with open(self.path, 'r') as f:
                self.config = [line.strip('\n').strip('\r') for line in f.readlines() if line != "\n"] 
        except Exception,e:
            if self.verbose:
                print("Warning: Config '" + self.path + "' does not exist or is emtpy")

    def enable(self,directory):
        dir = os.path.abspath(directory)
        if not self.dryrun:
            self.config.append(dir)
            # remove duplicates
            self.config = list(set(self.config))
        self.saveConfig()

    def disable(self,directory):

        dir = os.path.abspath(directory)
        if not self.dryrun:
            self.config = filter(lambda a: a != directory, self.config)
        self.saveConfig()

    def disableAll(self):
        if self.verbose:
            print("Disabled all directories")
        if not self.dryrun:
            self.config = []
        self.saveConfig()

    def saveConfig(self):
        with open(self.path, 'w') as f:
            f.write("\n".join(self.config))
            
    def status(self):
        print("\n".join(self.config))

    def enabledFolders(self):
        return self.config