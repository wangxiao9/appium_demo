__author__ = 'wangxiao'
import yaml


class PlatformSet:
    def __init__(self, platfrom, appName):
        self.platform = platfrom
        self.appName = appName

    def config(self, path=None):
        self.file = None
        if path is None:
            self.file = '../config/evn.yaml'
        else:
            self.file = path

        with open(self.file,  'r', encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
        return self.config

    def run(self):
        config = self.config()
        caps = {}
        if self.platform == 'android':
            caps["platformName"] = "android"
        else:
            caps["platformName"] = "ios"
            caps["automationName"] = "xcuitest"
        caps["deviceName"] = config[self.appName]['deviceName']
        caps["appPackage"] = config[self.appName]['appPackage']
        caps["appActivity"] = config[self.appName]['appActivity']
        caps["autoGrantPermissions"] = config[self.appName]['autoGrantPermissions']
        return caps


if __name__ == '__main__':
    type = PlatformSet('android', 'shoumi').run()
    print(type)
