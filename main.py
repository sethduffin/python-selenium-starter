from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import extensions
import os,sys

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.implicitly_wait(3)

extensions.set_driver(driver,action)

def error(e="Unkown"):
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print("Error: %s (%s %s)" % (e,fname,exc_tb.tb_lineno))
	input("-- Quit -- ")
	driver.quit()
	quit()

def run():
	# Script goes here

try:
	run()
except Exception as e:
	error(e)
else:
	driver.quit()