import matplotlib.pyplot as plt
import numpy as np

# 1. Datos extraídos de tus columnas en Excel
area = np.array([131.1, 271.7, 498.8, 664.2])
lambda_val = np.array([0.030, 0.037, 0.045, 0.053])

# Incertidumbres del área superficial (Eje X) extraídas de tu imagen
x_errors = np.array([0.65, 0.93, 1.26, 1.45])

# Errores calculados para Y
error_plus = np.array([0.00674, 0.00681, 0.00689, 0.00734])
error_minus = np.array([0.00747, 0.00650, 0.00737, 0.00850])
y_errors = [error_minus, error_plus]

# ==========================================
# Cálculo de la línea de mejor ajuste
# ==========================================
m, c = np.polyfit(area, lambda_val, 1)

x_line = np.linspace(0, 800, 100)
y_line = m * x_line + c
# ==========================================

# 2. Configurar la figura del gráfico
plt.figure(figsize=(7, 5), dpi=150)

# 3. Graficar los puntos con sus barras de error en AMBOS ejes
plt.errorbar(area, lambda_val, 
             xerr=x_errors,             # Incertidumbre en el eje X
             yerr=y_errors,             # Incertidumbre en el eje Y
             fmt='o', color='black', 
             ecolor='red', elinewidth=1.2, capsize=4, capthick=1.2, 
             markersize=5, label='Datos experimentales')

# 4. Dibujar la línea de mejor ajuste usando los puntos calculados
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
