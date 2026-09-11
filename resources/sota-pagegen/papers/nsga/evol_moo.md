### Reporte Técnico 1: Deb et al. (2002) — NSGA-II

#### Contexto y Propósito
El artículo de Kalyanmoy Deb y colaboradores introduce el **Algoritmo Genético de Ordenamiento No Dominado II (NSGA-II)**. Surgió como respuesta a las limitaciones identificadas en los algoritmos evolutivos multiobjetivo (MOEAs) de primera generación —como el NSGA original, MOGA y NPGA—, los cuales padecían tres problemas principales: alta complejidad computacional \\(O(M N^3)\\), ausencia de un mecanismo explícito de elitismo y la necesidad de especificar parámetros subjetivos de nicho (\\(\sigma_{share}\\)) para preservar la diversidad.

---

#### Métodos y Mecanismos Principales
1. **Algoritmo de Ordenamiento No Dominado Rápido (*Fast Nondominated Sort*)**:
   - Para reducir la complejidad computacional, el algoritmo calcula dos atributos para cada solución \\(p\\): el número de soluciones que la dominan (\\(n_p\\)) y el conjunto de soluciones dominadas por ella (\\(S_p\\)).
   - Esto permite identificar el primer frente no dominado en \\(O(M N^2)\\) operaciones. Las soluciones identificadas se descuentan temporalmente y el proceso se repite con las soluciones restantes para formar los frentes subsiguientes (\\(F_1, F_2, \dots\\)). La complejidad total del ciclo disminuye de \\(O(M N^3)\\) a \\(O(M N^2)\\), a costa de aumentar el requerimiento de memoria a \\(O(N^2)\\).

2. **Preservación de Diversidad mediante Distancia de Hacinamiento (*Crowding Distance*)**:
   - Reemplaza la función de compartición (*sharing function*), eliminando la dependencia del parámetro \\(\sigma_{share}\\) definido por el usuario.
   - La distancia de hacinamiento mide la densidad de soluciones alrededor de un punto mediante el cálculo del perímetro del cuboide formado por sus vecinos más cercanos a lo largo de cada objetivo.
   - Los puntos extremos de la frontera reciben un valor infinito de distancia. La complejidad del cálculo de la distancia de hacinamiento por frente es \\(O(M N \log N)\\), determinada por el ordenamiento por cada función objetivo.

3. **Operador de Comparación Hacinada (*Crowded-Comparison Operator* \\(\prec_n\\))**:
   - Define un orden parcial entre dos soluciones \\(i\\) y \\(j\\) basándose en dos atributos: rango de no dominancia (\\(i_{rank}\\)) y distancia de hacinamiento (\\(i_{distance}\\)).
   - Una solución \\(i\\) prevalece (\\(i \prec_n j\\)) si \\(i_{rank} < j_{rank}\\) (pertenece a un mejor frente) o, en caso de estar en el mismo frente (\\(i_{rank} = j_{rank}\\)), si reside en una región menos hacinada (\\(i_{distance} > j_{distance}\\)).

4. **Mecanismo de Elitismo**:
   - En cada generación \\(t\\), se combinan la población padre \\(P_t\\) y la descendencia \\(Q_t\\) para formar una población extendida \\(R_t\\) de tamaño \\(2N\\).
   - \\(R_t\\) se clasifica en frentes no dominados. La nueva población \\(P_{t+1}\\) se llena iterativamente con los mejores frentes.
   - Si el último frente no puede acomodarse completamente sin exceder el tamaño \\(N\\), sus miembros se ordenan en orden descendente según \\(\prec_n\\) y se seleccionan únicamente las soluciones necesarias para completar las \\(N\\) vacantes.

5. **Manejo de Restricciones (*Constrained NSGA-II*)**:
   - Modifica la definición de dominancia mediante el concepto de **dominancia restringida** (*constrained-domination*), aplicable mediante selección por torneo sin requerir parámetros de penalización.
   - Una solución \\(i\\) domina restringidamente a \\(j\\) si: 
     1. \\(i\\) es factible y \\(j\\) no lo es;
     2. Ambas son no factibles, pero \\(i\\) presenta una menor violación total de restricciones; o
     3. Ambas son factibles e \\(i\\) domina a \\(j\\) en el espacio de objetivos.

---

