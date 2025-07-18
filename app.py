import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título
st.title("📈 Calculadora de Pendiente Simple")

# Entrada de datos
st.subheader("Ingresa los puntos:")
col1, col2 = st.columns(2)

with col1:
    st.write("**Punto 1**")
    x1 = st.number_input("x1:", value=0.0)
    y1 = st.number_input("y1:", value=0.0)

with col2:
    st.write("**Punto 2**")
    x2 = st.number_input("x2:", value=1.0)
    y2 = st.number_input("y2:", value=2.0)

# Calcular pendiente
if x2 != x1:
    pendiente = (y2 - y1) / (x2 - x1)
    st.success(f"**Pendiente:** {pendiente:.4f}")
    
    # Ecuación de la recta
    b = y1 - pendiente * x1
    st.info(f"**Ecuación de la recta:** y = {pendiente:.4f}x + {b:.4f}")
    
    # Mostrar gráfico
    if st.checkbox("Mostrar gráfico", value=True):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Puntos
        ax.plot([x1, x2], [y1, y2], 'ro-', markersize=10, linewidth=2, label='Recta')
        
        # Etiquetas de puntos
        ax.annotate(f'P1({x1}, {y1})', (x1, y1), xytext=(5, 5), textcoords='offset points')
        ax.annotate(f'P2({x2}, {y2})', (x2, y2), xytext=(5, 5), textcoords='offset points')
        
        # Configuración
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(f'Pendiente = {pendiente:.4f}')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        st.pyplot(fig)
        
    # Información adicional
    st.write("---")
    st.write("**Información:**")
    st.write(f"• Distancia horizontal: {abs(x2 - x1):.4f}")
    st.write(f"• Distancia vertical: {abs(y2 - y1):.4f}")
    st.write(f"• Distancia total: {np.sqrt((x2-x1)**2 + (y2-y1)**2):.4f}")
    
    # Interpretación
    if pendiente > 0:
        st.write("• **Interpretación:** La recta es creciente ↗️")
    elif pendiente < 0:
        st.write("• **Interpretación:** La recta es decreciente ↘️")
    else:
        st.write("• **Interpretación:** La recta es horizontal ➡️")
        
else:
    st.error("Los puntos no pueden tener el mismo valor de x (línea vertical)")

# Fórmula
st.write("---")
st.write("**Fórmula utilizada:**")
st.latex(r"m = \frac{y_2 - y_1}{x_2 - x_1}")