from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()

#Insira seu nome de usuário e senha entre as aspas
username = ""
password = ""

class UnfollowBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def goToPage():
        browser.implicitly_wait(5)
        browser.get('https://instagram.com')
        sleep(5)


    def login(username, password):
        username_input = browser.find_element_by_css_selector(
            "input[name='username']")
        password_input = browser.find_element_by_css_selector(
            "input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)


    def saveLoginPage():
        try:
            browser.implicitly_wait(3), browser.get('https://instagram.com')
        finally:
            sleep(2)


    def declineNotifications():
        try:
            browser.implicitly_wait(3), browser.find_element_by_xpath(
                "//button[text()='Agora não']").click()
        finally:
            sleep(2)

    def get_people():
        sleep(2)
        scroll_box = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        prev_height, height = 0, 1
        while prev_height != height:
            prev_height = height
            sleep(3)
            height = browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        close = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
        close.click()
        return names

    def get_unfollowers():
        #Substitua o endereço entre aspas abaixo pela url do seu perfil
        browser.get("https://www.instagram.com/ronieboone/")
        sleep(3)
        Following = browser.find_element_by_xpath("//a[contains(@href,'/following')]")
        Following.click()
        following = UnfollowBot.get_people()
        Followers = browser.find_element_by_xpath("//a[contains(@href,'/followers')]")
        Followers.click()
        followers = UnfollowBot.get_people()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

def __main__():
    iteration = UnfollowBot
    iteration.goToPage()
    iteration.login(username, password)
    iteration.saveLoginPage()
    iteration.declineNotifications()
    iteration.get_unfollowers()
    try:
        iteration.browser.close()
    except:
        print("Falha")
        iteration.browser.close()

__main__()
