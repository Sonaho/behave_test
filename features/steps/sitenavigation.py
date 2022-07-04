from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *

@given ('I launch Chrome browser')
def step_impl(context):
    PATH = "D://DEV/chromedriver/chromedriver.exe"
    context.driver = webdriver.Chrome(PATH)

@when ('I open "{web}" and compare "{title}"')
def step_impl(context, web, title):
	test = True
	context.driver.get(web)
	if context.driver.title != title:
		test = False
	context.driver.quit()
	assert test

@when ("I search selenium")
def step_impl(context):
	context.driver.find_element(By.ID, "search").send_keys('selenium')
	çcontext.driver.find_element(By.CLASS_NAME, "search-form__button").click()


@then ('I landing at page "{web}"')
def step_impl(context, web):
	test = True
	if context.driver.current_url != web:
		test = False
	assert test
