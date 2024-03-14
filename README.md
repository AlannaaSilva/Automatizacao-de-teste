---

# 💻 Projeto para estudo de Testes Automatizados com Selenium 

## Sobre o Projeto

Este projeto contém um conjunto de testes automatizados desenvolvidos com Selenium WebDriver,
focados na automação de testes de interface do usuário para o site (https://front-end-squad11.vercel.app/).
Os testes visam garantir a qualidade e o correto funcionamento da funcionalidade de adicionar projeto.

## 📝 Pré-requisitos

Para executar os testes automatizados, é necessário ter o seguinte ambiente configurado:

- Python 3.8 ou superior
- Selenium WebDriver
- Google Chrome e ChromeDriver compatíveis com a versão do navegador
- (Opcional) Ambiente virtual Python (venv ou conda)

## Configuração do Ambiente

1. **Instalação do Python**

   Certifique-se de ter o Python 3.8 ou superior instalado em sua máquina. Você pode verificar a versão do Python com o seguinte comando:

   ```bash
   python --version
   ```

2. **Configuração do Ambiente Virtual (Opcional)**

   É recomendável utilizar um ambiente virtual para gerenciar as dependências do projeto. Para criar um ambiente virtual, execute:

   ```bash
   python -m venv venv
   ```

   Para ativar o ambiente virtual, use o comando:

   - No Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - No Linux ou macOS:

     ```bash
     source venv/bin/activate
     ```

3. **Instalação das Dependências**

   Com o ambiente virtual ativado, instale as dependências do projeto, incluindo o Selenium e o WebDriver Manager, com o seguinte comando:

   ```bash
   pip install selenium webdriver-manager
   ```

4. **Download do ChromeDriver**

   O WebDriver Manager gerencia automaticamente o ChromeDriver necessário para o Selenium. Não é necessário realizar o download manualmente.



## Executando os Testes

Para executar um teste específico, navegue até o diretório do projeto e execute o script de teste desejado com o Python. Por exemplo:

