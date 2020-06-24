age = int(input('enter your age'))
if age>0 and age<10:
   print ("1 - first decade")
elif age>10 and age<20:
   print ("2- second decade")
elif age>20 and age<30:
   print ("3 - third decade")
elif age>30 and age<40:
   print ("4 - fourth decade")
elif age>40 and age<50:
   print ("5 - fifth decade")
elif age>50 and age<60:
   print ("6 - sixth decade")
elif age>60 and age<70:
   print ("7 - seventh decade")
elif age>70 and age<80:
   print ("8 - eighth decade")
elif age>80 and age<90:
   print ("9 - ninth decade")
elif age>90 and age<100:
   print ("10 - tenth decade")
else:
   print ("not applicable plz enter valid age")

def fun():
    if age>10 and age<30:
        print('we are teenagers')
    elif age>30 and age<50:
        print('we are young')
    elif age>50 and age<80:
        print('we are old')
    elif age>80:
        print('i am too old')


fun()

        
