EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A 11000 8500
encoding utf-8
Sheet 1 1
Title "HR2 SW PCB"
Date "2020-06-13"
Rev "A"
Comp "Homebrew Robotics Club"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L HR2:HOLE;M2.5 H4
U 1 1 5F2F7A6B
P 2650 4450
F 0 "H4" H 2600 4500 50  0000 L CNN
F 1 "HOLE;M2.5" H 2450 4400 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 2850 4500 60  0001 L CNN
F 3 "M2.5 Mounting Hole" H 2850 4300 60  0001 L CNN
	1    2650 4450
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D8
U 1 1 5F30CB7A
P 5400 4150
F 0 "D8" V 5500 4250 50  0000 R CNN
F 1 "LED;GRNRA" V 5300 4600 50  0000 R CNN
F 2 "HR2:LED_GRNRA" H 5400 4150 50  0001 C CNN
F 3 "~" H 5400 4150 50  0001 C CNN
	1    5400 4150
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D10
U 1 1 5F30CF92
P 7200 4150
F 0 "D10" V 7300 4300 50  0000 R CNN
F 1 "LED;GRNRA" V 7100 4600 50  0000 R CNN
F 2 "HR2:LED_GRNRA" H 7200 4150 50  0001 C CNN
F 3 "~" H 7200 4150 50  0001 C CNN
	1    7200 4150
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D11
U 1 1 5F30EB24
P 8100 4150
F 0 "D11" V 8200 4300 50  0000 R CNN
F 1 "LED;GRNRA" V 8000 4600 50  0000 R CNN
F 2 "HR2:LED_GRNRA" H 8100 4150 50  0001 C CNN
F 3 "~" H 8100 4150 50  0001 C CNN
	1    8100 4150
	0    -1   -1   0   
$EndComp
$Comp
L HR2:BRIDGE_SW_OUTER;M1x8 CN108
U 1 1 5F387C15
P 2500 3000
F 0 "CN108" H 2850 2150 50  0000 C CNN
F 1 "BRIDGE_SW_OUTER;M1x8" H 2850 3150 50  0000 C CNN
F 2 "HR2:BRIDGE_SW_OUTER_M1x8" H 2700 3050 60  0001 L CNN
F 3 "" H 2700 2850 60  0001 L CNN
F 4 "SW Outer Bridge Connector" H 2700 2750 60  0001 L CNN "Field5"
	1    2500 3000
	1    0    0    1   
$EndComp
NoConn ~ 3300 2300
Wire Wire Line
	8100 4900 8100 4800
Text Label 3750 4900 0    50   ~ 0
GND
$Comp
L Transistor_FET:2N7000 Q11
U 1 1 5F39F103
P 8000 4600
F 0 "Q11" H 7850 4750 50  0000 L CNN
F 1 "2N7000;SOT23" H 7400 4550 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 8200 4525 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/2N/2N7000.pdf" H 8000 4600 50  0001 L CNN
	1    8000 4600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R34
U 1 1 5F3A3A4B
P 7850 3500
F 0 "R34" V 7750 3400 50  0000 L CNN
F 1 "330;1608" V 7950 3300 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7890 3490 50  0001 C CNN
F 3 "~" H 7850 3500 50  0001 C CNN
	1    7850 3500
	0    1    1    0   
$EndComp
Text Notes 2800 6450 0    50   ~ 0
Right Angle Green LED\nMfg Part #: TLPG5600\nDigi-Key part #: TLPG5600-ND\nForward Voltage Drop: 2.4V\nAbsolute max. current: 200mA\nTarget current: I=60mA\nR = (9V - 2.4V) / 75mA = 6.6V / .060A = 110Ohm\nW=I**2*R = (.060 * .060) * 110=.495W = .396W =.4W\nUse 3 330Ohm resistors in parallel to get 110Ohm\n1/8 Watt or larger should work.\n\n.\n
Wire Wire Line
	8100 4400 8100 4300
$Comp
L Device:R_US R33
U 1 1 5F3A820E
P 7850 3200
F 0 "R33" V 7750 3100 50  0000 L CNN
F 1 "330;1608" V 7950 3000 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7890 3190 50  0001 C CNN
F 3 "~" H 7850 3200 50  0001 C CNN
	1    7850 3200
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R35
U 1 1 5F3A878F
P 7850 3800
F 0 "R35" V 7750 3700 50  0000 L CNN
F 1 "330;1608" V 7950 3600 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7890 3790 50  0001 C CNN
F 3 "~" H 7850 3800 50  0001 C CNN
	1    7850 3800
	0    1    1    0   
