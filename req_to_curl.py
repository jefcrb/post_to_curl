f = open('input.txt', 'r')
METHODS = ["get", "post", "delete", "put"]
#RESERVED = ["cookie:", "user-agent:", "referer:"]
yes = ['y', 'yes']
i = 0
headersList = []
hostList = []
dataList = []

for line in f:
    temp = []
    tempFull = line.replace('"', '\\"')
    tempFull = tempFull.rstrip('\n')
    i += 1
    temp = line.split()

    if i == 1: #get method
        if temp[0].lower() in METHODS:
            method = temp[0].upper()
            hostList.append(temp[1])

    if i > 1 and ':' in line: #get headers
        headersList.append('-H "{}"'.format(tempFull))
        if temp[0].lower() == "host:":
            hostList.append(temp[1])

    #get data
    if len(temp) != 0 and ':' not in line and '=' in line:
        temp = line.split('&')
        for var in temp:
            dataList.append('-d \"{}\"'.format(var))


print("Data:")
for index in range(len(dataList)):
    splitData = dataList[index].split('=')
    print("{}. {}: {}".format(index+1, splitData[0], splitData[1]).replace("-d ", "").replace('"', ''))
userInput = input("Would you like to change any of these values? (y/N): ")
print(userInput)

if userInput.lower() in yes:
    userInput = input("Enter the number next to the value that you want to change: ")
    indexToChange = int(userInput)-1
    splitData = dataList[indexToChange].split('=')
    userInput = input("What would you like this value to be?: ")

    splitData[1] = userInput
    newData = '='.join(splitData)
    dataList[indexToChange] = "{}\"".format(newData)

host = "{}{}".format(hostList[1], hostList[0])   

command = "curl -i -X {} {} {} {}".format(method, ' '.join(headersList), ' '.join(dataList), host)

print(command.rstrip('\n'))