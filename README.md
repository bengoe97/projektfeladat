# projektfeladat

Gálné Bengő Evelin

Az elkészített Python program egy regisztrációs rendszert valósít meg egy grafikus felhasználói felületen, amelyet a Tkinter modullal készített GUI segítségével jelenít meg. A program lehetővé teszi személyek regisztrációját, az általuk megadott név és életkor alapján. Az alkalmazás lehetőséget biztosít a regisztrált személyek megtekintésére, adataik mentésére fájlba, valamint a fájlból történő betöltésre.

Modulok:

1. tkinter (tk):
    A Tkinter egy beépített GUI (grafikus felhasználói felület) modul a Pythonban.
2. messagebox (a tkinter része):
    A messagebox modul a Tkinter része, amely ablakokban megjelenő üzeneteket jelenít meg.
3. filedialog (a tkinter része):
   A filedialog modul a Tkinter része, amely fájlkezelési ablakokat biztosít.
4. scrolledtext (tkinter része):
   A scrolledtext modul a Tkinter része, amely görgethető szövegdobozt biztosít.

Függvények:

1. generate_random_id:
   
   Egy függvény, amely egy véletlenszerű azonosítót generál.
   
2. Szemely osztály:
   
   __init__(self, nev, kor, szemelyazonosito=None): Az osztály konstruktora.
   
   get_info(self): A Szemely objektum adatait visszaadó függvény.
  
3. RegisztraciosRendszer osztály:
   
   __init__(self): Az osztály konstruktora.
   
   szemely_regisztralasa(self, nev, kor): Új személy hozzáadását végző függvény.
   
   szemelyek_megtekintese(self): A regisztrált személyek adatainak listáját visszaadó függvény.
   
   atlag_eletkor(self): Az átlagéletkor kiszámítását végző függvény.
   
   regisztralt_szemelyek_szama(self): A regisztrált személyek számát visszaadó függvény.
   
   mentes_fajlba(self, fajlnev): A regisztrált személyek adatainak mentését végző függvény.
   
   betoltes_fajlbol(self, fajlnev): A regisztrált személyek adatainak betöltését végző függvény.
   
4. Alkalmazas osztály:
   
   __init__(self, master, regisztraciosrendszer): Az osztály konstruktora.
   
   szemely_regisztralasa(self): A regisztrációs gomb lenyomását kezelő függvény.
   
   szemelyek_megtekintese(self): A személyek megtekintése gomb lenyomását kezelő függvény.
   
   mentes_fajlba(self): A mentés gomb lenyomását kezelő függvény.
   
   betoltes_fajlbol(self): A betöltés gomb lenyomását kezelő függvény.
   
   frissit_adatokat(self): Az átlagéletkor és a regisztrált személyek számának frissítését végző függvény.
   
   betoltott_adatok_megtekintese(self): A betöltött adatok megtekintése gomb lenyomását kezelő függvény.
   
   mutass_lista_dialogus(self, cim, lista): Egy párbeszédablakot megjelenítő függvény.
   
   bezaras(self): A bezárás gomb lenyomását kezelő függvény.

