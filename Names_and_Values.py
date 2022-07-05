from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pywhatkit
import time
import pyautogui
import keyboard as k
import undetected_chromedriver as uc
import os
import wave
from pygame import mixer


@dataclass
class Product:
    Natiga: str = None
    Rm: str = None
    Name: str = None


def print_natiga(url, rkam_gloss):
    try:
        counter = 0
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        driver.get(url)
        counter = 0

        driver.find_element("xpath",
                            '/html/body/div/center/table/tbody/tr[6]/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/input').send_keys(
            rkam_gloss)
        driver.find_element("xpath",
                            '/html/body/div/center/table/tbody/tr[6]/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/input').click()

        try:
            Natiga = driver.find_element("xpath",
                                         '/html/body/div/center/table/tbody/tr[6]/td[2]/table/tbody/tr[2]/td/form/b/table/tbody/tr[23]/td[2]/p/span/b/font').text
            Rm = driver.find_element("xpath",
                                     '/html/body/div/center/table/tbody/tr[6]/td[2]/table/tbody/tr[2]/td/form/b/table/tbody/tr[1]/td[2]/p/span/b/font').text
            Name = driver.find_element("xpath",
                                       '/html/body/div/center/table/tbody/tr[6]/td[2]/table/tbody/tr[2]/td/form/b/table/tbody/tr[2]/td[2]/p/span/b/font').text
            print(Rm)
            print(Natiga)
            print(Name)

        except:
            Natiga = "None"
            pass
        driver.quit()
        return Product(Natiga=Natiga)
    except:
        Natiga = "None"

    return Product(Natiga=Natiga, Rm=Rm, Name=Name)


if __name__ == '__main__':

    clickty = True
    xxx = 0
    Sum = []
    Seats = 14400
    while clickty:
        x = print_natiga("http://www.comm.alexu.edu.eg/Result407.asp", Seats)
        Seats = Seats - 1

        Sum.append(x.Natiga)

        xxx = xxx + 1
        if xxx == 100:
            clickty = False

        print(Sum)

        # if "None" not in x.Natiga:
        #     clickty = False
        #
        #     pywhatkit.sendwhatmsg_to_group_instantly('group link','your message', 15)
        #     pyautogui.click(881, 596)
        #     time.sleep(4)
        #     k.press_and_release('enter')
        #
        #     pywhatkit.sendwhatmsg_instantly("number of the person", "your message ", 15)
        #     pyautogui.click(881, 596)
        #     time.sleep(4)
        #     k.press_and_release('enter')
        #     mixer.init()
        #     mixer.music.load("C:/Users/youss/Desktop/Noot.mp3")
        #     mixer.music.play()
        #     while mixer.music.get_busy():  # wait for music to finish playing
        #         time.sleep(1)
        #     # os.system("shutdown /s /t 1")
        # else:
        #     print("Not yet")
        #     time.sleep(30)
