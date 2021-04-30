from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

path = "C:\\webdriver\\chromedriver.exe"

class TestBikroy:
    def test_copyright(self):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("http://bikroy.com/")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        status = self.driver.find_element_by_class_name('copyright').is_displayed()
        if status == True:
            print("Winning First")
            allure.attach(self.driver.get_screenshot_as_png(), name="copyright", attachment_type=AttachmentType.PNG)
            assert True, "Copyright © Saltside Technologies"
        else:
            assert False

        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        new_status = self.driver.find_element_by_xpath("//html/body/nav/div/ul[3]/li[5]/a/span").is_displayed()
        if new_status == True:
            print("WInning")
            allure.attach(self.driver.get_screenshot_as_png(), name="postcard", attachment_type=AttachmentType.PNG)
            assert True, "POST YOUR ADD Button is there"
        else:
            assert False
        self.driver.close()
        
    def test_data(self):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://bikroy.com/en/ads/dhaka/")
        # self.driver.find_element_by_xpath('//*[@id="dd-button"]').click()
        # self.driver.find_element_by_xpath('//*[@id="price_asc"]').click()
        xpath = '//*[@id="app-wrapper"]//span[text()="Tk {}")]'
        elements = self.driver.find_elements_by_class_name("price--3SnqI")
        # new_list = []

        new_list = [int(i.text[3:8].replace(",","")) for i in elements if i.text[3:] != ""]
        # print(new_list)
        new_list.sort()

        min_val = min(new_list)
        if 1 <= len(str(min_val)) <= 3:
            new_func = self.driver.find_element_by_xpath(f'//*[@id="app-wrapper"]//span[text()="Tk {min_val}"]').click()
            another_status = self.driver.find_element_by_class_name('sub-title--37mkY')
            description = self.driver.find_element_by_class_name('heading--2u5sJ')
            self.driver.find_element_by_class_name('call-text--30D-J').click()
            phone = self.driver.find_element_by_class_name('phone-numbers--2COKR')
            # print(description.text)
            # print(phone.text)
            if another_status:
                allure.attach(self.driver.get_screenshot_as_png(), name="status", attachment_type=AttachmentType.PNG)
                assert True, another_status.text
            else:
                assert False
            
            if description:
                allure.attach(self.driver.get_screenshot_as_png(), name="description", attachment_type=AttachmentType.PNG)
                assert True, description.text + 'is here'
            else:
                assert False
            
            if phone:
                allure.attach(self.driver.get_screenshot_as_png(), name="phonenumber", attachment_type=AttachmentType.PNG)
                assert True, "Valid mobile Number is there"
            else:
                assert False


        elif len(str(min_val)) == 4:
            val = len(str(min_val))
            val.insert(1,',')
            val = ''.join(val)
            new_func = self.driver.find_element_by_xpath(f'//*[@id="app-wrapper"]//span[text()="Tk {val}"]').click()
        self.driver.close()


    @pytest.mark.parametrize("data", ["dhaka", "chattogram", "sylhet", "khulna", "barishal", "rajshahi", "rangpur", "mymensingh"])
    def test_case(self,data):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get(f"https://bikroy.com/en/ads/{data}/")
        # self.driver.find_element_by_xpath('//*[@id="dd-button"]').click()
        # self.driver.find_element_by_xpath('//*[@id="price_asc"]').click()
        xpath = '//*[@id="app-wrapper"]//span[text()="Tk {}")]'
        elements = self.driver.find_elements_by_class_name("price--3SnqI")
        # new_list = []

        new_list = [int(i.text[3:8].replace(",","")) for i in elements if i.text[3:] != ""]
        # print(new_list)
        new_list.sort()

        min_val = min(new_list)
        if 1 <= len(str(min_val)) <= 3:
            new_func = self.driver.find_element_by_xpath(f'//*[@id="app-wrapper"]//span[text()="Tk {min_val}"]').click()
            another_status = self.driver.find_element_by_class_name('sub-title--37mkY')
            description = self.driver.find_element_by_class_name('heading--2u5sJ')
            self.driver.find_element_by_class_name('call-text--30D-J').click()
            phone = self.driver.find_element_by_class_name('phone-numbers--2COKR')
            # print(description.text)
            # print(phone.text)
            if another_status:
                allure.attach(self.driver.get_screenshot_as_png(), name="status", attachment_type=AttachmentType.PNG)
                assert True, another_status.text
            else:
                assert False
            
            if description:
                allure.attach(self.driver.get_screenshot_as_png(), name="description", attachment_type=AttachmentType.PNG)
                assert True, description.text + 'is here'
            else:
                assert False
            
            if phone:
                allure.attach(self.driver.get_screenshot_as_png(), name="phonenumber", attachment_type=AttachmentType.PNG)
                assert True, "Valid mobile Number is there"
            else:
                assert False


        elif len(str(min_val)) == 4:
            val = len(str(min_val))
            val.insert(1,',')
            val = ''.join(val)
            new_func = self.driver.find_element_by_xpath(f'//*[@id="app-wrapper"]//span[text()="Tk {val}"]').click()
        self.driver.close()
