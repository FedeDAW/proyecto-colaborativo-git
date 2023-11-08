import base64

def base16_JorgeG(input_string):
    hexadecimal = ''.join([f'{ord(char):02x}' for char in input_string])
    return hexadecimal

def base64thomas(y):
    return base64.b64encode(y.encode()).decode()

def base64_Fede():
    texto = "hola mundo"
    strtext = base64.b64encode(bytes(texto, 'utf-8'))
    base64_str = strtext.decode('utf-8')
    print("mensaje :" + texto +", base64: "+base64_str)
    
def main():
    entrada = input("Introduce texto a convertir a base64: ")
    print(base64thomas(entrada))

if __name__ == "__main__":
    main()
