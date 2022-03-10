from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from faker import Faker
fake = Faker(locale='en_CA')

# ------------------------Fake date section------------------------------
first_name  = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name} {{fake.pyint(11,2999)}}'
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
phone_number = fake.phone_number()[:5]
country = fake.current_country()[:5]
city = fake.city()[:5]
address = fake.address().replace("\n"," ") [:10] #'123 langara'
state = 'BC' #fake.state()[:5]
postal_code = 'L6Y555' #fake.postal_code()[:5]
#------------------------------------------------------------------------
list_list = ['new_username', 'email','new_password','first_name','last_name', 'phone_number', 'country',
'city','address','state','postal_code','new_username','phone_number','country', 'city', 'address', 'state', 'postal_code']

list_name = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
'first_nameRegisterPage','last_nameRegisterPage', 'phone_numberRegisterPage', 'countryListboxRegisterPage'
,'cityRegisterPage', 'addressRegisterPage','state_/_province_/_regionRegisterPage','postal_codeRegisterPage']

#---------------------------------------------------------------------------------
driver = webdriver.Chrome('/Users/owner/Desktop/pythonProject/venv/chromedriver 2')

def setUp():
    print(f'Launch Advantage DEMO home page')
    print('---------------------------****---------------------------')
    driver.maximize_window()
    driver.implicitly_wait(0.25)

    driver.get('https://advantageonlineshopping.com/#/')

    print(driver.current_url)
    print(driver.title)

    if driver.current_url == 'https://advantageonlineshopping.com/#/' or driver.title == '${nbsp}Advantage Shopping': # use $nbsp without space for title
        print('Advantage DEMO home page launched. Move ahead!')
        print(f'current URL: {driver.current_url},Page Title: {driver.title}')

    else:
        print('Advantage DEMO home page did not launch.')
        print(driver.current_url)
        print(driver.title)

        # print(f'{app} homepage URL: {driver.current_url},\nHome Page Title: {driver.title}')
        sleep(3)

def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)

    driver.find_element(By.LINK_TEXT,'CREATE NEW ACCOUNT').click()
    sleep(2)

    #creating user details:
    driver.find_element(By.NAME,'usernameRegisterPage').send_keys(new_username)
    sleep(0.25)
    driver.find_element(By.NAME,'emailRegisterPage').send_keys(email)
    sleep(0.25)
    driver.find_element(By.NAME,'passwordRegisterPage').send_keys(new_password)
    sleep(0.25)
    driver.find_element(By.NAME,'confirm_passwordRegisterPage').send_keys(new_password)
    sleep(0.25)
    driver.find_element(By.NAME,'first_nameRegisterPage').send_keys(first_name)
    sleep(0.25)
    driver.find_element(By.NAME,'last_nameRegisterPage').send_keys(last_name)
    sleep(0.25)
    driver.find_element(By.NAME,'phone_numberRegisterPage').send_keys(phone_number)
    sleep(0.25)
    driver.find_element(By.NAME,'countryListboxRegisterPage').send_keys(country)
    sleep(0.25)
    driver.find_element(By.NAME,'cityRegisterPage').send_keys(city)
    sleep(0.25)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(address)
    sleep(0.25)
    driver.find_element(By.NAME,'state_/_province_/_regionRegisterPage').send_keys(state)
    sleep(0.25)
    driver.find_element(By.NAME,'postal_codeRegisterPage').send_keys(postal_code)
    sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').is_selected()
    sleep(0.25)
    driver.find_element(By.NAME,'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID,'register_btnundefined').click()
    # driver.find_element(By.XPATH,'//inputs[@id= " register_btnundefined" and @class= "sec-sender-a ng-scope invalid"]').click()
    sleep(0.25)
    print(' AOS home page displayed, welcome back')

def sign_out():
        driver.find_element(By.ID, 'hrefUserIcon').click()
        java_script = driver.find_element(By.XPATH, '//label[contains(.,"Sign out")]')
        driver.execute_script("arguments[0].click();", java_script)
        print('you logged out\n Thank you for shopping')
        sleep(0.25)


def log_in(new_username,new_password): 
    if driver.current_url == 'https://advantageonlineshopping.com/#/' and driver.title == '${nbsp}Advantage Shopping':
        # sleep(4)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(3)
        # if driver.current_url == 'https://advantageonlineshopping.com/#/':
        #     print('AOS home Login Page is displayed')# check we are on log in page
        #     sleep(0.25)
        driver.find_element(By.NAME, 'username').send_keys(new_username)
        sleep(3)
        driver.find_element(By.NAME, 'password').send_keys(new_password)
        sleep(3)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(3)
        print(f'---------New User"{new_username}/{new_password},{email}" is added----------------')
        if driver.find_element(By.LINK_TEXT, new_username).is_displayed():
            print(f'---------New User"{new_username}/{new_password},{email}" is added----------------')
            #logger('created')
        else:
            print(f'User is not created!')

# closing down the window
def teardown():  #
    if driver is not None:
        print('------------------**have a awesome day **------------------')
        print(f'The Test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()

# setUp()
# print('------------Welcome to Advantage Online Shopping webiste -------------')
# create_new_user()
# sign_out()
# log_in(new_username,new_password)
# teardown()