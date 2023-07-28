import time
import keyboard
from selenium import webdriver
from selenium.webdriver.edge.options import Options

https://app.powerbi.com/groups/me/apps/2166c6b5-4caa-4754-a059-818f45a07ed0/dashboards/97d04200-e513-4e50-adac-57547293752b?language=en-US&experience=power-bi
https://app.powerbi.com/groups/me/apps/bb540279-a3ba-4a9e-91ab-74ec3854e5fe/reports/b5829994-9ed6-4660-90ed-c46bcadd36fb/ReportSection4b34f5036922ed30394c?language=en-US&experience=power-bi

https://app.powerbi.com/links/Iji-Mr_vUz?ctid=a8df62d0-eea9-44ce-b4a2-65baa6380fe4&pbi_source=linkShare

# URLs to open
urls = [
    "https://www.site24x7.in/app/client#/home/noc-view",
    "https://admin.microsoft.com/#/healthoverview",
    "https://security.microsoft.com/homepage?tid=a8df62d0-eea9-44ce-b4a2-65baa6380fe4",
    "https://security.microsoft.com/incidents?filters=%257B%257D&range=%257B%2522timeRangeType%2522%253A%2522180%2522%257D&tid=a8df62d0-eea9-44ce-b4a2-65baa6380fe4",
    "https://endpoint.microsoft.com/#@propelinc.com/dashboard/private/14727706-e586-42ab-ba91-c19c0143987f",
    "https://endpointcentral.manageengine.in/webclient#/uems/patch-mgmt/patches-dashboard",
    "https://endpointcentral.manageengine.in/webclient#/uems/home/summary",
    "https://support.propelinc.com/app/itdesk/HomePage.do",
    "https://security.microsoft.com/quarantine?viewid=Email&tid=a8df62d0-eea9-44ce-b4a2-65baa6380fe4",
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
