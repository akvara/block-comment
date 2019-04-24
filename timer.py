import sys
import time
from datetime import datetime

from blockComment import block_comment
from getPage import get_page

start_time = time.time()
minutes = 1
interval = 60

if __name__ == '__main__':
    if len(sys.argv) > 1:
        minutes = int(sys.argv[1])
        print("Interval {} min.".format(minutes))

    while True:
        sys.stdout.write("{} Getting page ... ".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        comment_id = get_page()
        if comment_id:
            res = block_comment(comment_id)
            if res == 200:
                sys.stdout.write('comment {} deleted'.format(comment_id))
                interval = 20
            else:
                sys.stdout.write('could not delete: status code {}'.format(res))
        else:
            sys.stdout.write('no comments')
            interval = 60 * minutes

        sys.stdout.write('.\n')
        sys.stdout.flush()
        time.sleep(interval - ((time.time() - start_time) % interval))
