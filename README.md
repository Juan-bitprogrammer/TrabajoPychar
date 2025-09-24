# TrabajoPychar

## Integrantes: 

    Juan Jose Pelaez Agudelo

    Juan Esteban Osorno Duque 

    Jhonier Cespedes

    John Higuita

## 🔥 Resultado del codigo 

C:\Users\desarrollo\PycharmProjects\ventasCSV\.venv\Scripts\python.exe C:\Users\desarrollo\PycharmProjects\ventasCSV\main.py 
========== PREGUNTAS DE INVESTIGACIÓN ==========

1. Total de registros (ventas): 100000

2. Ventas por estado:
 ESTADO
Pendiente    33382
Cancelado    33362
Cerrado      33256
Name: count, dtype: int64

3. Valor total de ventas: 1,060,717,021

4. Promedio comisión en ventas cerradas: 532.91

5. Ciudad con más ventas cerradas:
 CIUDAD
Ciudad_11    1760
Name: count, dtype: int64

6. Valor total de ventas por ciudad:
 CIUDAD
Ciudad_1     53180354.93
Ciudad_10    54283477.48
Ciudad_11    55090117.15
Ciudad_12    52257702.59
Ciudad_13    52411542.65
Ciudad_14    53962557.36
Ciudad_15    52350841.08
Ciudad_16    51819065.01
Ciudad_17    54031701.40
Ciudad_18    53993109.65
Ciudad_19    53898776.57
Ciudad_2     51011693.79
Ciudad_20    52940195.61
Ciudad_3     53975136.51
Ciudad_4     53020170.48
Ciudad_5     52288438.38
Ciudad_6     52912962.85
Ciudad_7     51579010.60
Ciudad_8     53288516.02
Ciudad_9     52421650.66
Name: VALOR_VENTA, dtype: float64

7. Top 5 productos más vendidos:
 PRODUCTO
Producto_49    2098
Producto_11    2087
Producto_33    2086
Producto_32    2078
Producto_15    2061
Name: count, dtype: int64

8. Número de productos únicos vendidos: 50

9. Vendedor con más ventas cerradas:
 VENDEDOR
Vendedor_4    1198
Name: count, dtype: int64

10. Venta de mayor valor: 39999.8 Cliente: Cliente_9

11. Ventas con valor o comisión nula/negativa:
 Empty DataFrame
Columns: [CLIENTE, PRODUCTO, PRECIO, CANTIDAD, CIUDAD, VENDEDOR, FECHA, ESTADO, VALOR_VENTA, COMISION, CATEGORIA]
Index: []

12. Media de ventas por mes:
 FECHA
1     10633.241856
2     10616.023374
3     10446.408679
4     10561.166929
5     10660.848891
6     10644.529429
7     10645.507709
8     10658.532959
9     10619.175672
10    10597.144147
11    10470.829220
12    10726.471352
Name: VALOR_VENTA, dtype: float64

13. Mes con más ventas cerradas:
 FECHA
10    2931
Name: count, dtype: int64

14. Ventas por trimestre:
 FECHA
2020Q1    4979
2020Q2    5014
2020Q3    5006
2020Q4    5059
2021Q1    4925
2021Q2    4929
2021Q3    4979
2021Q4    5051
2022Q1    4953
2022Q2    4916
2022Q3    4921
2022Q4    5123
2023Q1    4996
2023Q2    5090
2023Q3    5093
2023Q4    5007
2024Q1    4980
2024Q2    4973
2024Q3    5044
2024Q4    4962
Freq: Q-DEC, Name: count, dtype: int64

15. Productos vendidos en más de 3 ciudades:
 PRODUCTO
Producto_1     20
Producto_10    20
Producto_11    20
Producto_12    20
Producto_13    20
Producto_14    20
Producto_15    20
Producto_16    20
Producto_17    20
Producto_18    20
Producto_19    20
Producto_2     20
Producto_20    20
Producto_21    20
Producto_22    20
Producto_23    20
Producto_24    20
Producto_25    20
Producto_26    20
Producto_27    20
Producto_28    20
Producto_29    20
Producto_3     20
Producto_30    20
Producto_31    20
Producto_32    20
Producto_33    20
Producto_34    20
Producto_35    20
Producto_36    20
Producto_37    20
Producto_38    20
Producto_39    20
Producto_4     20
Producto_40    20
Producto_41    20
Producto_42    20
Producto_43    20
Producto_44    20
Producto_45    20
Producto_46    20
Producto_47    20
Producto_48    20
Producto_49    20
Producto_5     20
Producto_50    20
Producto_6     20
Producto_7     20
Producto_8     20
Producto_9     20
Name: CIUDAD, dtype: int64

16. Registros duplicados: 0

17. Filas nulas eliminadas. Total filas ahora: 100000

18. Producto con mayor utilidad total:
 PRODUCTO
Producto_33    2.145228e+07
Name: UTILIDAD, dtype: float64

========== PREGUNTAS GROUPBY() ==========

a) Valor total de ventas por ciudad:
 CIUDAD
