from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, SessionNotCreatedException, WebDriverException
from sys import exit

def limit20(userlist):
	if len(userlist) > 20:
		print("The length of your list of Users is " + str(len(userlist)) + ". Please ensure your list is a maximum of 20 Users.")
		print("This limit exists to ensure you do not breach Instagram's internal limits on profile views.")
		exit(0)

def drivercheck(drivertype, driverpath):
	if drivertype == "Chrome":
		try:
			driver = webdriver.Chrome(executable_path=driverpath)
		except SessionNotCreatedException:
			print("Your Driverpath does not match with the Drivertype you specified (Chrome). Ensure the type and path are correct.")
			exit(0)
		except WebDriverException:
			print("Your Driverpath does not match with the Drivertype you specified (Chrome). Ensure the type and path are correct.")
			exit(0)

	# elif drivertype == "HeadlessChrome":
	# 	try:
	# 		chrome_options = webdriver.ChromeOptions()
	# 		chrome_options.headless = True
	# 		chrome_options.add_argument("--start-maximised")
	# 		driver = webdriver.Chrome(executable_path=driverpath, chrome_options=chrome_options)
		# except SessionNotCreatedException:
		# 	print("Your Driverpath does not match with the Drivertype you specified (HeadlessChrome). Ensure the type and path are correct.")
		# 	exit(0)
		# except WebDriverException:
		# 	print("Your Driverpath does not match with the Drivertype you specified (HeadlessChrome). Ensure the type and path are correct.")
		# 	exit(0)

	elif drivertype == "Gecko":
		try:
			driver = webdriver.Firefox(executable_path=driverpath)
		except SessionNotCreatedException:
			print("Your Driverpath does not match with the Drivertype you specified (Gecko). Ensure the type and path are correct.")
			exit(0)
		except WebDriverException:
			print("Your Driverpath does not match with the Drivertype you specified (Gecko). Ensure the type and path are correct.")
			exit(0)

	elif drivertype == "HeadlessGecko":
		try:
			gecko_options = webdriver.FirefoxOptions()
			gecko_options.headless = True
			driver = webdriver.Firefox(executable_path=driverpath, firefox_options=gecko_options)
		except SessionNotCreatedException:
			print("Your Driverpath does not match with the Drivertype you specified (HeadlessGecko). Ensure the type and path are correct.")
			exit(0)
		except WebDriverException:
			print("Your Driverpath does not match with the Drivertype you specified (HeadlessGecko). Ensure the type and path are correct.")
			exit(0)

	else:
		print("You have entered an incorrect DriverType. Your options are: [Chrome | Gecko | HeadlessGecko]")
		exit(0)
	return driver

def login(username, password, driver):

	driver.get('https://www.instagram.com/accounts/login')

	print("### Cookies: Accept [x]")

	try:
		driver.find_element_by_xpath("//button[text()='Accept']").click()
	except NoSuchElementException:
		print("### Cookies window not found. Skipping to login..")
		pass

	print("### Entering in Instagram Username and Password..")
	driver.implicitly_wait(2)
	driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
	driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
	driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
	
	driver.implicitly_wait(2)

	try:
		driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/p")
		print("### Your Username and/or Password is incorrect. Please enter a valid combination.")
		exit(0)

	except NoSuchElementException:
		pass


	driver.implicitly_wait(3)

	print("### Save Login Info: Not Now [x]")
	try:
		driver.find_element_by_xpath("//button[text()='Not Now']").click()
	except NoSuchElementException:
		print("Save Login Info popup not found. Skipping..")
		pass
	driver.implicitly_wait(1)

	print("### Notifications: Not Now [x]")
	try:
		driver.find_element_by_xpath("//button[text()='Not Now']").click()
	except NoSuchElementException:
		print("Notifications popup not found. Skipping..")
		pass
	driver.implicitly_wait(1)


