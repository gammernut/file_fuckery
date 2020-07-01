
import utill

import os

utill.print_header(code_name='File Fuckery')

# print(os.environ.get('USERPROFILE'))

os.chdir('C:\\Users\\gamme')

print(os.getcwd())  # gets the current working directory / folder


# for dirpath, dirnames, filenames in os.walk('C:\\Users\\gamme'):
#     print('current path: ', dirpath)
#     print('Dir: ', dirnames)
#     print('files', filenames)
#     print()


#print(os.path.isdir('C:\\Users\\gamme\\file_fuckery'))   # prints false since there is no fsdf folder
# print(os.path.isfile('D:\\fsdf'))   # prints false since there is no fsdf file
# print(os.path.splitext('D:\\tmp\\test.txt'))   # splits the file type off ie.
#  ('D:\\tmp\\test', '.txt')

file_fuck_path = os.path.isdir('C:\\Users\\gamme\\file_fuckery')

while file_fuck_path is False:
    os.mkdir('file_fuckery')
    os.chdir('C:\\Users\\gamme\\file_fuckery')
    os.makedirs('demo_1')
    break

print(os.getcwd())

file_fuck_path = os.path.isdir('C:\\Users\\gamme\\file_fuckery')

print(os.getcwd())

while file_fuck_path is True:
    os.chdir('C:\\Users\\gamme\\file_fuckery\\demo_1')

print(os.getcwd())


#     # os.chdir('C:\\Users\\gamme\\file_fuckery')
#     # os.makedirs('demo_1')
#     os.chdir('C:\\Users\\gamme\\file_fuckery\\demo_1')
#
# print(os.getcwd())

