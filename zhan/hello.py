from seleniumbase import BaseCase


# the first test case by me
class HelloClass(BaseCase):
    def test_basics(self):
        self.open("https://www.google.com/")
        self.type("input.gLFyf", "selenium")
        self.sleep(10)
