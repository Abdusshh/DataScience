import sys
 
# total arguments
n = len(sys.argv)
# print("Total arguments passed:", n)

input_file = None

if n > 2:
    print('Too many command-line arguments')
    sys.exit()
elif n < 2:
    print('Too few command-line arguments')
    sys.exit()
else:
    input_file = sys.argv[1]

# print(input_file)
if not input_file.endswith('.py'):
    print('Not a python file')
    sys.exit()

# open file
try:
    with open(input_file) as f:
        content = f.readlines()


    # print(content)

    important_lines = []

    for line in content:
        if not line.startswith('#') and not line == '\n':
            important_lines.append(line)

    print(len(important_lines))

except FileNotFoundError:
    print('File not found')    
    sys.exit()
