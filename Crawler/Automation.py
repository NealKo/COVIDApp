import time, json
from base_page import BasePage


def main():    
    config = json.load(open(".\\Tools\\Config.json", "r"))
    browser = BasePage()
    browser.open_explore(config['target_url'], ".\\Tools", config['user_agent'], config['screen_width'], config['screen_height'], config['pixel_ratio'])

    




    time.sleep(2)


if __name__ == '__main__':
        main()
