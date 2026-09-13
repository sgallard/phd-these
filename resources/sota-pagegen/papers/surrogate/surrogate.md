Reporte Técnico: Modelos Sustitutos para Optimización Combinatoria y AutoML

1. Revisión y Taxonomía de SAEAs en Optimización Combinatoria Costosa (Liu et al., 2024)

En el dominio de la computación avanzada, los Problemas de Optimización Combinatoria Costosa (ECOPs) representan un desafío estratégico de primer orden. A diferencia de la optimización continua, donde la suavidad del paisaje permite el uso de gradientes, los ECOPs se caracterizan por una alta rugosidad (ruggedness) del paisaje de fitness y una epistasis elevada inducida por estructuras discretas. En estos escenarios, la evaluación de una sola solución puede implicar simulaciones de alta fidelidad o entrenamientos de modelos de "caja negra" que consumen horas de CPU/GPU. Ante presupuestos computacionales finitos, el despliegue de modelos sustitutos (surrogates) es una necesidad crítica para realizar una búsqueda inteligente sin agotar los recursos del sistema.

1.1. Formulación Matemática y Naturaleza de los ECOPs

Basándonos en la taxonomía de Liu et al., un problema de optimización combinatoria se define formalmente como la búsqueda del valor óptimo dentro de un conjunto finito pero masivo de soluciones candidatas:

\min f(\mathbf{x}) \text{s.t. } g(\mathbf{x}) \leq 0, \mathbf{x} \in X

Donde f(\mathbf{x}) es la función objetivo, \mathbf{x} = [x_1, \dots, x_n] representa un vector de n variables de decisión discretas y X es el espacio de búsqueda. La complejidad NP-hard de estos problemas emana de la naturaleza de sus estructuras de datos:

* Ordinales y Binarias: Comunes en selección de características (Feature Selection) o secuencias de permutación (TSP).
* Árboles y Grafos: Estructuras complejas utilizadas en el diseño de arquitecturas neuronales (NAS) o logística de redes. Esta discontinuidad estructural impide el uso de operadores lineales, exigiendo que el modelo sustituto sea capaz de mapear relaciones no euclidianas de manera eficiente.

1.2. Taxonomía de Estrategias de Búsqueda (Search Strategies)

La navegación eficiente en espacios ECOP requiere una integración sinérgica de diversas estrategias de búsqueda:

1. Globales: Utilizan operadores evolutivos (cruzamiento y mutación), algoritmos de enjambre como el PSO discreto y modelos distribuidos como los Algoritmos de Estimación de Distribución (EDA). Destacan los modelos de Mallows para la exploración efectiva en espacios basados en permutaciones.
2. Locales: Se enfocan en la explotación intensiva de vecindarios promisorios mediante operadores de expansión como 2-opt/k-opt, desplazamientos y algoritmos de búsqueda local adaptativa (ALNS).
3. Híbridas: Implementadas frecuentemente en algoritmos meméticos, donde se concatenan fases de exploración global con refinamientos locales para maximizar la calidad de la solución final.
4. Basadas en Aprendizaje: Representan la frontera actual, integrando modelos como RankNet para aprender el orden de los individuos en la selección evolutiva, Q-learning para la selección dinámica de operadores y modelos de Optimización Combinatoria Neuronal (NCO) para la aproximación directa de soluciones óptimas.

1.3. Evaluación Basada en Modelos Sustitutos (Surrogate-based Evaluation)

La selección del modelo es vital para equilibrar el sesgo inductivo y la varianza. La siguiente tabla resume la taxonomía técnica:

Tipo de Modelo	Ejemplos Técnicos	Diferenciador Clave
Ingenuo	KNN, Regresión Lineal	Baja latencia; útil en fases iniciales con datos mínimos.
Discreto	Random Forest (RF)	Manejo nativo de discontinuidades; partición recursiva del espacio.
Similitud	Kriging (GP), RBFN	Proporciona una medida de incertidumbre (Standard Error) esencial para el Expected Improvement.
Mapeo	Autoencoders, LSTM	Proyecta estructuras complejas (grafos) en espacios latentes continuos transitables.
Simulación	Multi-fidelity Models	Combina aproximaciones rápidas con evaluaciones costosas de alta fidelidad.

La Construcción del modelo puede ser individual o mediante ensembles para mitigar errores de generalización. Su Gestión puede ser Online (actualización dinámica durante la búsqueda mediante criterios de infill) u Offline, dependiendo de la disponibilidad de datos históricos.

1.4. Retos Futuros y Conclusión de Sección

Cinco retos definen la agenda de investigación: la adaptabilidad a estructuras no ordinales, la gestión de la alta dimensionalidad, la robustez frente al ruido en evaluaciones estocásticas, la eficiencia en la transferencia de aprendizaje y la integración de conocimiento experto en el surrogate. Esta evolución hacia arquitecturas de aprendizaje profundo abre el camino para el uso de Transformers como aproximadores de alta fidelidad, como se detalla a continuación.

2. Transformers como Modelos Sustitutos para Programación Genética en AutoML (Teixeira & Pappa, 2025)

En AutoML, el problema CASH (Combined Algorithm Selection and Hyperparameter optimization) es uno de los procesos más costosos. Teixeira & Pappa proponen un cambio de paradigma: utilizar modelos de lenguaje para predecir la calidad relativa de pipelines de Scikit-Learn, eliminando la necesidad de entrenamientos iterativos costosos.

2.1. Formulación CASH y Gramática GGP

El problema CASH se define formalmente como la búsqueda de un algoritmo A^* y una configuración \lambda^* que maximicen la ganancia F (frecuentemente el F-measure):

