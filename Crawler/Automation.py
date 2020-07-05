import time, json
from base_page import BasePage


def main():    
    config = json.load(open(".\\Tools\\Config.json", "r"))
    browser = BasePage()
    browser.open_explore(config['target_url'], ".\\Tools", config['user_agent'], config['screen_width'], config['screen_height'], config['pixel_ratio'])
    result = browser.get_all_data()

    with open(".\\result.json", "w") as ofs:
        ofs.write(json.dumps(result))

    browser.close_explore()


if __name__ == '__main__':
        main()
