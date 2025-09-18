import os,pathlib;

cwd= pathlib.Path()
PiU = cwd.parent.absolute().as_posix()

mps = []

directory = PiU+"/history/states"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        currentfile = open(f,"r")
        while True:
            line = currentfile.readline()
            if line == "":
                break
            elif "manpower" in line:
                #print(line)
                toAppend = line.split("=")[1]
                if "state_category" in toAppend:
                    toAppend = toAppend.split("state_category")[0]
                mps.append(int(toAppend.strip()))
        currentfile.close()

mps.sort()
mps = list(filter(lambda pop: pop>1,mps))

divider = len(mps)/11

for i in range(11):
    if i != 0:
        print(mps[round(divider*i)-1])
