EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 6 6
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
NoConn ~ 4300 4250
NoConn ~ 6950 4250
NoConn ~ 4300 4850
NoConn ~ 4300 4750
NoConn ~ 4300 4650
NoConn ~ 6950 4850
NoConn ~ 6950 4750
NoConn ~ 6950 4650
NoConn ~ 4300 3850
NoConn ~ 6950 3850
Wire Wire Line
	7900 4500 8000 4500
Wire Wire Line
	7900 4550 7900 4500
Wire Wire Line
	7750 4550 7900 4550
Wire Wire Line
	7900 4400 8000 4400
Wire Wire Line
	7900 4450 7900 4400
Wire Wire Line
	7750 4450 7900 4450
Wire Wire Line
	7900 4300 8000 4300
Wire Wire Line
	7900 4150 7900 4300
Wire Wire Line
	7750 4150 7900 4150
Wire Wire Line
	7850 4200 8000 4200
Wire Wire Line
	7850 4250 7850 4200
Wire Wire Line
	7750 4250 7850 4250
$Comp
L Connector:Conn_01x04_Male J?
U 1 1 603C2499
P 8200 4400
AR Path="/603C2499" Ref="J?"  Part="1" 
AR Path="/603B418F/603C2499" Ref="J8"  Part="1" 
F 0 "J8" H 8308 4681 50  0000 C CNN
F 1 "Conn_01x04_Male" H 8308 4590 50  0000 C CNN
F 2 "" H 8200 4400 50  0001 C CNN
F 3 "~" H 8200 4400 50  0001 C CNN
	1    8200 4400
	-1   0    0    1   
$EndComp
Wire Wire Line
	5250 4500 5350 4500
Wire Wire Line
	5250 4550 5250 4500
Wire Wire Line
	5100 4550 5250 4550
Wire Wire Line
	5250 4400 5350 4400
Wire Wire Line
	5250 4450 5250 4400
Wire Wire Line
	5100 4450 5250 4450
Wire Wire Line
	5250 4300 5350 4300
Wire Wire Line
	5250 4150 5250 4300
Wire Wire Line
	5100 4150 5250 4150
Wire Wire Line
	5200 4200 5350 4200
Wire Wire Line
	5200 4250 5200 4200
Wire Wire Line
	5100 4250 5200 4250
$Comp
L Connector:Conn_01x04_Male J?
U 1 1 603C24AC
P 5550 4400
AR Path="/603C24AC" Ref="J?"  Part="1" 
AR Path="/603B418F/603C24AC" Ref="J7"  Part="1" 
F 0 "J7" H 5658 4681 50  0000 C CNN
F 1 "Conn_01x04_Male" H 5658 4590 50  0000 C CNN
F 2 "" H 5550 4400 50  0001 C CNN
F 3 "~" H 5550 4400 50  0001 C CNN
	1    5550 4400
	-1   0    0    1   
$EndComp
$Comp
L Driver_Motor:Pololu_Breakout_DRV8825 A?
U 1 1 603C24B3
P 4700 4250
AR Path="/603C24B3" Ref="A?"  Part="1" 
AR Path="/603B418F/603C24B3" Ref="A1"  Part="1" 
F 0 "A1" H 4700 5031 50  0000 C CNN
F 1 "Pololu_Breakout_DRV8825" H 4700 4940 50  0000 C CNN
F 2 "Module:Pololu_Breakout-16_15.2x20.3mm" H 4900 3450 50  0001 L CNN
F 3 "https://www.pololu.com/product/2982" H 4800 3950 50  0001 C CNN
	1    4700 4250
	1    0    0    -1  
$EndComp
$Comp
L Driver_Motor:Pololu_Breakout_DRV8825 A?
U 1 1 603C24C6
P 7350 4250
AR Path="/603C24C6" Ref="A?"  Part="1" 
AR Path="/603B418F/603C24C6" Ref="A2"  Part="1" 
F 0 "A2" H 7350 5031 50  0000 C CNN
F 1 "Pololu_Breakout_DRV8825" H 7350 4940 50  0000 C CNN
F 2 "Module:Pololu_Breakout-16_15.2x20.3mm" H 7550 3450 50  0001 L CNN
F 3 "https://www.pololu.com/product/2982" H 7450 3950 50  0001 C CNN
	1    7350 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 603C24CC
