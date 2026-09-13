### 1. Paper: Burke et al. (2004) – *A New Placement Heuristic for the Orthogonal Stock-Cutting Problem*

#### **Método / Funcionamiento**
El artículo aborda el **problema de corte de stock ortogonal bidimensional (2D)** para minimizar la altura total utilizada en una lámina de ancho fijo, permitiendo rotaciones de 90° y empaquetados no guillotinados. Introduce una **heurística dinámica de mejor ajuste (Best-Fit - BF)** que opera en tres fases principales:

1. **Preprocesamiento:** Rotará cualquier rectángulo cuya altura sea mayor que su ancho (garantizando \\(\text{ancho} \ge \text{altura}\\)) y luego ordena toda la lista en **orden decreciente de ancho** (desempatando por altura decreciente). Mantiene el perfil superior (*skyline*) de la lámina mediante un **arreglo lineal** cuyo tamaño equivale al ancho de la lámina, registrando la altura acumulada en cada coordenada \\(x\\).
2. **Fase de Empaquetado (Packing):** Identifica el espacio o "nicho" (*niche*) disponible más bajo en la lámina leyendo el arreglo lineal. Busca en la lista ordenada la pieza que **mejor encaje** en el ancho de ese nicho. Si la pieza no encaja exactamente, aplica una de tres **políticas de colocación en nichos**:
   * **Leftmost (LM):** Alinea la pieza al lado izquierdo del nicho.
   * **Tallest Neighbour (TN):** Coloca la pieza junto al vecino colindante más alto.
   * **Shortest Neighbour (SN):** Coloca la pieza junto al vecino colindante más bajo.
   Si ninguna pieza disponible cabe en el nicho más bajo, dicho espacio se considera desperdicio definitivo (*wastage*) y la altura de ese nicho se eleva automáticamente al nivel de su vecino más bajo.
3. **Postprocesamiento (Tratamiento de "Torres"):** Tras empaquetar todas las piezas, identifica la pieza más alta que esté sobresaliendo verticalmente (creando una "torre"), la remueve, la rota 90° e intenta reinsertarla en una posición inferior. Si esto reduce la altura total del empaquetado, acepta el cambio y repite el proceso hasta que no haya mejoras.

#### **Características**
* **Sin detección de solapamiento:** A diferencia de algoritmos tradicionales, no requiere costosas funciones de verificación de solapamiento (\\(O(1)\\) en la inserción), ya que la pieza siempre se ubica directamente sobre la superficie libre garantizada del *skyline*.
* **Olvído de huecos inviables:** Los huecos donde no cabe ninguna pieza restante se descartan de inmediato, eliminando la necesidad de mantener listas complejas de puntos libres.
* **Combinación de políticas:** Corre el algoritmo bajo las tres políticas (LM, TN, SN) y selecciona la mejor solución final.

#### **Resultados**
* **Eficiencia computacional:** Procesa instancias masivas de **3,152 rectángulos en menos de 2 segundos** (obteniendo una altura de 964 frente al óptimo de 960). En comparación, los enfoques metaheurísticos híbridos (*Genetic Algorithms* GA+BLF y *Simulated Annealing* SA+BLF) requerían entre 26 y 40 semanas de cómputo extrapolado para esa misma instancia.
* **Calidad de solución:** Supera consistentemente a las heurísticas clásicas *Bottom-Left* (BL) y *Bottom-Left-Fill* (BLF) en casi todas las categorías de pruebas de la literatura (Hopper & Turton, Valenzuela & Wang).
* **Escalabilidad:** Para problemas grandes (\\(>50\\) piezas), la heurística Best-Fit supera tanto en calidad como en tiempo a los algoritmos genéticos y recocido simulado.

---

### 2. Paper: Crainic et al. (2008) – *Extreme Point-Based Heuristics for Three-Dimensional Bin Packing*

#### **Método / Funcionamiento**
El estudio aborda el **problema de empaquetado de contenedores tridimensional (3D-BP)** y su variante 2D-BP, buscando empaquetar ortogonalmente un conjunto de ítems en el menor número de contenedores (*bins*) de dimensiones \\(W \times D \times H\\) sin solapamientos. 

1. **Concepto de Puntos Extremos (Extreme Points - EPs):** Extiende la noción de *Corner Points* (CPs). Al colocar un ítem \\(k\\) en \\((x_k, y_k, z_k)\\), se generan nuevos **EPs** proyectando los puntos de sus caras superiores y laterales en dirección a las paredes del bin o sobre las caras de otros ítems ya alojados.
2. **Heurísticas Constructivas Propuetas:**
   * **EP-FFD (Extreme Point First Fit Decreasing):** Ordena los ítems y coloca cada uno en el primer bin y en el primer EP disponible (con coordenadas \\(z, y, x\\) mínimas) donde quepa.
   * **EP-BFD (Extreme Point Best Fit Decreasing):** Evalúa todos los EPs de los bins existentes y coloca el ítem en el EP que maximice una **función de mérito**. Las funciones probadas incluyen: *Free Volume* (FV), *Maximum Packing* (MP), *Level Packing* (LEV) y **Residual Space (RS)**. La función RS minimiza la diferencia entre el tamaño del ítem y el espacio libre disponible en las direcciones X, Y y Z.
