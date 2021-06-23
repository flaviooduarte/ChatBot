import re
from bot import IAOOE
import schedule
import time

contatos = ['Meu Particular']

def produtividadePoda():
        print('-------------- Início do processo.')
        bot = IAOOE("poda")
        bot.ProdutividadePoda()
        bot.selecionaConversa("Meu Particular")
        bot.enviaArquivo(bot.dir_path + '/poda_flavio.png')
        bot.enviaMensagem("Produtividade de Poda dia a dia")
        time.sleep(3)
        bot.__exit__()

def produtividadeLV():
        print('-------------- Início do processo.')
        bot = IAOOE("lv")
        bot.ProdutividadeLV()
        bot.selecionaConversa("Meu Particular")
        bot.enviaArquivo(bot.dir_path + '/lv_flavio.png')
        bot.enviaMensagem("Produtividade de Linha Viva dia a dia")
        time.sleep(3)
        bot.__exit__()

def produtividadeencLV():
        print('-------------- Início do processo.')
        bot = IAOOE("enclv")
        bot.ProdutividadeEncLV()
        bot.selecionaConversa("Meu Particular")
        bot.enviaArquivo(bot.dir_path + '/enclv_flavio.png')
        bot.enviaMensagem("Produtividade média por encarregado de Linha Viva no mês")
        time.sleep(3)
        bot.__exit__()

def produtividadeencPoda():
        print('-------------- Início do processo.')
        bot = IAOOE("encpd")
        bot.ProdutividadeEncPoda()
        bot.selecionaConversa("Meu Particular")
        bot.enviaArquivo(bot.dir_path + '/encpd_flavio.png')
        bot.enviaMensagem("Produtividade média por encarregado de Poda no mês")
        time.sleep(3)
        bot.__exit__()

def NTC():
        print('-------------- Início do processo.')
        bot = IAOOE("ntc")
        bot.ntc()
        bot.selecionaConversa("Meu Particular")
        bot.enviaArquivo(bot.dir_path + '/ntc_flavio.png')
        bot.enviaMensagem("Panorama de execução das NTCs")
        time.sleep(3)
        bot.__exit__()

def clima():
        print('-------------- Início do processo.')
        bot = IAOOE("clima")
        bot.Clima()
        bot.selecionaConversa("Meu Particular")
        bot.enviaArquivo(bot.dir_path + '/clima_flavio.png')
        bot.enviaMensagem("Previsão do Tempo")
        time.sleep(3)
        bot.__exit__()

schedule.every().day.at("16:00").do(produtividadePoda)
schedule.every().day.at("16:15").do(produtividadeLV)
schedule.every().day.at("16:30").do(produtividadeencPoda)
schedule.every().day.at("16:45").do(produtividadeencLV)
schedule.every().day.at("17:00").do(NTC)
schedule.every().day.at("17:15").do(clima)

while True:
        schedule.run_pending()
        time.sleep(60)