Ciudad_1     53180354.93
Ciudad_10    54283477.48
Ciudad_11    55090117.15
Ciudad_12    52257702.59
Ciudad_13    52411542.65
Ciudad_14    53962557.36
Ciudad_15    52350841.08
Ciudad_16    51819065.01
Ciudad_17    54031701.40
Ciudad_18    53993109.65
Ciudad_19    53898776.57
Ciudad_2     51011693.79
Ciudad_20    52940195.61
Ciudad_3     53975136.51
Ciudad_4     53020170.48
Ciudad_5     52288438.38
Ciudad_6     52912962.85
Ciudad_7     51579010.60
Ciudad_8     53288516.02
Ciudad_9     52421650.66
Name: VALOR_VENTA, dtype: float64

b) Promedio de comisión por vendedor:
 VENDEDOR
Vendedor_1     527.624934
Vendedor_10    536.086989
Vendedor_11    520.213443
Vendedor_12    539.387270
Vendedor_13    530.525111
Vendedor_14    525.066466
Vendedor_15    544.132338
Vendedor_16    534.229295
Vendedor_17    533.754840
Vendedor_18    528.960570
Vendedor_19    525.450744
Vendedor_2     524.514530
Vendedor_20    530.211326
Vendedor_21    532.654936
Vendedor_22    540.454134
Vendedor_23    524.154540
Vendedor_24    525.177151
Vendedor_25    531.201263
Vendedor_26    529.019328
Vendedor_27    529.853876
Vendedor_28    535.618795
Vendedor_29    533.875449
Vendedor_3     521.438873
Vendedor_30    531.717288
Vendedor_4     526.000220
Vendedor_5     521.730300
Vendedor_6     533.377533
Vendedor_7     537.894224
Vendedor_8     527.043337
Vendedor_9     528.840930
Name: COMISION, dtype: float64

c) Número de ventas por estado y ciudad:
 CIUDAD     ESTADO   
Ciudad_1   Cancelado    1648
           Cerrado      1669
           Pendiente    1716
Ciudad_10  Cancelado    1683
           Cerrado      1661
           Pendiente    1655
Ciudad_11  Cancelado    1683
           Cerrado      1760
           Pendiente    1679
Ciudad_12  Cancelado    1591
           Cerrado      1698
           Pendiente    1709
Ciudad_13  Cancelado    1648
           Cerrado      1598
           Pendiente    1646
Ciudad_14  Cancelado    1722
           Cerrado      1622
           Pendiente    1634
Ciudad_15  Cancelado    1688
           Cerrado      1629
           Pendiente    1661
Ciudad_16  Cancelado    1641
           Cerrado      1621
           Pendiente    1644
Ciudad_17  Cancelado    1634
           Cerrado      1708
           Pendiente    1649
Ciudad_18  Cancelado    1645
           Cerrado      1712
           Pendiente    1671
Ciudad_19  Cancelado    1719
           Cerrado      1685
           Pendiente    1705
Ciudad_2   Cancelado    1648
           Cerrado      1665
           Pendiente    1615
Ciudad_20  Cancelado    1678
           Cerrado      1696
           Pendiente    1647
Ciudad_3   Cancelado    1742
           Cerrado      1626
           Pendiente    1725
Ciudad_4   Cancelado    1721
           Cerrado      1685
           Pendiente    1654
Ciudad_5   Cancelado    1731
           Cerrado      1617
           Pendiente    1686
Ciudad_6   Cancelado    1645
           Cerrado      1668
           Pendiente    1681
Ciudad_7   Cancelado    1642
           Cerrado      1632
           Pendiente    1602
Ciudad_8   Cancelado    1651
           Cerrado      1655
           Pendiente    1685
Ciudad_9   Cancelado    1602
           Cerrado      1649
           Pendiente    1718
dtype: int64

d) Categoría con mayor valor de ventas:
 CATEGORIA
Hogar    2.140956e+08
Name: VALOR_VENTA, dtype: float64

e) Total de ventas mensuales por ciudad:
 FECHA    CIUDAD   
2020-01  Ciudad_1      938322.80
         Ciudad_10     983432.87
         Ciudad_11     909481.36
         Ciudad_12     796278.26
         Ciudad_13     951821.13
                         ...    
2024-12  Ciudad_5      744640.61
         Ciudad_6      997503.75
         Ciudad_7     1042071.63
         Ciudad_8      895660.22
         Ciudad_9      957479.02
Name: VALOR_VENTA, Length: 1200, dtype: float64

f) Ventas cerradas por vendedor y ciudad:
 VENDEDOR    CIUDAD   
Vendedor_1  Ciudad_1     53
            Ciudad_10    56
            Ciudad_11    58
            Ciudad_12    38
            Ciudad_13    56
                         ..
Vendedor_9  Ciudad_5     48
            Ciudad_6     51
            Ciudad_7     53
            Ciudad_8     56
            Ciudad_9     60
Length: 600, dtype: int64

Process finished with exit code 0
