# Konfiguracja środowiska
1. Zainstaluj sterownik: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads, zakładka CP210x VCP Windows
2. Podłącz płytkę przez USB C
3. W Visual Studio Code zainstaluj plugin "Arduino". Za pomocą `Ctrl + Shift + P` wywołuj komendy do komunikacji z płytką.
4. Arduino: Board Manager -> Additional URLs -> Add -> wpisz https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json i zatwierdź -> wyłącz okno Board Manager
5. Arduino: Board Config -> ESP32 Dev Module (esp32), Core Debug Level: Verbose
6. Arduino: Select Serial Port -> COM4

# Uruchamianie kodu
1. Arduino: Upload
2. Gdy płytka jest zorientowana tak, że kabel USB wchodzi do niej od dołu, na prawo od kabla znajduje się przycisk flash, a na lewo reset. Gdy w konsoli output stanie na "Serial port COM4", wciśnij i przytrzymaj flash, następnie wciśnij reset, puść reset, puść flash (kolejność ma znaczenie).