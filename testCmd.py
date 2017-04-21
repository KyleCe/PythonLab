extendLen = 4
str = "1_1_djaf__fjdg_123.png"
index = str.rindex('_')
value = str[index + 1:-extendLen]
int_value = int(value)

str += value

print str
print len(value)
