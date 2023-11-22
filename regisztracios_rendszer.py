import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import json
import random
import string

class Szemely:
    def __init__(self, nev, kor, szemelyazonosito=None):
        self.nev = nev
        self.kor = int(kor)
        self.szemelyazonosito = szemelyazonosito if szemelyazonosito else generate_random_id()

    def get_info(self):
        return f"Személyazonosító: {self.szemelyazonosito}, Név: {self.nev}, Kor: {self.kor} év"

def generate_random_id(hossz=6):
    karakterek = string.ascii_letters + string.digits
    return ''.join(random.choice(karakterek) for _ in range(hossz))

class RegisztraciosRendszer:
    def __init__(self):
        self.szemelyek = []

    def szemely_regisztralasa(self, nev, kor):
        szemely = Szemely(nev, kor)
        self.szemelyek.append(szemely)
        return szemely

    def szemelyek_megtekintese(self):
        return [szemely.get_info() for szemely in self.szemelyek]

    def atlag_eletkor(self):
        if not self.szemelyek:
            return 0  # Ha nincs regisztrált személy, az átlag 0 év

        osszeg = sum(szemely.kor for szemely in self.szemelyek)
        return osszeg / len(self.szemelyek)

    def regisztralt_szemelyek_szama(self):
        return len(self.szemelyek)

    def mentes_fajlba(self, fajlnev):
        with open(fajlnev, 'w') as fajl:
            data = [{"szemelyazonosito": szemely.szemelyazonosito, "nev": szemely.nev, "kor": szemely.kor} for szemely in self.szemelyek]
            json.dump(data, fajl)

    def betoltes_fajlbol(self, fajlnev):
        with open(fajlnev, 'r') as fajl:
            data = json.load(fajl)
            self.szemelyek = [Szemely(szemely["nev"], szemely["kor"], szemely["szemelyazonosito"]) for szemely in data]

class Alkalmazas:
    def __init__(self, master, regisztraciosrendszer):
        self.master = master
        self.master.title("Regisztrációs Rendszer")
        self.master.geometry("500x350")  # Ablak méretének beállítása

        self.regisztraciosrendszer = regisztraciosrendszer

        self.nev_cim_label = tk.Label(master, text="Név:")
        self.nev_cim_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.nev_entry = tk.Entry(master, width=20)
        self.nev_entry.grid(row=0, column=1, padx=10, pady=10)

        self.kor_cim_label = tk.Label(master, text="Kor:")
        self.kor_cim_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.kor_entry = tk.Entry(master, width=20)
        self.kor_entry.grid(row=1, column=1, padx=10, pady=10)

        self.regisztracio_gomb = tk.Button(master, text="Regisztráció", command=self.szemely_regisztralasa)
        self.regisztracio_gomb.grid(row=0, column=4, pady=10, sticky="e")

        self.megtekintes_gomb = tk.Button(master, text="Személyek Megtekintése", command=self.szemelyek_megtekintese)
        self.megtekintes_gomb.grid(row=1, column=4, pady=10, sticky="e")

        self.mentes_gomb = tk.Button(master, text="Mentés Fájlba", command=self.mentes_fajlba)
        self.mentes_gomb.grid(row=2, column=4, pady=10, sticky="e")

        self.betoltes_gomb = tk.Button(master, text="Betöltés Fájlból", command=self.betoltes_fajlbol)
        self.betoltes_gomb.grid(row=3, column=4, pady=10, sticky="e")

        self.atlag_eletkor_label = tk.Label(master, text="Átlag életkor:")
        self.atlag_eletkor_label.grid(row=5, column=0, pady=10, sticky="e")

        self.regisztralt_szemelyek_label = tk.Label(master, text="Regisztrált személyek:")
        self.regisztralt_szemelyek_label.grid(row=6, column=0, pady=10, sticky="e")

        self.betoltott_adatok_gomb = tk.Button(master, text="Adatok betöltése", command=self.betoltott_adatok_megtekintese)
        self.betoltott_adatok_gomb.grid(row=7, column=4, columnspan=2, pady=10, sticky="e")

        self.bezaras_gomb = tk.Button(master, text="Bezárás", command=self.bezaras)
        self.bezaras_gomb.grid(row=8, column=4, pady=10, columnspan=2, sticky="e")

    def szemely_regisztralasa(self):
        nev = self.nev_entry.get()
        kor = self.kor_entry.get()

        if nev and kor:
            szemely = self.regisztraciosrendszer.szemely_regisztralasa(nev, kor)
            messagebox.showinfo("Regisztráció Sikeres", f"{szemely.get_info()} regisztrálva.")
            self.frissit_adatokat()
        else:
            messagebox.showwarning("Hiányzó Adatok", "Kérlek töltsd ki mindkét mezőt.")

    def szemelyek_megtekintese(self):
        szemelyek_info = "\n".join(self.regisztraciosrendszer.szemelyek_megtekintese())
        messagebox.showinfo("Személyek Információja", szemelyek_info)

    def mentes_fajlba(self):
        fajlnev = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON fájlok", "*.json")])
        if fajlnev:
            self.regisztraciosrendszer.mentes_fajlba(fajlnev)
            messagebox.showinfo("Fájl Mentes", "Az adatok sikeresen elmentve.")

    def betoltes_fajlbol(self):
        fajlnev = filedialog.askopenfilename(filetypes=[("JSON fájlok", "*.json")])
        if fajlnev:
            self.regisztraciosrendszer.betoltes_fajlbol(fajlnev)
            messagebox.showinfo("Fájl Betöltés", "Az adatok sikeresen betöltve.")
            self.frissit_adatokat()

    def frissit_adatokat(self):
        atlag_eletkor = self.regisztraciosrendszer.atlag_eletkor()
        self.atlag_eletkor_label.config(text=f"Átlag életkor: {atlag_eletkor:.2f} év")

        regisztralt_szemelyek_szama = self.regisztraciosrendszer.regisztralt_szemelyek_szama()
        self.regisztralt_szemelyek_label.config(text=f"Regisztrált személyek: {regisztralt_szemelyek_szama}")

    def betoltott_adatok_megtekintese(self):
        betoltott_adatok = self.regisztraciosrendszer.szemelyek_megtekintese()
        self.mutass_lista_dialogus("Betöltött Adatok", betoltott_adatok)

    def mutass_lista_dialogus(self, cim, lista):
        uj_ablak = tk.Toplevel(self.master)
        uj_ablak.title(cim)

        scroltext = scrolledtext.ScrolledText(uj_ablak, width=40, height=10)
        scroltext.pack()

        for elem in lista:
            scroltext.insert(tk.END, elem + "\n")
    def bezaras(self):
        self.master.destroy()
def main():
    regisztraciosrendszer = RegisztraciosRendszer()

    root = tk.Tk()
    app = Alkalmazas(root, regisztraciosrendszer)
    root.mainloop()

if __name__ == "__main__":
    main()