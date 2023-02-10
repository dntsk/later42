from bs4 import BeautifulSoup
from newspaper import Article, Config


def sanitize_img_size(html: str):
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.find_all("img"):
        img["width"] = "100%"
        img["height"] = "auto"
    return str(soup)


def get_content(url: str):
    config = Config()
    config.keep_article_html = True
    article = Article(url, config=config)
    article.download()
    article.parse()

    return article
