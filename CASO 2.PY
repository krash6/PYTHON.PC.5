import pandas as pd

# Datos de las críticas de Roberto y Clara
datos_roberto = {'ID': [97503, 97503, 97503, 97503],
                 'Críticas': ['Excelente', 'Muy buena', 'Regular', 'Mala']}
datos_clara = {'ID': [90387, 90387, 90387],
               'Críticas': ['Excelente', 'Muy buena', 'Excelente']}

# Crear dataframes para Roberto y Clara
df_roberto = pd.DataFrame(datos_roberto)
df_clara = pd.DataFrame(datos_clara)

# Combinar los dataframes de Roberto y Clara en uno solo
df_completo = pd.concat([df_roberto, df_clara], ignore_index=True)

# Guardar el dataframe como un archivo Excel
df_completo.to_excel("roberto.xlsx", index=False)