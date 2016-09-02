from django_selenium_clean import SeleniumTestCase


class HomeTest(SeleniumTestCase):
    def test_selenium_clean(self):
        from django_selenium_clean import selenium

        def tracefunc(frame, event, arg, indent=[0]):
            import inspect
            try:
                klass = frame.f_locals['self'].__class__
            except KeyError:
                klass = frame.f_locals.get('cls')
            if klass:
                class_name = klass.__module__ + klass.__name__
            else:
                class_name = ''
            name = '{}.{}'.format(class_name, frame.f_code.co_name)
            if event == "call":
                indent[0] += 2
                try:
                    arg_string = inspect.formatargvalues(*inspect.getargvalues(frame))
                except Exception:
                    arg_string = ''
                print(" " * indent[0] + "> call {", name, arg_string)
            elif event == "return":
                print("<" + " " * indent[0], "} exit ", name)
                indent[0] -= 2
            return tracefunc

        for i in xrange(5):
            selenium.get('{}/{}'.format(self.live_server_url, i))
            print(i)

    def test_selenium(self):
        from selenium.webdriver.chrome.webdriver import WebDriver
        selenium = WebDriver()
        try:
            for i in xrange(5):
                selenium.get('{}/{}'.format(self.live_server_url, i))
                print(i)
        finally:
            selenium.quit()

    def test_urllib(self):
        from urllib2 import urlopen
        for i in xrange(10):
            try:
                urlopen('{}/{}'.format(self.live_server_url, i))
            except Exception as e:
                print(e)
            print(i)