$EndComp
Wire Wire Line
	8000 3800 8100 3800
Wire Wire Line
	8100 3800 8100 3500
Wire Wire Line
	8100 3200 8000 3200
Wire Wire Line
	8000 3500 8100 3500
Connection ~ 8100 3500
Wire Wire Line
	8100 3500 8100 3200
Wire Wire Line
	7700 3800 7600 3800
Wire Wire Line
	7600 3800 7600 3500
Wire Wire Line
	7600 3200 7700 3200
Wire Wire Line
	7700 3500 7600 3500
Connection ~ 7600 3500
Wire Wire Line
	7600 3500 7600 3200
Wire Wire Line
	8100 4000 8100 3800
Connection ~ 8100 3800
Wire Wire Line
	7200 4900 7200 4800
$Comp
L Transistor_FET:2N7000 Q10
U 1 1 5F3B5AC4
P 7100 4600
F 0 "Q10" H 6950 4750 50  0000 L CNN
F 1 "2N7000;SOT23" H 6500 4550 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 7300 4525 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/2N/2N7000.pdf" H 7100 4600 50  0001 L CNN
	1    7100 4600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R31
U 1 1 5F3B5ACE
P 6950 3500
F 0 "R31" V 6850 3400 50  0000 L CNN
F 1 "330;1608" V 7050 3300 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6990 3490 50  0001 C CNN
F 3 "~" H 6950 3500 50  0001 C CNN
	1    6950 3500
	0    1    1    0   
$EndComp
Wire Wire Line
	7200 4400 7200 4300
$Comp
L Device:R_US R30
U 1 1 5F3B5AD9
P 6950 3200
F 0 "R30" V 6850 3100 50  0000 L CNN
F 1 "330;1608" V 7050 3000 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6990 3190 50  0001 C CNN
F 3 "~" H 6950 3200 50  0001 C CNN
	1    6950 3200
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R32
U 1 1 5F3B5AE3
P 6950 3800
F 0 "R32" V 6850 3700 50  0000 L CNN
F 1 "330;1608" V 7050 3600 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6990 3790 50  0001 C CNN
F 3 "~" H 6950 3800 50  0001 C CNN
	1    6950 3800
	0    1    1    0   
$EndComp
Wire Wire Line
	7100 3800 7200 3800
Wire Wire Line
	7200 3800 7200 3500
Wire Wire Line
	7200 3200 7100 3200
Wire Wire Line
	7100 3500 7200 3500
Connection ~ 7200 3500
Wire Wire Line
	7200 3500 7200 3200
Wire Wire Line
	6800 3800 6700 3800
Wire Wire Line
	6700 3800 6700 3500
Wire Wire Line
	6700 3200 6800 3200
Wire Wire Line
	6800 3500 6700 3500
Connection ~ 6700 3500
Wire Wire Line
	6700 3500 6700 3200
Wire Wire Line
	7200 4000 7200 3800
Connection ~ 7200 3800
Wire Wire Line
	5900 3800 5800 3800
Wire Wire Line
	5800 3800 5800 3500
Wire Wire Line
	5800 3200 5900 3200
Wire Wire Line
	5900 3500 5800 3500
Connection ~ 5800 3500
Wire Wire Line
	5800 3500 5800 3200
Wire Wire Line
	5400 4900 5400 4800
$Comp
L Transistor_FET:2N7000 Q8
U 1 1 5F3B8D4A
P 5300 4600
F 0 "Q8" H 5150 4750 50  0000 L CNN
F 1 "2N7000;SOT23" H 4700 4550 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 5500 4525 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/2N/2N7000.pdf" H 5300 4600 50  0001 L CNN
	1    5300 4600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R25
U 1 1 5F3B8D54
P 5150 3500
F 0 "R25" V 5050 3400 50  0000 L CNN
F 1 "330;1608" V 5250 3300 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5190 3490 50  0001 C CNN
F 3 "~" H 5150 3500 50  0001 C CNN
	1    5150 3500
	0    1    1    0   
$EndComp
Wire Wire Line
	5400 4400 5400 4300
