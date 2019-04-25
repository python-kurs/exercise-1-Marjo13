# Exercise 1
# Answers to questions that ask for non-code answers can simply be added as 
# comments.

# 1) The following line causes a SyntaxError. Please correct the line so that 
#it's output is 'Hallo Welt!' [1P]
print("Hallo Welt!")

# 2) Calculate the difference between a and b and assign the result to a 
# variable called 'v_1'. What are the datatypes of a, b and 'v_1'? [2P]
a = 976.543     #float
b = 345         #integer

v_1 = a-b       #float

# 3) Calculate the remainder of the division 100/17 by only using one operator 
# and save the result in v_2 (look into the Python docs for help) [1P]

v_2 = 100%17

# 4) The speed of light is about 300'000 km/s. Calculate the wavelength (in 
# nanometers) of a light wave with a frequency of 5.0E+14 per second. 
# Save the result in v_3.

# Can we see this light? [4P] 
# Yes, Orange-Yellowish (https://science.nasa.gov/ems/09_visiblelight)

speed = 300000
speedms = 300000*1000
frqs = 5.0E+14
lengthm = speedms/frqs

v_3 = int(lengthm*1E+9)

# 5) Print the following string to the console using the format-function and 
# the variables 'n' and 'pi': "Pi rounded to the first 10 decimals is: 
# 3.1415926536" [2P]
n  = 10
pi = 3.14159265358979323846264338

print("Pi rounded to the first {0:2d} decimals is: {1:2.10f}".format(n, pi))

# ------------------------------------
# - Don't change stuff below this line
# ------------------------------------

print(v_1)
print(v_2)
print(v_3)
