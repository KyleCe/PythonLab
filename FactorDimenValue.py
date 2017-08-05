import os

# <dimen name="dp235">200.0dp</dimen>
# replace 200.0 with 150.0

cwd = os.getcwd()

dataDir = cwd + '/to_process'
outDir = cwd + '/output'
fileName = 'dimens.xml'
extend = '.xml'
lineRange = ['\n', '\r\n']
head = '\">'
tail = 'dp</dimen>'
tailSp = 'sp</dimen>'
pxStr = 'px'
scaleFactor = 0.75
processSP = False

out = outDir + '/' + fileName

if os.path.isfile(out):
    os.remove(out)


def parse_with_factor(line, factor):
    old = line
    if tail in line:
        last_index = line.index(tail)
    # elif tailSp in line:
    #     if processSP:
    #         last_index = line.index(tailSp)
    else:
        return line
    first_index = line.index(head)
    old_val = line[first_index + head.__len__(): last_index]
    val = float(old_val) * factor
    val = "{0:.2f}".format(val)
    old_str = line[first_index + head.__len__(): last_index + 2]
    return old.replace(old_str, str(val) + pxStr)


for root, dirs, fileList in os.walk(dataDir):
    pass
    with open(out, 'w+') as outfile:
        for f in fileList:
            if f.endswith(extend):
                with open(dataDir + '/' + f) as infile:
                    for line in infile:
                        line = parse_with_factor(line, scaleFactor)
                        outfile.write(line)
