import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AnimalArchiveTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='path/to/chromedriver')
        self.driver.maximize_window()

    def test_existence_elements(self):
        self.driver.get('path/to/index.html')
        
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

    def test_size_location_elements(self):
        self.driver.get('path/to/index.html')

        # Test the size and location of dog image
        dog_image = self.driver.find_element_by_css_selector("img[alt='Dog Image']")
        self.assertEqual(dog_image.size['width'], 300)
        self.assertEqual(dog_image.size['height'], 200)
        # Add more size and location checks for other elements here

    def test_content_elements(self):
        self.driver.get('path/to/index.html')

        # Test the content of the title
        title = self.driver.find_element_by_tag_name("h1")
        self.assertEqual(title.text, "Animal Archive")
        # Add more content checks for other elements here

    def test_links_flow(self):
        self.driver.get('path/to/index.html')

        # Test link to Dogs.html
        dogs_link = self.driver.find_element_by_link_text("Dogs")
        dogs_link.click()
        self.assertEqual(self.driver.current_url, 'path/to/Dogs.html')

        # Test link to Cats.html
        self.driver.get('path/to/index.html')
        cats_link = self.driver.find_element_by_link_text("Cats")
        cats_link.click()
        self.assertEqual(self.driver.current_url, 'path/to/Cats.html')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
