from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import func

def meu_mapa():
    voltar = 1
    while voltar !=0:
        nome = str(input('Digite o seu nome:\n'))

        dia_mes = func.nascimento()
        hora_minuto = func.hora_nascimento()

        dia = int(dia_mes[0:2])
        mes = int(dia_mes[3:])
        ano = func.ano_nascimento()

        hora = int(hora_minuto[0:2])
        minuto = int(hora_minuto[3:])

        cidade = str(input('Qual a cidade que você nasceu?'))
        estado = str(input('Qual o estado que você nasceu?'))

        print('\nAguarde enquanto alinho seus astros.\n')

        driver = webdriver.Chrome()

        # Acessar o site:
        driver.get(r'https://astro.cafeastrology.com/natal.php')

        #preencher nome
        preencher_nome = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[2]/form/div/div[1]/input[5]').send_keys(nome)

        # Preencher a data de nascimento
        dia_nascimento = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[2]/form/div/div[1]/select[2]')

        for x in range(dia - 1):
            dia_nascimento.send_keys(Keys.DOWN)

        mes_nascimento = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[2]/form/div/div[1]/select[1]')
        for x in range(mes - 1):
            mes_nascimento.send_keys(Keys.DOWN)

        ano_nascimento = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[2]/form/div/div[1]/select[3]')
        if ano > 2000:
            for x in range(ano - 2000):
                ano_nascimento.send_keys(Keys.DOWN)
        elif ano < 2000:
            for x in range(2000 - ano):
                ano_nascimento.send_keys(Keys.UP)
        elif ano == 2000:
            ano_nascimento.send_keys(ano)

        # Preencher a hora de nascimento
        preencher_hora = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[2]/form/div/div[1]/select[4]')
        if hora > 12:
            for x in range(hora - 12):
                preencher_hora.send_keys(Keys.DOWN)
        elif hora < 12:
            for x in range(12 - hora):
                preencher_hora.send_keys(Keys.UP)
        elif hora == 12:
            preencher_hora.send_keys(hora)

        preencher_minutos = driver.find_element(By.XPATH,
                                                '/html/body/div[3]/div/div[2]/form/div/div[1]/select[5]')
        for x in range(minuto):
            preencher_minutos.send_keys(Keys.DOWN)

        # Preencher a Cidade de Nascimento

        preencher_cidade = driver.find_element(By.XPATH,
                                               '/html/body/div[3]/div/div[2]/form/div/div[1]/div/div[1]/input').send_keys(
            cidade)

        preencher_estado = driver.find_element(By.XPATH,
                                               '/html/body/div[3]/div/div[2]/form/div/div[1]/div/div[1]/select')
        driver.implicitly_wait(10)
        preencher_estado.send_keys(cidade + ", " + estado)

        Submit = driver.find_element(By.XPATH,
                                     '/html/body/div[3]/div/div[2]/form/div/div[2]/input')
        Submit.click()

        mapa = driver.find_element(By.XPATH,
                                   '/html/body/div[3]/div/div[2]/div[3]/div[1]/table').text

        print(mapa)


