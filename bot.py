## Importando bibliotecas
import os
import time
from datetime import datetime
from PIL import Image
# Bibliotecas Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
#import pyodbc
import pandas as pd
from collections import Counter # contador da quantidade de elementos em uma lista

diretorio = os.getcwd()

# Definição da classe para o bot
class IAOOE:

	dir_path = diretorio

	def __init__(self, nome_bot):
		'''
		Função criada para configuração do drive do chrome
		'''
		print('\n'*2)
		print('IAOOE inicada.')
		self.gravaLog('--IAOOEInicio--')
		self.chrome = self.dir_path+'\chromedriver.exe'
		self.options = webdriver.ChromeOptions()
		self.options.add_argument(r'user-data-dir='+self.dir_path+'\profile\wwp2') # carrega os dados de cache
		self.options.add_argument('--log-level=3')
		self.options.add_argument('--mute-audio')
		#self.options.add_argument('--headless')
		self.options.add_argument('--disable-gpu')
		self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)
		self.driver.get('https://web.whatsapp.com/')
		self.driver.implicitly_wait(10) # Aguarda 20 segundos para o carregamento da página
		print('apos - implicitly_wait')
#		WebDriverWait(self.driver, 240).until(ec.visibility_of_element_located((By.CLASS_NAME, '_2rZZg'))) # Aguarda 20 segundos para carregar o whatsapp
#		WebDriverWait(self.driver, 240).until(ec.visibility_of_element_located((By.CLASS_NAME, '_3Kxus'))) # Aguarda 20 segundos para carregar o whatsapp
		print('apos - webdriverwait')
		self.user = '4005918'
		self.psw = 'Felet*15'

	def selecionaConversa(self, contato):
		self.driver.find_element_by_xpath('//*[@title="Nova conversa"]').click() # botão de nova conversa
		#self.caixa_de_pesquisa = self.driver.find_element_by_class_name('_2zCfw')
#		barra_localizar = self.driver.find_element_by_class_name('ZP8RM')
		barra_localizar = self.driver.find_element_by_class_name('_2Evw0') # LABEL DENTRO DA DIV DA CAIXA
		#print('-->barra_localizar')
#		caixa_texto_localizar = barra_localizar.find_element_by_class_name('_3u328')
		caixa_texto_localizar = barra_localizar.find_element_by_class_name('_1awRl')# copyable-text selectable-text
		print('-->caixa_texto_localizar')
		time.sleep(2)
		#keyboard.type(contato)
		#self.caixa_de_pesquisa.send_keys(contato)
		caixa_texto_localizar.send_keys(contato)
		print('-->caixa_texto_localizar.send_keys')
		time.sleep(2)
		self.driver.find_element_by_class_name('_3Pwfx').click()
		print('-->botao clicar')
		self.gravaLog('--selecionaConversa-- ' + contato)

	def enviaMensagem(self,mensagem):	
#exemplo: self.caixa_de_mensagem = self.driver.find_element_by_class_name('_3FeAD')
#exemplo: barra_mensagem = self.driver.find_element_by_class_name('_2i7Ej')
		barra_mensagem = self.driver.find_element_by_class_name('DuUXI')
