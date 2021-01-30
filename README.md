# InstaScrape
It currently can scrape a specified Instagram Profiles following count, follower count, post count, name, bio, website, verification check and private profile check.

Due to the limitation Instagram has implemented on anonymous users, this script requires a Username and Password to function. This allows you to bypass this. After various levels of testing, I have limited the script to process a *maximum of 20 profiles at a time*.

The script will open up an automated window which can be viewed in real time by the user *(if drivertype=Chrome or drivertype=Gecko)*. It will first log you in, deal with the various pop-ups *(Save Password, Cookies, Notifications etc.)* and take you to the front page. It will then loop through the list of users you have provided.







## Installation & Requirements
Download or Copy the **InstaScrape.py** file. You can then import the necessary functions in a new Python file.

You will need the **Selenium** Package for Python. You can download it via pip.
```bash
pip install selenium
```
You will need [ChromeDriver](https://chromedriver.chromium.org/) or [GeckoDriver](https://github.com/mozilla/geckodriver/releases) to run Selenium.

## Usage
InstaScrape shares five paramenters for each of its functions:

```python
ProfileDetails(username, password, userlist, drivertype, driverpath)
```


* *username*: Your Instagram Username.

* *password*: Your Instagram Password.

* *userlist*: A list of Instagram Usernames you can pass through for the script to analyse.

* *drivertype*: This takes 3 values: "Chrome", "Gecko" and "HeadlessGecko". Chrome and Gecko will open a window while HeadlessGecko will not show the browser.

* *driverpath*: The path to where your driver is saved on your device.

## Available Features
```python
VerifiedUsers(username, password, users, drivertype, driverpath) ### Name and Verified Value (True/False) 
PrivateUsers(username, password, users, drivertype, driverpath) ### Name and Private Value (True/False) 
PostCount(username, password, users, drivertype, driverpath) ### Name and Post Count Value (int)
FollowingCount(username, password, users, drivertype, driverpath) ### Name and Following Count (int)
FollowerCount(username, password, users, drivertype, driverpath) ### Name and Follower Count (int)
UserWebsite(username, password, users, drivertype, driverpath) ### Name and Website Value (str)
UserBio(username, password, users, drivertype, driverpath) ### Name and User Bio Value (str)
UserRealName(username, password, users, drivertype, driverpath) ### Name and User Real Name (str)
ProfileDetails(username, password, users, drivertype, driverpath) ### Name and all values above
```


## Example

```python
from InstaScrape import ProfileDetails

username="myinstagramusername"
password="supersecretpassword"

ChromeDriver = "C:/Users/skathii/drivers/chromedriver.exe"

users = [
'anamesolonginstascrapewillskipit',
'theweeknd',
'kyliejenner',
'cristiano'
]

x = ProfileDetails(username, password, users, drivertype="Chrome", driverpath="ChromeDriver")
print(x)

```

gives us:

```python
### Cookies: Accept [x]
### Entering in Instagram Username and Password..
### Save Login Info: Not Now [x]
### Notifications: Not Now [x]
Username anamesolonginstascrapewillskipit does not exist. Skipping...
Cannot find Bio for: cristiano

The following Instagram Profiles could not be found:
['anamesolonginstascrapewillskipit']


[{'username': 'theweeknd', 'private': False, 'verified': True, 'real_name': 'The Weeknd', 'website': 'youtu.be/XXYlFuWEuKI', 'bio': 'save your tears', 'post_count': 270, 'followers': 28264399, 'following': 4}, {'username': 'kyliejenner', 'private': False, 'verified': True, 'real_name': 'Kylie \U0001f90d', 'website': 'kyliecosmetics.com', 'bio': '@kyliecosmetics @kylieskin', 'post_count': 6623, 'followers': 213156595, 'following': 47}, {'username': 'cristiano', 'private': False, 'verified': True, 'real_name': 'Cristiano Ronaldo', 'website': 'www.cristianoronaldo.com', 'bio': 'blank', 'post_count': 2998, 'followers': 258466764, 'following': 465}]

```

