from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('http://oferta.senasofiaplus.edu.co/sofia-oferta/')


post = driver.find_element_by_xpath('//div[@onclick="cerrarNoticiaPrincipal()"]')
post.click()

Boton = driver.find_element_by_xpath('//input[@class="ingresobutton2"]')
Boton.send_keys(Keys.ENTER)
time.sleep(5)


usuario = driver.find_element_by_name("ingreso")
usuario.send_keys("72276604")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("josso_password")
clave.send_keys("Cc701012013*")
clave.send_keys(Keys.ENTER)