def check_user(user, driver, errorlist):
	
	driver.get('https://www.instagram.com/' + user)
	driver.implicitly_wait(1)
	try:
		driver.find_element_by_xpath("/html/body/div[1]/section/main/div/h2")
		driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div")
		print("Username " + str(user) + " does not exist. Skipping...")
		errorlist.append(user)
		username = 0
	except:
		username = user
	return username


def check_private(user, driver):
	try:
		driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div/div/h2")
		driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div/div/div")
		private = True
	except NoSuchElementException:
		private = False
	return private

def check_verified(user, driver):
	try:
		driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span")
		verified = True
	except NoSuchElementException:
		verified = False
	return verified

def check_name(user, driver):
	try:
		real_name = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/h1').text
	except NoSuchElementException:
		print("Cannot find Name for: " + str(user))
		real_name = "blank"
	return real_name

def check_website(user, driver):
	try:
		website = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/a').text
	except NoSuchElementException:
		print("Cannot find Website for: " + str(user))
		website = "blank"
	return website

def check_bio(user, driver):
	try:
		bio = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/span').text.replace('\n', ' [lb] ')
	except NoSuchElementException:
		print("Cannot find Bio for: " + str(user))
		bio = "blank"
	return bio

def check_postcount(user, driver):
	try:
		post_count = int(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span').text.replace(',',''))
	except NoSuchElementException:
		print("Cannot find Post Count for: " + str(user))
		post_count = 0
	return post_count

def check_followercount(user, driver, private):
	try:
		if private == False:
			followers = int(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title').replace(',',''))
		elif private == True:
			followers = int(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/span/span').get_attribute('title').replace(',',''))
	except NoSuchElementException:
		print("Cannot find Followers for: " + str(user))
		followers = 0
	return followers

def check_followingcount(user, driver, private):
	try:
		if private == False:
			following = int(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text.replace(',',''))
		elif private == True:
			following = int(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/span/span').text.replace(',',''))
	except NoSuchElementException:
		print("Cannot find Following for: " + str(user))
		following = 0
	return following	


def ProfileDetails(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		private = check_private(user, driver)
		verified = check_verified(user, driver)
		real_name = check_name(user, driver)
		website = check_website(user, driver)
		bio = check_bio(user, driver)
		post_count = check_postcount(user, driver)
		followers = check_followercount(user, driver, private)
		following = check_followingcount(user, driver, private)

		userdetail['username']= username
		userdetail['private']= private
		userdetail['verified']= verified
		userdetail['real_name']= real_name 
		userdetail['website']= website
		userdetail['bio']= bio
		userdetail['post_count']= post_count
		userdetail['followers']= followers
		userdetail['following']= following
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details

def VerifiedUsers(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		verified = check_verified(user, driver)

		userdetail['username']= username
		userdetail['verified']= verified
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details

def PrivateUsers(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		private = check_private(user, driver)

		userdetail['username']= username
		userdetail['private']= private
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details

def PostCount(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		post_count = check_postcount(user, driver)

		userdetail['username']= username
		userdetail['post_count']= post_count
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details

def FollowingCount(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		private = check_private(user, driver)
		following = check_followingcount(user, driver, private)

		userdetail['username']= username
		userdetail['following']= following
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details

def FollowerCount(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		private = check_private(user, driver)
		followers = check_followercount(user, driver, private)

		userdetail['username']= username
		userdetail['followers']= followers
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details

def UserWebsite(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		website = check_website(user, driver)

		userdetail['username']= username
		userdetail['website']= website
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details

def UserBio(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		bio = check_bio(user, driver)

		userdetail['username']= username
		userdetail['bio']= bio
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details

def UserRealName(username, password, userlist, drivertype, driverpath):
	limit20(userlist)
	driver = drivercheck(drivertype, driverpath)
	login(username, password, driver)
	details = []
	errorlist = []
	
	for user in userlist:
		userdetail = {}
		username = check_user(user, driver, errorlist)

		if username == 0:
			continue

		real_name = check_name(user, driver)

		userdetail['username']= username
		userdetail['real_name']= real_name
		details.append(userdetail)

	driver.quit()
	print("\nThe following Instagram Profiles could not be found:")
	print(errorlist)

	return details