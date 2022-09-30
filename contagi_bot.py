'''
Lista comandi

info - Informazioni sul bot
mappa_contagi - Visualizza la mappa interattiva dei contagi
contagi_ita - Visualizza l'andamento nazionale dei contagi
'''

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import datetime
import requests


TOKEN = "*****************************"

'''
def get_ora():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")


def get_data():
    today = datetime.date.today()
    return today.strftime("%d/%m/%Y")


def get_data_ora():
    return f'{get_data()} - {get_ora()}'
'''

def get_data_ora(string):
	campi = string.split('-')
	sstmp = campi[2].split('T')

	return f'{sstmp[0]}/{campi[1]}/{campi[0]} - {sstmp[1]}'


def get_index(dati, nome, tipo):
    for i in range(0, len(dati)):
        if dati[i][tipo].upper() == nome.upper():
            return i


def risposta2(update, context):
    request = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json')
    dati = request.json()
    indice_regione = get_index(dati, "ITA", "stato")

    update.message.reply_text("Stato: Italia" + '\n' + "----------------------------" + '\n' + "Nuovi positivi: " + str(dati[indice_regione]["nuovi_positivi"]) + '\n'
                              + "Totale positivi: " + str(dati[indice_regione]["totale_positivi"]) + '\n' + "Ricoverati con sintomi: " + str(dati[indice_regione]["ricoverati_con_sintomi"]) + '\n'
                              + "Terapia intensiva: " + str(dati[indice_regione]["terapia_intensiva"]) + '\n' + "Totale ospedalizzati: " + str(dati[indice_regione]["totale_ospedalizzati"]) + '\n'
                              + '\n' + "Ultimo aggiornamento: " + get_data_ora(dati[indice_regione]["data"]))


def extract_regione(text):
    text = text.split()[1].strip()

    if text == str("Valle") or text == str("valle") or text == str("VDA") or text == str("vda") or text == str("valled'aosta") or text == str("valledaosta"):
        text = str("Valle d'Aosta")
        return text
    else:
        return text


def risposta(update, context):
    request = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni-latest.json')
    dati = request.json()
    regione = str(extract_regione(update.message.text))
    indice_regione = get_index(dati, regione, "denominazione_regione")
    update.message.reply_text("Regione: " + str(dati[indice_regione]["denominazione_regione"]) + '\n' + "----------------------------" + '\n' + "Nuovi positivi: " + str(dati[indice_regione]["nuovi_positivi"]) + '\n'
                              + "Totale positivi: " + str(dati[indice_regione]["totale_positivi"]) + '\n' + "Ricoverati con sintomi: " + str(dati[indice_regione]["ricoverati_con_sintomi"]) + '\n'
                              + "Terapia intensiva: " + str(dati[indice_regione]["terapia_intensiva"]) + '\n' + "Totale ospedalizzati: " + str(dati[indice_regione]["totale_ospedalizzati"]) + '\n'
                              + '\n' + "Ultimo aggiornamento: " + get_data_ora(dati[indice_regione]["data"]))


def start(update, context):
    update.message.reply_text("Per ricevere informazioni sui contagi digita /contagi con il nome di una regione (Esempio: /contagi Liguria).")


def info(update, context):
    update.message.reply_text("Il progetto Contagi Bot è nato durante la seconda ondata da Covid-19 per poter rimanere aggiornati sull'andamento dei contagi velocemente. "
                              "Lo script è stato programmato in Python, in modo tale che, alla ricezione di un comando dall'applicazione, "
			      "esegue una richiesta HTTP alla repository Github del dipartimento della Protezione Civile per prelevare i dati in formato JSON che vengono aggiornati giornalmente.")


def mappa(update, context):
    update.message.reply_text("Ecco la mappa interattiva relativa all'Italia sui contagi: http://opendatadpc.maps.arcgis.com/apps/opsdashboard/index.html#/b0c68bce2cce478eaac82fe38d4138b1")


if __name__ == '__main__':
    upd = Updater(TOKEN, use_context=True)
    disp = upd.dispatcher

    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("info", info))
    disp.add_handler(CommandHandler("mappa_contagi", mappa))
    disp.add_handler(CommandHandler("contagi_ita", risposta2))
    disp.add_handler(CommandHandler("contagi", risposta))

    upd.start_polling()
    upd.idle()
