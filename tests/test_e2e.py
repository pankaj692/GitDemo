from selenium import webdriver
import time
import pytest
from tests.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        button1 = self.driver.find_element_by_xpath('/html/body/app-root/app-header-component/nav/app-login-component/button')
        button1.click()
        print("click sucessfully")
        time.sleep(1)

        # click continue with email
        button2 = self.driver.find_element_by_xpath('//*[@id="login"]/div/div[3]/button')
        button2.click()
        print("click sucessfully")

        # enter the mail id
        Email = "don.don692@gmail.com"
        user_name = self.driver.find_element_by_xpath('//*[@id="login"]/div/form/div[2]/input')
        user_name.send_keys(Email)
        print("Email entered")

        # enter the password
        Password = "Pankaj692@"
        user_name = self.driver.find_element_by_xpath('//*[@id="login"]/div/form/div[3]/input')
        user_name.send_keys(Password)
        print("Password entered")

        # click the login button
        button3 = self.driver.find_element_by_xpath('//*[@id="login"]/div/form/div[5]/button')
        button3.click()
        print("click sucessfully")

        print(self.driver.title)
