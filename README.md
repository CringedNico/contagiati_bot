# Bot Contagi
## Test
Il bot è utilizzabile al seguente link: [ContagiBot](https://t.me/ContagiatiBot)
## Informazioni
Il progetto Contagi Bot è nato durante la seconda ondata da Covid-19 per poter rimanere aggiornati sull'andamento dei contagi velocemente.

Lo script è stato programmato in Python, con l'aggiunta delle API di Telegram, in modo tale che, alla ricezione di un comando dall'applicazione, esegue una richiesta HTTP alla repository Github del dipartimento della Protezione Civile per prelevare i dati in formato JSON che vengono aggiornati giornalmente.
In seguito, formatta il testo e inoltra il messaggio all'utente che ha effettuato la richiesta.

Lo script è hostato su un VPS Oracle (come per il progetto di Zabbix) e viene eseguito all'avvio del server grazie al servizio creato appositamente.
