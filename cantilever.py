import odbAccess

###-USER INPUT-###

fileName = 'bottomMassKinematic'

iFrame = 19

###-USER INPUT END-###

odbPath = 'C:/Users/sunnyi/Documents/Abaqus/August/TTO - Cicada/3107/' + fileName + '.odb'

odb = session.openOdb(odbPath)


frame = odb.steps['frequency'].frames[iFrame]

energyData = frame.fieldOutputs['ELSE']

x = 0

for i in energyData.values:
	x += i.data


print odbPath
print("%3.2e" % (x))
