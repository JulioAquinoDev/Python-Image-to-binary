import base64

# Initial function
def inicio():
    file = ""
    # Getting the value of a function
    # Function receiving value to return
    f = obterArquivo(file)

    # convert file
    binary = converterBinario(f)

    # wirite text
    escreve(binary)
    print("fechou")

    
# Getting the file path
def obterArquivo(file):
    # getting path
    file = input("Digite o caminha do arquivo:")
    # return value
    print("Obtendo o path da imge")
    return file

def converterBinario(f):
    with open(f, "rb") as file:
        binaryData = base64.b64encode(file.read())
    print("Obtendo o binary da image")
    return binaryData

def escreve(binary):
    
    with open("Binary_da_imagem.bin", "wb") as a:
        a.write(binary)
        
    print("Gerando TXT com binary.")
    
def converterImagem():
    with open("Binary_da_imagem.bin", "rb") as file:
        data = file.read()
    print("Lendo txt binario")
    criarImagem(data)
    
def criarImagem(data):
    y = base64.b64decode((data))
    with open("Binary_da_imagem.jpg", "wb") as a:
        a.write(y)
    print("Gerando Img")
    print("OK")

##with open("login.jpg", "rb") as file:
##binaryData = file.read()
##
##
##
##
##with open("Binary_da_imagem.txt", "a+") as f:
##f.write(binaryData)

# Função para iniciar o script
# Function to star the scrpit
inicio()
a = ""
converterImagem()
