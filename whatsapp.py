from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# Criando driver para o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# Entrando no whatsapp web
driver.get('https://web.whatsapp.com/')

# Tempo para logar com o QR code
time.sleep(20)

# Contatos - Os nomes devem estar idênticos aos nomes salvos na lista de contatos do WhatsApp
contatos = ['Contato1', 'Contato2', 'Contato3']


def buscar_contato(contato):
  campo_busca = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
  time.sleep(3)
  campo_busca.click()
  campo_busca.send_keys(contato)
  campo_busca.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
  campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
  time.sleep(3)
  campo_mensagem[1].click()
  campo_mensagem[1].send_keys(mensagem)
  campo_mensagem[1].send_keys(Keys.ENTER)

# Para cada contato indicado, fazer a busca e escrever a mensagem
for contato in contatos:
  buscar_contato(contato)
  enviar_mensagem(f'Olá, {contato}, como vai você?')

  

  
  
