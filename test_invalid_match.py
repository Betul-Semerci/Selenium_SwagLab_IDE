# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import global_constants as c

class TestInvalidMatch():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_invalid_match(self):
    self.driver.get(c.BASE_URL)
    self.driver.maximize_window()
    self.driver.find_element(By.XPATH, "//input[@id=\'user-name\']").click()
    self.driver.find_element(By.ID, "user-name").send_keys("1")
    self.driver.find_element(By.XPATH, "//input[@id=\'password\']").click()
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    assert self.driver.find_element(By.XPATH, "//div[@id=\'login_button_container\']/div/form/div[3]/h3").text == "Epic sadface: Username and password do not match any user in this service"
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div[2]/div").click()
    self.driver.find_element(By.ID, "user-name").send_keys("problem_user")
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div[2]").click()
    self.driver.find_element(By.ID, "password").send_keys("1")
    self.driver.find_element(By.ID, "login-button").click()
    assert self.driver.find_element(By.XPATH, "//div[@id=\'login_button_container\']/div/form/div[3]/h3").text == "Epic sadface: Username and password do not match any user in this service"
    self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div[2]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username and password do not match any user in this service"
    self.driver.close()
  
