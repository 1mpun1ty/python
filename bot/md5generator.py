#
#BROKEN!!!
#
import os
seed=0
while seed==0:
    inputvar=int(input("seed text to be hashed: "))
    command=os.popen('echo "'+inputvar+'" | md5sum').readlines('echo "'+inputvar+'" | md5sum')
    seed=1
while seed==1:
    print(command)
    print("done!")
    break
