from selenium import webdriver


def start_chrome(base_url, exec_path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(exec_path, options=chrome_options)
    driver.get(base_url)
    return driver


if __name__ == "__main__":
    start_chrome()