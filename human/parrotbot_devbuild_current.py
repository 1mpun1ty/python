height_i = int(input(i+'height in inches: ')) #add invalid input check
weight_lbs = int(input(i+'weight in pounds: ')) #add invalid input check
height_m=height_i/39.3701
weight_kg=weight_lbs*2.205
bmi=weight_kg/(height_m*height_m)
print(o+str(name)+"'s bmi is "+str(bmi))
print(o+str(name)+' is '+str(age)+' years old.')
print(o+str(name)+"'s temperature is "+str(temperature)+' degrees F.')
if breathing=='no':
        print(o+str(name)+' is not breathing!')
        print(o+'###END OF PROGRAM###')
        time.sleep(1)
        print(o+"Restarting...")
        time.sleep(60)
        os.system('python3.7 parrotbot_devbuild.py')
else:
    print("python interpreter: bot offline...")
