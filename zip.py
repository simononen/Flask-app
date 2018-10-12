import zipfile

f = open('new_file.txt', 'w+')
f.write('Here is some text')
f.close()

comp_file = zipfile.ZipFile('my_compresed_info.zip', 'w')

comp_file.write('new_file.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


zib_obj = zipfile.ZipFile('my_compresed_info.zip', 'r')