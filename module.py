from selenium import webdriver

def search_reddit(search_term,n):
    url = 'https://old.reddit.com/'
    browser = webdriver.Chrome()
    browser.get(url)
    form = browser.find_element_by_id("search")
    search_bar = form.find_elements_by_tag_name('input')[0]
    search_bar.send_keys(search_term)
    form.submit()

    posts_per_page = 22
    pages = n//(posts_per_page+1)+1
    html_posts = []

    for _ in range(pages):
        html_posts_container = browser.find_element_by_id("siteTable")
        html_cur_page_posts = html_posts_container.find_elements_by_class_name("thing")
        html_posts += [e.get_attribute('innerHTML') for e in html_cur_page_posts]
        browser.find_element_by_link_text("next ›").click()

    html_posts = html_posts[:n]