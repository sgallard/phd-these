# Nota interna: por qué los aspiration vectors usan las 4,449 páginas completas (no filtradas)

Esto NO va en la tesis. Es solo preparación por si alguien pregunta por qué el cómputo de los
aspiration vectors (percentiles 25 y 50 de f1-f4, estratificados por numarticles, ver nsga.tex
~line 406-413) usa las 4,449 páginas utilizables de La Provence completas, en lugar de restringirse
al pool de 2,775 páginas (exact-match + admissible-elasticity) que sí se usa para filtrar el
conjunto elegible de las 30 instancias de benchmark.

## Contexto del "error"

Originalmente se asumió (incorrectamente, en una iteración de esta sección) que el cómputo de
aspiration vectors también se restringía al pool de 2,775. En la práctica, no fue así: se usaron
las 4,449 páginas sin filtrar por el bucket de elasticidad. Al revisar si esto es un problema real,
la conclusión es que no lo es, por las siguientes razones.

## Por qué no es un problema

1. **Magnitud acotada**: las páginas con elasticidad no admitida (>15% o <-15%, "unallowed
   elasticity") son 721 de 4,449 (~16%). No son la mayoría del corpus, así que su influencia sobre
   los percentiles 25/50 por estrato de numarticles es limitada, y además se diluyen entre los
   distintos estratos (no están concentradas en un único numarticles).

2. **El efecto está acotado a f2 y f3, no a todo el vector objetivo**: un artículo estirado más allá
   del rango admisible por su template afecta específicamente el objetivo de estilo (f2, desviación
   respecto a la relación de aspecto/estilo canónico del template) y el objetivo de capacidad de
   texto (f3, penalización por exceso/déficit de capacidad), ya que ambos dependen directamente de
   cuánto se deformó el template respecto a su geometría nominal. No afecta directamente a f1
   (cobertura) ni a f4 (alineación/posición), que dependen de otras variables de la solución. Esto
   significa que la "contaminación" del pool no filtrado se refleja como valores más altos (peores,
   bajo minimización) específicamente en f2/f3 para esa fracción de páginas, sin distorsionar el
   resto del vector objetivo.

3. **Es visible y consistente con el propio diseño de la métrica de percentiles**: este efecto se
   observa en los parallel coordinates plots (algunas trayectorias con f2/f3 más altos que el resto
   dentro de un mismo estrato), es decir, no es un artefacto oculto sino algo que el propio análisis
   exploratorio ya deja ver.

4. **Argumento adicional (no discutido originalmente)**: el propio texto de nsga.tex ya describe el
   percentil 50 (mediana) como reflejo del "standard of typical professional practice" -- incluir
   estas páginas con elasticidad extrema en el cómputo de la mediana es, si acaso, más fiel a la
   práctica profesional real (que incluye compromisos y decisiones imperfectas) que un pool
   artificialmente idealizado. El argumento es más débil para el percentil 25 (el punto "exigente"),
   pero incluso ahí el efecto es marginal por los puntos 1 y 2.

## Conclusión

No hace falta re-computar los aspiration vectors sobre el pool filtrado de 2,775. La decisión de
usar las 4,449 páginas completas es defendible y, en todo caso, coherente con el objetivo de que la
mediana capture la práctica profesional real. Si se pregunta en una defensa, esta nota resume el
argumento; no se incluyó en el texto de la tesis para no sobrecargar la sección con una discusión
que no aporta al lector promedio.
