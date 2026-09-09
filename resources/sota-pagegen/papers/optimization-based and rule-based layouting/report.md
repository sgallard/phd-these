### 1. **GRIDS: Interactive Layout Design with Integer Programming**
*(Dayama, Todi, Saarelainen & Oulasvirta, CHI 2020)*

* **Objetivo y Contexto**: Presenta un enfoque computacional interactivo para respaldar las etapas tempranas de diseño de interfaces de usuario (GUIs) durante el bocetado y wireframing. Busca asistir la creatividad humana mediante sugerencias en tiempo real, permitiendo explorar soluciones iniciales, completar diagramaciones parciales y buscar alternativas locales.
* **Metodología y Formulación Matemática**:
  * **Programación Lineal Entera Mixta (MILP)**: Combina variables continuas para definir la posición y dimensiones físicas de cada elemento (\\(L_e, R_e, T_e, B_e, W_e, H_e\\)) con variables binarias/discretas para definir el ordenamiento espacial relativo.
  * **Independencia del Lienzo (Canvas-Independent)**: En lugar de discretizar el lienzo en píxeles (lo que requeriría millones de variables), define la relación espacial mediante variables binarias de ordenamiento relativo: \\(\Gamma_{e\bar{e}}\\) (indica si el elemento \\(e\\) está ubicado arriba de \\(\bar{e}\\)) y \\(\Pi_{e\bar{e}}\\) (indica si \\(e\\) está a la izquierda de \\(\bar{e}\\)). Esto reduce drásticamente la complejidad matemática a solo \\(O(n^2)\\) respecto al número de elementos \\(n\\) (ej. 110 variables discretas y 20 continuas para 5 elementos, frente a ~2.4 millones en enfoques discretos).
  * **Empaquetamiento y Restricciones Estructuradas**: Garantiza matemáticamente un empaquetamiento estricto (*packing*), asegurando que ningún elemento se solape ni sobresalga del lienzo.
  * **Alineación Global (*Aligned Groups*)**: Introduce el concepto de *Alignment Groups* (Left-Group \\(LG\\), Right-Group \\(RG\\), Top-Group \\(TG\\), Bottom-Group \\(BG\\)) para agrupar bordes que comparten líneas de grilla virtuales. Minimizar la cantidad total de líneas de grilla utilizadas optimiza directamente la alineación del diseño.
  * **Contorno Rectangular (*Rectangular Outline*)**: Define el rectángulo contenedor mínimo (*Smallest Rectangular Outline*, SRO) e introduce funciones de penalización/recompensa para forzar a que el borde externo del conjunto de elementos adopte un contorno rectangular.
  * **Ubicación Preferencial y Bloqueos**: Permite fijar elementos en coordenadas exactas (*locking*), definir pertenencia jerárquica (cabeceras, barras laterales) o minimizar distancias de recorrido funcional.
  * **Diversificación Controlada del Espacio de Diseño**: Calcula los límites extremos (\\(\Gamma_{max}, \Gamma_{min}, \Pi_{max}, \Pi_{min}\\)) para construir un polígono en un espacio 2D de disimilitud. Esto permite muestrear sistemáticamente el espacio de diseño y ofrecer alternativas óptimas o cercanas al óptimo pero visualmente diversas.
* **Evaluación y Desempeño**:
  * *Estudio de Calidad Percibida* (\\(N=13\\)): Demostró una correlación estadísticamente significativa (\\(p < 0.0001\\)) entre el puntaje de optimización MILP y la calificación estética otorgada por usuarios.
  * *Estudio con Diseñadores Profesionales* (\\(N=16\\)): Los diseñadores integraron las sugerencias del optimizador en el 44.17% de sus diseños finales, destacando su utilidad para destrabar la exploración creativa temprana. Computa 5 sugerencias bien estructuradas en menos de 2 segundos para 5 elementos.

---

### 2. **Adaptive Grid-Based Document Layout**
*(Jacobs, Li, Schrier, Bargeron & Salesin, ACM TOG / SIGGRAPH 2003)*

* **Objetivo y Contexto**: Presenta un marco seminal para la diagramación automática y dinámica de documentos complejos y multipágina adaptados a múltiples formatos de pantalla o medios de despliegue.
* **Metodología y Formulación**:
  * **Resolución de Restricciones (*Constraint Solving*)**: Utiliza solucionadores de restricciones aritméticas y lineales para ajustar dinámicamente el contenido del documento según las dimensiones disponibles del lienzo.
  * **Adaptación Jerárquica**: Define una jerarquía de restricciones duras (*hard constraints*, como límites físicos y no superposición) y blandas (*soft constraints*, como preferencias de alineación o proporciones) para reorganizar el flujo de texto e imágenes manteniendo la estructura del grid.
* **Estado de la Fuente**:
  * *Nota de precisión sobre la fuente*: El documento cargado en el cuaderno (`adaptive-grid-based.pdf`) contiene problemas de codificación de fuentes en su capa de texto PDF. No obstante, sus fundamentos técnicos y su contribución sobre la diagramación adaptativa estructurada mediante *constraint solvers* y grillas dinámicas se hallan documentados y citados en los otros estudios del corpus.

---

### 3. **LayoutRectifier: An Optimization-based Post-processing for Graphic Design Layout Generation**
*(Shen, Shamir & Igarashi, Computer Graphics Forum / Pacific Graphics 2025)*