#exemplo: caixa_texto_mensagem = barra_mensagem.find_element_by_class_name('_3u328')
		caixa_texto_mensagem = barra_mensagem.find_element_by_class_name('_1awRl')
		caixa_texto_mensagem.send_keys('*IA OOE:* {}'.format(mensagem))
		time.sleep(1)
		self.botao_enviar = self.driver.find_element_by_class_name('_2Ujuu')
		self.botao_enviar.click()
		time.sleep(1)
		self.gravaLog('--enviaMensagem-- ' + mensagem)

	def enviaArquivo(self, arquivo, mensagem = None):
		self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
		self.driver.find_element_by_css_selector("input[type='file']").send_keys(arquivo)
		time.sleep(2)
		barra_mensagem = self.driver.find_element_by_class_name('DuUXI')
		caixa_mensagem_arquivo = barra_mensagem.find_element_by_class_name('_2HE1Z')
		if mensagem != None:
			caixa_mensagem_arquivo.send_keys('*IA OOE:* {}'.format(mensagem))
		time.sleep(1)
		self.driver.find_element_by_css_selector("span[data-icon='send']").click()
		self.gravaLog('--enviaArquivo-- Mensagem: {} || Arquivo: {}'.format(mensagem,arquivo))

	def gravaLog(self, mensagem):
		f = open('log_conversa.txt', "a")
		f.write("{0}{1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), mensagem))
		f.close()

	def encerrarBot(self):
		self.driver.quit()
		time.sleep(1)

		if self.driver is not None:
			self.driver.quit()
			time.sleep(1)
			# Colocar no inicio do codigo também
			delete_paths = ['./profile/wwp2/Local State', './profile/wwp2/Default/Preferences']

		for delete_path in delete_paths:
			if os.path.exists(delete_path):
				os.remove(delete_path)

		print('IAOOE fim.')
		self.gravaLog('--IAOOEFim--')

	def ProdutividadePoda(self):
		# Carregando o painel e salvando como imagem
		options_poda = webdriver.ChromeOptions()
		options_poda.add_argument('--headless')
		options_poda.add_argument('--disable-gpu')
		options_poda.add_argument('--window-size=1390x2500')
		driver_poda = webdriver.Chrome(self.chrome, options=options_poda)
		url = 'https://app.powerbi.com/view?r=eyJrIjoiMDNjOTQ2MmQtZGIwNC00NTIyLTg3NjQtOTllMWE5MzkyNDhkIiwidCI6IjBjNmMyM2RlLTU0NmItNDVmZi04MTFhLWE4OGNjNTE0YWU1ZiJ9'
		driver_poda.get(url)
		time.sleep(3)
		element = driver_poda.find_element_by_xpath('/html/body/div[1]/root/div/div/div[1]/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[4]/transform/div/div[3]/div/visual-modern')
		location = element.location
		size = element.size
		driver_poda.save_screenshot('poda_flavio.png')
		time.sleep(2)
		driver_poda.close()

		# Cropando a imagem
		im = Image.open(r"poda_flavio.png")
		x = location['x']
		y = location['y']
		width = location['x']+size['width']+88
		height = location['y']+size['height']+24
		im1 = im.crop((int(x), int(y)-23, int(width), int(height)))
		im1.save('poda_flavio.png')

	def ProdutividadeLV(self):
		# Carregando o painel e salvando como imagem
		options_lv = webdriver.ChromeOptions()
		options_lv.add_argument('--headless')
		options_lv.add_argument('--disable-gpu')
		options_lv.add_argument('--window-size=1390x2500')
		driver_lv = webdriver.Chrome(self.chrome, options=options_lv)
		url = 'https://app.powerbi.com/view?r=eyJrIjoiODA3ZWVlNGQtYWUwMC00NmY4LWJkYWMtNTc5YTVkZTNmNjIyIiwidCI6IjBjNmMyM2RlLTU0NmItNDVmZi04MTFhLWE4OGNjNTE0YWU1ZiJ9'
		driver_lv.get(url)
		time.sleep(3)
		element = driver_lv.find_element_by_xpath('/html/body/div[1]/root/div/div/div[1]/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[4]/transform/div/div[3]/div/visual-modern')
		location = element.location
		size = element.size
		driver_lv.save_screenshot('lv_flavio.png')
		time.sleep(2)
		driver_lv.close()

		# Cropando a imagem
		im = Image.open(r"lv_flavio.png")
		x = location['x']
		y = location['y']
		width = location['x']+size['width']+88
		height = location['y']+size['height']+24
		im1 = im.crop((int(x), int(y)-23, int(width), int(height)))
		im1.save('lv_flavio.png')

	def ProdutividadeEncLV(self):
		# Carregando o painel e salvando como imagem
		options_enclv = webdriver.ChromeOptions()
		options_enclv.add_argument('--headless')
		options_enclv.add_argument('--disable-gpu')
		options_enclv.add_argument('--window-size=1390x2500')
		driver_enclv = webdriver.Chrome(self.chrome, options=options_enclv)
		url = 'https://app.powerbi.com/view?r=eyJrIjoiODA3ZWVlNGQtYWUwMC00NmY4LWJkYWMtNTc5YTVkZTNmNjIyIiwidCI6IjBjNmMyM2RlLTU0NmItNDVmZi04MTFhLWE4OGNjNTE0YWU1ZiJ9'
		driver_enclv.get(url)
		time.sleep(3)
		element = driver_enclv.find_element_by_xpath('/html/body/div[1]/root/div/div/div[1]/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[7]/transform/div/div[3]/div/visual-modern')
		location = element.location
		size = element.size
		driver_enclv.save_screenshot('enclv_flavio.png')
		time.sleep(2)
		driver_enclv.close()

		# Cropando a imagem
		im = Image.open(r"enclv_flavio.png")
		x = location['x']
		y = location['y']
		width = location['x'] + size['width']+66
		height = location['y'] + size['height']+35
		im1 = im.crop((int(x)-5, int(y)-30, int(width), int(height)))
		im1.save('enclv_flavio.png')

	def ProdutividadeEncPoda(self):
		# Carregando o painel e salvando como imagem
		options_encpd = webdriver.ChromeOptions()
		options_encpd.add_argument('--headless')
		options_encpd.add_argument('--disable-gpu')
		options_encpd.add_argument('--window-size=1390x2500')
		driver_encpd = webdriver.Chrome(self.chrome, options=options_encpd)
		url = 'https://app.powerbi.com/view?r=eyJrIjoiMDNjOTQ2MmQtZGIwNC00NTIyLTg3NjQtOTllMWE5MzkyNDhkIiwidCI6IjBjNmMyM2RlLTU0NmItNDVmZi04MTFhLWE4OGNjNTE0YWU1ZiJ9'
		driver_encpd.get(url)
		time.sleep(3)
		element = driver_encpd.find_element_by_xpath('/html/body/div[1]/root/div/div/div[1]/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[7]/transform/div/div[3]/div/visual-modern')
		location = element.location
		size = element.size
		driver_encpd.save_screenshot('encpd_flavio.png')
		time.sleep(2)
		driver_encpd.close()

		# Cropando a imagem
		im = Image.open(r"encpd_flavio.png")
		x = location['x']
		y = location['y']
		width = location['x'] + size['width']+66
		height = location['y'] + size['height']+35
		im1 = im.crop((int(x)-5, int(y)-30, int(width), int(height)))
		im1.save('encpd_flavio.png')

	def ntc(self):
		# Carregando o painel e salvando como imagem
		options_ntc = webdriver.ChromeOptions()
		options_ntc.add_argument('--headless')
		options_ntc.add_argument('--disable-gpu')
		options_ntc.add_argument('--window-size=1390x2500')
		driver_ntc = webdriver.Chrome(self.chrome, options=options_ntc)
		url = 'https://app.powerbi.com/view?r=eyJrIjoiZDc0ODdmMTYtNmNmNi00OWZhLWE5MTAtODRkNDY5YjI1Njc2IiwidCI6IjBjNmMyM2RlLTU0NmItNDVmZi04MTFhLWE4OGNjNTE0YWU1ZiJ9&pageName=ReportSection'
		driver_ntc.get(url)
		time.sleep(3)
		element = driver_ntc.find_element_by_xpath('/html/body/div[1]/root/div/div/div[1]/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[11]/transform/div/div[3]/div/visual-modern')
		location = element.location
		size = element.size
		driver_ntc.save_screenshot('ntc_flavio.png')
		time.sleep(2)
		driver_ntc.close()

		# Cropando a imagem
		im = Image.open(r"ntc_flavio.png")
		x = location['x']
		y = location['y']
		width = location['x'] + size['width'] + 50
		height = location['y'] + size['height'] + 35
		im1 = im.crop((int(x), int(y), int(width), int(height)))
		im1.save('ntc_flavio.png')

	def Clima(self):
		# Carregando o painel e salvando como imagem
		options_clima = webdriver.ChromeOptions()
		options_clima.add_argument('--headless')
		options_clima.add_argument('--disable-gpu')
		options_clima.add_argument('--window-size=1390x2500')
		driver_clima = webdriver.Chrome(self.chrome, options=options_clima)
		url = 'https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/321/riodejaneiro-rj/'
		driver_clima.get(url)
		time.sleep(3)
		element = driver_clima.find_element_by_xpath('/html/body/div[3]/div[5]/div[4]/div[1]/div/div[4]/section[1]')
		location = element.location
		size = element.size
		driver_clima.save_screenshot('clima_flavio.png')
		time.sleep(2)
		driver_clima.close()

		# Cropando a imagem
		im = Image.open(r"clima_flavio.png")
		x = location['x']
		y = location['y']
		width = location['x'] + size['width'] + 15
		height = location['y'] + size['height']
		im1 = im.crop((int(x) - 35, int(y), int(width), int(height)))
		im1.save('clima_flavio.png')

	def __exit__(self):
		self.encerrarBot()
