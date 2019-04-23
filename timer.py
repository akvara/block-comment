import time
from getPage import get_page
from blockComment import block_comment
import requests

start_time = time.time()
while True:
    print("Getting page ...")
    comment_id = get_page()
    if comment_id:
        block_comment(comment_id)
        # block_comment('16494739')
        print('Comment {} deleted'.format(comment_id))
    else:
        print('No comments')

    time.sleep(60.0 - ((time.time() - start_time) % 60.0))
