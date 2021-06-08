#!/usr/bin/python

#Se importan bibliotecas para recibir opciones de la linea de comandos
#También para realizar cifrado simetrico y asimetrico
import sys, getopt
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# def encrypt(filename, key):
#    f=Fernet(key)
#    with open(filename, "rb") as file:
#    file_data = file.read()
#    encrypted_data = f.encrypt(file_data)
#    with open(filename, "wb") as file:
#    file.write(encrypted_data)

def muestraExplicacion():
   print("""
      Uso:

      Para cifrar archivos:
      cifra.py -i <inputfile> -c <size> -o <outputfile>

      Para descifrar archivos:
      cifra.py -i <inputfile> -d <keyfile> -o <outputfile>

      """)

def main(argv):
   #Se definen las variables a utilizar asi como los valores por default
   inputfile = ''
   outputfile = 'output'
   key_size = 16
   key_file = ''

   flag_input, flag_output, flag_key = False, False, False

   #El bloque try-except permite atrapar errores en caso de una mala 
   # captura de datos
   try:
      opts, args = getopt.getopt(argv,"hi:dc:o:",["ifile=","keyfile=","ofile="])
   except getopt.GetoptError:
      muestraExplicacion()
      sys.exit(2)

   #Se recorren las opciones y se activan las banderas correspondientes
   for opt, arg in opts:
      if opt == '-h':
         muestraExplicacion()
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         flag_input = True
      elif opt in ("-o", "--ofile"):
         outputfile = arg
         flag_output = True
      elif opt in ("-d", "--keyfile"):
         key_file = arg
         flag_key = True
      elif opt in ("-d", "--keysize"):
         key_size = arg
         flag_key = True

   if flag_output and flag_input and flag_key and key_file in ('16', '128', '256'):
      print('Banderas para cifrado')
   elif flag_output and flag_input and flag_key and key_file == 'key':
      print('Banderas para descifrado')
   else:
      print('Error en los argumentos')
      muestraExplicacion()
      sys.exit(3)

   # print('Input file is "', inputfile)
   # print('Output file is "', outputfile)


if __name__ == "__main__":
   main(sys.argv[1:])