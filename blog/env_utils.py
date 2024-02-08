def user_data(path):
    f = open(path, 'r')
    id = f.readline().strip()
    password = f.readline().strip()
    f.close()
    return id, password