$Comp
L Device:R_US R24
U 1 1 5F3B8D5F
P 5150 3200
F 0 "R24" V 5050 3100 50  0000 L CNN
F 1 "330;1608" V 5250 3000 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5190 3190 50  0001 C CNN
F 3 "~" H 5150 3200 50  0001 C CNN
	1    5150 3200
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R26
U 1 1 5F3B8D69
P 5150 3800
F 0 "R26" V 5050 3700 50  0000 L CNN
F 1 "330;1608" V 5250 3600 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5190 3790 50  0001 C CNN
F 3 "~" H 5150 3800 50  0001 C CNN
	1    5150 3800
	0    1    1    0   
$EndComp
Wire Wire Line
	5300 3800 5400 3800
Wire Wire Line
	5400 3800 5400 3500
Wire Wire Line
	5400 3200 5300 3200
Wire Wire Line
	5300 3500 5400 3500
Connection ~ 5400 3500
Wire Wire Line
	5400 3500 5400 3200
Wire Wire Line
	5000 3800 4900 3800
Wire Wire Line
	4900 3800 4900 3500
Wire Wire Line
	4900 3200 5000 3200
Wire Wire Line
	5000 3500 4900 3500
Connection ~ 4900 3500
Wire Wire Line
	4900 3500 4900 3200
Wire Wire Line
	5400 4000 5400 3800
Connection ~ 5400 3800
Wire Wire Line
	4500 4900 4500 4800
$Comp
L Transistor_FET:2N7000 Q7
U 1 1 5F3BEA19
P 4400 4600
F 0 "Q7" H 4250 4750 50  0000 L CNN
F 1 "2N7000;SOT23" H 3800 4550 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 4600 4525 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/2N/2N7000.pdf" H 4400 4600 50  0001 L CNN
	1    4400 4600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R22
U 1 1 5F3BEA23
P 4250 3500
F 0 "R22" V 4150 3400 50  0000 L CNN
F 1 "330;1608" V 4350 3300 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4290 3490 50  0001 C CNN
F 3 "~" H 4250 3500 50  0001 C CNN
	1    4250 3500
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R21
U 1 1 5F3BEA2E
P 4250 3200
F 0 "R21" V 4150 3100 50  0000 L CNN
F 1 "330;1608" V 4350 3000 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4290 3190 50  0001 C CNN
F 3 "~" H 4250 3200 50  0001 C CNN
	1    4250 3200
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R23
U 1 1 5F3BEA38
P 4250 3800
F 0 "R23" V 4150 3700 50  0000 L CNN
F 1 "330;1608" V 4350 3600 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4290 3790 50  0001 C CNN
F 3 "~" H 4250 3800 50  0001 C CNN
	1    4250 3800
	0    1    1    0   
$EndComp
Wire Wire Line
	4400 3800 4500 3800
Wire Wire Line
	4500 3800 4500 3500
Wire Wire Line
	4500 3200 4400 3200
Wire Wire Line
	4400 3500 4500 3500
Connection ~ 4500 3500
Wire Wire Line
	4500 3500 4500 3200
Wire Wire Line
	4100 3800 4000 3800
Wire Wire Line
	4000 3800 4000 3500
Wire Wire Line
	4000 3200 4100 3200
Wire Wire Line
	4100 3500 4000 3500
Connection ~ 4000 3500
Wire Wire Line
	4000 3500 4000 3200
Connection ~ 4500 3800
Wire Wire Line
	3300 2800 3900 2800
Wire Wire Line
	3300 3000 3600 3000
Wire Wire Line
	8100 4900 7200 4900
Wire Wire Line
	7200 4900 6300 4900
Wire Wire Line
	5400 4900 4500 4900
Wire Wire Line
	4500 4400 4500 4300
Wire Wire Line
	4500 4000 4500 3800
$Comp
L Device:LED D7
U 1 1 5F30BFB1
P 4500 4150
F 0 "D7" V 4600 4250 50  0000 R CNN
F 1 "LED;GRNRA" V 4400 4600 50  0000 R CNN
F 2 "HR2:LED_GRNRA" H 4500 4150 50  0001 C CNN
F 3 "~" H 4500 4150 50  0001 C CNN
	1    4500 4150
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5400 4900 6300 4900
Connection ~ 6300 3800
Wire Wire Line
	6300 4000 6300 3800
Wire Wire Line
	6300 3500 6300 3200
Connection ~ 6300 3500
Wire Wire Line
	6200 3500 6300 3500
Wire Wire Line
	6300 3200 6200 3200
Wire Wire Line
	6300 3800 6300 3500
Wire Wire Line
	6200 3800 6300 3800
