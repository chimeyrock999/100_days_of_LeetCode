class Page:
    def __init__(self, url = None , prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        currPage = Page(homepage, None, None)
        self.currPage = currPage

    def visit(self, url: str) -> None:
        newPage = Page(url, self.currPage, None)
        self.currPage.next = newPage
        self.currPage = newPage 

    def back(self, steps: int) -> str:
        while self.currPage.prev and steps > 0:
            steps -= 1
            self.currPage = self.currPage.prev
        return self.currPage.url

    def forward(self, steps: int) -> str:
        while self.currPage.next and steps > 0:
            steps -= 1
            self.currPage = self.currPage.next
        return self.currPage.url