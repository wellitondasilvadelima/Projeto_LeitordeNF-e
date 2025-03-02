import os

def path():
    # -------|  Variable declaration |-------
    path_input   =  './input'
    path_data    =  './data'
    path_output  =  './output'
    okay = False
    # -------| END Variable declaration |-------

    if not os.path.exists(path_input):
        os.makedirs(path_input)
        okay = True

    if not os.path.exists(path_data):
        os.makedirs(path_data)

    if not os.path.exists(path_output):
        os.makedirs(path_output)
        
    return path_input, path_data, okay