import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os, sys

class AnimalArchiveTest(unittest.TestCase):

    def setUp(self):

        service = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

        # Get the version from the command-line argument
        version = sys.argv[1]

        # Set the base URL based on the version
        if version == "first":
            self.base_url = 'file://' + os.path.abspath('first_version/')
            
        elif version == "second":
            self.base_url = 'file://' + os.path.abspath('second_version/')
        else:
            raise ValueError("Invalid version argument: must be 'first' or 'second'")
    
    def test_existence_elements(self):
        self.driver.get(self.base_url + '/index.html')
        
        # Test existence of navigation elements
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Home"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Dogs"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Cats"))
        )
        
        # Test existence of other elements
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Dog Image']"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Cat Image']"))
        )
    '''
    def test_images_have_previous_and_next_buttons(self):
        self.driver.get(self.base_url + '/index.html')

        # Test that the dog image has previous and next buttons
        previous_button = self.driver.find_element(by=By.XPATH, value="//button[@onclick='changeImage(true, -1)']")
        next_button = self.driver.find_element(by=By.XPATH, value="//button[@onclick='changeImage(true, 1)']")
        self.assertTrue(previous_button.is_displayed())
        self.assertTrue(next_button.is_displayed())
    '''

    def test_size_location_elements_dog(self):
        self.driver.get(self.base_url + '/index.html')

        # Test the size and location of dog image
        dog_image = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Dog Image']")
        self.assertEqual(dog_image.size['width'], 383)
        self.assertEqual(dog_image.size['height'], 336)

    def test_size_location_elements_cat(self):
        self.driver.get(self.base_url + '/index.html')

        # Test the size and location of cat image
        cat_image = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cat Image']")
        self.assertEqual(cat_image.size['width'], 288)
        self.assertEqual(cat_image.size['height'], 300)

    def test_content_elements(self):
        self.driver.get(self.base_url + '/index.html')

        # Test the content of the title
        title = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(title.text, "Animal Archive")
        # Add more content checks for other elements here

    def test_links_flow(self):
        self.driver.get(self.base_url + '/index.html')

        # Test link to Dogs.html
        dogs_link = self.driver.find_element(By.LINK_TEXT, "Dogs")
        dogs_link.click()
        self.driver.get(self.base_url + '/Dogs.html')

        # Test link to Cats.html
        self.driver.get(self.base_url + '/index.html')
        cats_link = self.driver.find_element(by=By.LINK_TEXT, value="Cats")
        cats_link.click()
        self.driver.get(self.base_url + '/Cats.html')

    def test_dog_image_links_to_dogs_page(self):
        self.driver.get(self.base_url + '/index.html')

        # Click on the dog image and test that it links to Dogs.html
        dog_image = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Dog Image']")
        dog_image.click()
        self.driver.get(self.base_url + '/Dogs.html')

        # Click the 'Back to Home' link and test that it takes you back to the home page
        home_link = self.driver.find_element(By.LINK_TEXT, "Back to Home Page")
        home_link.click()
        self.assertEqual(self.driver.current_url, self.base_url + '/index.html')

    def test_cats_image_links_to_cats_page(self):
        self.driver.get(self.base_url + '/index.html')

        # Click on the cats image and test that it links to Cats.html
        cats_image = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cat Image']")
        cats_image.click()
        self.assertEqual(self.driver.current_url, self.base_url + '/Cats.html')

        # Click the 'Back to Home' link and test that it takes you back to the home page
        home_link = self.driver.find_element(By.LINK_TEXT, "Back to Home Page")
        home_link.click()
        self.assertEqual(self.driver.current_url, self.base_url + '/index.html')

    def test_dogs_page_has_golden_retriever_image(self):
        self.driver.get(self.base_url + '/Dogs.html')

        # Test that the page has a golden retriever image
        dog_image = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Dog Image']")
        self.assertTrue(dog_image.is_displayed())

    def test_cats_page_has_cat_image(self):
        self.driver.get(self.base_url + '/Cats.html')

        # Test that the page has a cat image
        cat_image = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cat Image']")
        self.assertTrue(cat_image.is_displayed())

    def test_home_page_background_color(self):
        self.driver.get(self.base_url + '/index.html')

        # Test that the background color of the home page is white
        body = self.driver.find_element(By.CSS_SELECTOR, "body")
        self.assertEqual(body.value_of_css_property("background-color"), "rgba(0, 0, 0, 0)")

    '''
    def test_other_page_exists(self):
        self.driver.get(self.base_url + '/index.html')

        # Test that the 'Other' link is present and links to the Other.html page
        other_link = self.driver.find_element(By.LINK_TEXT, "Other")
        other_link.click()
        self.assertEqual(self.driver.current_url, self.base_url + '/Other.html')
    '''

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
