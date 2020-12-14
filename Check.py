import codecs
import Const as const

archivo_salida="archivo_procesado.csv"
check_file = codecs.open(const.OUT_PATH+archivo_salida, 'r', encoding='utf-8')
for line in check_file:
  print line