import zipfile


zip_file = zipfile.ZipFile("a.zip", "r")
zip_file.extractall("b")
zip_file.close()