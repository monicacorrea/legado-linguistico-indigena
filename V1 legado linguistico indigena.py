#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Datos de la tabla
data = {
    "Lengua Indígena": ["Náhuatl", "Quechua", "Maya", "Taíno", "Guaraní", "Aimara", "Mapudungun", "Cumanagoto", "Muisca", "Chibcha", "Tupí", "Arawak", "Caribe", "Wayuu", "Purépecha", "Zapoteco", "Mixteco", "Tsotsil", "Tzeltal", "Rarámuri", "Yucateco", "Kuna", "Shuar", "Ashaninka", "Shipibo", "Aguaruna"],
    "Palabras en Español": [
        "Chocolate, Tomate, Aguacate",
        "Papa, Quinoa, Llama",
        "Tabaco, Cacao, Huracán",
        "Canoa, Hamaca, Tabaco",
        "Mandioca, Yacaré, Tapioca",
        "Quinoa, Alpaca, Chicha",
        "Poncho, Mate, Malón",
        "Catire", "Chicha", "",
        "Petaca", "Hamaca, Huracán",
        "Yotojolo, Muma", "Corunda, Uchepo", 
        "", "", "", "", "", "", "", "", "", "", "", ""
    ],
    "Palabras en Inglés": [
        "Chocolate, Tomato, Avocado",
        "Potato, Quinoa, Llama",
        "Tobacco, Cocoa, Hurricane",
        "Canoe, Hammock, Tobacco",
        "Manioc, Caiman, Tapioca",
        "Quinoa, Alpaca, Chicha",
        "Poncho, Mate, Malon",
        "", "", "",
        "Hammock, Hurricane",
        "", "",
        "", "", "", "", "", "", "", "", "", "", ""
    ],
    "Ubicación de la Tribu": ["México (Aztecas)", "Perú, Bolivia, Ecuador (Incas)", "México, Guatemala, Belice, Honduras (Mayas)", "Caribe", "Paraguay, Brasil, Argentina", "Perú, Bolivia, Chile", "Chile, Argentina (Mapuches)", "Venezuela", "Colombia (Muiscas)", "Colombia", "Brasil", "Caribe, Sudamérica", "Caribe", "Colombia, Venezuela (Wayuu)", "México (Purépechas)", "México (Zapotecas)", "México (Mixtecos)", "México (Tsotsiles)", "México (Tzeltal)", "México (Rarámuris)", "México (Mayas)", "Panamá, Colombia (Kunas)", "Ecuador, Perú (Shuar)", "Perú, Brasil (Ashaninkas)", "Perú, Brasil (Shipibos)", "Perú (Aguarunas)"]
}

# Ajustar automáticamente las listas para que tengan la misma longitud
max_length = max(len(v) for v in data.values())
for key in data:
    while len(data[key]) < max_length:
        data[key].append("")  # Agregar valores vacíos para igualar longitudes

# Crear el DataFrame
df = pd.DataFrame(data)

# Mostrar la tabla
print(df.to_markdown(index=False, numalign="left", stralign="left"))

# Creado por
print("\n\nCreado por\nMónica Correa - www.monicacorrea.com")


# In[ ]:




