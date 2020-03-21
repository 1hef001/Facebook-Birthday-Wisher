from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException

# from bs4 import BeautifulSoup



driver = webdriver.Chrome(executable_path=r'C:/Webdrivers/chromedriver.exe')
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
assert "Facebook" in driver.title
username = driver.find_element_by_name("email")
username.clear()
username.send_keys("ashwins50@ymail.com")
password = driver.find_element_by_name("pass")
password.clear()
password.send_keys("AdiAsh17@")
password.send_keys(Keys.RETURN)
# user = driver.find_element_by_class_name("_2s25 _606w").click()
# user.send_keys(Keys.RETURN)
assert "No results found" not in driver.page_source
# driver.quit()

# soup_l1 = BeautifulSoup(driver.page_source, 'lxml')
url = driver.find_element_by_xpath('//a[@title="Profile"]').get_attribute('href')
# soup_l1.find('a', title='Profile').get('href')
driver.get(url+'&sk=friends_with_upcoming_birthdays')
driver.implicitly_wait(30)
id = url.split('=')[1]
# print(id)
# soup_l2 = BeautifulSoup(driver.page_source, 'lxml')
links = driver.find_elements_by_xpath('//a[@role="link"]')
profiles = []
for link in links:
	profiles.append(link.get_attribute('href'))

# print(profiles)
profiles.remove(None)
profile = []
for i in profiles:
	# print(i)
	if id in i:
		pass
	elif 'viewas' in i:
		pass
	elif 'photo' in i:
		pass
	elif 'friends' in i:
		pass
	else:
		profile.append(i)

profile = list(dict.fromkeys(profile))
print(profile)

bdtd = []
for x in profile:
	if 'id' in x:
		driver.get(x + "&sk=about")
	else:
		driver.get(x + '/about')
	driver.implicitly_wait(30)
	for bd in driver.find_elements_by_xpath("//span[@class='oi732d6d ik7dh3pa d2edcug0 qv66sw1b c1et5uql a8c37x1j s89635nw ew0dbk1b jq4qci2q a3bd9o3v knj5qynh oo9gr5id']"):
		if 'Today is his birthday' in bd.text:
			bdtd.append(x)
	# print(bdtd)

profile = list(dict.fromkeys(bdtd))

while True:
	if profile == []:
		break
	x = profile[0]
	try:
		if 'id' in x:
			id = x.split('=')[1]
			# print(id)
		else:
			id = x.split('com/')[1]
			# print(id)
		MAIN_URL = 'https://www.facebook.com/messages/t/' + id
		driver.get(MAIN_URL)
		driver.implicitly_wait(30) 
		msg = driver.switch_to.active_element
		# msg = msg.click()
		msg.clear()
		msg.send_keys('Happy Birthday')
		msg.send_keys(Keys.RETURN)
		profile.remove(x)
	except Exception:
		pass

driver.quit()


# for link in links:
# 	a = link.get_attribute('href')
# 	profiles
	# print(a)
# 	if 'profile' not in a or 'friends' not in a or 'photo' not in a:
# 		profiles.append(a)
# print(profiles)