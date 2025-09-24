import pandas as pd

# ================== LECTURA DEL ARCHIVO ==================
df = pd.read_csv('ventas.csv')

# Asegurar que FECHA esté en formato datetime
df['FECHA'] = pd.to_datetime(df['FECHA'], errors='coerce')

pd.set_option('display.max_columns', None)

print("========== PREGUNTAS DE INVESTIGACIÓN ==========\n")

# 1. ¿Cuántos registros (ventas) hay en total?
print("1. Total de registros (ventas):", len(df))

# 2. ¿Cuántas ventas fueron Cerradas, Pendientes y Canceladas?
print("\n2. Ventas por estado:\n", df['ESTADO'].value_counts())

# 3. ¿Cuál es el valor total de ventas realizadas?
print("\n3. Valor total de ventas:", f"{df['VALOR_VENTA'].sum():,.0f}")

# 4. ¿Cuál es el promedio de comisión pagada por venta cerrada?
print("\n4. Promedio comisión en ventas cerradas:",
      f"{df[df['ESTADO']=='Cerrado']['COMISION'].mean():,.2f}")

# 5. ¿Qué ciudad generó el mayor número de ventas cerradas?
print("\n5. Ciudad con más ventas cerradas:\n",
      df[df['ESTADO']=='Cerrado']['CIUDAD'].value_counts().head(1))

# 6. ¿Cuál es el valor total de ventas por ciudad?
print("\n6. Valor total de ventas por ciudad:\n",
      df.groupby('CIUDAD')['VALOR_VENTA'].sum())

# 7. ¿Cuáles son los 5 productos más vendidos (por número de registros)?
print("\n7. Top 5 productos más vendidos:\n",
      df['PRODUCTO'].value_counts().head(5))

# 8. ¿Cuántos productos únicos fueron vendidos?
print("\n8. Número de productos únicos vendidos:", df['PRODUCTO'].nunique())

# 9. ¿Cuál es el vendedor con mayor número de ventas cerradas?
print("\n9. Vendedor con más ventas cerradas:\n",
      df[df['ESTADO']=='Cerrado']['VENDEDOR'].value_counts().head(1))

# 10. ¿Cuál es la venta con el mayor valor y qué cliente la realizó?
venta_max = df.loc[df['VALOR_VENTA'].idxmax()]
print("\n10. Venta de mayor valor:", venta_max['VALOR_VENTA'],
      "Cliente:", venta_max['CLIENTE'])

# 11. ¿Existen ventas con valor o comisión nula o negativa?
print("\n11. Ventas con valor o comisión nula/negativa:\n",
      df[(df['VALOR_VENTA'] <= 0) | (df['COMISION'] <= 0)])

# 12. ¿Cuál es la media de ventas por mes?
print("\n12. Media de ventas por mes:\n",
      df.groupby(df['FECHA'].dt.month)['VALOR_VENTA'].mean())

# 13. ¿Cuál fue el mes con más ventas cerradas?
print("\n13. Mes con más ventas cerradas:\n",
      df[df['ESTADO']=='Cerrado']['FECHA'].dt.month.value_counts().head(1))

# 14. ¿Cuántas ventas se realizaron en cada trimestre del año?
print("\n14. Ventas por trimestre:\n",
      df['FECHA'].dt.to_period('Q').value_counts().sort_index())

# 15. ¿Qué productos han sido vendidos en más de 3 ciudades diferentes?
print("\n15. Productos vendidos en más de 3 ciudades:\n",
      df.groupby('PRODUCTO')['CIUDAD'].nunique()[lambda x: x > 3])

# 16. ¿Existen duplicados en los datos?
print("\n16. Registros duplicados:", df.duplicated().sum())

# 17. Eliminar filas con nulos en CLIENTE, PRODUCTO, VALOR_VENTA
df = df.dropna(subset=['CLIENTE','PRODUCTO','VALOR_VENTA'])
print("\n17. Filas nulas eliminadas. Total filas ahora:", len(df))

# 18. Crear columna UTILIDAD (95% del valor de venta)
df['UTILIDAD'] = df['VALOR_VENTA'] * 0.95
utilidad_producto = df.groupby('PRODUCTO')['UTILIDAD'].sum().sort_values(ascending=False).head(1)
print("\n18. Producto con mayor utilidad total:\n", utilidad_producto)


print("\n========== PREGUNTAS GROUPBY() ==========\n")

# • Valor total de ventas por ciudad
print("a) Valor total de ventas por ciudad:\n", df.groupby('CIUDAD')['VALOR_VENTA'].sum())

# • Promedio de comisión por vendedor
print("\nb) Promedio de comisión por vendedor:\n", df.groupby('VENDEDOR')['COMISION'].mean())

# • Número de ventas por estado y por ciudad
print("\nc) Número de ventas por estado y ciudad:\n", df.groupby(['CIUDAD','ESTADO']).size())

# • Categoría de producto con el mayor valor de ventas
print("\nd) Categoría con mayor valor de ventas:\n", df.groupby('CATEGORIA')['VALOR_VENTA'].sum().sort_values(ascending=False).head(1))

# • Total de ventas mensuales por ciudad
print("\ne) Total de ventas mensuales por ciudad:\n", df.groupby([df['FECHA'].dt.to_period('M'),'CIUDAD'])['VALOR_VENTA'].sum())

# • Ventas cerradas por vendedor y ciudad
print("\nf) Ventas cerradas por vendedor y ciudad:\n", df[df['ESTADO']=='Cerrado'].groupby(['VENDEDOR','CIUDAD']).size())

