import sys, getopt

def imprimeAyuda():
   print("""
      Uso:

      Para cifrar archivos:
      cifra.py -i <inputfile> -c <size> -o <outputfile>

      Para descifrar archivos:
      cifra.py -i <inputfile> -d <keyfile> -o <outputfile>

      """)

def elArchivoEsValido(archivo):
    #Valida el archivo
    return True

def cifraElArchivoSimetrico(archivo):
    print('Aqui se inserta Fernet para cifrado')
    return

def decifraElArchivoSimetrico(archivo):
    print('Aqui se inserta Fernet para decifrado')
    return

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