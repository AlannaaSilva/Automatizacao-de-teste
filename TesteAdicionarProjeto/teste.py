from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Importa a classe Service
caminho_foto = 'TesteAdicionarProjeto\imagens\imagem-teste.jpg' 

servico = Service(ChromeDriverManager().install())  #Cria uma instância de Service
navegador = webdriver.Chrome(service=servico)

navegador.get('https://front-end-squad11.vercel.app/')

navegador.find_element('xpath',' //*[@id=":r0:"]').send_keys('testealanna@gmail.com') #emailLogin

sleep(2)

navegador.find_element('xpath',' //*[@id=":r1:"] ').send_keys('123456789') #senhaLogin

sleep(2)

navegador.find_element('xpath',' //*[@id=":r2:"]').click() #botaoentrar

sleep(5)



navegador.find_element('xpath','//*[@id=":r3:"]').click() #adicionar projeto botao

sleep(5)

navegador.find_element('xpath', '//input[@name="title" and @type="text"]').send_keys('Exemplo de título para teste')


sleep(2)

navegador.find_element('xpath', '//input[@id="tags-outlined"]').send_keys('ux')

sleep(2)

navegador.find_element('xpath', '//input[@name="link" and @type="text"]').send_keys('www.behance.com.br')


sleep(2)


navegador.find_element('xpath', '//textarea[@id="outlined-multiline-static"]').send_keys('Esse é um exemplo de como a descrição deve ser!')

sleep(2)


navegador.execute_script('document.getElementById("fileInput").style.display="block";')
sleep(2) 

navegador.find_element('xpath', '//input[@id="fileInput" and @name="imagem" and @type="file"]').send_keys(caminho_foto)  # Fazer o upload do arquivo
 

sleep(2)


 # navegador.find_element('xpath',' //*[@id="root"]/main/div/div[4]/div/form/div[1]/p[2]').click() # visualizar publicação

# sleep(2)

 # navegador.find_element('xpath',' //*[@id=":ro:"]').click() # salvar publicação


# sleep(40)


