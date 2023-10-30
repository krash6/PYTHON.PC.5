import pandas as pd

# Cargar los datos desde el archivo Excel
ruta_archivo = r'C:\Users\Sebastian\Downloads\cripto_currency.xlsx'
df = pd.read_excel(ruta_archivo)

# Imprimir las bases cargadas
print(df)

# Añadir una columna adicional que especifique el tipo de moneda
df['Tipo de Moneda'] = 'Criptomoneda'

# Generar un resumen de los datos mediante un agrupamiento
resumen = df.groupby(['Tipo de Moneda']).agg({'Precio': 'mean', 'Volumen': 'sum'})

# Almacenar los datos en un reporte Excel
ruta_reporte = r'C:\Users\Sebastian\Downloads\reporte_cripto.xlsx'
resumen.to_excel(ruta_reporte)

# Crear una imagen y guardarla en el archivo Excel
figura = df.plot(x='Fecha', y='Precio', title='Variación de precios de criptomonedas', kind='line').get_figure()
figura.savefig('grafico_cripto.png')

# Método de envío de correos
 
# El proceso de envío de correos normalmente requiere configuraciones adicionales, como credenciales de correo electrónico.

# Ejemplo de código para enviar correos
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor de correo
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login("tu_email@example.com", "tu_password")

# Crear el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = "tu_email@example.com"
mensaje['To'] = "destinatario@example.com"
mensaje['Subject'] = "Asunto del correo"

# Agregar el cuerpo del mensaje
cuerpo = "Este es un correo de prueba enviado desde Python."
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Enviar el correo
server.send_message(mensaje)
print("Correo enviado con éxito")

# Cerrar la conexión del servidor
server.quit()