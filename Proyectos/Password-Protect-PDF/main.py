import shutil, os
import PyPDF2

ruta_original = 'C:/Users/Fran/Desktop/Python/Proyectos/Password-Protect-PDF/pdf/original.pdf'
ruta_copia = 'C:/Users/Fran/Desktop/Python/Proyectos/Password-Protect-PDF/pdf/copia.pdf'

# Crear copia del archivo original
with open(ruta_original, 'rb') as archivo_original:
    pdf_original = PyPDF2.PdfReader(archivo_original)
    pdf_copia = PyPDF2.PdfWriter()
    for pagina in range(len(pdf_original.pages)):
        pdf_copia.add_page(pdf_original.pages[pagina])

    # Establecer la contraseña para la copia
    pdf_copia.encrypt(user_password='admin', owner_pwd='admin1')

    # Escribir el archivo copia en disco
    with open(ruta_copia, 'wb') as archivo_copia:
        pdf_copia.write(archivo_copia)

# Borrar el archivo original
os.remove(ruta_original)