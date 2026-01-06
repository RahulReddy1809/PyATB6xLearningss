# In Automation, you often compare expected nad actual outputs
# Write code to check if a test case passed or failed

# expected_title = "Dashboard"
# actual_title = "dashboard"

"""
expected_title = "Dashboard"
actual_title = "dashboard "   # not matching as we have lower case here

if expected_title.strip() == actual_title.strip():
    print("Passed API request")
else:
    print("Failed API request")
"""

# For matching with lower case

expected_title = "Dashboard"
actual_title = "dashboard "   # not matching as we have lower case here

if expected_title.strip().lower() == actual_title.strip().lower():
    print("Passed API request")
else:
    print("Failed API request")
