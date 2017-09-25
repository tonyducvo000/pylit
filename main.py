#Given a line of text, find all the occurrence of alliteration
import sys
from pathlib import Path


#my_file = Path(sys.argv[1])
my_file = Path("/home/work/test/pycharm/in")
if not my_file.is_file():
    print ("File does not exist!")
    sys.exit()


con = str(my_file)

line_number = 0

with open(con, "r") as myfile:
    for line in myfile:
        string = line.lower().split()
        string2 = string

        index = 0
        line_number += 1
        result = []


        while True:

            if (len(string2) - index == 1 or len(string2) - index == 0):
                break

            if string2[index][0] == string2[index + 1][0]:
                result.append(string[index])
                result.append(string[index+1])
                index += 2
                while True:
                    if string2[index][0] == string2[index - 1][0]:
                        result.append(string[index])
                        index += 1
                    else:
                        break
            else:
                index += 1


        resultString = " ".join(result)
        for ch in [',', '.']:
            if ch in resultString:
                resultString = resultString.replace(ch, "")

        print("Alliterations for line #" + str(line_number) + ": " + resultString)


exit(0)
