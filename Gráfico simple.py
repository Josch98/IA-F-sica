import matplotlib.pyplot as plt
import numpy as np

# 1. Datos extraídos de tus columnas en Excel
area = np.array([131.1, 271.7, 498.8, 664.2])
lambda_val = np.array([0.030, 0.037, 0.045, 0.053])

# Errores calculados en tus columnas F y G
error_plus = np.array([0.00674, 0.00681, 0.00689, 0.00734])
error_minus = np.array([0.00747, 0.00650, 0.00737, 0.00850])

# Matplotlib requiere que los errores asimétricos estén en formato [error_negativo, error_positivo]
y_errors = [error_minus, error_plus]

# 2. Configurar la figura del gráfico
plt.figure(figsize=(7, 5), dpi=150)

# 3. Graficar los puntos y sus barras de error (fmt='o' hace que sean solo puntos dispersos)
plt.errorbar(area, lambda_val, yerr=y_errors, fmt='o', color='black', 
             ecolor='red', elinewidth=1.2, capsize=4, capthick=1.2, 
             markersize=5, label='Datos experimentales')

# 4. Configurar el plano cartesiano (Etiquetas con LaTeX para formato científico)
plt.xlabel('Área superficial ($A$ / $cm^2$)', fontsize=11) 
plt.ylabel('Coeficiente de amortiguamiento ($\lambda$ / $s^{-1}$)', fontsize=11)
plt.title('Gráfico de $\lambda$ en función del Área Superficial', fontsize=12, fontweight='bold', pad=15)

# 5. Forzar a que el plano empiece cerca del origen (opcional pero recomendado)
plt.xlim(0, 800)
plt.ylim(0, 0.08)

# 6. Añadir cuadrícula limpia y leyenda
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')

# 7. Mostrar o guardar el gráfico
plt.tight_layout()
plt.savefig('grafico_lambda.png') # Se guardará como imagen en tu computadora
plt.show()