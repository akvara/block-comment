import re
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_page():
    # page_url = 'https://www.skelbiu.lt/skelbimai/raspberry-pi-2-3-3b-kompiuteriai-39759585.html'
    page_url = 'https://www.skelbiu.lt/skelbimai/saldytuvas-candy-su-defektu-40265827.html'

    page = urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')

    comment_block = soup.find('div', attrs={'class': 'comment'})
    m = re.search('data-id="([0-9]+)', str(comment_block))
    return m.group(1) if m else None
