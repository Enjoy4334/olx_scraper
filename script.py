from selenium import webdriver
import fake_useragent

#Using Selenium in the background
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(chrome_options=options)


#Selenium detection bypass
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
     "source": """
          const newProto = navigator._proto_
          delete newProto.webdriver
          navigator._proto_ = newProto
          """
    })


#fake user agent for module requests
user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}