* **Objetivo y Contexto**: Propone un método de posprocesamiento basado en optimización que opera sin necesidad de entrenamiento (*training-free*). Su objetivo es rectificar automáticamente las fallas comunes (desalineación, solapamientos indeseados y contención insatisfecha) que generan los modelos profundos de generación de diagramaciones (como VAE, GAN, Transformers o modelos de Difusión).
* **Metodología en Dos Etapas Alternadas**:
  1. **Inferencia de Grilla Exemplar y Extracción de Alineación**:
     * Extrae un sistema de grillas de referencia (\\(G_e\\)) recuperando esquemas de diagramación ejemplares del conjunto de entrenamiento mediante similitud de IoU.
     * Detecta relaciones intrínsecas de alineación (\\(\mathcal{R}\\)) entre pares de elementos aplicando principios Gestalt de continuidad perceptual (utilizando un umbral angular \\(< 18^\circ\\) entre puntos finales).
  2. **Etapa A: Búsqueda Discreta y Snapping (*Search-and-Snap*)**:
     * Evalúa opciones discretas de ajuste (ajuste por vértices y por bordes) para encajar los elementos en las líneas de la grilla de referencia \\(G_e\\), minimizando la función de costo global de alineación \\(E_{all}\\).
     * Para tareas de diseño conscientes del contenido (*content-aware*), integra un término de oclusión (\\(E_{occ}\\)) basado en mapas de saliencia para evitar tapar zonas clave de las imágenes de fondo.
  3. **Etapa B: Actualización Continua vía Función Difierenciable de Contención (*Box Containment Function*)**:
     * Resuelve el problema de la "deficiencia de gradiente" (*gradient deficiency*) de las métricas IoU o DIoU convencionales (las cuales no producen gradientes útiles cuando dos elementos están totalmente separados o completamente contenidos).
     * Define la métrica IoCA (*Intersection over Child Area* = \\(|b_c \cap b_p| / |b_c|\\)) e introduce funciones diferenciables de contención:
       * **Contención Positiva** (\\(E_{contain}^+\\)): Fuerza a elementos secundarios (como *text-over-image*) a quedar totalmente englobados dentro del área de elementos primarios (como *image*).
       * **Contención Negativa** (\\(E_{contain}^-\\)): Expulsa y elimina el solapamiento entre elementos donde la superposición está prohibida (\\(E_{ove}\\)).
     * Optimiza continuamente la posición y tamaño (\\(x, y, w, h\\)) mediante el algoritmo Adam durante 100 iteraciones, preservando la relación de aspecto (\\(E_{aspect}\\)) y el área original (\\(E_{size}\\)). El flujo alterna entre la Etapa A y B por \\(T=5\\) iteraciones.
* **Evaluación y Resultados**:
  * Evaluado en conjuntos de datos *content-agnostic* (PubLayNet para documentos, Magazine para revistas) y *content-aware* (CGL para afiches/posters) sobre modelos generativos como LayoutGAN++, LayoutDM, BLT, LayoutFormer++ y RALF.
  * Procesa rectificaciones en tiempos muy reducidos (\\(0.22\text{ s}\\) a \\(0.71\text{ s}\\) por layout), superando cuantitativamente a métodos de refinamiento basados en LLMs o recristalización en espacio latente (como CLG o Simulated Annealing) sin alterar la estructura original del diseño.

---

### 4. **Síntesis Comparativa: Puntos en Común y Lecciones Extraíbles**

#### **Puntos en Común**
* **La Grilla como Estructura Canónica**: Todos los artículos parten de la premisa de que los sistemas de grillas son la base espacial fundamental del diseño gráfico para garantizar orden visual, alineación y empaquetamiento estético.
* **Uso de Optimización Matemática vs. Reglas Heurísticas Puramente Rígidas**: Superan el uso de plantillas estáticas o heurísticas manuales utilizando solucionadores matemáticos formales (Programación Lineal Entera Mixta en **GRIDS**, Solucionadores de Restricciones en **Jacobs et al.** y Optimización Difierenciable en Dos Etapas en **LayoutRectifier**).
* **Formalización de Criterios Perceptuales y de Gestalt**: Transcriben reglas estéticas de diseño (alineación de bordes, contorno rectangular exterior, proximidad y no-solapamiento) a funciones de costo o restricciones numéricas precisas.

#### **Lecciones y Aprendizajes Extraíbles**
1. **Modelación Independiente de la Escala del Lienzo**: La formulación de **GRIDS** demuestra que definir las posiciones mediante ordenamientos relativos binarios (\\(\Gamma, \Pi\\)) en lugar de coordinar píxeles individuales reduce la complejidad computacional en varios órdenes de magnitud, permitiendo la generación e interacción en tiempo real.
2. **Sinergia Híbrida (Deep Learning + Optimización Determinista)**: **LayoutRectifier** evidencia que los modelos generativos profundos (Diffusion, Transformers, GANs) son excelentes para proponer distribuciones variadas, pero fallan en la precisión sintáctica fina (alineaciones perfectas o bordes exactos). Un post-procesamiento determinista guiado por grillas corrige estas imprecisiones sin perder la diversidad generada.
3. **Superación de la Deficiencia de Gradiente**: Para ajustar layouts continuamente mediante algoritmos basados en gradiente, las funciones IoU convencionales resultan insuficientes cuando las cajas no se tocan. Desarrollar funciones de costo basadas en distancias ponderadas y proporciones del área del elemento secundario (IoCA) resulta crítico para lograr convergencia matemática limpia.
4. **Diseño Mixto (Mixed-Initiative)**: Los métodos matemáticos exactos no deben restringirse a entregar una única respuesta óptima rígida; deben permitir la exploración de espacios de soluciones diversos y soportar la adición de restricciones en vivo (bloqueos y preferencias) por parte del diseñador humano.