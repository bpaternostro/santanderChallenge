import codecs
import Const as const

def processFiles(archivo_entrada, archivo_salida):
    try:
        in_file = codecs.open(const.IN_PATH+archivo_entrada, 'r', encoding='utf-16-le')
        out_file = codecs.open(const.OUT_PATH+archivo_salida, 'w', encoding='utf-8')

        aux = []
        for line in in_file:
            fixed_line = line.replace('\t', '|')
            #valido que la fila este completa, sino lo guardo en un array para tratarlo aparte
            if repr(fixed_line).count('|') == 4:
                out_file.write(fixed_line)
            else:
                aux.append(fixed_line)
    except Exception as e:
        print "Error:", e, "procesando linea - metodo processFiles."
        return False

    in_file.close()
    out_file.close()

    return aux

###################################################################################################################
###################################################################################################################

archivo_entrada="datos_data_engineer.tsv"
archivo_salida="archivo_procesado.csv"

filas_incompletas=processFiles(archivo_entrada,archivo_salida)

if(filas_incompletas!=False):
    #Intente procesarlas al final e incoporarlas al csv pero me quedaban atributos incompletos y no quise asumir nada incorrecto.
    message="Existen " + str(len(filas_incompletas)) + " filas sin procesar. A continuacion un detalle:"
    print message
    for row in filas_incompletas:
        print row
else:
    message = "Existieron inconvenientes en el procesamiento del archivo."
    print message


