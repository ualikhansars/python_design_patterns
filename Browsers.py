from abc import ABC, abstractmethod


class Browser(ABC):
    @abstractmethod
    def get_size(self):
        pass


class ExtensionDecorator(Browser):
    @abstractmethod
    def get_size(self):
        pass


class Firefox(Browser):
    size = 2.0

    def __init__(self):
        pass

    def get_size(self):
        return self.size


class Chrome(Browser):
    size = 2.5

    def __init__(self):
        pass

    def get_size(self):
        return self.size


class BetterTTV(ExtensionDecorator):
    extension_size = 2.0

    def __init__(self, browser):
        self.browser = browser

    def get_size(self):
        return self.browser.get_size() + self.extension_size


class AdBlock(ExtensionDecorator):
    extension_size = 4.0

    def __init__(self, browser):
        self.browser = browser

    def get_size(self):
        return self.browser.get_size() + self.extension_size

    def enable_extension(self):
        print("Ad is blocked\n")