#### Métricas de Evaluación y Benchmarking Experimental
El desempeño de NSGA-II se evaluó frente a SPEA (Zitzler & Thiele) y PAES (Knowles & Corne) utilizando dos métricas independientes sobre 9 problemas no restringidos (SCH, FON, POL, KUR, ZDT1-4, ZDT6):
- **Métrica de Convergencia (\\(\Upsilon\\))**: Mide la distancia euclidiana promedio entre las soluciones obtenidas y un conjunto de puntos de referencia en la Frontera de Pareto real (valores menores indican mejor convergencia).
- **Métrica de Diversidad y Extensión (\\(\Delta\\))**: Evalúa la uniformidad de la distribución de las soluciones y el grado de cobertura de los extremos.

Además, se probaron problemas con fuerte interacción entre variables (*epistasis/rotación*) y 4 problemas restringidos (CONSTR, SRN, TNK, y WATER con 5 objetivos y 7 restricciones).

---

#### Conclusiones Principales de Deb et al.
- **Superioridad de Rendimiento**: NSGA-II logró una convergencia y una distribución de soluciones sustancialmente mejores que SPEA y PAES en casi todos los problemas de prueba.
- **Robustez Algorítmica**: La eliminación de parámetros explícitos de nicho simplifica la aplicación práctica de los MOEAs sin sacrificar la diversidad en la frontera.
- **Sensibilidad a la Epistasis**: Las rotaciones en el espacio de decisiones y la interacción entre variables representan desafíos severos para los operadores de variación tradicionales, subrayando la necesidad de mecanismos avanzados para problemas acoplados.
- **Efectividad en Restricciones**: La dominancia restringida demostró ser altamente eficiente para guiar la búsqueda desde regiones no factibles hacia los bordes factibles de Pareto sin ajustar parámetros de penalización.

---

### Reporte Técnico 2: Zhou et al. (2011) — Estado del Arte de los MOEAs

#### Contexto y Propósito
Este artículo presenta una revisión exhaustiva del progreso en el campo de los algoritmos evolutivos multiobjetivo durante el período 2003-2011. Se centra en problemas multiobjetivo continuos y complejos, categorizando marcos algorítmicos, estrategias de selección, operadores de reproducción y aplicaciones del mundo real.

---

#### Taxonomía de Marcos Algorítmicos Principales
1. **MOEAs Basados en Descomposición (MOEA/D)**:
   - Descomponen un problema multiobjetivo (MOP) en un conjunto de subproblemas de optimización escalar (*Scalar Optimization Problems*, SOPs) mediante vectores de pesos.
   - Definen relaciones de vecindad entre subproblemas basándose en la distancia entre sus vectores de pesos. Cada subproblema se optimiza utilizando información compartida de sus vecinos.
   - Permite la integración directa de técnicas de búsqueda local escalar.

2. **MOEAs Basados en Preferencias**:
   - Incorporan la articulación de preferencias del Tomador de Decisiones (*Decision Maker*, DM) en distintas etapas (a priori, interactiva o a posteriori).
   - Emplean funciones de valor, puntos/direcciones de referencia y dominancia guiada/sesgada para dirigir el esfuerzo de búsqueda hacia zonas de interés específicas (como las regiones de codo o *knees*).

3. **MOEAs Basados en Indicadores**:
   - Utilizan indicadores de calidad escalar (p. ej., Hipervolumen \\(I_H\\), indicador \\(R2\\), \\(\epsilon\\)-indicador) directamente en la fase de selección para guiar la población.
   - Algoritmos representativos como IBEA e HypE (este último usa estimaciones de Hipervolumen mediante simulaciones de Montecarlo para manejar múltiples objetivos) reducen la necesidad de operadores ad-hoc de diversidad.

4. **Algoritmos Meméticos e Híbridos**:
   - Combinan la búsqueda global poblacional con métodos de búsqueda local (*Memetic MOEAs*).
   - Integran operadores como la búsqueda en colina con pasos laterales (*Hill Climber with Sidestep*, HCS), aproximaciones cuadráticas locales, Búsqueda Tabú, GRASP y Temple Simulado.

5. **MOEAs Coevolutivos**:
   - Evolucionan simultáneamente múltiples subpoblaciones competitivas o cooperativas bajo el principio de "divide y vencerás" para abordar descomposición de problemas y entornos dinámicos.

---

