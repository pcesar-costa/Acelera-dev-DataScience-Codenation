import src.sidebar.main_sidebar as msb
import src.pages.Home as Home
import src.pages.Dashboard as Dashboard

class Pagination():
    def __init__(self):
    self._pages = {
        "Home": Home,
        "Dashboard": Dashboard
    }
    
    self._page = self._pages['Home']

    def get_pages(self):
        return self._pages.keys()

    def get_page(self):
        return self._page

    def set_page(self, page):
        self._page = self._pages[page]
