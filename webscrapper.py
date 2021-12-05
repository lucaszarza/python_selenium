import time

from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)  # Optional argument, if not specified will search path.

driver.get('http://www.itau.com.br/');

agencia = driver.find_element_by_id('agencia')
agencia.send_keys('0390')

conta = driver.find_element_by_id('conta')
conta.send_keys('16306-1')

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

time.sleep(30)

login = driver.find_element_by_id('acessar')
login.click()

time.sleep(4)

basic_access = driver.find_element_by_id('rdBasico')
basic_access.click()

time.sleep(3)

ctn_button = driver.find_element_by_id('btn-continuar')
ctn_button.click()

time.sleep(3)
time.sleep(5)

driver.find_element_by_xpath('/html/body/div[2]/button').click()
time.sleep(3)


driver.find_element_by_xpath('/html/body/div[1]/header/div[5]/div/div/nav/ul/li[2]/ul/li[2]/a').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/section/div/div[3]/section/div[1]/div/div[7]/div/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/cpv-select/div/div/select/option[10]').click()

time.sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/section/div/div[3]/section/div[1]/div/div[8]/div[2]/div/nav/ul/li[3]/a').click()

time.sleep(4)

driver.quit()



# driver.quit()