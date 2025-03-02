import os
import pandas as pd
from info_nfs import get_info_nfs
from move_files import move_allfiles

# Function that obtains files from the input folder and performs the reading to obtain the data and saves it in an XLSX file.

def nfe_reader(path_input,path_data, label):
    # -------|    Variable declaration   |-------
    msg_alert  = ""
    msg_output = ""
    msg_error  = ""
    msg_return = ""
    move_okay  = False
    # -------| END Variable declaration |-------

    label.config(text="START PROCESS!")
    list_nfs = os.listdir(path_input) # Get the files contained in the directory

    if (list_nfs != []):

        cols = ["Document number","Issuing company","CNPJ","Customer name","Adress","Product name","Quantity","Gross weight","Total","Total tributável"]
        rows = []

        for nfs_name in list_nfs:
            if(".xml" == os.path.splitext(nfs_name)[1]): # Checks if files have the correct extension

                move_okay, e = get_info_nfs(nfs_name,rows) 

                if (move_okay == True):
                    move_allfiles(path_input,path_data, nfs_name)
                else:
                    msg_error += "\n" + e
            else:
                msg_alert += ", " + nfs_name

        # Checks to create a message informing the user
        if(rows != []):
            table = pd.DataFrame(columns=cols,data=rows)
            table.to_excel("./output/NotasFiscais.xlsx",index=False)
            msg_output = (" - XML generated in OUTPUT folder")
        else:
            msg_output = (" - Output file CANNOT be generated")

        if (msg_alert == ""):
            msg_return = "PROCESS COMPLETED!\n - Completed files from input folder moved to data folder.\n"+msg_output+"."+"\n\n"+msg_error
        else:
            msg_return = "PROCESS COMPLETED!\n- Files from input folder moved to data folder\n"+msg_output+" - ALERT!!!! "+msg_alert+" is not an xml extension file.\n\n"+msg_error
    else:
        msg_return = "The input folder is empty!"
    
    return msg_return