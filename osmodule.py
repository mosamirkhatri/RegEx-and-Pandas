import os
from datetime import datetime
# print(dir(os))

# print(os.getcwd()) #Current Working directory

os.chdir('C:/Users/') #Change directory

# print(os.getcwd()) #Current Working directory


# os.mkdir('OS-Demo') make only one directory
# os.makedirs('OS-demo/sub-dir') #makes subdirectories too

# os.rmdir('OS-demo')

# os.removedirs('OS-demo/sub-dir')

# print(os.listdir()) #list contents of Current Working directory

# os.rename('test.txt', 'Demo.txt') #rename file names

# mod_time = os.stat('Demo.txt').st_mtime #Info about the file

# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk('D:/Media'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files: ', filenames)
#     print()

# print(os.environ.get('EMAIL_USER'))
# print(os.environ.get('USERPROFILE'))



# print(os.path.join(os.environ.get('USERPROFILE'), 'PandasAndRegex', 'Dem.txt'))

##############
# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
###########These method works on any path given even if its fake

# print(os.path.exists('/tmp/Demo.txt')) Path real or not
# print(os.path.isdir('C:/Users/samirkhatri/PandasAndRegEx/Demo.txt'))
# print(os.path.isfile('/tmp/Demo.txt'))


# print(os.path.splitext('C:/Users/samirkhatri/PandasAndRegEx/Demo.txt')) split extension

os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

print(os.environ.get('API_USER'))
