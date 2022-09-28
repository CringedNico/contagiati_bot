'''
Lista comandi

info - Informazioni sul bot
mappa_contagi - Visualizza la mappa interattiva dei contagi
contagi_ita - Visualizza l'andamento nazionale dei contagi
'''

TOKEN="***************"

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import datetime
import requests

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


def start(update, context):
    update.message.reply_text("Per ricevere informazioni sui contagi digita /contagi con il nome di una regione (Esempio: /contagi Liguria).")


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
