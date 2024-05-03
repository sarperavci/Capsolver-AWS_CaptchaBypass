from selenium import webdriver
import time
import capsolver

class CapsolverAWSBypasser:
    def __init__(self, webdriver:webdriver.Chrome , page_url , api_key):
        capsolver.api_key = api_key
        self.page_url = page_url
        self.solution = None
        self.webdriver = webdriver

    def solve_recaptcha(self):
        self.solution = capsolver.solve({
            "type": "AntiAwsWafTaskProxyLess",
             "websiteURL": self.page_url,})

        time.sleep(.1)
        
        self.webdriver.add_cookie({'name': 'aws-waf-token', 'value': self.solution["cookie"], 'domain': '.efw47fpad9.execute-api.us-east-1.amazonaws.com', 'path': '/' })
        self.webdriver.refresh()