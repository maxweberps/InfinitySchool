import urllib.request
from bs4 import BeautifulSoup

def meu_horoscopo():
    signos = ['aries', 'touro', 'gemeos', 'cancer', 'leao',
              'virgem', 'libra', 'escorpiao', 'sagitario',
              'capricornio', 'aquario', 'peixes', 'invalido']

    while True:
        signo = int(input('Qual seu signo?\n[1] Áries\n[2] Touro\n[3] Gêmeos\n[4] Câncer\n'
                          '[5] Leão\n[6] Virgem\n[7] Libra\n[8] Escorpião\n[9] Sagitário\n'
                          '[10] Capricórnio\n[11] Aquário\n[12] Peixes\n[0] Voltar ao menú anterior.\n'))
        if 0 < signo < 13:
            url = f'https://www.horoscopovirtual.com.br/horoscopo/{signos[signo-1]}'

            # Código para header: (usa 'disfarce' de um navegar para acessar a pagina)
            header = ({'User-Agent':
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                           (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0', \
                       'Accept-Language': 'en-US, en;q=0.5'})

            # Solicitação HTTP
            request = urllib.request.Request(url, headers=header)
            abrir = urllib.request.urlopen(request)
            html = abrir.read()
            abrir.close()

            soup = BeautifulSoup(html,'html.parser')
            texto = soup.find('p', {'class': 'text-pred'}).get_text()

            print(texto[:-13:])
