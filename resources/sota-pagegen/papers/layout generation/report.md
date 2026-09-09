### Panorama General del Dominio: *layoutgen-survey.pdf*

El artículo de revisión (*survey*) proporciona un marco taxonómico y conceptual para la generación inteligente de layouts en el contexto de **AIGC (Artificial Intelligence-Generated Content)**, situándose en la intersección entre visión por computador, estética computacional e inteligencia artificial.

#### 1. Taxonomía de Modelos Generativos
El *survey* clasifica los avances en la literatura según la arquitectura profunda subyacente:
* **Modelos Autoregresivos (Transformers):** Modelan la generación de layout como una secuencia de predicciones de tokens condicionales, capturando dependencias globales mediante mecanismos de autoatención (*self-attention*).
* **Variational Autoencoders (VAEs):** Aprenden un espacio latente continuo para modelar distribuciones complejas de layouts y atributos de objetos (como recuentos de categorías o relaciones condicionales).
* **Generative Adversarial Networks (GANs):** Emplean un generador y un discriminador (frecuentemente basados en grafos, renderizadores de *wireframes* o bloques de atención) para sintetizar diseños realistas y evaluar la coherencia estético-espacial.
* **Modelos Basados en Flujos y Difusión (*Flow-based & Diffusion Models*):** Enfoques recientes que abordan la generación y edición de layouts mediante procesos de difusión latente o mapeos biyectivos.

#### 2. Representación de Layout y Entradas Multimodales
Un layout se abstrae primariamente como un conjunto de **primitivas gráficas compuestas** parametrizadas por sus **cajas delimitadoras (*Bounding Boxes - bbx*)**. 
* **Atributos de Salida:** Parámetros geométricos como coordenadas (\\(x, y\\)), ancho (\\(w\\)), alto (\\(h\\)) y categoría del elemento (\\(c\\)).
* **Formatos de Entrada:** Varían desde etiquetas de categorías simples hasta grafos de relaciones (*relation graphs* o *scene graphs*), restricciones del usuario (alineación, no-solapamiento) y datos multimodales complejos (imágenes, palabras clave de texto, proporciones de área).

#### 3. Metodología de Evaluación
El *survey* estandariza la evaluación en dos grandes verticales:
* **Cuantitativa:** Mide la fidelidad mediante **FID (Fréchet Inception Distance)** e **Inception Score (IS)**, la verosimilitud estocástica mediante **Negative Log-Likelihood (NLL)**, y métricas geométricas explícitas como **Alineación (*Alignment*)**, **Solapamiento (*Overlap*)** y **Cobertura del Canvas (*Coverage*)**.
* **Cualitativa:** Evaluaciones humanas (**User Studies**) mediante pruebas A/B o escalamiento de preferencias conducidos con usuarios promedio o expertos en diseño.

---

### Análisis Técnico de los Trabajos Particulares

#### 1. *LayoutTransformer* (Gupta et al., 2021)
* **Enfoque Técnico:** Aborda la generación y completado de layouts modelando los elementos como una secuencia plana de tokens procesados por un **decodificador Transformer autoregresivo** con autoatención enmascarada (*masked self-attention*).
* **Proyección Independiente de Atributos:** A diferencia de concatenar todos los atributos de un elemento en un solo vector, proyecta cada atributo (\\(c, x, y, w, h\\)) de forma independiente a un espacio latente continuo antes de pasarlos al decodificador. Esto permite al módulo de atención enfocarse en atributos específicos, lo que resulta crítico en dominios con simetrías alineadas a los ejes (como documentos o interfaces móviles).
* **Propiedades Emergentes:** Demuestra que el aprendizaje de layouts actúa como una tarea *proxy* que hace **emerger relaciones semánticas** entre categorías de objetos en el espacio de características sin requerir *embeddings* lingüísticos explícitos.
* **Aplicación:** Generación desde cero (\\(\langle bos \rangle\\)) o completado condicional a partir de una semilla inicial de primitivas en dominios variados (RICO, PubLayNet, COCO, Part-Net 3D).

#### 2. *Neural Design Network - NDN* (Lee et al., 2019)
* **Enfoque Técnico:** Utiliza **Graph Neural Networks (GNN)** combinadas con un **Conditional VAE (CVAE)** iterativo para sintetizar layouts condicionados a restricciones explícitas del usuario.
* **Arquitectura de Tres Módulos:**
  1. *Predicción de Relaciones:* Recibe un grafo parcial de nodos (componentes) y aristas (restricciones de ubicación o tamaño especificadas por el usuario) e infiere un grafo completo de relaciones mediante una red convolucional de grafos (GCN) y un vector latente \\(z\\).
  2. *Generación de Bounding Boxes:* Predice iterativamente las posiciones y dimensiones \\(\{x_i, y_i, w_i, h_i\}\\) sobre el canvas a partir del grafo completo de relaciones.
  3. *Módulo de Refinamiento:* Ajusta iterativamente las cajas delimitadoras predichas para perfeccionar la alineación y la calidad estética.
* **Funcionalidades:** Permite la generación con restricciones parciales y la **recomendación de layouts** (sugerir la mejor posición/tamaño para un elemento nuevo en un canvas existente).

