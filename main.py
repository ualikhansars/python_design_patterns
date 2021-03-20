from Browsers import Firefox, Chrome, BetterTTV, AdBlock


def main():
    print("Design Patterns In Python")

    chrome = Chrome()

    print("Chrome size is ", chrome.get_size())

    firefox = Firefox()

    firefox = BetterTTV(firefox)

    firefox = AdBlock(firefox)

    print("Firefox size is ", firefox.get_size())

    firefox.enable_extension()





if __name__ == "__main__":
    main()