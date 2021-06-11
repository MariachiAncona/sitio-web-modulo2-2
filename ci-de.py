import sys, getopt
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


def decifraElArchivo(archivo):
    print('Decifra con RSA: ', archivo)
    try:
        file_in = open(archivo, "wb+")

        private_key = RSA.import_key(open("private.pem").read())

        enc_session_key, nonce, tag, ciphertext = [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
    
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        file_in.write(data)
        file_in.close()
    except ValueError as e:
        return print('Falla al decifrar el archivo')

def cifraElArchivo(archivo):
    print('Cifrado con RSA: ', archivo)

    generaClaves()
    file_out = open(archivo, "wb+")

    recipient_key = RSA.import_key(open("receiver.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(file_out.read())
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()


def generaClaves():
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)
    file_out.close()

def imprimeAyuda():
   print("""
      Uso:

      Para cifrar archivos con algoritmo simetrico:
      python ci-de.py -i <inputfile> 

      Para descifrar archivos con algoritmo simetrico:
      python ci-de.py -i <inputfile> -d 

      Para cifrar archivos con algoritmo asimetrico:
      python ci-de.py -i <inputfile> -a

      Para descifrar archivos con algoritmo asimetrico:
      python ci-de.py -i <inputfile> -da

      """)

def elArchivoEsValido(archivo):
    try:
        with open(archivo, 'r') as f:
            f.close()
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def generaClave(clave="clave.key"):
    claveCifrado = Fernet.generate_key()
    with open( clave, "wb") as archivoClave:
        archivoClave.write(claveCifrado)
    return clave

def cifraElArchivoSimetrico(archivo):
    print('Cifrado simetrico de ', archivo)
    with open(generaClave(), "rb") as key:
        ferni = Fernet(key.read())
        key.close()
    with open(archivo, "wb+") as file:
        datosCifrados = ferni.encrypt(file.read())
        file.write(datosCifrados)
        file.close()
    return

def decifraElArchivoSimetrico(archivo):
    print('Decifrado simetrico de ', archivo)
    key = "clave.key"
    #key = input("Ingresa el nombre de la clave: ")
    try:
        with open(key, 'rb') as f:
            ferni = Fernet(f.read())
            with open(archivo, "rb") as file:
                encrypted_data = file.read()
                decrypted_data = ferni.decrypt(encrypted_data)
                print(encrypted_data)
                file.close()
            with open(archivo, "wb") as file:
                file.write(decrypted_data)
                print(decrypted_data)
                file.close()
            f.close()
            

    except FileNotFoundError as e:
        print("El archivo de la llave es invalido_!")

    except IOError as e:
        print("El archivo de la llave es invalido")


def main(argv):
   inputfile = ''
   seDecifra = False
   esSimetrico = True
   sitio = 'Agregar nuestros sitios para mostrar'
   try:
      opts, args = getopt.getopt(argv,"hi:da",["ifile=","seDecifra=","esSimetrico="])
   except getopt.GetoptError:
      print ("""
            Error al tratar de usar el programa

            Para visualizar el uso de cifra para cifrado simetrico:
            a. Teeclee python cifraS.py -h
            b. visite el sitio:

            """)
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         imprimeAyuda()
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-d", "--seDecifra"):
         seDecifra = True
      elif opt in ("-a", "--asimetrico"):
          esSimetrico = False

   print ('------------***--------------')
   print ('Input file is ', inputfile)
   print ('Se decifra: ', seDecifra)
   print ('Es simetrico: ', esSimetrico)

   seValidoElArchivo = elArchivoEsValido(inputfile)
    #Cifra el archivo
   if seValidoElArchivo and not seDecifra and esSimetrico:
       cifraElArchivoSimetrico(inputfile)
   elif seValidoElArchivo and seDecifra and esSimetrico:
       decifraElArchivoSimetrico(inputfile)
   elif seValidoElArchivo and not seDecifra and not esSimetrico:
       cifraElArchivo(inputfile)
   elif seValidoElArchivo and seDecifra and not esSimetrico:
       decifraElArchivo(inputfile)
   else:
       imprimeAyuda()

if __name__ == "__main__":
   main(sys.argv[1:])