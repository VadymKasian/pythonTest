from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
library = []


@given("open browser")
def step_impl(context):
    driver.get("https://amazon.com")


@Then("type search query")
def step_iml(context):
    searchField = driver.find_element_by_id("twotabsearchtextbox")
    searchField.send_keys("Java")
    searchField.send_keys(Keys.ENTER)


@Then("press book filter")
def step_iml(context):
    searchField = driver.find_element_by_xpath(
        "//span[contains(@class,'a-size-base a-color-base') and contains(text(),'Books')]")
    searchField.click()


@Then("add tooks to list")
def step_iml(context):
    bookList = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-medium']")
    print(len(bookList))

    for element in bookList:
        title = element.find_element_by_xpath(".//div[@class='sg-col-inner']/div/h2").text
        author = element.find_element_by_xpath(
            ".//div[@class='sg-col-inner']/div/div[@class='a-row a-size-base a-color-secondary']").text
        book = [title, author]
        library.append(book)

    for book in library:
        print("Title - " + str(book[0]) + " \nauthor - " + str(book[1]) + "\n")


@Then("check book from url contains in list")
def step_iml(context):
    driver.get(
        "https://www.amazon.com/Effective-Java-Joshua-Bloch/dp/0134685997/ref=sr_1_1?dchild=1&keywords=java&qid=1585726876&rnid=2941120011&s=books&sr=1-1")

    title = driver.find_element_by_class_name("a-size-extra-large").text
    author = driver.find_element_by_xpath("//span[@class='author notFaded']").text
    contains = False
    for book in library:
        if book[0] == title:
            contains = True

    print("Book\nTitle - " + title + "\nAuthor - " + author)
    print("contains - " + str(contains))

    driver.close()
