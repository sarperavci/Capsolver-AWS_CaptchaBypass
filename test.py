from CapsolverAWSBypasser import CapsolverAWSBypasser
from selenium import webdriver

CAPSOLVER_API_KEY = "YOUR API KEY"

URL=  "https://efw47fpad9.execute-api.us-east-1.amazonaws.com/latest"

page = webdriver.Chrome()
page.get( URL )

print("Solving...")
awsSolver = CapsolverAWSBypasser( page , URL ,CAPSOLVER_API_KEY )
awsSolver.solve_recaptcha()

page.refresh()

input("Press Enter to close the page")
