
import base64

def base64_Fede():
    texto = "hola mundo"
    strtext = base64.b64encode(bytes(texto, 'utf-8'))
    base64_str = strtext.decode('utf-8')
    print("mensaje :" + texto +", base64: "+base64_str)

base64_Fede() 