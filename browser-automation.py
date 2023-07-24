import time
import keyboard
from selenium import webdriver
from selenium.webdriver.edge.options import Options

# URLs to open
urls = [
    "https://www.apple.com/",
    "https://www.google.com/",
    "https://netflix.com",
    "https://amazon.in",
    "https://flipkart.com",
    "https://news.com",
    "https://yahoo.com",
    "https://propelinc.com",
    "https://microsoft.com",
    # Add the other URLs here
]

# Set up Edge options
edge_options = Options()
edge_options.use_chromium = True

# Initialize the Edge browser
driver = webdriver.Edge(options=edge_options)

try:
    # Open the first URL
    driver.get(urls[0])

    # Open the remaining URLs in new tabs
    for url in urls[1:]:
        driver.execute_script(f"window.open('{url}', '_blank');")

    # Wait for 5 seconds to ensure all tabs are loaded
    time.sleep(20)

    # Press F11 to toggle full-screen mode
    keyboard.press_and_release('F11')

    # Loop through the tabs and refresh them every 5 seconds
    while True:
        # Get the number of open tabs
        num_tabs = len(driver.window_handles)

        # Loop through each tab and refresh
        for i in range(num_tabs):
            # Switch to the current tab
            driver.switch_to.window(driver.window_handles[i])
            # Refresh the page
            driver.refresh()
            time.sleep(20)  # Wait for 5 seconds before switching to the next tab

except KeyboardInterrupt:
    # If you press Ctrl+C while the script is running, it will exit gracefully
    pass

finally:
    # The browser will remain open after the loop ends.
    pass