A^*_{\lambda^*} = \text{argmax}_{A^{(j)} \in \mathcal{A}, \lambda \in \Lambda^{(i)}} \frac{1}{k} \sum_{i=1}^k F(A^{(j)}_\lambda, D_{train}^{(i)}, D_{valid}^{(i)})

Es fundamental notar que, a diferencia de la definición tradicional de minimización de pérdida, este trabajo lo aborda como un problema de maximización de desempeño. Para asegurar la validez estructural de los pipelines, se emplea una Gramática GGP (Grammar-based Genetic Programming) con 38 reglas BNF, que restringen la combinación de preprocesamiento y clasificación.

2.2. Paradigma de Aprendizaje de Relaciones Binarias y Arquitectura del Transformer

En lugar de realizar una regresión para predecir el valor exacto de fitness (sujeto a alta propagación de error), se migra al aprendizaje de relaciones binarias. El surrogate aprende la relación f(p_i) \geq f(p_j), actuando como un filtro de selección robusto. Esto es significativamente más tolerante al ruido: una pequeña desviación numérica no altera el ranking en un torneo evolutivo.

La arquitectura se basa en un Transformer Encoder con:

* Tokenización WordPiece: Vocabulario de 301 tokens, entrenado específicamente en pipelines del dataset wine-quality-red, debido a que la gramática incluye terminales dependientes del número de atributos del dataset.
* Especificaciones: 4 capas de atención, d\_model=128 y embeddings posicionales.

Se prefiere el Encoder sobre el Decoder debido a su naturaleza de atención bidireccional, necesaria para comprender el contexto completo de dos secuencias de pipelines comparadas simultáneamente, a diferencia del enfoque autorregresivo limitado de los Decoders.

2.3. Algoritmo GGPEnc y Resultados Empíricos

El framework GGPEnc integra el Transformer en el proceso de selección de torneos. Los resultados demuestran una correlación de Spearman superior a 0.92, con una aceleración que alcanza 285 veces en los casos más extremos (y consistentemente por encima de 235x). Además, la capacidad de fine-tuning en solo 30 épocas permite transferir el conocimiento a nuevos datasets con una degradación mínima de la precisión, validando la eficiencia de los modelos de "Deep Mapping" frente a métodos tradicionales.

3. Algoritmo Evolutivo Híbrido con Extreme Learning Machine (Guo et al.)

El problema de localización de instalaciones capacitadas en dos etapas (TSCFLP) es un pilar de la logística industrial que busca minimizar costos fijos y de transporte en redes de suministro complejas (Plantas \rightarrow Depósitos \rightarrow Clientes).

3.1. Formulación del Problema TSCFLP como MILP

El TSCFLP se define como un modelo de Programación Lineal Entera Mixta (MILP). Su complejidad reside en las restricciones de capacidad de las plantas (b_i) y depósitos (p_j), donde cada evaluación de una configuración binaria (abrir/cerrar) requiere resolver un subproblema de flujo de costo mínimo.

3.2. Arquitectura de Extreme Learning Machine (ELM)

Para acelerar este ciclo, se implementan Extreme Learning Machines (ELM) basadas en SLFNs (Single hidden-layer feed-forward neural networks). La ventaja crítica de la ELM es que evita el entrenamiento iterativo por gradiente descendente y, por ende, el riesgo de desvanecimiento del gradiente (vanishing gradient).

La convergencia es analítica, determinando los pesos de salida \beta^* mediante la inversión pseudo-inversa de Moore-Penrose: \beta^* = H^\dagger T Donde H es la matriz de salida de la capa oculta (con pesos de entrada aleatorios) y T es la matriz de objetivos (target). Esta velocidad de entrenamiento permite un reentrenamiento online frecuente durante el proceso evolutivo.

3.3. Framework HEA/FA y Resultados

El framework integra:

1. Inicialización vía CBR (Cost-Benefit Ranking): Prioriza instalaciones con menor ratio costo/capacidad.
2. Heurística MIH (Modified and Improved Heuristic): Asegura la factibilidad de las soluciones binarias basándose en el teorema de equilibrio de flujos (\sum x_{ij} = \sum s_{jk} = \sum q_k).
3. Operador CX Adaptado: Preserva los alelos de los padres en soluciones binarias.

En instancias de 50 y 100 plantas, el algoritmo redujo los tiempos de ejecución de GA estándar (que oscilaban entre 236s y 2784s) a escalas industriales razonables, manteniendo métricas de RPD competitivas y una convergencia estable.

4. Análisis Comparativo Sintético

Las aproximaciones analizadas convergen en el uso de modelos de bajo costo para evitar la resolución de problemas internos NP-hard (como el entrenamiento de redes en AutoML o el flujo de costo mínimo en TSCFLP). La integración de surrogates permite democratizar la optimización de alta complejidad, permitiendo su ejecución en hardware convencional.

4.1. Cuadro Comparativo de Aproximaciones Técnicas

Criterio	Survey (Liu et al.)	Transformer (Teixeira)	ELM (Guo et al.)
Representación del Dominio	Discreto (ordinal, árbol, grafo)	Pipelines (Árboles de sintaxis)	Binario (Apertura de nodos)
Tipo de Surrogate	Taxonomía General (GP, RF, RFN)	Transformer Encoder	ELM / SLFN
Estrategia de Manejo	Online / Infill dinámico	Fine-tuning / Transfer	Retraining dinámico (10% Elites)
Reducción de Tiempo	Dependiente del modelo	Hasta 285x	De ~46 min a escalas aceptables

Como reflexión final, la tendencia hacia el Binary Relation Learning y el Deep Mapping marca un hito en la optimización: el rol del modelo sustituto ha evolucionado de un simple estimador de valores a un filtro de selección inteligente. Esta transición es fundamental para manejar el ruido inherente a las funciones objetivo industriales y representa el futuro de la arquitectura de modelos de optimización autónomos.
