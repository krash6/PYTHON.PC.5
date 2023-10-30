import pandas as pd

# Simulación de datos
datos = {
    'property_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'property_name': ['Property A', 'Property B', 'Property C', 'Property D', 'Property E', 'Property F', 'Property G', 'Property H', 'Property I', 'Property J'],
    'room_type': ['Shared room', 'Shared room', 'Private room', 'Shared room', 'Shared room', 'Private room', 'Shared room', 'Shared room', 'Shared room', 'Private room'],
    'price': [20, 25, 30, 35, 40, 45, 50, 50, 50, 55],
    'review_scores_rating': [90, 95, 85, 92, 88, 93, 94, 98, 97, 84]
}

# Crear un DataFrame a partir de los datos
df = pd.DataFrame(datos)

# Filtrar las propiedades que se ajustan al presupuesto y tipo de habitación
df_filtered = df[(df['price'] <= 50) & (df['room_type'] == 'Shared room')]

# Ordenar las propiedades filtradas por precio y puntuación en orden ascendente
df_sorted = df_filtered.sort_values(by=['price', 'review_scores_rating'], ascending=[True, False])

# Obtener las 10 propiedades más baratas después de aplicar los filtros y la clasificación
top_10_properties = df_sorted.head(10)

# Mostrar las 10 propiedades más baratas para Diana
print(top_10_properties)