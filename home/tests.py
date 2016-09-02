from django_selenium_clean import SeleniumTestCase


class HomeTest(SeleniumTestCase):
    def test_selenium_clean(self):
        from django_selenium_clean import selenium
        for i in xrange(5):
            selenium.get('{}/{}'.format(self.live_server_url, i))
            print(i)
