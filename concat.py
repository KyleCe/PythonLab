import os

dataDir = '/Users/elex/Documents/temp/to_process'
outDir = '/Users/elex/IdeaProjects/Test/output'
fileName = 'concat_result.txt'
extend = '.txt'
nameRange = range(806, 850)
lineRange = ['\n', '\r\n']

out = outDir + '/' + fileName

if os.path.isfile(out):
    os.remove(out)


def get_integer_in_name(int_file):
    return int(os.path.splitext(int_file)[0][1:])


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


for root, dirs, fileList in os.walk(dataDir):
    pass
    with open(out, 'w+') as outfile:
        for f in fileList:
            if f.endswith(extend):
                if get_integer_in_name(f) in nameRange:
                    with open(dataDir + '/' + f) as infile:
                        line = infile.read()
                        if has_numbers(line):
                            outfile.write(line)
