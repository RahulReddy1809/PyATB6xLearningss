# Check whether a web page loads within 3 seconds (Performance test condition)
# load time --> Page load too slow : 4.2 Seconds = Passed
# load time -->  Page load too slow : 3 Seconds = Failed

load_time = float(input("Enter load time: "))

if load_time == 3:
    print(f"Page loaded in {load_time} seconds")
else:
    print("Page loaded too slow")