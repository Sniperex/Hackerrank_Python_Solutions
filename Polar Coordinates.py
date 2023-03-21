# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
complex_number=complex(input())
r=math.sqrt((complex_number.real**2)+complex_number.imag**2)
if complex_number.real<0 and complex_number.imag>0:
    phi=math.atan(abs(complex_number.imag/complex_number.real))
    phi=math.pi-phi
elif complex_number.real>0 and complex_number.imag<0:
    phi=math.atan(abs(complex_number.imag/complex_number.real))
    phi=-phi
elif complex_number.real==0:
    phi=math.pi/2
elif complex_number.real<0 and complex_number.imag<0:
    phi=math.atan((complex_number.imag/complex_number.real))
    phi=-math.pi+phi
    
else:
    phi=math.atan(complex_number.imag/complex_number.real)
print(r,phi,sep='\n')