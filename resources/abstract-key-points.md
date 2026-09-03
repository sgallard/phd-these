# Puntos clave para el abstract general de la tesis

---

## 0. Restricciones de formato

| Elemento | Restricción |
|---|---|
| **`\begin{abstract}` (inglés)** | **≈ 3000 caracteres**, espacios incluidos |
| **`\begin{resume}` (francés)** | **≈ 3000 caracteres**, espacios incluidos |
| `\keywords{}` / `\motscles{}` | **6** palabras clave cada uno |
| Plataforma de depósito | admite hasta 4000; se usa el mismo texto de 3000 |

El `2000 / 5` que figuraba antes en este documento era un remanente del template LaTeX de
partida y no corresponde a ninguna restricción real.

**Se adopta 3000 caracteres como longitud objetivo.** No es el máximo de la plataforma (4000),
sino el punto en que el argumento completo cabe sin que el texto se convierta en una lista de
resultados. 3000 caracteres ≈ 450–480 palabras ≈ 20–24 frases: alcanza para las tres
contribuciones con su evidencia, pero obliga a que **cada frase haga trabajo argumentativo**.
Los 1000 caracteres que se dejan sobre la mesa compran legibilidad, que en un abstract vale
más que exhaustividad.

**D0 (resuelta): un solo texto de ~3000 caracteres para todo.** El mismo abstract va a la
plataforma de depósito y a `resume.tex`. Fuente única de verdad, sin riesgo de que la
contracubierta y el índice nacional acaben diciendo cosas distintas.

