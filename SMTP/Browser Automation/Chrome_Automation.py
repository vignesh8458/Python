from selenium import webdriver
import time
import keyboard

#"chrome-extension://moffahdcgnjnglbepimcggkjacdmpojc/ieability.html?url=http%3A%2F%2F192.168.12.100%2Fdoc%2Fpage%2Fpreview.asp",
urls = [
    #"https://app.powerbi.com/links/Iji-Mr_vUz?ctid=a8df62d0-eea9-44ce-b4a2-65baa6380fe4&pbi_source=linkShare",
    "https://www.site24x7.in/app/client#/home/noc-view",
    "https://admin.microsoft.com/#/healthoverview",
    "https://security.microsoft.com/homepage?",
    "https://security.microsoft.com/incidents?",
    "https://endpoint.microsoft.com/#@propelinc.com/dashboard/",
    #"https://endpointcentral.manageengine.in/webclient#/uems/patch-mgmt/patches-dashboard",
    #"https://endpointcentral.manageengine.in/webclient#/uems/home/summary",
    #"https://support.propelinc.com/app/itdesk/HomePage.do",
    "https://security.microsoft.com/quarantine?viewid=Email&tid=a8df62d0-eea9-44ce-b4a2-65baa6380fe4",
    # Add the other URLs here
]

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("user-data-dir=C:\\Users\\helpdesk\\AppData\\Local\Google\\Chrome\\User Data")

#chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("useAutomationExtension", False)
#chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# Replace 'path_to_chromedriver' with the actual path where you've placed the ChromeDriver executable.
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)



try:
    # Open the first URL
    driver.get(urls[0])
    keyboard.press_and_release('F11')

    time.sleep(5)

    # Open the remaining URLs in new tabs
    for url in urls[1:]:
        driver.execute_script(f"window.open('{url}', '_blank');")

    # Wait for 5 seconds to ensure all tabs are loaded
    time.sleep(5)

    # Press F11 to toggle full-screen mode
    #keyboard.press_and_release('F11')
    
    # Keep track of the current tab index
    current_tab_index = 0

    while True:
        # Get the number of open tabs
        num_tabs = len(driver.window_handles)

        # Loop through each tab
        for i in range(num_tabs):
            # Switch to the current tab
            driver.switch_to.window(driver.window_handles[i])

            # Refresh the tab if it's not the first tab
            if current_tab_index > 0:
                driver.refresh()

            # Increment the tab index
            current_tab_index += 1

            # Reset the tab index when it reaches the end
            if current_tab_index >= num_tabs:
                current_tab_index = 0

        # Wait for 60 seconds before refreshing again
        time.sleep(60)

except KeyboardInterrupt:
    pass

finally:
    pass
In this modified code, the current_tab_index keeps track of the current tab being processed. If the index is greater than 0 (i.e., not the first tab), the script will refresh the page. The index is then incremented, and if it reaches the end of the tab list, it is reset to 0. This way, only the first tab will not be refreshed, and the other tabs will be refreshed in a cyclic manner.







except KeyboardInterrupt:
    # If you press Ctrl+C while the script is running, it will exit gracefully
    pass

finally:
    # The browser will remain open after the loop ends.
    pass
