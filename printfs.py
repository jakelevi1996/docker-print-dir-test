import os

print('cwd: ', os.getcwd())

files = os.listdir('.')
print('Files: ', ', '.join(files))