print "All results are approximate!\n"

def f_convert():
	fahrenheit = raw_input("Insert a temperature in Fahrenheit: ")
	f_to_c = (float(fahrenheit) - 32) * 5/9
	f_to_k = (float(fahrenheit) + 459.67) * 5/9
	print "%s degrees Fahrenheit. This is also\n %s degrees Celsius\n and %s degrees Kelvin.\n" % (fahrenheit, f_to_c, f_to_k)

def c_convert():
	celsius = raw_input("Insert a temperature in Celsius: ")
	c_to_f = float(celsius) * 9/5 + 32
	c_to_k = float(celsius) + 273.15
	print "%s degrees Celsius. This is also\n %s degrees Fahrenheit\n and %s degrees Kelvin.\n" % (celsius, c_to_f, c_to_k)

def cent_convert():
	centimeters = raw_input("Insert an amount of Centimeters: ")
	cm_to_in = float(centimeters) * 0.3937
	cm_to_ft = float(centimeters) * 0.03281
	cm_to_mi = float(centimeters) * 0.000006214
	cm_to_yd = float(centimeters) * 0.01094
	cm_to_mm = float(centimeters) * 10
	cm_to_m = float(centimeters) * 0.01
	cm_to_km = float(centimeters) * 0.00001
	print "%s centimeters. This is also\n %s inches,\n %s feet,\n %s miles,\n %s yards,\n %s millimeters,\n %s meters,\n and %s kilometers.\n" % (centimeters, cm_to_in, cm_to_ft, cm_to_mi, cm_to_yd, cm_to_mm, cm_to_m, cm_to_km)


def inch_convert():
	inches = raw_input("Insert an amount of Inches: ")
	in_to_ft = float(inches) * 0.08333
	in_to_mi = float(inches) * 0.00001578
	in_to_yd = float(inches) * 0.02778
	in_to_mm = float(inches) * 25.4
	in_to_cm = float(inches) * 2.54
	in_to_m = float(inches) * 0.0254
	in_to_km = float(inches) * 0.0000254
	print "%s inches. This is also\n %s feet,\n %s miles,\n %s yards,\n %s millimeters,\n %s centimeters,\n %s meters,\n and %s kilometers.\n" % (inches, in_to_ft, in_to_mi, in_to_yd, in_to_mm, in_to_cm, in_to_m, in_to_km)

selection = raw_input("Please select whether you want to convert fahrenheit (1), celsius (2), centimeters (3), or inches (4): ")

if selection == '1': 
      f_convert() 
elif selection == '2': 
      c_convert()
elif selection == '3':
      cent_convert() 
elif selection == '4': 
      inch_convert()
else: 
      print "Unknown Option Selected!"
