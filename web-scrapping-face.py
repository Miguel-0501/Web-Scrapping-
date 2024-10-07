from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# Iniciamos el navegador
driver = webdriver.Chrome()

# Abrimos la página web (Facebook)
driver.get("https://web.facebook.com/")
# Hacemos el login
driver.find_element(By.XPATH,"//input[contains(@id,'email')]").send_keys("Michi_0501@hotmail.es")
driver.find_element(By.XPATH,"//input[contains(@id,'pass')]").send_keys("Mich!vz0501")
driver.find_element(By.XPATH,"//button[contains(@name,'login')]").click()

# Entramos a la página del grupo 
url = 'https://www.facebook.com/groups/2972719419686661'
driver.get(url)

keywors = ["feliz", "felicidades", "felicitaciones", "cumpleaños", "cumple"]

# Aqui es donde se va hacer el scrapping de las publicaciones de Facebook
div_elements = driver.find_elements(By.CLASS_NAME, 'x1yztbdb div')
data = []

