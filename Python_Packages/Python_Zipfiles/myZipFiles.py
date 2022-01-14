import zipfile


#___________________________________________________________

# my_zip = zipfile.ZipFile('files.zip', 'w')

# my_zip.write('test.txt')
# my_zip.write('thumbnail.jpg')

# my_zip.close()


#___________________________________________________________
# More efficient way

# with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write('test.txt')
#     my_zip.write('thumbnail.jpg')


#___________________________________________________________

# with zipfile.ZipFile('files.zip', 'r') as my_zip:
#     print(my_zip.namelist())      # prints name of the files within the archive
#     my_zip.extractall('files')    # extracts all files in archive 
#     # my_zip.extract('thumbnail.jpg') # extracts specific file


#___________________________________________________________

# # Different compression types: tar, gztar, bztar, xztar

# import shutil

# path = '/Users/User/Desktop/Python/Python_Zipfiles/files'

# # shutil.make_archive('test2', 'zip', path)
# # shutil.unpack_archive('test2.zip', 'untest2')

# shutil.make_archive('test2', 'bztar', path)
# shutil.unpack_archive('test2.tar.bz2', 'untest2')       # .tar.bz2 extention

#___________________________________________________________

# https://insights.stackoverflow.com/survey


import requests 
import zipfile

r = requests.get('https://drive.google.com/uc?export=download&id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV')

# # Extracting data from link
# with open('data.zip', 'wb') as f: 
#     f.write(r.content)    

# # Print out files that were downloaded
with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())