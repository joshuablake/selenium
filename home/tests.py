from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class HomeTets(LiveServerTestCase):
    def test_selenium(self):
        selenium = WebDriver()
        try:
            for i in xrange(5):
                print('Requesting {}'.format(i))
                selenium.get('{}/{}'.format(self.live_server_url, i))
        finally:
            selenium.quit()
