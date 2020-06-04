import requests
import tkinter as window
class convertitore():

    def __init__(self):
        self.finestra=window.Tk()
        self.finestra.configure(bg="grey50")
        self.finestra.geometry("600x600")
        self.frame=window.Frame(self.finestra,bg="grey80",width=300,height=50)
        self.frame.place(y=10,x=130)
        self.etichetta_tit=window.Label(self.frame,text="convertitore")
        self.etichetta_tit.config(font=("Courier", 22))
        self.etichetta_tit.place(y=10, x=45)
        self.etichetta = window.Label(self.finestra, text="valute")
        self.etichetta.config(font=("Courier", 15))
        self.etichetta.place(y=130,x=65)
        self.etichetta_eur = window.Label(self.finestra, text="Euro")
        self.etichetta_eur.config(font=("Courier", 15))
        self.etichetta_eur.place(y=130, x=250)
        self.etichetta_res = window.Label(self.finestra, text="Valore")
        self.etichetta_res.config(font=("Courier", 15))
        self.etichetta_res.place(y=130, x=390)
        self.lista=window.Listbox(self.finestra,width=25,height=20,bg="snow")
        self.lista.place(y=160,x=30)
        self.testo_eur=window.Text(self.finestra,width=10,height=1,bg="snow")
        self.testo_eur.place(y=160,x=235)
        self.testo_valore = window.Text(self.finestra, width=10, height=1, bg="snow")
        self.testo_valore.place(y=160, x=385)
        self.pulsante=window.Button(self.finestra,text="Aggiorna",command=self.formatta_info)
        self.pulsante.place(y=200,x=235)
        self.pulsante_calcola = window.Button(self.finestra, text="Calcola",command=self.calcola)
        self.pulsante_calcola.place(y=250, x=235)



        self.finestra.mainloop()

    def get_data(self,indirizzo_api="https://api.exchangeratesapi.io/latest"):
        self.indirizzo_api=indirizzo_api
        self.richiesta=requests.get(self.indirizzo_api)
        self.file=self.richiesta.json()
        return self.file

    def formatta_info(self):
        self.file_jason=self.get_data()
        self.file_jason=list(self.file_jason["rates"])
        for i in range(len(self.file_jason)):
            self.lista.insert(window.END,self.file_jason[i])



    def prova(self):
        selezione=self.lista.curselection()[0]
        valute=self.get_data()
        lista=list(valute["rates"])
        valuta=lista[selezione]
        return valuta


    def calcola(self):
        self.testo_valore.delete(1.0,window.END)
        valute=self.get_data()
        lista=valute["rates"]
        valore=lista[self.prova()]
        quantita=self.testo_eur.get(1.0,window.END)
        calcolo=valore*float(quantita)
        self.testo_valore.insert(1.0,calcolo)



mio_convertitore=convertitore()