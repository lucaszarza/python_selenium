import time

from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.itau.com.br/');

agencia = driver.find_element_by_id('agencia')
agencia.send_keys('0367')

conta = driver.find_element_by_id('conta')
conta.send_keys('15587-6')

time.sleep(2)

login = driver.find_element_by_id('btnLoginSubmit')
login.click()

time.sleep(3)

cpf = driver.find_element_by_id('campoCpf')
time.sleep(2)
cpf.send_keys('14370152801')

time.sleep(5)

continue_button = driver.find_element_by_id('botao-continuar')
continue_button.click()

time.sleep(2)

counter = 15
while counter > 0:
    alert(f'Você tem {counter} segundos para digitar a senha do banco!')
    counter -=1
    time.sleep(1)


login = driver.find_element_by_id('acessar')
login.click()


# driver.quit()