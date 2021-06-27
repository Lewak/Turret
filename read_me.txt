INSTRUKCJA DLA IDIOTÓW
vol.1 RASPBERRY JAKO ETHERNET GADGET
	1. Podłączyć raspberry za pomocą kabla USB (DO PORTU USBIN nie USB POWER!)
	2. Sprawdzić w menadżerze urządzeń czy jest wykrywany jako usb ethernet gadget. Jak tak, przejść do kroku 5
	3. Pobrać sterownik usb ethernet gadget stąd: https://www.catalog.update.microsoft.com/Search.aspx?q=USB%20RNDIS%20Gadget
	4. Za pomocą opcji menadżera urządzeń, uaktualnić driver, wybrać katalog z pobranym plikiem i go zainstalowac. Sprawdzić czy teraz jest wykrywany, jak nie to można
	się popłakać i zawołać mazura
	5. Spróbować połączyć się za pomocą komendy ssh, adres IP można zdobyć poprzez ipconfig
	6. Mozna zainstalowac sterownik Bonjour, by moc używać nazwy .local w IDE (możliwe że niepotrzebne)
	7. By uruchomić internet na raspberry. Należy wejść w windows panel sterownia, ethernet settings -> change adapter settings i wybrać AKTUALNE DZIAŁAJĄCE
	POŁĄCZENIE INTERNETOWE (NIE IP RASPBERRY) -> settings ->sharing -> w obu checkboxach zaznaczyć allow.
	8. Powinno działać 

vol.2 DŹWIĘK I IO
	1. Plik do dźwięku znajduje sie w: /etc/asound.conf
	2. Plik autostartu z komendami uruchamianymi przy boocie to /etc/rc.local (komenda sudo pigpiod -t 0)
		
vol.3 PROCEDURA URUCHAMIANIA TURRETA
	1. Wpisać login i password w deployment w file->settings->deployment: login:pi hasło: raspberry
	2. Prawy przycisk na pliki programu i deployment->send to raspberrypi