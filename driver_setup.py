from selenium import webdriver


def start_chrome(base_url, exec_path):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument("--kiosk")
    # chrome_options.add_argument("--start-fullscreen")
    # chrome_options.add_argument('window-size=1920x1080')
    # chrome_options.add_argument("--no-proxy-server")
    # chrome_options.add_argument("--proxy-server='direct://'")
    # chrome_options.add_argument("--proxy-bypass-list=*")
    driver = webdriver.Chrome(exec_path, options=chrome_options)
    driver.get(base_url)
    # driver.set_window_size(1920, 1080)
    # driver.fullscreen_window()
    return driver


if __name__ == "__main__":
    start_chrome()