#### Paradigmas de Búsqueda y Operadores de Reproducción
- **Evolución Diferencial (DE)**: Adaptada a MOPs (p. ej., DEMO, PDE) utilizando vectores de diferencia ponderada para generar mutaciones eficientes en espacios continuos.
- **Sistemas Inmunes Artificiales (AIS)**: Simulan la selección clonal y la maduración de afinidad mediante hipermutación para mantener la diversidad.
- **Optimización por Cúmulo de Partículas (MOPSO)**: Emplea poblaciones secundarias/archivos y esquemas de selección de líderes en áreas de baja densidad para dirigir el enjambre.
- **Algoritmos de Estimación de Distribución (EDAs)**: Reemplazan los operadores de cruce y mutación tradicionales mediante la construcción explícita y muestreo de modelos probabilísticos (p. ej., modelos Gaussianos multivariados como RM-MEDA) que capturan dependencias entre variables.

---

#### Tratamiento de Clases de Problemas Complejos
- **Muchos Objetivos (*Many-Objective Problems*, \\(M > 3\\))**: La dominancia de Pareto pierde presión de selección porque casi todas las soluciones se vuelven no dominadas. Se abordan mediante modificación de área de dominancia, L-optimidad y enfoques basados en indicadores o descomposición.
- **Problemas Costosos Computacionalmente**: Utilización de metamodelos y procesos estocásticos Gaussianos (p. ej., MOEA/D-EGO, ParEGO) para predecir valores de función objetivo y reducir evaluaciones directas.
- **Problemas Dinámicos, Ruidosos y Multimodales**: Introducción de mecanismos de predicción del Frente de Pareto en el tiempo, modelos locales hiperesféricos para filtrar ruido y formulaciones biobjetivo (usando gradientes) para encontrar múltiples óptimos locales/globales.

---

#### Conclusiones Principales de Zhou et al.
- **Transición de Paradigma**: La investigación ha evolucionado desde los enfoques basados exclusivamente en dominancia de Pareto hacia marcos basados en descomposición e indicadores de calidad.
- **Importancia de la Estructura de las Soluciones**: Explotar las regularidades del conjunto de Pareto en el espacio de decisiones (p. ej., mediante EDAs) mejora significativamente la escalabilidad.
- **Desafíos Críticos Inminentes**: Persisten retos conceptuales en la optimización con múltiples objetivos (\\(M > 3\\)), el ajuste adaptativo de parámetros en tiempo real, la interacción efectiva con el usuario (DM) y el manejo de entornos ruidosos y dinámicos.

---

### Reporte Técnico 3: Giagkiozis et al. (2013) — Visión General de Algoritmos Poblacionales

#### Contexto y Propósito
Giagkiozis, Purshouse y Fleming presentan una revisión conceptual y estructurada de las metodologías poblacionales para optimización multiobjetivo (*Population-Based Optimisation Techniques*, PBOTs). El estudio sintetiza el marco operativo unificado de estas técnicas, analiza los métodos de extensión a MOPs y ofrece una evaluación comparativa cualitativa entre siete familias algorítmicas.

---

#### Estructura General Unificada de las PBOTs
Todas las PBOTs comparten una arquitectura iterativa común compuesta por:
1. **Inicialización**: Generación de la población en el espacio factible.
2. **Evaluación de la Función Objetivo**.
3. **Evaluación de la Calidad de la Población**: Asignación de aptitud según la extensión multiobjetivo seleccionada.
4. **Operador de Variación**: Combinación de perturbaciones estocásticas (mutación) y combinación de información (recombinación/cruce).
5. **Selección y Elitismo**: Filtrado para conformar la siguiente generación.
6. **Criterio de Parada**.

---

#### Principales Métodos de Extensión Multiobjetivo
- **Métodos Basados en Dominancia de Pareto**: MOGA, NSGA, NSGA-II, SPEA, SPEA2. Utilizan relaciones de dominancia para rangos de aptitud y técnicas de densidad/hacinamiento para mantener la diversidad.
- **Métodos Basados en Descomposición**: Transforman el MOP en un conjunto de subproblemas escalares mediante funciones escalarizantes (Suma Ponderada, Tchebycheff, *Normal Boundary Intersection* - NBI, MOEA/D).
- **Métodos Basados en Indicadores**: Emplean métricas cualitativas (destacando el indicador de Hipervolumen) directamente como función de aptitud dentro del algoritmo (p. ej., HypE).

---

