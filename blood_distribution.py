bloodTypes = input().split()
numPatients = input().split()
bloodReceived = 0

def bloodLeft(a,b):
    bloodTypes[a] = int(bloodTypes[a]) - min(int(bloodTypes[a]), int(numPatients[b]))
    numPatients[b] = int(numPatients[b]) - min(int(bloodTypes[a]), int(numPatients[b]))
    return min(bloodTypes[a], numPatients[b])

bloodReceived = bloodLeft(0,0) + bloodLeft(0,1) + bloodLeft(1,1)

bloodReceived += bloodLeft(0,2) + bloodLeft(2,2) + bloodLeft(0,4) + bloodLeft(4,4)

bloodReceived += bloodLeft(0,3) + bloodLeft(1,3) + bloodLeft(2,3) + bloodLeft(3,3) + bloodLeft(0,5) + bloodLeft(1,5) + bloodLeft(4,5) + bloodLeft(5,5)

bloodReceived += bloodLeft(0,6) + bloodLeft(2,6) + bloodLeft(4,6) + bloodLeft(6,6)

bloodReceived += bloodLeft(0,7) + bloodLeft(1,7) + bloodLeft(2,7) + bloodLeft(3,7) + bloodLeft(4,7) + bloodLeft(5,7) + bloodLeft(6,7) + bloodLeft(7,7)

print(bloodReceived)










