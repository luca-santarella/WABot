#Luca Santarella

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# add a delay so that all elements of 
# the webpage are loaded before proceeding 
import time 
import sys 

#class that allows to manage Whatsapp chats using Whatsapp Web and Chrome
class WABot(object):
	
	driver = None

	def __init__(self):
		# ChromeOptions allows us use the userdata of chrome 
		# so that you don't have to sign in manually everytime. 
		chropt = Options() 
	  
		# adding userdata argument to ChromeOptions object 
		chropt.add_argument("--user-data-dir=[insert-yout-path-here]") 
	  
		# Creating a Chrome webdriver object 
		self.driver = webdriver.Chrome(executable_path ="/bin/chromedriver",options = chropt) 

		#access Whatsapp Web
		self.driver.get("https://web.whatsapp.com/") 
		# delay added to give time for all elements to load 
		time.sleep(10) 
		print("Connection was successful")
		
	#method used to send a message "msg" to a contact "nameContact"
	def send_msg(self, nameContact, msg):
		# find the chat of your contact 
		try:
		    elemContact = self.driver.find_element_by_xpath('//span[@title ="{}"]'.format(nameContact))
		except Exception as ex:
		    print(ex)
		# simulates a mouse click on the element 
		elemContact.click()
	  

		# find the chat box element
		elemChat = []
		elemChat = self.driver.find_elements_by_class_name("_3FRCZ")
		# write the message
		elemChat[1].send_keys(msg)
		# find the Send button
		elemSend = self.driver.find_element_by_class_name("_1U1xa")
		# simulate a click on it
		elemSend.click()

		time.sleep(1)

		print("Message "+msg+" was sent to "+nameContact)
	
	#method that allows to delete last message sent to "nameContact"
	def delete_last_msg(self, nameContact):
		#find the chat of your contact 
		try:
		    elemContact = self.driver.find_element_by_xpath('//span[@title ="{}"]'.format(nameContact))
		except Exception as ex:
		    print(ex)
		#simulate a mouse click on the element 
		elemContact.click()
	
		#find list of messages
		elemMSGs = []
		elemMSGs = self.driver.find_elements_by_class_name("eRacY")
		#get the last message sent
		elemMenuLastMSG = elemMSGs[-1]
		#simulate hovering over in order to make appear the menu for the last message
		hover = ActionChains(self.driver).move_to_element(elemMenuLastMSG).perform()
		#wait until menu appears
		try:
			elemSubMenu = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "_2oA--")))
		except Exception as ex:
		    print(ex)
		elemSubMenu.click()
		#find the options for the menu
		elemDelete = []
		elemDelete = self.driver.find_elements_by_class_name("Ut_N0")
		#get the last option in order to delete message
		elemDeleteLastOption = elemDelete[-1]
		elemDeleteLastOption.click()

		#find option "Delete for everyone" option
		elemOptionsMSGs = []
		elemOptionsMSGs = self.driver.find_elements_by_class_name("S7_rT")
		elemMenuLastOptionMSG = elemOptionsMSGs[-1]

		elemMenuLastOptionMSG.click()
		print("Last message from "+nameContact+"'s chat was deleted")

	#closing chat and Chrome window
	def close_chat(self):
		self.driver.close()

