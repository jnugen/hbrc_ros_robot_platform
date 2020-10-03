EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 8
Title "HR2 Master Board"
Date "2020-10-03"
Rev ""
Comp "HomeBrew Robotics Club"
Comment1 "Copyright © 2020 by HomeBrew Robotics Club "
Comment2 "MIT License"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L HR2:HR2_EncoderMate;2XF1X3 CN55
U 1 1 5F4A855F
P 9000 1500
F 0 "CN55" H 9300 1650 50  0000 C CNN
F 1 "HR2_EncoderMate;2XF1X3" H 9450 850 50  0000 C CNN
F 2 "HR2:ENCODER_MATE" H 9200 1550 60  0001 L CNN
F 3 "HR2 Encoder Mating Connector" H 9200 1350 60  0001 L CNN
F 4 "HR2 Encoder Mating Connector" H 9200 1250 60  0001 L CNN "Field5"
	1    9000 1500
	-1   0    0    -1  
$EndComp
$Comp
L HR2:HR2_EncoderMate;2XF1X3 CN?
U 1 1 5F4A92D6
P 9000 3400
AR Path="/5F4A92D6" Ref="CN?"  Part="1" 
AR Path="/5F4A826A/5F4A92D6" Ref="CN56"  Part="1" 
F 0 "CN56" H 9300 3550 50  0000 C CNN
F 1 "HR2_EncoderMate;2XF1X3" H 9450 2750 50  0000 C CNN
F 2 "HR2:ENCODER_MATE" H 9200 3450 60  0001 L CNN
F 3 "HR2 Encoder Mating Connector" H 9200 3250 60  0001 L CNN
F 4 "HR2 Encoder Mating Connector" H 9200 3150 60  0001 L CNN "Field5"
	1    9000 3400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4500 4600 4500 4200
Text HLabel 5100 4400 2    50   Input ~ 0
LMOTOR_CTL2
Text HLabel 5100 3900 2    50   Input ~ 0
RMOTOR_CTL2
Text HLabel 5100 3800 2    50   Input ~ 0
RMOTOR_CTL1
Text HLabel 5100 4100 2    50   Input ~ 0
9V
Wire Wire Line
	4400 3800 5100 3800
Wire Wire Line
	4400 3900 5100 3900
Wire Wire Line
	4400 4000 6000 4000
Wire Wire Line
	4400 4100 5100 4100
Wire Wire Line
	4500 4200 4400 4200
Wire Wire Line
	4400 4400 5100 4400
Wire Wire Line
	4400 4600 4500 4600
Text HLabel 5100 4500 2    50   Input ~ 0
LMOTOR_CTL1
$Comp
L HR2:DRV8833PWPR;16HTSSOP U1
U 1 1 5F4C0C8C
P 3600 3000
F 0 "U1" H 3850 3150 50  0000 C CNN
F 1 "DRV8833PWPR;16HTSSOP" H 4000 1250 50  0000 C CNN
F 2 "Package_SO:HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask3x3mm_ThermalVias" H 3800 3050 60  0001 L CNN
F 3 "Dual H-Bridge Motor Drive" H 3800 2850 60  0001 L CNN
F 4 "DualH-Bridge Motor Drive" H 3800 2750 60  0001 L CNN "Field5"
	1    3600 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4400 4500 5100 4500
Wire Wire Line
	6000 4000 6000 4100
$Comp
L Device:C C3
U 1 1 5F4C3DE1
P 6000 4250
F 0 "C3" H 5900 4350 50  0000 L CNN
F 1 "10nF,16V,X7R;1608" H 6050 4150 50  0000 L CNN
F 2 "" H 6038 4100 50  0001 C CNN
F 3 "~" H 6000 4250 50  0001 C CNN
	1    6000 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5F4CB112
P 5800 4750
F 0 "C2" H 5700 4850 50  0000 L CNN
F 1 "2.2uF,6.3V;1608" H 5150 4650 50  0000 L CNN
F 2 "" H 5838 4600 50  0001 C CNN
F 3 "~" H 5800 4750 50  0001 C CNN
	1    5800 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5800 4600 5800 4300
Wire Wire Line
	5800 4300 4400 4300
Wire Wire Line
	4500 4600 4500 5000
Wire Wire Line
	4500 5000 5800 5000
Wire Wire Line
	5800 5000 5800 4900
Connection ~ 4500 4600
Wire Wire Line
	5800 5000 6000 5000
Wire Wire Line
	6000 5000 6000 4400