#### Evaluación Comparativa de las 7 Familias Algorítmicas
Los autores evalúan cualitativamente siete familias (GAs, ES, AIS, ACO, DE, PSO, EDA) a través de 11 dimensiones técnicas:

| Familia Algorítmica | Fortalezas Principales | Limitaciones Clave |
| :--- | :--- | :--- |
| **Algoritmos Genéticos (GA)** | Gran flexibilidad de representación; muy bien documentados para MOPs. | Sensibles a la selección de operadores; alto costo en alta dimensión. |
| **Estrategias de Evolución (ES)** | Muy eficaces en espacios continuos; adaptación intrínseca de parámetros (\\(\sigma\\)). | Menos adecuadas para problemas puramente discretos o combinatorios. |
| **Sistemas Inmunes Artificiales (AIS)** | Excelente preservación de memoria y diversidad mediante selección clonal. | Complejidad de implementación y escasez de soporte en librerías estándar. |
| **Optimización por Colonia de Hormigas (ACO)** | Dominantes en problemas combinatorios; fácil incorporación de información a priori (feromonas). | Dificultad severa para extenderse a espacios continuos y a más de 3 objetivos. |
| **Evolución Diferencial (DE)** | Simplicidad de implementación, muy bajo costo computacional y excelente para problemas continuos. | Rendimiento reducido en problemas combinatorios y dependencias de variables no alineadas. |
| **Optimización por Cúmulo de Partículas (PSO)** | Rápida velocidad de convergencia en espacios continuos no convexos. | Propensión al estancamiento en óptimos locales si los líderes no se seleccionan adecuadamente. |
| **Algoritmos de Estimación de Distribución (EDA)** | Gestión óptima de parámetros; excelente incorporación de conocimiento previo y captura de dependencias. | Altísimo costo computacional por iteración para construir modelos probabilísticos en alta dimensión. |

---

#### Conclusiones Principales de Giagkiozis et al.
- **Pérdida de Escalabilidad en Dominancia de Pareto**: Los métodos basados en dominancia de Pareto se degradan severamente cuando \\(M > 3\\) debido a la pérdida de presión de selección, motivando la transición hacia descomposición e indicadores.
- **Costo Computacional vs. Representación**: Existe una brecha entre la complejidad computacional per cápita del algoritmo (p. ej., DE/PSO son ligeros; EDA es pesado) y su capacidad de adaptarse a paisajes discontinuos o epistáticos.
- **Necesidad de Enfoques Híbridos y Modelos Sustitutos**: Se sugiere la integración de modelos de aproximación cuadrática/surrogates (algoritmos meméticos) e híbridos EDA-Indicador para abordar problemas industriales reales de alto costo.

---

### Reporte Unificado: Síntesis, Puntos en Común y Estado del Arte

#### 1. El Dilema Fundamental de la Optimización Multiobjetivo
Los tres estudios coinciden explícitamente en que la optimización multiobjetivo plantea dos objetivos contrapuestos que deben satisfacerse simultáneamente:
1. **Convergencia**: Guiar la población lo más cerca posible hacia la verdadera Frontera de Pareto óptima (\\(PF^*\\)).
2. **Diversidad y Extensión**: Mantener una distribución uniforme y amplia de las soluciones a lo largo de todo el frente de compromiso.

Ninguna métrica escalar única basta para evaluar ambos aspectos de forma aislada, lo que exige herramientas de evaluación cuantitativas bien definidas (como la métrica \\(\Upsilon\\) y \\(\Delta\\) de Deb et al., o el Hipervolumen e IGD revisados por Zhou et al. y Giagkiozis et al.).

---

#### 2. Evolución Histórica de los Paradigmas Algorítmicos
Al cruzar la información de las tres publicaciones, se observa una evolución clara estructurada en tres fases históricas:

```
[Fase 1: No Elitista]           [Fase 2: Elitista y Dominancia]        [Fase 3: Descomposición e Indicadores]
- VEGA, MOGA, NSGA              - NSGA-II, SPEA2, PAES                - MOEA/D, IBEA, HypE
- Nichos con parámetro σ_share  - Crowding distance (sin parámetros)  - Manejo de Many-Objective (M > 3)
- Alta complejidad O(MN^3)      - Complejidad reducida O(MN^2)        - Uso de vectores de pesos e indicadores
```

