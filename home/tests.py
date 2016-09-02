from django.test import LiveServerTestCase


class HomeTets(LiveServerTestCase):
    def load_urls(self, func):
        for i in xrange(5):
            print(i)
            print('requesting')
            try:
                func('{}/{}'.format(self.live_server_url, i))
            except Exception as err:
                print(err)
            print('returned')

    def test_selenium(self):
        from selenium.webdriver.chrome.webdriver import WebDriver
        selenium = WebDriver()
        selenium.implicitly_wait(1000)
        selenium.set_page_load_timeout(1000)
        try:
            self.load_urls(selenium.get)
        finally:
            selenium.quit()
