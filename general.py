import os
def create_dir(directory):
  if not os.path_exists(directory):
    os.makedir(directory)
def write_file(path, data):
  f = open(path, 'w')
  f.write(data)
  f.close()
