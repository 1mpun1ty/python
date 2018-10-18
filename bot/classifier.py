#filler data
x=1

#labels
shapeL=["cube","square","rectangle"]
dimensionL=["length","width","depth"]

#dimensions
length=[x,x,x]
width=[x,x,x]
depth=[x,x,x]

#features
shapeF=["cube","square","rectangle"]
dimensionF=[length,width,depth]

#object
labelO=[shapeL,dimensionL]
featureO=[shapeF,dimensionF]

#group
objectC=[labelO,featureO]
featurelessobjectC=[labelO]

#groups
classification=[objectC,featurelessobjectC]

#test code
print(" objects:")
print("labels:")
print(classification[0][0])
print("features:")
print(classification[0][1])
print(" featureless objects:")
print(classification[1])