~~Cabida en la maqueta **verificada por compilación**: 3000 + 3000 entran sin tocar la clase.~~
**Falso, corregido el 2026-08-28.** Esa afirmación nunca se verificó de verdad. Medido por
barrido sobre el documento completo, la página de `ResumeMotsCles` admitía **~3 300 caracteres
para los dos resúmenes juntos** (~1 550 EN + ~1 750 FR): a partir de 3 450 desbordaba, y con
7 200 la caja del résumé francés **se descartaba silenciosamente** —el francés simplemente no
aparecía en el PDF—. El síntoma era un `Overfull \vbox` de 38,8 pt en esa página, presente ya
con el *lorem ipsum* del template. El comentario original de la plantilla (*"pas plus de 2000
caractères"*) estaba mucho más cerca de la realidad que esta decisión.

**Resuelto modificando la clase, no el texto.** `ResumeMotsCles` en `these-ISSS.cls` ahora
inserta un salto de página entre el bloque inglés y el francés, de modo que **cada idioma ocupa
su propia página**. Con eso caben 3 384 EN + 3 833 FR sin ningún desbordamiento, verificado por
compilación e inspección del PDF (páginas vii y viii).

⚠ Consecuencia a confirmar con la escuela doctoral: la contracubierta pasa de una página a dos.
Si exigen página única, hay que volver a ~1 550 / ~1 750 caracteres y rehacer los seis
movimientos en la mitad de espacio.


El título ya está fijado en `title.tex` y tiene tres partes explícitas:

 *Automating Newspaper Layout Production: Learned Template Retrieval, Multi-Objective
 Page Building, and User-Validated Large-Print Adaptation*

El abstract **debe** cubrir esas tres partes en ese orden. Es la restricción estructural
más fuerte que existe: si el abstract no las refleja, hay incoherencia con la portada.

---

## 1. Estructura propuesta (6 movimientos + presupuesto de caracteres)

| # | Movimiento | Contenido | Caracteres |
|---|---|---|---|
| 1 | Contexto industrial | Cambio en la industria actual; paradigma content-driven; el layout 2D como valor a preservar; producción manual como cuello de botella | ~380 |
| 2 | Problema y objetivo | Automatizar el workflow web-to-print de un CMS industrial; **una** página como unidad de decisión; naturaleza multi-objetivo y criterio tácito | ~350 |
| 3 | Contribución 1 | Similitud topológica aprendida + retrieval de templates (aislado y page-aware) | ~520 |
| 4 | Contribución 2 | Formalización MOCOP + método evolutivo; resultado principal (factibilidad + calidad + tiempo) | ~800 |
| 5 | Contribución 3 | Transferencia a large-print + estudio de usuarios | ~600 |
| 6 | Cierre | Validación en datos industriales reales; doble impacto económico/societal; perspectivas a futuro | ~250 |

Total ≈ 2900 caracteres, deja ~100 de margen sobre el objetivo de 3000.

**Proporciones que hay que respetar:** el Movimiento 4 sigue siendo el bloque más largo
(~27 % del texto) y los Movimientos 3+4+5 juntos son el 65 %. Los movimientos 1 y 2, que son
los que más tienden a inflarse al redactar, no deben pasar del 25 % combinado: el contexto
justifica el problema, no lo sustituye.

**Regla de oro para las cifras:** máximo **7 afirmaciones numéricas**. Por encima de eso el
abstract se convierte en una tabla de resultados y el argumento deja de leerse. 

---

## 2. Movimiento 1 — Contexto industrial

Ideas a comprimir en 3–4 frases:

- **Cambio en la industria actual.**
- La prensa pasó de un paradigma **layout-driven** (el periodista escribía dentro de un
  espacio geométrico fijo) a uno **content-driven** (se escribe web-first, sin topología).
- El layout bidimensional **sigue teniendo valor** y no es reducible al papel físico:
  aporta conciencia estructural, puntos de entrada, jerarquía editorial y serendipia que
  un feed lineal destruye. En la tesis, *print* designa el layout 2D, físico **o** digital.
- Consecuencia operativa: el contenido web no estructurado debe encajarse *a posteriori* en
  canvas 2D estructurados. En el CMS industrial estudiado (**Melody**, Demain Un Autre Jour,
  desplegado en **+150 redacciones**), esto se hace **manualmente** en dos pasos —asignación
  de gabarito y colocación en el canvas— y cuesta **horas por edición**.
  ⚠ Este *"horas por edición"* es **portante** desde la revisión del objetivo general: es la
  base de comparación de su cláusula temporal, y el único lugar del abstract donde aparece el
  coste de la práctica manual. No se poda en ningún recorte (ver D4(ii)). Enunciarlo en su
  unidad —**por edición**, no por página— es obligatorio: la tesis no cronometra el trabajo
  manual por página.

**Qué NO poner:** las cifras macroeconómicas del sector (−42 % de ingresos desde 1990,
−61 % de publicidad 1990–2015, AI Overviews, Apig). Son buenas para el Capítulo 1, pero en
el abstract consumen espacio sin sostener ninguna contribución. No es un problema de
presupuesto: no sostienen ninguna afirmación de la tesis, así que sobrarían con 3000 y con
4000 caracteres igual.

**D1 (resuelta).** Se nombra **Melody** explícitamente, con la empresa en una sola aposición:
*"Melody (Demain Un Autre Jour), deployed in over 150 newsrooms"*. La empresa no se vuelve a
nombrar. La financiación CIFRE **no** se menciona: es meta-tesis y va en la sección de
*fundings*.

**D1b (resuelta).** El corpus de evaluación **sí se nombra** (`La Provence`, diario regional).
La razón original para omitirlo era la economía de caracteres —tres nombres propios en 2000—
y con 3000 sigue habiendo margen suficiente. Nombrarlo refuerza la trazabilidad del dato
industrial. Aparece **una sola vez**, en el Movimiento 4, junto al corpus.

---

## 3. Movimiento 2 — Problema y objetivo

Objetivo (`chapters/context/main.tex:194`, **revisado**):

Automate the Melody web-to-print workflow, generating a complete print page from a set of web articles without manual template assignment nor manual placement, **in a few minutes per page against the hours of manual editing currently required**, and with objective values within the ranges observed in operator-produced pages of the same publisher.

**Qué cambió y por qué importa para el abstract.** El objetivo ya no fija un umbral absoluto
(*"in under two minutes"*). Ese número era post-hoc —salía de redondear el peor caso medido,
111,77 s— y dependía del hardware, lo que lo hacía no falsable. Ahora la cláusula temporal
enuncia una **magnitud** con base de comparación explícita, simétrica con la cláusula de
calidad, y el requisito industrial que la origina (*a few minutes per page*, formulación
literal del socio) queda documentado en §2.1 del Capítulo 1.

Consecuencia operativa: **el objetivo se enuncia en magnitud, el abstract reporta la cifra
medida.** No es una incoherencia sino una división de trabajo deliberada — ver D4, reescrita.

Elementos técnicos que justifican la dificultad. Con 350 caracteres cabe **uno**, fusionado:

- Acoplamiento de una **selección discreta de templates** con un **packing 2D** → espacio de
  búsqueda `O(M^n · n! · |E|^n)`, NP-difícil.
- La calidad de página **no es un escalar**: cuatro criterios en conflicto que responden a
  cuatro intereses distintos (coste de producción, integridad del contenido, navegación del
  lector, práctica de diseño del editor).
- El cuarto criterio es **tácito**: los operadores reconocen qué combinaciones de templates
  respetan el estilo de su periódico pero no saben enunciar la regla; solo existe la traza
  histórica → hay que **aprenderlo**, no escribirlo.

→ *Decisión:* el segundo y el tercero, **fusionados en una sola frase**. Es lo que distingue
esta tesis de un trabajo puro de bin-packing y lo que prepara la contribución 1. El primero
(NP-dificultad, con la cota `O(M^n · n! · |E|^n)`) **se omite**: a 3000 caracteres ya no hay
sitio para las dos cosas, y la NP-dificultad es el argumento menos distintivo de los tres
—cualquier problema de packing lo tiene, y no explica por qué esta tesis necesitó aprender
nada—. La complejidad queda implícita en el resultado del Movimiento 4 (los pipelines
desacoplados fallan), que es donde de verdad importa.

---

## 4. Movimiento 3 — Contribución 1 (Capítulo `template`)

Tres piezas. Con 520 caracteres caben las tres, pero **solo si se encadenan en una sola
frase** en vez de enunciarse por separado (ver la prueba de cabida al final de la sección).

1. **Medida de similitud topológica entre gabaritos.** Dos candidatas formalizadas
   (`tdIoU`, geométrica-analítica, y `tGMN`, aprendida con una Graph Matching Network
   reentrenada).
2. **`TRS`/`TRF`: retrieval diversity-aware para un artículo aislado.** Clustering
   estructural offline + selección online por cluster weights con supresión intra-cluster.
   Ataca la diversidad estructural y además el sesgo de popularidad de los catálogos
   industriales (long tail).
3. **`GWES` (Geometric-Weighted Editorial Score): scoring page-aware.** Transformer encoder
   sobre la secuencia de artículos de la página + matriz de afinidad topológica `tGMN`.
   Es la pieza que alimenta el objetivo del estilo editorial en el capítulo siguiente.

**D2 (resuelta).** Las tres piezas entran, en el orden e hilo de la opción (a):
**métrica → retrieval → scoring page-aware**. El retrieval diversity-aware se enuncia
explícitamente en vez de quedar implícito bajo "template retrieval", porque es el objetivo
específico 1 declarado.

**Prueba de cabida a 520 caracteres** (borrador desechable, solo para verificar que entra):

> *A learned topological similarity between templates, obtained by retraining a graph
> matching network, underpins two retrieval mechanisms: a diversity-aware template retrieval
> framework that counters the popularity bias of industrial catalogues, and a page-aware
> scoring model — a Transformer encoder over the page's article sequence combined with the
> topological affinity matrix — which recovers the publisher's tacit assignment style with
> 82.6 % top-1 accuracy against historical human assignments.* **(487 caracteres)**

Confirma que las tres piezas caben, pero también marca el límite: no hay espacio para
`tdIoU`, ni para el clustering estructural offline, ni para el mecanismo de supresión
intra-cluster. Se nombra **qué hace** cada pieza, nunca **cómo**.

**D2b (resuelta).** El retrieval se describe **sin sigla**. Siglas solo para `tGMN` y `GWES`,
que son las que reaparecen en movimientos posteriores.

Formulación exacta: **`diversity-aware template retrieval framework`**. La palabra es
*framework*, no *strategy* ni *method*, porque es la que usa el capítulo:
`chapters/template/sections/problem-definition.tex:19` dice literalmente *"the Template
Retrieval System (**TRS**) and its **diversity-aware framework** (TRF)"*, y
`recsys.tex:47` titula la sección *"Online Component: Template Retrieval Framework (TRF)"*.
Es decir, `TRS` es el sistema completo (clustering estructural offline + selección online) y
`TRF` es específicamente el componente online diversity-aware. Lo que el abstract describe
—*"diversity-aware"*— es `TRF`; usar *framework* mantiene la trazabilidad exacta con el
capítulo sin gastar la sigla.

**D2c (resuelta).** El **estudio perceptual en línea con 42 participantes** que arbitró entre
`tdIoU` y `tGMN` **no entra en el abstract**. Se re-examinó dos veces (a 4000 y a 3000
caracteres) y la decisión se mantiene; a 3000 las tres razones son válidas otra vez:

1. **Presupuesto.** Consumiría una de las siete plazas numéricas en validar una *decisión de
   diseño interna*, no una contribución.
2. **Colisión semántica.** El abstract ya contiene un estudio con usuarios (24 participantes)
   y el título promete literalmente *"User-Validated Large-Print Adaptation"*. Un segundo
   estudio con usuarios diluye exactamente el eslogan del título: el lector no sabrá cuál es
   *el* estudio.
3. **Riesgo asimétrico.** Un estudio con efecto débil, relegado a apéndice en el paper y
   destacado en el abstract, es una invitación explícita a la pregunta *"¿cómo se estableció
   la significancia?"* en la defensa. En el abstract no hay espacio para contextualizarlo;
   en el capítulo sí, y ahí se queda como evidencia de apoyo.

→ Consecuencia: `tGMN` **se justifica por su función, no por un experimento** — es la matriz
de afinidad topológica que alimenta el scoring page-aware y, a través de él, el objetivo
tácito del Movimiento 4. Esto además refuerza el hilo hacia la contribución 2.

---

## 5. Movimiento 4 — Contribución 2 (Capítulo `pagegen`), el núcleo

Es la contribución principal y debe ocupar el bloque más largo (~800 caracteres, ~27 % del
abstract). A 3000 caracteres el reparto interno recomendado es: formalización ~200,
resultado principal (tríptico) ~450, variante guiada ~150. Nótese que **la formalización se
lleva menos que el resultado**: nombrar el problema es barato, demostrar que se resolvió no.

- **Formalización:** generación de página como **MOCOP** (Multi-Objective Combinatorial
  Optimization Problem) sobre tres variables de decisión por artículo —gabarito `t_i`,
  posición `p_i`, elasticidad vertical `e_i`— con restricciones duras (**página única**,
  no-solape, límites de página, alineación al grid, coherencia de título e imágenes).
- **Cuatro objetivos en conflicto**, en este orden: cobertura de página, integridad de
  capacidad textual, calidad de posicionamiento (zona crítica del artículo principal +
  alineación vertical) y, **al final**, el estilo editorial aprendido vía `GWES`.
  El orden no es decorativo: los tres primeros son especificables analíticamente, el cuarto
  es tácito, y ponerlo al final cierra el arco con la contribución 1 (*el cuarto criterio no
  se escribe, se aprende — y por eso hizo falta el capítulo anterior*).
  - **Formulación compacta recomendada** (~170 caracteres): *"three analytically specifiable
    objectives — page coverage, text-capacity integrity and placement quality — and a fourth,
    tacit one, learned from historical human assignments"*. Mismo orden, y el contraste
    analítico/tácito queda en la propia sintaxis.
  - En el **cuerpo de la tesis** se usan las macros de `sty/custom/macros.sty` (que ya no
    llevan número; el número no se muestra en el texto). En el **abstract**, ver D6.
- **Método `EvoPageGEN`:** motor evolutivo NSGA-III con cromosoma de tres segmentos +
  decodificador de packing por extreme points con backtracking exhaustivo (C++) +
  módulo de evaluación híbrido (analítico + neuronal). Dos variantes:
  `EvoPageGEN-NSGA-III` (uniforme) y `EvoPageGEN-RNSGA-III` (guiado por puntos de
  aspiración extraídos de los percentiles 25 y 50 de los diseños humanos históricos. Recordar que the lower the better, por eso esos percentiles).
- **Resultado que hay que contar sí o sí:** los pipelines **desacoplados** (seleccionar
  gabarito primero, empaquetar después) **no garantizan ni siquiera la factibilidad básica
  de una sola página** —se desbordan a 2 páginas cuando `n ≥ 6`— mientras que la
  optimización simultánea la mantiene al 100 %. Es el argumento estructural más fuerte
  de la tesis: justifica por qué el problema **debe** resolverse conjuntamente.
- **Segundo resultado:** la variante guiada por preferencias no pierde diversidad útil,
  sino que **poda espacio inviable** — comprime el frente de Pareto (de ~123 a ~18
  soluciones) y multiplica por ~6–8 la densidad de soluciones dentro de la región de
  interés histórica. Es lo que convierte un generador teórico en una herramienta usable
  por un editor.

**D3 (resuelta).** No se afirma paridad con operadores humanos: no hay comparación directa
página-generada vs. página-humana (ni juicio de expertos ni A/B). Lo que sí existe es
(i) alineación con distribuciones objetivas históricas, (ii) `GWES` entrenado sobre
asignaciones humanas reales, (iii) dominancia de Pareto sobre baselines. → El abstract usa
*"within the objective ranges observed in operator-produced pages"*, nunca *"comparable to
human quality"*.

**D4 (reescrita tras la revisión del objetivo general).** La versión anterior de esta decisión
eliminaba el *"from hours of manual editing"* porque ese lado nunca se cronometró. El objetivo
revisado lo reintroduce, así que la decisión se rehace en tres puntos.

**(i) El abstract conserva la cifra; el objetivo no.** No hay contradicción: un objetivo cuyo
umbral se deriva de su propio resultado es circular y no falsable, mientras que un abstract
que reporta un resultado medido no tiene ese problema. El abstract reporta resultados → se
mantiene *"in under two minutes for pages of up to eight articles"*. Es más informativo por
carácter que *"a few minutes"*, y el acotamiento **por tamaño de instancia, no por hardware**
sigue siendo válido tal cual se argumentó: (a) la afirmación es verificable y verdadera dentro
de su alcance declarado; (b) informa de la escala real de una página, dato que si no está
ausente; (c) evita el debate de máquina, ya tratado en el capítulo. El caveat de hardware
(8 núcleos / 32 GB, secuencial, `ngen`=300) **sigue sin ir al abstract**: no cabe con
naturalidad y suena defensivo.

**(ii) El contraste con la edición manual vuelve, pero repartido, no afirmado.** El motivo
original para excluirlo —nadie cronometró el lado manual— sigue siendo válido **para cualquier
afirmación de razón**. Pero el contraste no necesita una frase propia: el Movimiento 1 ya dice
que la producción manual cuesta **horas por edición**, y el Movimiento 4 dice **menos de dos
minutos por página**. El lector hace la comparación; el abstract no la enuncia. Coste: cero
caracteres.

  ⚠ **Consecuencia:** el *"horas por edición"* del Movimiento 1 pasa a ser **portante**. Antes
  era color de contexto; ahora es la base de comparación de la cláusula temporal del objetivo.
  No se poda en ningún recorte.

**(iii) No se mezclan unidades.** *Horas por edición* y *minutos por página* son magnitudes
distintas. El abstract **nunca** debe decir *"an order of magnitude faster"*, *"×30"* ni
ninguna razón entre ambas: la tesis no contiene ningún cronometraje manual **por página** que
la sustente. Fue exactamente por esto que la formulación por orden de magnitud se descartó
también en el objetivo. Ambas magnitudes se enuncian cada una en su unidad y se dejan
convivir.

**D12 (nueva, derivada de la revisión del objetivo).** ¿Entra en el abstract la **tolerancia
industrial declarada** (*a few minutes per page*, requisito del socio ahora documentado en
§2.1 del Capítulo 1)? → **No.**

Dos razones. **Presupuesto:** costaría ~70 caracteres en el Movimiento 2, que es el más
ajustado de los seis (350 caracteres) y ya carga con el objetivo más la dificultad
multi-objetivo/tácita. **Redundancia funcional:** el requisito existe en el manuscrito para
*desarbitrarizar* el objetivo —para que el umbral no parezca elegido a conveniencia—, y esa es
una pregunta que se hace un lector del Capítulo 1, no un lector de abstract. Al lector del
abstract le basta con las dos magnitudes que ya tiene (horas manuales, menos de dos minutos
automatizados) para juzgar si el resultado es relevante.

→ Si el Movimiento 2 acaba con holgura al redactar, es el **primer candidato a reincorporar**.

**D5 (resuelta).** La factibilidad **no se enuncia sola**. "100 % de factibilidad" sin nada
más se lee como *"cumple el mínimo"*, cuando el mensaje real es *"cumple el mínimo que los
demás ni siquiera cumplen, y además con calidad y en tiempo operativo"*. El movimiento cierra
con el **tríptico factibilidad / calidad / tiempo**, que recorre los tres criterios del
objetivo general y demuestra que la tesis logra lo que se propuso:

 …retains 100 % single-page feasibility where decoupled select-then-pack pipelines overflow,
 Pareto-dominates them across the four objectives, and produces pages whose objective values
 fall within the ranges observed in operator-produced pages of the same publisher, in under
 two minutes for pages of up to eight articles.

El tríptico ya **no** reproduce el objetivo palabra por palabra, y no debe intentarlo: el
objetivo enuncia el criterio temporal como magnitud (*a few minutes per page*) y el abstract
lo enuncia como resultado medido (*under two minutes for pages of up to eight articles*). Es
la asimetría deliberada de D4(i). Los otros dos criterios —factibilidad y rangos objetivos—
sí se corresponden literalmente.

Sobre **qué evidencia de calidad** usar: se descarta el hipervolumen con Wilcoxon
(`W = 0, p < 0,001, r = 1,10`). Es lo más fuerte estadísticamente, pero en un abstract los
estadísticos se leen como relleno técnico. Se usa la **dominancia de Pareto** —preferentemente
sin porcentaje, porque "70–100 % de las ejecuciones" es un rango vago— más la afirmación de
rangos objetivos, que es la que responde de verdad a *"¿pero es buena la página?"* sin violar
D3.

**D6 (resuelta).** El abstract **no depende de ninguna sigla no expandida** y **no usa macros
LaTeX que no degraden a texto plano**. Razón: ese mismo texto se copia al portal de depósito
(ADUM / theses.fr) como texto plano, donde cualquier macro se rompe. `GWES`, `TRS` y
`EvoPageGEN` solo aparecen si se expanden en su primera aparición.

**D7 (resuelta).** El resultado de la variante guiada (frente 123 → 18, densidad en la región
de interés ×6–8) va **al final del Movimiento 4**, no en el cierre. Es un argumento distinto
al de calidad frente a baselines —habla de *usabilidad por un editor*— pero pertenece a la
misma contribución y separarlo del Movimiento 4 lo dejaría huérfano.

Formulación, **sin cifras**, en una sola frase:
*"a preference-guided variant further narrows the Pareto front to the region occupied by
historical human designs, turning the generator into a tool an editor can actually browse"*.

Razón de omitir las cifras, ahora más fuerte que a 4000: el Movimiento 4 dispone de ~800
caracteres y ya lleva cinco números (4 449 / 345 / 100 % / <2 min / 8 artículos). Añadir
`123 → 18` y `6,7 % → 58,1 %` lo convierte en una tabla, y la frase de la variante guiada
solo tiene ~150 caracteres asignados. Sin cifras entra; con ellas, no.

---

## 6. Movimiento 5 — Contribución 3 (Capítulo `magnification`)

El giro argumentativo que hay que dejar explícito: **los mismos principios de re-layouting
desarrollados por razones industriales sirven para un problema de accesibilidad.** Sin esa
frase-bisagra, el tercer capítulo parece pegado con cola.

- **Escenario:** *constrained visual access scenarios* (CVAS), dos casos complementarios —
  pantalla pequeña con visión normal, y baja visión incluso en pantalla grande (tablet).
- **Comparación:** magnificación gestual (pan & zoom, el estándar de facto) vs. **edición
  large-print de acceso directo** generada automáticamente por re-layouting.
- **Estudio controlado:** 24 participantes (19 con visión normal, 5 con baja visión
  reclutados en el servicio de oftalmología del CHU Pasteur, Niza), condiciones calibradas
  individualmente por **Critical Print Size** vía test MNREAD, dos tareas (leer todos los
  titulares / localizar un titular objetivo).
- **Hallazgo clave, y es doble:**
  - **Rendimiento:** tiempos de compleción sustancialmente menores en large-print, con la
    ganancia concentrada en los participantes con baja visión.
  - **Integridad conductual (lo verdaderamente novedoso):** el pan & zoom **no solo ralentiza,
    sino que desvía la estrategia de lectura** respecto a la trayectoria natural de la página;
    el large-print la preserva. Esto es lo que un abstract debe destacar, porque el
    resultado "es más rápido" era esperable y el resultado "cambia cómo se lee" no lo era.
  - Preferencia subjetiva (NASA-TLX + pregunta directa) a favor del large-print.

**D8 (resuelta).** No se desglosa el n=5 de baja visión: se dice *"24 participants, including
readers with low vision"*. El desglose y su justificación metodológica están en el capítulo.

**D9 (revisada a la baja por el ajuste a 3000).** A 4000 caracteres entraban las tres cosas:
las cifras de rendimiento (−37 % / −50 %), el hallazgo de la trayectoria **y** su cifra
(69,3 % → 87,5 %). A 3000 el Movimiento 5 baja a ~600 caracteres y cuatro entradas numéricas
(24 / −37 / −50 / 69,3→87,5) lo saturan. Se recorta así:

- **Se mantienen** `24 participantes` y las dos cifras de rendimiento `−37 % / −50 %`.
- **Se suprime la cifra** `69,3 % → 87,5 %`, pero **no el hallazgo**: la preservación de la
  trayectoria de lectura se enuncia **cualitativamente**.

Razón del recorte por ese lado y no por otro: `69,3 % → 87,5 %` es una métrica de similitud
de trayectoria que **necesita explicarse para significar algo** —el lector no sabe respecto a
qué trayectoria de referencia, ni cómo se mide la similitud—, y explicarla cuesta más
caracteres que el hallazgo entero en prosa. Las cifras de tiempo, en cambio, se entienden
solas. Es el caso raro en que la versión sin número es *más* informativa por carácter.

Lo que **no** cambia es el orden retórico, que sigue siendo lo importante: la velocidad va
**subordinada** al cambio de estrategia, nunca al revés. *"Más rápido —y, sobre todo,
preservando la trayectoria de lectura que el pan & zoom desvía"*. El resultado "es más
rápido" era esperable; "cambia cómo se lee" no lo era, y es lo que justifica el capítulo.

---

## 7. Inventario de cifras disponibles (para elegir 7)

**Capítulo template**
- `LayoutGMN` reentrenada: 98 % de accuracy en test; dataset aumentado de 5 341 gabaritos.
- Estudio perceptual: 42 participantes (Prolific), 40 tripletas. → **descartado (D2c)**.
- Clustering: 81 clusters sobre el catálogo Publihebdos.
- `TRS` vs. baselines: **≈2× diversidad estructural**, **≈1,5× cobertura de long-tail**,
  ejecución en milisegundos.
- `GWES`: **Top-1 82,6 % / Top-3 95,1 % / Top-5 97,6 %** con contexto completo, sobre un
  catálogo de 345 gabaritos (test: 232 páginas, 587 artículos).
- Suavizado por `tGMN`: opciones viables por artículo 1,89 → 3,23 (**1,7×**); pico de
  confianza −71 %.

**Capítulo pagegen**
- Corpus: **4 449 páginas de producción** utilizables (de 6 007 extraídas), La Provence.
- Benchmark: 30 instancias reales × 30 semillas.
- Factibilidad de página única: **100 %** vs. desbordamiento de los baselines desacoplados.
- Dominancia de Pareto sobre baselines desacoplados: **70–100 %** de las ejecuciones (n ≤ 6).
- Hipervolumen 4D: superioridad estadística total (Wilcoxon W = 0, p < 0,001, r = 1,10);
  y también en el subespacio 3D del ablado (p = 0,037). → **descartado para el abstract (D5)**.
- Variante guiada: frente de **123 → 18** soluciones; densidad en ROI **6,7 % → 58,1 %**
  (n = 6) y **9,2 % → 47,1 %** (n = 8); p < 0,001, r = 1,03.
- Tiempo de ejecución por página: **56–90 s** (uniforme) y **68,5–111,8 s** (guiada). La
  variante guiada es **más lenta en todos los estratos**, con un sobrecoste estable del
  **21–24 %** que se descompone en la razón de poblaciones (330/286 = +15,4 %) más el coste
  del niching por puntos de referencia de RNSGA-III.
  ⚠ **El margen del "under two minutes" es estrecho**: 111,77 s ± 2,01 en n=8, es decir
  ~118 s a +3σ. La afirmación se sostiene para n ≤ 8, en la configuración de referencia
  (8 núcleos / 32 GB), secuencial y con `ngen`=300 — alcance ya explicitado en el capítulo,
  que además cuantifica la mitigación disponible (`ngen` 300→200 ⇒ ~75 s, ~38 % de margen).
  Si en el abstract se usa una cifra temporal, debe ser esta y no una genérica → resuelto
  en D4(i) acotando por número de artículos.
  ⚠ Este margen estrecho es precisamente lo que motivó **sacar la cifra del objetivo general**
  (que ahora dice *a few minutes per page*): un umbral a ~8 s de su propio peor caso, y además
  dependiente de la máquina, no es un criterio que un objetivo de tesis pueda sostener. Como
  **resultado medido y acotado a n ≤ 8**, en cambio, la cifra es correcta y se mantiene en el
  abstract.

**Capítulo magnification**
- 24 participantes (19 visión normal / 5 baja visión); 18 páginas de estímulo.
- Tarea 1 (leer titulares): **−37 %** de tiempo global (71,7 s → 45,2 s); **−42 %** en baja
  visión (114,7 s → 66,3 s); −16 % en visión normal.
- Tiempo de transición entre artículos: **−57 %** en baja visión (8,0 s → 3,5 s).
- Similitud con la trayectoria de lectura de referencia: **69,3 % → 87,5 %**.
- Tarea 2 (localizar titular): **−50 %** de tiempo (18,7 s → 9,2 s), consistente en ambos grupos.
- **100 %** de los participantes fueron más rápidos con large-print.
- 12,5 % prefirió pan & zoom pese a rendir peor (sensación de control) — matiz honesto,
  probablemente fuera del abstract incluso con 4000 caracteres: es un contra-matiz que
  necesita explicación para no restar.

### Selección final para el abstract de 3000 (7 afirmaciones, ~10 numerales)

| # | Cifra | Qué sostiene | Mov. |
|---|---|---|---|
| 1 | **+150 redacciones** (despliegue de Melody) | escala industrial del problema | 1 |
| 1b | **horas por edición** (coste manual actual) | base de comparación de la cláusula temporal del objetivo; portante desde D4(ii) | 1 |
| 2 | **82,6 %** de Top-1 sobre asignaciones históricas reales | el estilo editorial tácito **es** aprendible | 3 |
| 3 | **4 449 páginas** de producción y **345 gabaritos** (La Provence) | no es un juguete académico | 4 |
| 4 | **100 %** de factibilidad de página única vs. desbordamiento de los desacoplados | la tesis central: hay que optimizar conjuntamente | 4 |
| 5 | **< 2 min** para páginas de hasta **8** artículos | viabilidad operativa, acotada y verificable; evidencia del criterio temporal del objetivo | 4 |
| 6 | **24 participantes** | escala del estudio controlado | 5 |
| 7 | **−37 % / −50 %** de tiempo de lectura y de localización | resultado de rendimiento | 5 |

Reparto: 1 cifra al contexto, 1 a la contribución 1, 3 a la contribución 2, 2 a la
contribución 3. Es deliberado y refleja el peso relativo de las tres contribuciones.

La entrada **1b no consume plaza numérica**: *"horas"* es una magnitud sin numeral, y por eso
el tope de siete afirmaciones numéricas se mantiene intacto. Se tabula igualmente porque
desde D4(ii) sostiene una afirmación del objetivo y hay que protegerla de las podas.

~~**Primera poda si el borrador se pasa de 3000:** `−37 %`, dejando solo `−50 %` (tarea de
localización, que es la caída más grande y la consistente en ambos grupos).~~
**Regla retirada el 2026-08-28: era incorrecta.** Las dos cifras no son intercambiables.
`−37 %` (Tarea 1, leer titulares) es la que concentra el efecto en baja visión —−42 % en
lectores \LV frente a −16 % en visión normal, `magnification/results.tex:151`—, mientras que
`−50 %` (Tarea 2, localizar) es *consistente entre grupos* —−51 % NV / −50 % LV,
`results.tex:310`—. Podar `−37 %` borra la única evidencia numérica de *"la ganancia concentrada
en los participantes con baja visión"*, que §6 declara parte del hallazgo clave, y además
obligaría a reescribir la frase: mantener *"los mayores beneficios para los lectores
malvoyants"* junto a `−50 %` sería **factualmente incorrecto**.

**Primera poda, sustituta:** `345 gabaritos` (antes segunda, ver D10). No tocar las cuatro
primeras ni la 1b: son las que sostienen afirmaciones que sin cifra se vuelven vacías.

**Descartadas conscientemente:**

| Cifra | Motivo |
|---|---|
| 42 participantes (estudio perceptual) | D2c — colisiona con el estudio del título y es riesgo asimétrico |
| 69,3 % → 87,5 % (trayectoria) | D9 — la métrica necesita explicación; el hallazgo entra en prosa |
| Wilcoxon `W = 0, p < 0,001, r = 1,10` | D5 — los estadísticos se leen como relleno técnico |
| `123 → 18` y densidad en ROI | D7 — el Movimiento 4 ya va saturado de números |
| 98 % de accuracy de la GMN reentrenada | métrica interna de un componente, no de una contribución |
| 5 341 gabaritos aumentados / 81 clusters | D10 — pertenecen a otros componentes y a otro editor |
| ≈2× diversidad / ≈1,5× long-tail | el retrieval entra descrito, no cuantificado |
| 12,5 % de preferencia por pan & zoom | contra-matiz honesto que necesita explicación para no restar |
| −57 % de tiempo de transición en baja visión | redundante con −37 % / −50 % |

**Sobre "template".** La palabra **se usa y no es opcional**: el título ya dice *"Learned
Template Retrieval"*. Y sí es terminología estándar, por partida doble — en la práctica del
oficio (los *page templates* / *master pages* de InDesign y QuarkXPress son el objeto que
Melody llama gabarito) y en la literatura de generación automática de layout, donde
*template-based layout generation* es una familia de métodos con nombre propio. El riesgo no
es que no se entienda, es la ambigüedad con "plantilla de contenido" (un esqueleto de texto),
y para eso basta una glosa de dos o tres palabras en su primera aparición:
*"predefined geometric page templates"*, ~20 caracteres.

**D10 (resuelta y verificada).** El tamaño del catálogo es **345**, y es el mismo objeto para
la contribución principal. A 3000 caracteres es la **segunda cifra a podar** si el borrador
se pasa, pero entra de partida porque cuesta ~15 caracteres al ir pegada al corpus:

- `chapters/template/sections/gwes.tex:109` — *"The structural template catalog
  $\templatecatalog$ is composed by $\catalogsize = 345$ designs from `\laprovence`"*.
- `chapters/pagegen/sections/problem-formalization.tex:16-18` — la variable de decisión
  `\templatesel{i}` recorre $\{1,\dots,\catalogsize\}$ sobre **ese mismo** `\templatecatalog`.
- `chapters/pagegen/sections/results.tex:27` — confirma explícitamente que el catálogo
  estático viene *"from the same newspaper group"* que el corpus de páginas.

Es decir: no hay dos catálogos, hay uno solo (La Provence, 345 gabaritos) compartido por
`GWES` y por el motor evolutivo. Los otros dos números pertenecen a componentes distintos y
**no** van al abstract: 5 341 es el dataset **aumentado** de entrenamiento de la GMN
(variantes sintéticas por eliminación de imágenes, `recsys.tex:240`), y 81 son los clusters
del catálogo **Publihebdos**, que es otro editor.

→ En el Movimiento 4: *"4,449 production pages and a catalogue of 345 templates from La
Provence"*. Las dos cifras describen el mismo escenario y se refuerzan mutuamente.

---

## 8. Palabras clave (6 + 6)

**Inglés** — candidatas:
`automated document layout` · `automated newspaper layout` ·
`multi-objective combinatorial optimization` · `evolutionary algorithms` ·
`newspaper design` · `template retrieval` · `graph neural networks` ·
`low-vision accessibility` · `large-print` · `human-centered computing`

→ **Selección final (6):**
`automated newspaper layout` · `multi-objective combinatorial optimization` ·
`evolutionary algorithms` · `template retrieval` · `large-print` ·
`low-vision accessibility`

Criterio aplicado: se evitan solapes (`automated newspaper layout` ya cubre `newspaper
design`) y se evita repetir literalmente el título más allá de lo necesario, porque en la
mayoría de índices el título se indexa junto a las keywords.

**D11 (resuelta a favor de `large-print`).** Se descarta `graph neural networks`. Los dos
argumentos que lo descartan son buenos y el segundo es decisivo:

1. *Atribución.* La GMN se **adaptó**, no se propuso. Una keyword no es una reivindicación de
   autoría —es un término de indexación— pero sí fija la expectativa del lector que llega por
   ella, y quien busca `graph neural networks` espera una contribución de arquitectura y aquí
   encontraría una aplicación. La expectativa defraudada es un coste real.
2. *Cobertura, y este es el argumento que zanja.* `low-vision accessibility` **no cubre la
   contribución 3 entera**: el estudio abarca dos escenarios de acceso visual restringido
   (CVAS) —pantalla pequeña con visión normal, y baja visión incluso en pantalla grande—.
   Con solo `low-vision accessibility`, la mitad del estudio queda fuera del índice. El par
   `large-print` + `low-vision accessibility` sí cubre el objeto completo: la **intervención**
   (large-print por re-layouting) y la **población** (baja visión). Ninguna keyword individual
   hace ese trabajo.

Coste asumido: el lado de aprendizaje automático no tiene término propio en la lista. Queda
parcialmente anclado por `template retrieval`, que en el título aparece como *"**Learned**
Template Retrieval"*, y por el propio abstract, que nombra la Graph Matching Network y el
Transformer encoder en texto corrido. Es un coste menor: nadie busca una tesis de generación
de layout tecleando `graph neural networks`, mientras que `large-print` sí es un término por
el que esta tesis debería aparecer y hoy casi nada lo ocupa.

Lo que **no** cubre ninguna de las seis: el escenario de pantalla pequeña con visión normal.
No hay término estándar y searchable para eso (`constrained visual access` es nomenclatura
propia de la tesis, no de la comunidad), así que se acepta la laguna en vez de gastar una
plaza en un término que nadie buscaría.

**Francés** — traducción alineada (6):
`mise en page automatisée de journaux` · `optimisation combinatoire multi-objectif` ·
`algorithmes évolutionnaires` · `recherche de gabarits` · `gros caractères` ·
`accessibilité basse vision`

Nota de terminología: se usa **`gabarit`**, que es el término del oficio en francés y el que
emplea Melody, en lugar de `modèle` o `template`.

---

## 9. Cosas a evitar explícitamente

- **No** decir "IA" ni "inteligencia artificial" a secas: la tesis usa una GMN, un
  Transformer y un algoritmo evolutivo, cada uno con un rol preciso. La imprecisión aquí
  invita preguntas incómodas.
- **No** prometer paridad con operadores humanos (ver D3).
- **No** enunciar ninguna razón entre el tiempo manual y el automatizado —*"an order of
  magnitude faster"*, *"×30"*, *"from hours to minutes"* como afirmación de mejora medida—.
  Las unidades no son las mismas (horas **por edición** vs. minutos **por página**) y la tesis
  no cronometra el trabajo manual por página. Ambas magnitudes se enuncian por separado, cada
  una en su unidad, y el lector compara (ver D4(iii)).
- **No** meter las cifras de crisis del sector (contexto, no contribución).
- **No** usar sinónimos variables para el mismo objeto: *template* siempre *template*
  (nunca *layout skeleton*, *blueprint*, *design*); *page* siempre *page*.
- **No** dejar `GWES`, `TRS`, `EvoPageGEN` . mejor no usar la sigla (ver D6). NO USAR LA SIGLA, POR SI EL NOMBRE DEL ALGORITMO CAMBIA ENTONCES EL ABSTRACT QUEDARA OBSOLETO.
- **No** usar macros LaTeX en el abstract: el texto se reutiliza en plano en la plataforma.
- **No** gastar los 3000 caracteres en detalle de método. El presupuesto está asignado a
  **evidencia** (cifras que sostienen afirmaciones) y a **argumento** (la frase-bisagra del
  Movimiento 5, el tríptico del Movimiento 4), no a descripción técnica. Regla práctica: se
  dice **qué hace** cada componente y **qué demuestra**, nunca **cómo está construido**.
- **No** subir a 4000 "ya que la plataforma lo permite". 3000 es una elección, no un límite:
  la diferencia se la comería el detalle de método, que es justo lo que no aporta.
- Voz: **pasiva académica, tercera persona del singular**, coherente con el resto de la tesis.

---

## 10. Pendientes del manuscrito — NO CONSIDERAR PARA EL ABSTRACT, ASUMIR QUE ESTÁN HECHOS

Conviene tenerlos presentes: el abstract se somete antes, pero describe un documento que
debe existir.

- [ ] `chapters/conclusion/conclusion.tex` está **vacío** (solo el `\chapter{}`).
- [ ] Secciones de estado del arte **vacías o con notas**: `template/sections/sota.tex`,
      `pagegen/sections/sota.tex`, `magnification/sections/sota.tex`.
- [ ] `chapters/template/sections/template-definition.tex` vacío (0 líneas).
- [ ] Definición formal de `tGMN` marcada con *"EXPLAIN IN DETAIL"* / *"FINISH DEFINING GMN"*.
- [ ] Secciones de datasets `Publihebdos` y `La Provence` (`definitions/main.tex`) sin contenido.
- [ ] `biblio.bib` **vacío**; las referencias siguen repartidas en `biblio_temp.bib`,
      `biblio_study.bib`, `biblio_nsga.bib`. Varias citas son `placeholder-*`.
- [ ] `\chapter{Publications}` en `main.tex` contiene solo `---`.
- [x] ~~Tabla de runtime de `EvoPageGEN-RNSGA-III`~~ — hecha (`tab:exec_time_rnsga_comparison`,
      nueva subsección *Execution Time* dentro de la comparación guiada vs. uniforme), con
      el análisis del sobrecoste. La discusión quedó también corregida.
- [x] ~~Paralelización a nivel de edición~~ — **descartado deliberadamente**. Toda la
      formulación es single-page por restricción dura ($\pageindex{i} = 1$); introducir un
      nivel de edición que la tesis nunca modela añadiría complejidad sin sostén formal.

---

## 11. Estado de las decisiones

| ID | Pregunta | Estado |
|---|---|---|
| D0 | Longitud del abstract | ✅ **~3000 caracteres**, un solo texto para plataforma y `resume.tex` |
| D1 | ¿Nombrar Melody / Demain Un Autre Jour? | ✅ sí, en una sola aposición; CIFRE no se menciona |
| D1b | ¿Nombrar La Provence? | ✅ sí |
| D2 | ¿Cuántas piezas de la contribución 1? | ✅ las tres, en orden métrica → retrieval → scoring |
| D2b | ¿Sigla `TRS` o descripción sin sigla? | ✅ sin sigla: *diversity-aware template retrieval framework* |
| D2c | ¿Entra el estudio perceptual de 42 participantes? | ✅ no |
| D3 | ¿Se afirma paridad con operadores humanos? | ✅ no: *"within the objective ranges observed…"* |
| D4 | ¿Cómo se acota el *"under two minutes"*? | ✅ **reescrita**: el objetivo enuncia magnitud (*a few minutes per page*), el abstract reporta la cifra medida, acotada por tamaño de instancia (≤ 8 artículos) y no por hardware; el contraste con las horas manuales se reparte entre Mov. 1 y Mov. 4, sin afirmar ninguna razón |
| D5 | ¿Factibilidad sola o tríptico? | ✅ tríptico factibilidad / calidad / tiempo |
| D6 | ¿Macros y siglas en el abstract? | ✅ ninguna macro; siglas solo si se expanden |
| D7 | Variante guiada: ¿dónde y con cifras? | ✅ final del Movimiento 4, sin cifras |
| D8 | ¿Se desglosa el n=5 de baja visión? | ✅ no: *"24 participants, including readers with low vision"* |
| D9 | ¿Rendimiento o trayectoria de lectura? | ✅ ambos, pero la trayectoria **sin cifra**; velocidad subordinada a ella |
| D10 | Tamaño del catálogo de gabaritos | ✅ **345** (La Provence), verificado en el manuscrito |
| D11 | Sexta keyword | ✅ `large-print` (se descarta `graph neural networks`) |
| D12 | ¿Entra la tolerancia industrial declarada? | ✅ no; primer candidato a reincorporar si el Mov. 2 queda con holgura |

**No queda ninguna decisión abierta.** El documento está listo para redactar la primera
versión del abstract: ~3000 caracteres, seis movimientos con el presupuesto de §1, las siete
afirmaciones numéricas de §7 y las seis palabras clave de §8.

**Sincronización con el manuscrito (2026-08-28).** El objetivo general fue revisado en
`chapters/context/main.tex:194` y este documento está alineado con esa versión. 
---

