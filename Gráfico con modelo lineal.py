import matplotlib.pyplot as plt
import numpy as np

# 1. Datos extraídos de tus columnas en Excel (image_6f9b3f.png)
area = np.array([131.1, 271.7, 498.8, 664.2])
lambda_val = np.array([0.030, 0.037, 0.045, 0.053])

# Errores calculados
error_plus = np.array([0.00674, 0.00681, 0.00689, 0.00734])
error_minus = np.array([0.00747, 0.00650, 0.00737, 0.00850])
y_errors = [error_minus, error_plus]

# ==========================================
# NUEVO: Cálculo de la línea de mejor ajuste
# ==========================================
# np.polyfit calcula la pendiente (m) y la ordenada al origen (c) para un grado 1 (recta)
m, c = np.polyfit(area, lambda_val, 1)

# Creamos un rango de puntos X desde 0 hasta 800 para dibujar la línea continua
x_line = np.linspace(0, 800, 100)
y_line = m * x_line + c
# ==========================================

# 2. Configurar la figura del gráfico
plt.figure(figsize=(7, 5), dpi=150)

# 3. Graficar los puntos con sus barras de error
plt.errorbar(area, lambda_val, yerr=y_errors, fmt='o', color='black', 
             ecolor='red', elinewidth=1.2, capsize=4, capthick=1.2, 
             markersize=5, label='Datos experimentales')

# 4. Dibujar la línea de mejor ajuste usando los puntos calculados
# El formato {:.5f} y {:.4f} limita la cantidad de decimales en la leyenda
plt.plot(x_line, y_line, color='blue', linestyle='-', linewidth=1.5,
         label=f'Línea de mejor ajuste ($y = {m:.5f}x + {c:.4f}$)')

# 5. Configurar el plano cartesiano (Etiquetas con LaTeX)
plt.xlabel('Área superficial ($A$ / $cm^2$)', fontsize=11) 
plt.ylabel('Coeficiente de amortiguamiento ($\lambda$ / $s^{-1}$)', fontsize=11)
plt.title('Gráfico de $\lambda$ en función del Área Superficial', fontsize=12, fontweight='bold', pad=15)

# 6. Forzar límites fijos del plano cartesiano
plt.xlim(0, 800)
plt.ylim(0, 0.08)

# 7. Cuadrícula y leyenda
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')

# 8. Guardar y mostrar
plt.tight_layout()
plt.savefig('grafico_lambda_ajustado.png') 
plt.show()