$Comp
L Device:R_US R29
U 1 1 5F3B8D25
P 6050 3800
F 0 "R29" V 5950 3700 50  0000 L CNN
F 1 "330;1608" V 6150 3600 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6090 3790 50  0001 C CNN
F 3 "~" H 6050 3800 50  0001 C CNN
	1    6050 3800
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R27
U 1 1 5F3B8D1B
P 6050 3200
F 0 "R27" V 5950 3100 50  0000 L CNN
F 1 "330;1608" V 6150 3000 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6090 3190 50  0001 C CNN
F 3 "~" H 6050 3200 50  0001 C CNN
	1    6050 3200
	0    1    1    0   
$EndComp
Wire Wire Line
	6300 4400 6300 4300
$Comp
L Device:R_US R28
U 1 1 5F3B8D10
P 6050 3500
F 0 "R28" V 5950 3400 50  0000 L CNN
F 1 "330;1608" V 6150 3300 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6090 3490 50  0001 C CNN
F 3 "~" H 6050 3500 50  0001 C CNN
	1    6050 3500
	0    1    1    0   
$EndComp
$Comp
L Transistor_FET:2N7000 Q9
U 1 1 5F3B8D06
P 6200 4600
F 0 "Q9" H 6050 4750 50  0000 L CNN
F 1 "2N7000;SOT23" H 5600 4550 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 6400 4525 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/2N/2N7000.pdf" H 6200 4600 50  0001 L CNN
	1    6200 4600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6300 4900 6300 4800
$Comp
L Device:LED D9
U 1 1 5F30CF88
P 6300 4150
F 0 "D9" V 6400 4250 50  0000 R CNN
F 1 "LED;GRNRA" V 6200 4600 50  0000 R CNN
F 2 "HR2:LED_GRNRA" H 6300 4150 50  0001 C CNN
F 3 "~" H 6300 4150 50  0001 C CNN
	1    6300 4150
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3900 4600 3900 2800
Wire Wire Line
	5100 4600 4800 4600
Wire Wire Line
	4800 4600 4800 2700
Wire Wire Line
	3300 2700 4800 2700
Wire Wire Line
	6000 4600 5700 4600
Wire Wire Line
	5700 4600 5700 2600
Wire Wire Line
	3300 2600 5700 2600
Wire Wire Line
	6900 4600 6600 4600
Wire Wire Line
	6600 4600 6600 2500
Wire Wire Line
	3300 2500 6600 2500
Wire Wire Line
	7800 4600 7500 4600
Wire Wire Line
	7500 4600 7500 2400
Wire Wire Line
	3300 2400 7500 2400
Wire Wire Line
	4500 4900 3600 4900
Wire Wire Line
	3600 4900 3600 3000
Connection ~ 4500 4900
Connection ~ 5400 4900
Connection ~ 6300 4900
Connection ~ 7200 4900
Wire Wire Line
	3300 2900 4000 2900
Wire Wire Line
	4000 2900 4000 3200
Connection ~ 4000 3200
Wire Wire Line
	4000 2900 4900 2900
Wire Wire Line
	4900 2900 4900 3200
Connection ~ 4000 2900
Connection ~ 4900 3200
Wire Wire Line
	4900 2900 5800 2900
Wire Wire Line
	5800 2900 5800 3200
Connection ~ 4900 2900
Connection ~ 5800 3200
Wire Wire Line
	5800 2900 6700 2900
Wire Wire Line
	6700 2900 6700 3200
Connection ~ 5800 2900
Connection ~ 6700 3200
Wire Wire Line
	6700 2900 7600 2900
Wire Wire Line
	7600 2900 7600 3200
Connection ~ 6700 2900
Connection ~ 7600 3200
Text Label 3950 4600 0    50   ~ 0
LED7
Text Label 4850 4600 0    50   ~ 0
LED8
Text Label 5750 4600 0    50   ~ 0
LED9
Text Label 6650 4600 0    50   ~ 0
LED10
Text Label 7550 4600 0    50   ~ 0
LED11
Text Label 3350 3000 0    50   ~ 0
GND
Text Label 3650 2900 0    50   ~ 0
9V
Text Notes 2800 6850 0    50   ~ 0
Note: GRNRA = Green Right Angle 0.254mm (approx.) lead spacing
Text Notes 2800 6600 0    50   ~ 0
Note: LED's are labeled from 1 to 16 in a clockwise\ndirection starting in the NW quadrant near the X axis.
Text Notes 2150 4250 0    50   ~ 0
Note: Mounting Hole for above\narm expansion plates.
Wire Wire Line
	4200 4600 3900 4600
$EndSCHEMATC