P 6800 3950
AR Path="/603C24CC" Ref="R?"  Part="1" 
AR Path="/603B418F/603C24CC" Ref="R5"  Part="1" 
F 0 "R5" V 6593 3950 50  0000 C CNN
F 1 "R" V 6684 3950 50  0000 C CNN
F 2 "" V 6730 3950 50  0001 C CNN
F 3 "~" H 6800 3950 50  0001 C CNN
	1    6800 3950
	0    1    1    0   
$EndComp
$Comp
L Device:R R?
U 1 1 603C24D3
P 6800 4050
AR Path="/603C24D3" Ref="R?"  Part="1" 
AR Path="/603B418F/603C24D3" Ref="R7"  Part="1" 
F 0 "R7" V 6593 4050 50  0000 C CNN
F 1 "R" V 6684 4050 50  0000 C CNN
F 2 "" V 6730 4050 50  0001 C CNN
F 3 "~" H 6800 4050 50  0001 C CNN
	1    6800 4050
	0    1    1    0   
$EndComp
Wire Wire Line
	4700 3650 4700 3350
Text HLabel 4700 3350 1    50   Input ~ 0
12V
Text HLabel 7350 3650 1    50   Input ~ 0
12V
Wire Wire Line
	6300 3950 6450 3950
Wire Wire Line
	6650 4050 6450 4050
Wire Wire Line
	6450 4050 6450 3950
Connection ~ 6450 3950
Wire Wire Line
	6450 3950 6650 3950
Text HLabel 6300 3950 0    50   Input ~ 0
5V
$Comp
L Device:R R?
U 1 1 603D354E
P 4100 4050
AR Path="/603D354E" Ref="R?"  Part="1" 
AR Path="/603B418F/603D354E" Ref="R4"  Part="1" 
F 0 "R4" V 3893 4050 50  0000 C CNN
F 1 "R" V 3984 4050 50  0000 C CNN
F 2 "" V 4030 4050 50  0001 C CNN
F 3 "~" H 4100 4050 50  0001 C CNN
	1    4100 4050
	0    1    1    0   
$EndComp
Wire Wire Line
	4250 4050 4300 4050
$Comp
L Device:R R?
U 1 1 603D41C9
P 4100 3950
AR Path="/603D41C9" Ref="R?"  Part="1" 
AR Path="/603B418F/603D41C9" Ref="R3"  Part="1" 
F 0 "R3" V 3893 3950 50  0000 C CNN
F 1 "R" V 3984 3950 50  0000 C CNN
F 2 "" V 4030 3950 50  0001 C CNN
F 3 "~" H 4100 3950 50  0001 C CNN
	1    4100 3950
	0    1    1    0   
$EndComp
Wire Wire Line
	4250 3950 4300 3950
Wire Wire Line
	3700 4050 3700 3950
Wire Wire Line
	3700 4050 3950 4050
Connection ~ 3700 3950
Wire Wire Line
	3700 3950 3950 3950
Wire Wire Line
	3550 3950 3700 3950
Text HLabel 3550 3950 0    50   Input ~ 0
5V
Text HLabel 7450 5050 3    50   Input ~ 0
12V_GND
Text HLabel 7350 5050 3    50   Input ~ 0
5V_GND
Text HLabel 4700 5050 3    50   Input ~ 0
5V_GND
Text HLabel 4800 5050 3    50   Input ~ 0
12V_GND
Text HLabel 6950 4350 0    50   Input ~ 0
STEP_2
Text HLabel 6950 4450 0    50   Input ~ 0
DIR_2
Text HLabel 4300 4350 0    50   Input ~ 0
STEP_1
Text HLabel 4300 4450 0    50   Input ~ 0
DIR_1
$EndSCHEMATC