#### 3. *BLT: Bidirectional Layout Transformer* (Kong et al., 2022)
* **Enfoque Técnico:** Aborda la "cadena de dependencia inmutable" de los Transformers autoregresivos convencionales introduciendo un **Transformer no-autoregresivo bidireccional** basado en una arquitectura tipo BERT.
* **Decodificación Paralela por Refinamiento Iterativo:** Genera todos los atributos del layout simultáneamente en paralelo a lo largo de un número pequeño de iteraciones, reemplazando atributos de baja confianza por tokens `[mask]` y refinándolos.
* **Muestreo Jerárquico (*Hierarchical Mask Sampling*):** Guía la máscara y el refinamiento mediante un orden estricto de grupos semánticos: **Categoría (\\(C\\)) \\(\rightarrow\\) Tamaño (\\(S\\)) \\(\rightarrow\\) Posición (\\(P\\))**.
* **Ventajas:** Facilita la generación condicional altamente flexible (el usuario puede fijar cualquier atributo arbitrario) y logra una **aceleración de 4x a 10x** en la inferencia frente a modelos autoregresivos.

#### 4. *Constrained Layout Generation via Latent Optimization - CLG-LO* (Kikuchi et al., 2021)
* **Enfoque Técnico:** Formula la generación con restricciones como un **problema de optimización en el espacio latente** de un modelo generativo ya entrenado de forma no restringida, evitando la necesidad de reentrenar la red para cada nueva regla o pérdida.
* **Backbone LayoutGAN++:** Propone una versión mejorada de LayoutGAN que incorpora bloques Transformer en el generador y el discriminador, junto con una pérdida auxiliar de reconstrucción que estabiliza el entrenamiento.
* **Algoritmo de Optimización:** Dado un vector latente \\(z\\), utiliza optimizadores iterativos (como Adam o CMA-ES) para buscar el código latente \\(z^*\\) que minimiza las funciones de costo asociadas a la alineación, el no-solapamiento y las relaciones posicionales deseada por el usuario.

#### 5. *Content-aware Generative Modeling / ContentGAN* (Zheng et al., 2019)
* **Enfoque Técnico:** Presenta el primer marco generativo profundo **consciente del contenido** (*content-aware*), diseñando layouts condicionados a la semántica visual de las imágenes y la semántica textual de las publicaciones (revistas).
* **Arquitectura Multimodal y GAN Condicional:**
  1. *Red de Embedding Multimodal:* Tres codificadores independientes procesan imágenes (redes convolucionales), texto (palabras clave extraídas) y atributos de alto nivel (categoría de diseño, proporción de área de texto \\(T_p\\) e imagen \\(I_p\\)), fusionándolos en un vector condicional \\(y\\).
  2. *Red Generativa de Layout:* Una GAN condicional cuyo codificador \\(E\\), generador \\(G\\) y discriminador \\(D\\) operan condicionados en \\(y\\) para aprender la distribución de layouts y extraer características conscientes del contenido.
* **Post-procesamiento Morfológico:** Utiliza etiquetado de componentes conectados y operaciones morfológicas para corregir bordes irregulares y desalineaciones de píxeles.
* **Control por Bocetos:** Permite al usuario guiar la síntesis dibujando un boceto (*sketch*) sobre la página, el cual se convierte en un vector de restricciones para el generador.

---

### Resumen Comparativo: Elementos en Común

1. **Formulación Geométrica Basada en Cajas Delimitadoras (*Bounding Boxes*):**
   Todos los trabajos particulares convergen en abstraer los elementos de diseño (texto, imágenes, títulos, botones) mediante cajas delimitadoras parametrizadas por tuplas numéricas cuadriláteras \\((c, x, y, w, h)\\) escaladas al canvas.

2. **Transición hacia el Control Condicional y Restricciones del Usuario:**
   Aunque la generación incondicional sirvió como punto de partida, todos los modelos buscan resolver tareas condicionales:
   * **NDN** y **CLG-LO** mediante grafos y optimización latente.
   * **BLT** y **LayoutTransformer** permitiendo condicionamiento sobre categorías, tamaños o esquemas parciales.
   * **ContentGAN** condicionando según el contenido visual/textual y bocetos.

3. **Uso de Datasets Estándar en la Industria:**
   Existe una alta solapamiento en la evaluación experimental. Los conjuntos de datos más utilizados por estos modelos son:
   * **RICO:** Interfaces de usuario para aplicaciones móviles.
   * **PubLayNet:** Layouts de documentos científicos.
   * **Magazine / Image Ads:** Diseños editoriales y publicitarios.

4. **Necesidad Explícita de Módulos o Pasos de Refinamiento:**
   Debido a que las redes neuronales profundas tienden a generar imprecisiones continuas o ligeras desviaciones espaciales, casi todos incorporan etapas dedicadas a corregir la alineación:
   * **NDN** cuenta con un *Refinement Module*.
   * **ContentGAN** aplica post-procesamiento morfológico.
   * **BLT** utiliza *Iterative Attribute Refinement*.
   * **CLG-LO** incluye términos explícitos de alineación en su función de pérdida de optimización latente.

5. **Métricas de Evaluación Híbridas (Alineación, Overlap y User Studies):**
   Todos los estudios validan sus resultados combinando métricas geométricas automatizadas (medición de solapamiento IoU y alineación de bordes), métricas generativas (FID, NLL) y estudios cualitativos con usuarios para medir la estética y legibilidad.

