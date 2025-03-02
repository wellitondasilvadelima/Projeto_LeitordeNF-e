import shutil
import os

# Verifica se a pasta de destino existe, senão, cria
def move_allfiles(origin,destination,file):

    # Move o arquivo da pasta origem para a pasta destino
        path_origin = os.path.join(origin, file)
        path_destination = os.path.join(destination, file)

        if os.path.isfile(path_origin):  # Verifica se é um arquivo
            shutil.move(path_origin, path_destination)