1. **Primera Generación (No Elitistas y Paramétricos)**: Algoritmos como VEGA, MOGA y el NSGA original. Presentaban alta complejidad computacional, carecían de memoria de elites y requerían el ajuste manual de parámetros de nicho (\\(\sigma_{share}\\)).
2. **Segunda Generación (Elitistas Basados en Dominancia)**: Encabezados por NSGA-II, SPEA2 y PAES. Introdujeron esquemas de ordenamiento rápido no dominado, preservación de elites combinando poblaciones padre-hijo (\\(2N\\)) y estimadores de densidad sin parámetros (como la distancia de hacinamiento).
3. **Tercera Generación (Descomposición e Indicadores)**: Algoritmos como MOEA/D, IBEA y HypE. Diseñados para superar el colapso de la presión de selección en problemas con más de tres objetivos (\\(M > 3\\)).

---

#### 3. Importancia Crítica del Elitismo y Gestión de la Memoria
Tanto Deb et al. como Zhou et al. y Giagkiozis et al. destacan que **el elitismo es indispensable**. La preservación directa de las mejores soluciones no dominadas (ya sea mediante una población extendida \\(2N\\) o archivos externos) evita la pérdida de soluciones óptimas encontradas en generaciones previas y acelera drásticamente la velocidad de convergencia del algoritmo.

---

#### 4. La Barrera de la Alta Dimensionabilidad (*Many-Objective Optimization*, \\(M > 3\\))
Existe un consenso unánime entre Zhou et al. y Giagkiozis et al. (y anticipado en los análisis de escalabilidad de Deb et al.) sobre el fallo estructural de la dominancia de Pareto en espacios de alta dimensión:
- A medida que el número de objetivos \\(M\\) aumenta (\\(M > 3\\)), la proporción de soluciones no dominadas en una población aleatoria se aproxima al 100%.
- Esto provoca que el operador de selección pierda casi por completo su presión de selección hacia el frente óptimo, convirtiendo la búsqueda en un paseo aleatorio a menos que se adopten enfoques de descomposición (vectorial) o basadas en indicadores de calidad como el Hipervolumen.

---

#### 5. Desafíos Estructurales Comunes en el Espacio de Decisiones
Los tres documentos identifican barreras fundamentales que dificultan el desempeño de los MOEAs:
- **Interacción de Variables y Epistasis (Problemas Rotados)**: Los operadores tradicionales de variación punto a punto fallan cuando las variables de decisión están fuertemente acopladas, requiriendo operadores invariantes a la rotación o modelos probabilísticos (EDAs).
- **Manejo de Restricciones Sin Parámetros**: La tendencia dominante es evitar penalizaciones subjetivas, utilizando reglas de dominancia restringida o jerarquización factible.
- **Costo Computacional de Evaluación**: La necesidad de aplicar modelos de sustitución (*surrogates/metamodels*) como Procesos Gaussianos para optimizar problemas reales costosos.

---

### Cuadro Comparativo Consolidado de los Tres Trabajos

| Dimensión de Análisis | Deb et al. (2002) | Zhou et al. (2011) | Giagkiozis et al. (2013) |
| :--- | :--- | :--- | :--- |
| **Tipo de Estudio** | Propuesta algorítmica específica (NSGA-II) y validación. | Revisión del estado del arte en MOEAs (2003–2011). | Visión general conceptual y matriz comparativa de PBOTs. |
| **Enfoque Principal** | Superar la complejidad \\(O(M N^3)\\), falta de elitismo y parámetros \\(\sigma_{share}\\). | Clasificación de marcos (MOEA/D, Preferencias, Indicadores, Meméticos). | Mapeo unificado de 7 familias algorítmicas y sus capacidades. |
| **Respuesta al Desafío \\(M > 3\\)** | Diseñado y validado principalmente para 2 a 5 objetivos. | Identifica la descomposición e indicadores como solución al fallo de dominancia. | Ratifica teóricamente la degradación de la dominancia de Pareto en alta dimensión. |
| **Manejo de Restricciones** | Propone la Dominancia Restringida por torneo sin penalizaciones. | Revisa técnicas multiobjetivo y de inmunidad para restricciones. | Trata el manejo de restricciones como un módulo ortogonal del algoritmo. |
| **Recomendación Futura** | Investigar la interacción entre variables (epistasis/linkage). | Explotar regularidades de la PS y desarrollar algoritmos interactivos. | Desarrollar modelos híbridos EDA-Indicador y modelos sustitutos (*surrogates*). |

---