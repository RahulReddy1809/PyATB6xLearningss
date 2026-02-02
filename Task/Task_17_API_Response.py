# simulate a page loading check using  while loop
# if page loaded within 5 seconds, print success : else time out

# hint : use a counter (like wait_time) and break

import time
import random

wait_time = 0
page_loaded = False

def api_response():
    return random.choice([False, True])

while wait_time < 5:
    page_loaded = api_response()
    if page_loaded:
        print(f"✅ Page loaded Successfully in {wait_time+1} seconds." )
        break
    else:
        print(f"checking... (second {wait_time+1})")
        time.sleep(1) # wait for 1 second
        wait_time+=1

if not page_loaded:
    print("❌ timed out ! page failed to load within 5 seconds")

api_response()
