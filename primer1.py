import time
pocetna_pozicija = 0
cilj = 50
trenutna_pozicija = 0
brzina = 10

for x in range (10):
    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("Stigao do cilja.")
        break
    elif trenutna_pozicija > cilj:
        print("Prosli ste.")
    elif trenutna_pozicija < cilj:
        print("Niste jos stigli.")
    trenutna_pozicija += brzina
    time.sleep(1)

