from ftplib import FTP
import zipfile


ano = 2022
estado = "PA"
dir = "/FTP/PDA/TISS/AMBULATORIAL"

ftp = FTP("dadosabertos.ans.gov.br")
ftp.connect()
ftp.login("anonymous", "anonymous")

files = ftp.dir(f"{dir}/{ano}/{estado}")

def list_files(dir:str, ano:int, estado:str):
    ftp = FTP("dadosabertos.ans.gov.br")
    ftp.connect()
    ftp.login("anonymous", "anonymous")

    files = ftp.nlst(f"{dir}/{ano}/{estado}")
    ftp.quit()
    return files   

fls = list_files(dir, ano, estado)
fls

files = get_tiss(ftp, dir, ano, estado)
for file in files:
    fw = file.replace(f"{dir}/{ano}/{estado}/", "")
    cmd = f"RETR {file}"
    localfile = open(fw, "wb")
    ftp.retrbinary(cmd, localfile.write, 1024)
    # try:
    #     with zipfile.ZipFile(f"./{fw}", 'r') as zip_ref:
    #         zip_ref.extractall("./tmp")
    # except:
    #     print("Erro: ", fw)