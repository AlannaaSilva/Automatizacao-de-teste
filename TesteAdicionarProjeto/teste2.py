from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())  #Cria uma instância de Service
navegador = webdriver.Chrome(service=servico)

navegador.get('https://front-end-squad11.vercel.app/')

navegador.find_element('xpath',' //*[@id=":r0:"]').send_keys('testealanna@gmail.com') #emailLogin

sleep(2)

navegador.find_element('xpath',' //*[@id=":r1:"] ').send_keys('123456789') #senhaLogin

sleep(2)

navegador.find_element('xpath',' //*[@id=":r2:"]').click() #botaoentrar

sleep(5)


# Testar se  funcionalidade de adicionar projeto

navegador.find_element('xpath','//*[@id=":r3:"]').click() 

sleep(5)

#Testar se o sistema impede a adição de um titulo incorreto com (menos de 4 caracteres).
navegador.find_element('xpath', '//input[@name="title" and @type="text"]').send_keys('Olá')
sleep(2)

# Testar se  funcionalidade de adicionar tag

# Encontre e clique no campo de entrada "TAGS"
navegador.find_element('xpath', '//input[@id="tags-outlined"]').click()
sleep(4)

# Encontre e clique na primeira opção de TAG
navegador.find_element('xpath', "//li[@role='option'][1]").click()

sleep(2)

#Testar se o sistema impede a adição de um link incorreto com (menos de 4 caracteres).
navegador.find_element('xpath', '//input[@name="link" and @type="text"]').send_keys('www')

sleep(2)

# Testar se o sistema impede a adição de um descrição incorreto com (menos de 4 caracteres)
navegador.find_element('xpath', '//textarea[@id="outlined-multiline-static"]').send_keys('des')

sleep(2)

navegador.find_element('xpath',' //*[@id=":r6:"]').click() # salvar publicação

sleep(10)

navegador.quit()
