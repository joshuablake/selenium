from django.test import LiveServerTestCase


class HomeTets(LiveServerTestCase):
    def load_urls(self, func):
        for i in xrange(5):
            try:
                func('{}/{}'.format(self.live_server_url, i))
            except Exception as err:
                print(err)
            print(i)

    def test_selenium(self):
        from selenium.webdriver.chrome.webdriver import WebDriver
        selenium = WebDriver()
        try:
            self.load_urls(selenium.get)
        finally:
            selenium.quit()
