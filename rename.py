import glob, os, sys

os.chdir(os.path.dirname(__file__))
# inDirec = '/Users/elex/Documents/test/'
inDirec = '/Users/elex/Documents/temp/name/pic'

staticPrefix = 'boot_'
style = '0000'
extend = '.png'
extendLen = 4
limitLen = len(style)
prefix = ''
for root, dirs, fileList in os.walk(inDirec):
    pass
for file in fileList:
    if file.endswith(extend):
        index = file.rindex('_')
        value = file[index + 1:-extendLen]
        to_name_value = int(value) - 1
        valueLen = len(value)
        prefix = str(to_name_value)
        if valueLen < limitLen:
            loop = limitLen - valueLen
            for i in range(0, loop):
                prefix = '0' + prefix
        prefix = staticPrefix + prefix
        # else:
        #     prefix = staticPrefix
        os.rename(os.path.join(root, file), os.path.join(root, prefix + extend))
