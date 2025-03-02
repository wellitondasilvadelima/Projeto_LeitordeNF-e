import xmltodict
from nf_data import data

def get_info_nfs(nfs_name,list_value):
    okay = False
    msg_error = ""

    with open(f"input/{nfs_name}","rb") as file_xml:

        dict_file_xml = xmltodict.parse(file_xml)
        try:
            if("NFe" in dict_file_xml):
                nf_info = dict_file_xml["NFe"]["infNFe"]
            else:
                nf_info = dict_file_xml["nfeProc"]["NFe"]["infNFe"]

            if("prod" in nf_info["det"]):
                data.product = nf_info["det"]["prod"]["xProd"]
                data.quant_product = nf_info["det"]["prod"]["qCom"]
            else:
                data.product         = ""
                data.quant_product   = ""
                for i in range(len(nf_info["det"])):
                    data.product       += nf_info["det"][i]["prod"]["xProd"]+","
                    data.quant_product += nf_info["det"][i]["prod"]["qCom"]+","
        
            if("vol" in nf_info["transp"]):
                data.gross_weight = nf_info["transp"]["vol"]["pesoB"]
            else:
                data.gross_weight = "Não informado"
        
            if ("vTotTrib" in nf_info["total"]["ICMSTot"]):
                data.total_taxable = nf_info["total"]["ICMSTot"]["vTotTrib"]
            else:
                data.total_taxable = nf_info["total"]["ICMSTot"]["vICMS"]

            data.number          = nf_info["@Id"]
            data.cnpj            = nf_info["emit"]["CNPJ"]
            data.company         = nf_info["emit"]["xNome"]
            data.customer_name   = nf_info["dest"]["xNome"]
            data.customer_adress = nf_info["dest"]["enderDest"]["xLgr"]+"-"+ nf_info["dest"]["enderDest"]["nro"]+","+nf_info["dest"]["enderDest"]["xMun"]+"-"+nf_info["dest"]["enderDest"]["UF"]+","+nf_info["dest"]["enderDest"]["xPais"]
            data.total           = nf_info["total"]["ICMSTot"]["vNF"]

            list_value.append([ data.number, 
                                data.cnpj,
                                data.company, 
                                data.customer_name, 
                                data.customer_adress, 
                                data.product,
                                data.quant_product,
                                data.gross_weight, 
                                data.total,  
                                data.total_taxable])
            okay = True
        except Exception:
            msg_error = "Error obtaining NF-e information "+nfs_name
            
    return okay,msg_error