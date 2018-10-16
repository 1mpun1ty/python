#name = 'Parker'
#age = 18
#pulse=0
#breathing='no'
#temperature=98
#height = 69
#weight = 120
print("###PARROT_BOT_R1###")
print("Hello there! I'm parrot! Tell me about yourself? (agree or disagree):")
if input()=='agree':
    name = str(input('Enter your name: '))
    age = int(input('age in years: '))
    pulse= int(input('pulse in beats per minute: '))
    breathing= str(input('breathing (yes or no): '))
    temperature= int(input('temperature in degrees F: '))
    height = int(input('height in inches: '))
    weight = int(input('weight in pounds: '))
    if age > 0: #check if the person has been alive for at least some time
        alive='yes'
    else:
        if age<=0: #check if the person is not alive yet
            alive='no'
    if pulse>0 or breathing=='yes': #check if person is alive (has pulse or is breathing)
                alive='yes'
    if temperature<95 or temperature>109: #check if temperature is outside the stable range
                alive='no'
    if alive=='no': #check if person is not alive. If person is not alive, pronounce them dead and get help!
        print('WARNING: No time to evaluate '+str(name)+'! Get Help!')
    if breathing=='no':
        print(str(name)+' is not breathing!')
    if alive=='yes': #check if person is alive. If person is alive, say so, then evaluate the person.
        print(str(name)+' is alive! His pulse is '+str(pulse)+' bpm (beats per minute)') #declare the person alive and state their pulse.
        print(str(name)+"'s height is "+str(height)+' inches. His weight is '+str(weight)+' pounds.')
        print(str(name)+' is '+str(age)+' years old.')
        print(str(name)+"'s temperature is "+str(temperature)+' degrees F.')
        if breathing=='no':
            print(str(name)+' is not breathing!')
