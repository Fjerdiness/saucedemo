from selenium import webdriver
from dicts.tests import test_login

def main():
    driver = webdriver.Chrome()  
    try:
        test_login(driver)
        
        # test_other_function(driver)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