Connection ~ 5800 5000
$Comp
L Device:R_US R12
U 1 1 5F4D52D3
P 7250 4800
F 0 "R12" V 7150 4750 50  0000 C CNN
F 1 "1KΩ.1W;1608" V 7350 4800 50  0000 C CNN
F 2 "" V 7290 4790 50  0001 C CNN
F 3 "~" H 7250 4800 50  0001 C CNN
	1    7250 4800
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R11
U 1 1 5F4D52DD
P 7250 4500
F 0 "R11" V 7150 4450 50  0000 C CNN
F 1 "1KΩ.1W;1608" V 7350 4500 50  0000 C CNN
F 2 "" V 7290 4490 50  0001 C CNN
F 3 "~" H 7250 4500 50  0001 C CNN
	1    7250 4500
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R10
U 1 1 5F4D52E7
P 7250 4200
F 0 "R10" V 7150 4150 50  0000 C CNN
F 1 "1KΩ.1W;1608" V 7350 4200 50  0000 C CNN
F 2 "" V 7290 4190 50  0001 C CNN
F 3 "~" H 7250 4200 50  0001 C CNN
	1    7250 4200
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R9
U 1 1 5F4D52F1
P 7250 3900
F 0 "R9" V 7150 3850 50  0000 C CNN
F 1 "1KΩ.1W;1608" V 7350 3900 50  0000 C CNN
F 2 "" V 7290 3890 50  0001 C CNN
F 3 "~" H 7250 3900 50  0001 C CNN
	1    7250 3900
	0    1    1    0   
$EndComp
Wire Wire Line
	7400 4800 7600 4800
Wire Wire Line
	7600 4800 7600 4500
Wire Wire Line
	7600 3900 7400 3900
Wire Wire Line
	7400 4200 7600 4200
Connection ~ 7600 4200
Wire Wire Line
	7600 4200 7600 3900
Wire Wire Line
	7400 4500 7600 4500
Connection ~ 7600 4500
Wire Wire Line
	7600 4500 7600 4200
Wire Wire Line
	7100 4500 6900 4500
Wire Wire Line
	6900 4500 6900 4800
Wire Wire Line
	6900 4800 7100 4800
Wire Wire Line
	7100 4200 6900 4200
Wire Wire Line
	6900 4200 6900 4500
Connection ~ 6900 4500
Wire Wire Line
	7100 3900 6900 3900
Wire Wire Line
	6900 3900 6900 4200
Connection ~ 6900 4200
Wire Wire Line
	8100 3500 7200 3500
Wire Wire Line
	7200 3500 7200 3600
Wire Wire Line
	7200 3600 4400 3600
Wire Wire Line
	5800 1500 8100 1500
Text Label 4450 3100 0    50   ~ 0
LMOTOR_OUT
Text Label 4450 3300 0    50   ~ 0
LMOTOR_OUT
Text Label 4450 3800 0    50   ~ 0
RMOTOR_CTL1
Text Label 4450 3900 0    50   ~ 0
RMOTOR_CTL2
Text Label 4550 4500 0    50   ~ 0
LMOTOR_CTL1
Text Label 4550 4400 0    50   ~ 0
LMOTOR_CTL2
Wire Wire Line
	8100 1600 5900 1600
Wire Wire Line
	5800 1500 5800 3100
Wire Wire Line
	4400 3300 5900 3300
Wire Wire Line
	5900 1600 5900 3300
Wire Wire Line
	4400 3000 5100 3000
Text HLabel 5100 3000 2    50   Input ~ 0
MOTOR_SLEEP
Text Label 4450 3000 0    50   ~ 0
MOTOR_SLEEP
Text HLabel 5100 3700 2    50   Output ~ 0
MOTOR_FAULT
Wire Wire Line
	4400 3700 5100 3700
Text Label 4450 3700 0    50   ~ 0
MOTOR_FAULT
Wire Wire Line
	4400 3100 5800 3100
Wire Wire Line
	4400 3200 6900 3200
Connection ~ 6900 3200
Connection ~ 6900 2600
Wire Wire Line
	6900 2300 6900 2600
Wire Wire Line
	7100 2300 6900 2300
Connection ~ 6900 2900
Wire Wire Line
	6900 2600 6900 2900
Wire Wire Line
	7100 2600 6900 2600
Wire Wire Line
	6900 3200 7100 3200
Wire Wire Line
	6900 2900 6900 3200
Wire Wire Line
	7100 2900 6900 2900
Wire Wire Line
	7600 2900 7600 2600
Connection ~ 7600 2900
Wire Wire Line
	7400 2900 7600 2900
Wire Wire Line
	7600 2600 7600 2300
Connection ~ 7600 2600
Wire Wire Line
	7400 2600 7600 2600
Wire Wire Line
	7600 2300 7400 2300
Wire Wire Line
	7600 3200 7600 2900
Wire Wire Line
	7400 3200 7600 3200
$Comp
L Device:R_US R5
U 1 1 5F4CD3C4
P 7250 2300
F 0 "R5" V 7150 2250 50  0000 C CNN
F 1 "1KΩ.1W;1608" V 7350 2300 50  0000 C CNN
F 2 "" V 7290 2290 50  0001 C CNN
F 3 "~" H 7250 2300 50  0001 C CNN
	1    7250 2300
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R6
U 1 1 5F4CCE9C
P 7250 2600
F 0 "R6" V 7150 2550 50  0000 C CNN
F 1 "1KΩ.1W;1608" V 7350 2600 50  0000 C CNN
F 2 "" V 7290 2590 50  0001 C CNN
F 3 "~" H 7250 2600 50  0001 C CNN
	1    7250 2600
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R7
U 1 1 5F4CC9D3
P 7250 2900
F 0 "R7" V 7150 2850 50  0000 C CNN
F 1 "1KΩ.1W;1608" V 7350 2900 50  0000 C CNN
F 2 "" V 7290 2890 50  0001 C CNN
F 3 "~" H 7250 2900 50  0001 C CNN
	1    7250 2900
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R8
U 1 1 5F4CC3F2
P 7250 3200
F 0 "R8" V 7150 3150 50  0000 C CNN
F 1 "1KΩ.1W;1608" V 7350 3200 50  0000 C CNN
F 2 "" V 7290 3190 50  0001 C CNN
F 3 "~" H 7250 3200 50  0001 C CNN
	1    7250 3200
	0    1    1    0   
