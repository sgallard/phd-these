Reporte Técnico: Estado del Arte en Problemas de Empaquetado Bidimensional (Survey de Lodi et al., 2002)

1. Introducción y Taxonomía de los Problemas de Corte y Empaque

La optimización del empaquetado bidimensional constituye un pilar estratégico en la investigación operativa aplicada a procesos industriales, particularmente en sectores como la madera, el vidrio y la logística. La relevancia de este campo radica en la reducción directa de costos operativos mediante la minimización del desperdicio de materia prima. La clasificación taxonómica propuesta por Lodi et al. (2002) es esencial para sistematizar la resolución de estos problemas, empleando a menudo la notación de tres campos (\alpha | \beta | \gamma) para distinguir entre las restricciones de los ítems, las de los contenedores y los objetivos de optimización.

Dentro de este marco, se definen formalmente dos problemas fundamentales:

* Two-Dimensional Bin Packing Problem (2BP): Requiere asignar un conjunto de n ítems rectangulares a un número ilimitado de contenedores (bins) idénticos de dimensiones W \times H, minimizando el número total de contenedores utilizados.
* Two-Dimensional Strip Packing Problem (2SP): Utiliza un único contenedor de ancho fijo W y altura infinita (strip). El objetivo es posicionar todos los ítems minimizando la altura total (H_{total}) requerida.

El impacto de las restricciones físicas es determinante: la orientación fija no es solo una simplificación matemática, sino un requisito físico ineludible en industrias como la maderera o textil, donde la "veta" (grain) o los patrones decorativos impiden la rotación de las piezas. De igual forma, los cortes de guillotina (cortes ortogonales de borde a borde) simplifican la automatización del corte pero restringen drásticamente el espacio de soluciones factibles. Estas sutilezas estructurales demandan una transición hacia modelos matemáticos de alta precisión.

2. Modelado Matemático y Representación Estructural

Garantizar la factibilidad de las soluciones en sistemas automatizados exige el uso de Programación Lineal Entera (ILP) y representaciones gráficas robustas que eviten el solapamiento geométrico.

Formulaciones de Programación Lineal

El modelo de Gilmore-Gomory (2BP-GG) es el referente histórico, basado en un enfoque de generación de columnas donde cada variable x_j representa un patrón de empaque completo. Dada la explosión combinatoria de patrones posibles, su resolución requiere un problema esclavo de tipo knapsack bidimensional. Alternativamente, las formulaciones de coordenadas discretas (Beasley; Hadjiconstantinou y Christofides) utilizan variables x_{ipq} para situar la esquina inferior izquierda del ítem i en las coordenadas (p, q), asegurando la integridad espacial mediante restricciones explícitas de no superposición.

Teoría de Grafos y Factibilidad

El enfoque de Fekete y Schepers aporta una validación elegante mediante grafos de intervalos. Un patrón de empaque se representa mediante dos grafos, G_w y G_h, que modelan las proyecciones horizontales y verticales de los ítems. La condición necesaria y suficiente para un patrón geométrico válido es que E_w \cap E_h = \emptyset. Esto implica que, si dos ítems solapan sus proyecciones en el eje horizontal, deben estar separados obligatoriamente en el vertical.

Dada la naturaleza fuertemente NP-hard de estos modelos generales, la carga computacional motiva el uso de simplificaciones estructurales como el empaquetado por niveles, discutido a continuación.

3. Empaquetado por Niveles (Level Packing) y Modelos Polinomiales

El empaquetado por niveles (level packing) simplifica la colocación organizando los ítems en filas horizontales, donde la altura de cada nivel viene determinada por su ítem más alto. Esta estructura es predilecta en la industria por su facilidad de implementación en líneas de producción automatizadas.

Lodi et al. formalizan este enfoque mediante modelos ILP de tamaño polinomial para 2LBP y 2LSP. Asumiendo que los ítems están ordenados por altura no creciente (h_1 \ge h_2 \ge \dots \ge h_n), el modelo para 2LBP utiliza variables binarias y_i para indicar si el ítem i inicializa un nivel y x_{ij} para indicar si el ítem j se asigna al nivel i:

 \sum_{i=1}^{j-1} x_{ij} + y_j = 1 \quad (j = 1, \dots, n)   \sum_{j=i+1}^{n} w_j x_{ij} \le (W - w_i)y_i \quad (i = 1, \dots, n-1) 

Esta restricción estructural reduce significativamente el espacio de búsqueda. Aunque el empaquetado por niveles suele suboptimizar el área total frente al empaquetado general, su eficiencia computacional lo convierte en la base fundamental para el desarrollo de algoritmos de aproximación.

4. Algoritmos de Aproximación y Heurísticas Constructivas

En contextos de tiempo real o con grandes volúmenes de ítems, las heurísticas off-line son indispensables para obtener soluciones de alta calidad de forma casi instantánea.

Comparativa de Algoritmos para Strip Packing (2SP)

Los algoritmos clásicos operan bajo el principio de ordenar los ítems por altura no creciente antes del empaquetado:

