import time
from getPage import get_page
from blockComment import block_comment
from datetime import datetime


start_time = time.time()

while True:
    print("{} Getting page ...".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    comment_id = get_page()
    if comment_id:
        res = block_comment(comment_id)
        if res == 200:
            print('Comment {} deleted'.format(comment_id))
        else:
            print('Could not delete: status code {}'.format(res))
    else:
        print('No comments')

    time.sleep(600.0 - ((time.time() - start_time) % 600.0))
