import sys, getopt
from cryptography.fernet import Fernet

def imprimeAyuda():
   print("""
      Uso:

      Para cifrar archivos:
      cifra.py -i <inputfile> -c <size> -o <outputfile>

      Para descifrar archivos:
      cifra.py -i <inputfile> -d <keyfile> -o <outputfile>

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


def cargarClave(clave="clave.key"):
    #abre el archivo de la llave
    return open(clave, "wb").read

def generaClave(clave="clave.key"):
    claveCifrado = Fernet.generate_key()
    with open( clave, "wb+") as archivoClave:
        archivoClave.write(claveCifrado)
    return clave

def cifraElArchivoSimetrico(archivo):
    print('Cifrado simetrico de ', archivo)
    with open(generaClave(), "rb") as key:
        ferni = Fernet(key.read())
    with open(archivo, "wb+") as file:
        datosCifrados = ferni.encrypt(file.read())
        file.write(datosCifrados)
        file.close()
    return

def decifraElArchivoSimetrico(archivo):
    print('Decifrado simetrico de ', archivo)
    #key = "clave.key"
    key = input("Ingresa el nombre de la clave: ")
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
            

    except FileNotFoundError as e:
        print("El archivo de la llave es invalido_!")

    except IOError as e:
        print("El archivo de la llave es invalido")




def cifraElArchivo(archivo):
    print('Aqui se inserta RSA')
    return

def decifraElArchivo(archivo):
    print('Aqui se inserta AES')
    return

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
         print ('cifraS.py -i <inputfile> -o <outputfile>')
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