$EndComp
Wire Wire Line
	4400 3400 8100 3400
Text HLabel 8700 2800 2    50   Input ~ 0
3.3V
Text HLabel 8500 2550 2    50   Output ~ 0
LQUAD_B
Text HLabel 8500 2450 2    50   Output ~ 0
LQUAD_A
Text HLabel 8500 4400 2    50   Output ~ 0
RQUAD_A
Text HLabel 8500 4500 2    50   Output ~ 0
RQUAD_B
Wire Wire Line
	6000 5000 7600 5000
Wire Wire Line
	7600 3700 8100 3700
Connection ~ 6000 5000
Wire Wire Line
	6900 3900 6900 3500
Wire Wire Line
	6900 3500 4400 3500
Connection ~ 6900 3900
Wire Wire Line
	7600 5000 7600 4800
Connection ~ 7600 4800
Wire Wire Line
	7600 3700 7600 3900
Connection ~ 7600 3900
Wire Wire Line
	7600 3200 7600 3700
Connection ~ 7600 3200
Connection ~ 7600 3700
Wire Wire Line
	8100 1800 7600 1800
Wire Wire Line
	7600 1800 7600 2300
Connection ~ 7600 2300
Text HLabel 8500 5000 2    50   Input ~ 0
GND
Wire Wire Line
	7600 5000 8500 5000
Connection ~ 7600 5000
Wire Wire Line
	8100 3600 7700 3600
Wire Wire Line
	7700 3600 7700 2800
Wire Wire Line
	7700 1700 8100 1700
Wire Wire Line
	8700 2800 7700 2800
Connection ~ 7700 2800
Wire Wire Line
	7700 2800 7700 1700
Wire Wire Line
	8100 1900 7900 1900
Wire Wire Line
	7900 1900 7900 2550
Wire Wire Line
	7900 2550 8500 2550
Wire Wire Line
	8100 2000 8000 2000
Wire Wire Line
	8000 2000 8000 2450
Wire Wire Line
	8000 2450 8500 2450
Wire Wire Line
	8100 3800 7900 3800
Wire Wire Line
	8500 4400 7900 4400
Wire Wire Line
	7900 3800 7900 4400
Wire Wire Line
	8500 4500 8000 4500
Wire Wire Line
	8000 4500 8000 3900
Wire Wire Line
	8000 3900 8100 3900
Text Label 8400 2800 0    50   ~ 0
3.3V
Text Label 8050 4400 0    50   ~ 0
RQUAD_A
Text Label 8050 4500 0    50   ~ 0
RQUAD_B
Text Label 8050 2450 0    50   ~ 0
LQUAD_A
Text Label 8050 2550 0    50   ~ 0
LQUAD_B
Text Label 4900 4100 0    50   ~ 0
9V
Text Label 8050 5000 0    50   ~ 0
GND
$Comp
L HR2:LIDAR_ADAPTER;2xF1x2 CN3
U 1 1 5F613DD3
P 6300 5400
F 0 "CN3" H 6550 5550 50  0000 C CNN
F 1 "LIDAR_ADAPTER;2xF1x2" H 6800 4500 50  0000 C CNN
F 2 "HR2:LIDAR_ADAPTER_2xF1x2" H 6500 5450 60  0001 L CNN
F 3 "Lidar Adapter Connectors" H 6500 5250 60  0001 L CNN
F 4 "Lidar Adapter Connectors" H 6500 5350 60  0001 L CNN "manf#"
	1    6300 5400
	1    0    0    -1  
$EndComp
Text HLabel 8500 5400 2    50   Input ~ 0
5v
Wire Wire Line
	7300 5700 7600 5700
Wire Wire Line
	7600 5700 7600 5000
Wire Wire Line
	7300 5400 8500 5400
Text HLabel 8500 5500 2    50   Output ~ 0
LDR_TX
Text HLabel 8500 5600 2    50   Input ~ 0
LDR_RX
Text HLabel 8500 5800 2    50   Input ~ 0
LDR_SPIN
Text HLabel 8500 5900 2    50   Input ~ 0
LDR_EN
Text HLabel 8500 6000 2    50   Input ~ 0
LDR_PWM
Wire Wire Line
	7300 6000 8500 6000
Wire Wire Line
	7300 5900 8500 5900
Wire Wire Line
	7300 5800 8500 5800
Wire Wire Line
	7300 5600 8500 5600
Wire Wire Line
	7300 5500 8500 5500
$EndSCHEMATC
