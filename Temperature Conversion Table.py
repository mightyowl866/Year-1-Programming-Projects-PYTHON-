def c_to_f(temp_c):
    temp_f = (temp_c *1.8) +32
    return temp_f
#Function for Celcius to Fahrenheit conversion

for c in range(0,101,10):
    print(c, '\t', c_to_f (c))
    #Results
    