from selenium import webdriver

def get_browser_page_source():
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    browser.get('https://www.dba.dk/')
    search_field = browser.find_elements_by_id('searchField')
    search_field.send_keys('tv')
    search_field.submit()

if __name__ == '__main__':
    get_browser_page_source()