Algoritmo	Mecanismo de Asignación	Cota de Peor Caso (Asymptotic)
NFDH	Abre un nuevo nivel si el ítem no cabe en el actual.	NFDH(I) \le 2 OPT(I) + 1
FFDH	Coloca el ítem en el primer nivel existente donde quepa.	FFDH(I) \le 1.7 OPT(I) + 1
BFDH	Elige el nivel que maximiza la ocupación del ancho residual.	Superior en desempeño práctico
BL (Bottom-Left)	Desplaza el ítem hacia abajo y hacia la izquierda.	BL(I) \le 3 OPT(I)

Algoritmos Híbridos para 2BP

El algoritmo Hybrid First-Fit (HFF) ejemplifica la potencia de la descomposición 2D en 1D: primero genera niveles mediante FFDH y luego empaqueta dichos niveles en contenedores usando el algoritmo First-Fit unidimensional. La literatura establece para este método una cota de rendimiento de HFF(I) \le \frac{17}{8} OPT(I) + 5, una métrica de alta fiabilidad para el analista. No obstante, para superar estas cotas rígidas, es necesario recurrir a marcos metaheurísticos.

5. Frameworks Metaheurísticos y Búsqueda Local

Las metaheurísticas permiten explorar el espacio de soluciones de forma estocástica o dirigida, escapando de los óptimos locales mediante mecanismos de aceptación de soluciones inferiores.

* Simulated Annealing (Dowsland): Utiliza una función objetivo basada en el área de solapamiento total para guiar la transición de estados inviables a configuraciones factibles de menor altura.
* Algoritmos Genéticos (Jakobs): Codifica las soluciones como permutaciones de ítems que luego son procesadas por un decodificador tipo Bottom-Left.
* Guided Local Search (Færø et al.): Implementa penalizaciones dinámicas sobre características de la solución (como el solapamiento) para diversificar la búsqueda.

El Unified Framework de Lodi, Martello y Vigo, basado en Búsqueda Tabú, destaca por su versatilidad. Su núcleo es un vecindario de recombinación de k contenedores: se seleccionan k contenedores para intentar reubicar sus ítems en otros espacios y así liberar un contenedor objetivo. La eficacia de estas metaheurísticas se valida sistemáticamente mediante su comparación con las cotas inferiores teóricas.

6. Teoría de Cotas Inferiores (Lower Bounds)

Las cotas inferiores son fundamentales para la poda en algoritmos exactos y para certificar la calidad de las heurísticas.

Se distinguen las cotas geométricas como L_{bg} y L_{sg} (basadas puramente en el área) de las cotas especializadas. Entre estas, L_{b2} es de especial relevancia para 2BP; se define como el máximo entre B_W(q) y B_H(q), considerando incompatibilidades dimensionales que impiden que los ítems se coloquen uno al lado del otro. Es matemáticamente superior, pues L_{b2} domina a L_{bg} y ofrece una mayor precisión con una complejidad de O(n^2).

Un avance teórico mayor son las Dual Feasible Functions (DFF) de Fekete y Schepers. Estas funciones actúan como una "escala conservadora", transformando las dimensiones de los ítems de modo que su consumo de recursos (ancho o alto) sea representado de forma más estricta que el simple valor físico. Esto permite capturar la naturaleza discreta del problema, generando cotas mucho más ajustadas que guían los métodos de resolución exacta.

7. Métodos de Resolución Exacta y Conclusiones

Los algoritmos exactos proporcionan el estándar de oro para la optimización, resolviendo instancias de tamaño moderado mediante esquemas enumerativos avanzados.

Para el problema 2SP, se emplea un Branch-and-Bound basado en "puntos esquina" (corner points). El número de posiciones candidatas para colocar un nuevo ítem es finito y está acotado por k \le |I| + 1, donde |I| es el número de ítems ya colocados. En 2BP, se utiliza un esquema de ramificación de dos niveles: el árbol externo gestiona la asignación de ítems a contenedores, mientras que un árbol interno (o un procedimiento de verificación) valida la factibilidad del patrón dentro del contenedor. Este proceso se apoya en el principio left-most downward, que garantiza que siempre existe una solución óptima donde cada ítem está desplazado tanto como es posible hacia la esquina inferior izquierda.

Síntesis de Hallazgos Críticos:

1. Dominio de la Complejidad: La naturaleza fuertemente NP-hard de los problemas 2BP y 2SP ratifica que la combinación de metaheurísticas con cotas inferiores potentes (como las basadas en DFF) es la estrategia más robusta para la industria.
2. Rendimiento del Empaquetado Híbrido: El uso de algoritmos de dos fases, como HFF, ofrece garantías teóricas sólidas (HFF \le \frac{17}{8} OPT + 5), permitiendo un control predecible sobre la eficiencia del material.
3. Integración de Grafos y Búsqueda Binaria: La resolución exacta moderna ha evolucionado hacia la integración de modelos de grafos de intervalos con búsqueda binaria para determinar dimensiones críticas, optimizando el uso de puntos esquina para reducir el factor de ramificación. En resumen, el equilibrio entre el rigor del modelo y la agilidad de la búsqueda local define el éxito en la optimización del empaquetado bidimensional.
