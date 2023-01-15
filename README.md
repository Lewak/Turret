# INSTRUKCJA DLA IDIOTÓW
## vol.1 RASPBERRY JAKO ETHERNET GADGET
1. Podłączyć raspberry za pomocą kabla USB (DO PORTU USBIN nie USB POWER!)
2. Sprawdzić w menadżerze urządzeń czy jest wykrywany jako usb ethernet gadget. Jak tak, przejść do kroku 6
3. Pobrać sterownik usb ethernet gadget (Acer Incorporated. - Other hardware - USB Ethernet/RNDIS Gadget) stąd: 
	https://www.catalog.update.microsoft.com/Search.aspx?q=USB%20RNDIS%20Gadget
4. Wypakować pobrane archiwum, kliknąć ppm na RNDIS.inf i wybrać install
5. Wejść w menadżer urządzeń, odłączyć i podłączyć RPi, żeby zobaczyć jako co jest wykrywane - może to być np. port COM. Wybrać to urządzenie, 
	update driver, browse my computer, let me pick from a list.., have disk, wybrać RNDIS.inf. Sprawdzić czy teraz jest wykrywany, 
	jak nie to można się popłakać i zawołać mazura.
6. Spróbować połączyć się za pomocą komendy ssh, adres IP można zdobyć poprzez ipconfig albo spróbować użyć: ssh pi@raspberrypi.local (hasło to raspberry)
7. Mozna zainstalowac sterownik Bonjour, by moc używać nazwy .local w IDE (możliwe że niepotrzebne)
8. By uruchomić internet na raspberry. Należy wejść w windows panel sterownia, network and sharing -> change adapter settings
	(old: ethernet settings -> change adapter settings) 
	wybrać AKTUALNE DZIAŁAJĄCE POŁĄCZENIE INTERNETOWE (NIE IP RASPBERRY) -> properties -> settings ->sharing -> w obu checkboxach zaznaczyć allow 
	i wybrać Ethernet gadget RPi
9. Powinno działać 

## vol.2 DŹWIĘK I IO
1. Plik do dźwięku znajduje sie w: /etc/asound.conf
2. Plik autostartu z komendami uruchamianymi przy boocie to /etc/rc.local (komenda sudo pigpiod -t 0)
		
## vol.3 PROCEDURA URUCHAMIANIA TURRETA
1. Wpisać login i password w deployment w file->settings->deployment: login:pi hasło: raspberry
2. Prawy przycisk na pliki programu i deployment->send to raspberrypi

## vol.4 PROCEDURA URUCHAMIANIA PŁYKI ENDERA
1. Zainstalować środowisko kombatybilne z Arduino (np Visual Studio Code z pluginem). 
2. Zainstalować boardy Sanguino
3. Przed uploadem ustawić port COM, ustawić płytkę Sanguino z procesorem Atmega1284 16Mhz.