3. **Reglas de Ordenamiento por Clusters:** Agrupa los ítems según su área de base o altura en intervalos o *clusters* (\\(\delta \in\\)) antes de ordenar por el segundo criterio, logrando empaquetados mucho más homogéneos.
4. **Heurística Compuesta C-EPBFD:** Ejecuta cíclicamente EP-BFD con función de mérito *Residual Space* variando la partición de *clusters* \\(\delta\\) y selecciona la mejor solución global.

#### **Características**
* **Aprovechamiento de voladizos y huecos interiores:** A diferencia de los *Corner Points*, los EPs permiten colocar ítems debajo de estructuras voladizas o en cavidades formadas por piezas de distintos tamaños, reduciendo significativamente el volumen desperdiciado.
* **Complejidad polinomial:** La actualización de la lista de EPs al insertar un ítem toma tiempo \\(O(n)\\), y los algoritmos EP-FFD y EP-BFD tienen una complejidad total de **\\(O(n^3)\\)**.
* **Independencia del problema:** La regla EP es generalizable a cualquier problema de empaquetado 2D o 3D y puede incorporar restricciones adicionales (como posiciones fijas).

#### **Resultados**
* **Ventaja EP vs. CP:** Usar Puntos Extremos reduce la cantidad de bins necesarios hasta en un **18%** respecto a *Corner Points* en secuencias sin ordenamiento previo.
* **Rendimiento en 3D-BP:** En las instancias estándar de Martello et al., **C-EPBFD supera a todas las heurísticas constructivas previas** (*S-Pack*, *MPV-BS*, *HA*) y al algoritmo exacto *Branch & Bound* (MPV con tiempo límite de 1000s). Obtiene soluciones a menos del **2%** del algoritmo de metaheurística *Guided Local Search* (GLS) y a menos del **5%** de la cota inferior óptima (LB), pero ejecutándose en **menos de 0.5 segundos** (tres órdenes de magnitud más rápido).
* **Rendimiento en 2D-BP:** Aplicado a 10 clases benchmark 2D sin adaptar la formulación, C-EPBFD superó a 7 heurísticas 2D especializadas (FBL, FFF, FBF, AD, FC, KP, HBM), reduciendo el número total de bins entre un **9% y un 15%**.

---

### 3. Paper: Chazelle (1983) – *The bottom-left bin packing heuristic: An efficient implementation*

#### **Método / Funcionamiento**
Describe e implementa las heurísticas fundamentales de empaquetado 2D **Bottom-Left (BL)** y **Bottom-Left-Fill (BLF)**:

1. **Bottom-Left (BL):** Recibe una secuencia ordenada de rectángulos. Cada pieza se posiciona inicialmente en la esquina superior derecha del contenedor y se desliza de forma continua hacia abajo y hacia la izquierda tanto como sea posible hasta chocar con el borde o con otras piezas.
2. **Bottom-Left-Fill (BLF):** Mantiene un registro ordenado de todos los puntos y nichos libres en el contenedor. Al colocar una pieza, evalúa los puntos en orden de abajo hacia arriba y de izquierda a derecha, lo que le permite **rellenar huecos interiores** dejados por piezas anteriores si una pieza posterior encaja perfectamente.

#### **Características**
* **Complejidad computacional:** Chazelle establece una implementación eficiente para BL con complejidad **\\(O(N^2)\\)**. En cambio, BLF requiere **\\(O(N^3)\\)** debido a la búsqueda continua de nichos interiores y la costosa prueba de solapamiento acumulativa contra todas las piezas previas.
* **Sensibilidad al orden de entrada:** La calidad del empaquetado depende drásticamente de la secuencia inicial de las piezas.
* **Inconveniente de BL:** Puede encerrar "huecos" donde no caben piezas inmediatas, los cuales quedan inutilizados para el resto del proceso, generando pérdidas de corte (*trim loss*).

#### **Resultados**
* **BLF vs. BL:** BLF supera a BL en calidad y densidad de empaquetado hasta en un **25%** gracias a su capacidad de rellenar cavidades interiores.
* **Preordenamiento:** Ordenar previamente las piezas por ancho o altura decreciente mejora el desempeño de ambas heurísticas hasta en un **10%** respecto a listas aleatorias.
* **Comparativa global:** Aunque BLF fue durante años el estándar de referencia, es superado tanto en calidad como en tiempo de ejecución por las heurísticas de *Best-Fit* (Burke et al.) y *Puntos Extremos* (Crainic et al.).

---
