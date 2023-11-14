from selenium import webdriver
 
 
# Driver Code
if __name__ == '__main__':
 
    # create object
    edgeBrowser = webdriver.Edge(r"msedgedriver.exe")
 
    # open browser and navigate to facebook
    edgeBrowser.get('https://www.facebook.com')
