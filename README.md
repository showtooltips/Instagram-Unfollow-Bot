## Instalação:
  
### Windows:

Faça download dos seguintes arquivos:
- Firefox: https://www.mozilla.org/en-US/firefox/download/thanks/
- Python: https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe
- Geckodriver: https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-win64.zip

Instale os programas e extraia o Geckodriver para dentro da pasta Documentos do seu computador. Em seguida, execute os seguintes comandos no terminal:
```
$ cd InstaBot
$ pip install selenium
```
Caso tenha alguma dificuldade com a instalação de algum dos itens acima, abaixo estão os links com a instalação detalhada de cada um:

- Selenium Application: https://selenium-python.readthedocs.io/installation.html
- Firefox WebDriver: https://selenium-python.readthedocs.io/installation.html#drivers
      
## Uso:
```
$ python InstaBot.py
```
Para rodar varias instâncias simultaneamente é só duplicar a pasta e rodar um 'InstaBot.py' diferente para cada uma delas

## Troubleshooting:
1. Tente 'python3' ao invés de 'python' e 'pip3' ao invés de 'pip' caso algum desses comando dê problema.
2. Caso haja algum problema com o firefox e/ou geckodriver, assegure-se de que os caminhos são os listados abaixo:
   - Linux:
     - Firefox: /usr/lib/firefox/firefox/
     - Geckodriver: /usr/local/bin/geckodriver/
   - Windows:
     - Firefox: C:\Program Files\Mozilla Firefox\firefox.exe
     - Geckodriver: C:\User\Documents\geckodriver.exe

## Obs.:
Suporte para outras línguas ainda não implementado. Seu navegador e páginas deverão ser acessados em Português-BR.