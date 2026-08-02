# Auditoría de artistas y bandas en TikTok

Fecha de corte: 26 de julio de 2026  
Catálogo analizado: 469 videos de `tiktok_own_videos.json`

## Resumen ejecutivo

- Se identificó un protagonista principal en 440 de 469 videos (93.8%).
- Los 29 restantes son publicaciones genéricas, recuerdos sin contexto suficiente, promoción de música propia o clips cuyo caption no identifica con seguridad al protagonista.
- Aparecen 241 entidades distintas en captions o hashtags: 130 artistas y 111 bandas.
- Han sido protagonistas principales 202 entidades: 109 artistas y 93 bandas.
- La mediana del canal es 5,168 vistas. El umbral del 10% superior es 85,195 vistas.
- “Mención” no equivale a “video sobre esa persona”. Ejemplo: Chris Cornell aparece en videos cuyo protagonista es Soundgarden, Jimmy Page, Toni Cornell o Mad Season.
- La saturación más evidente hoy no es de artistas aislados sino de series consecutivas: Weiland, Layne/Mad Season, Frusciante y Linkin Park concentran 18 de los últimos 38 videos (47.4%).

## Cómo se hizo el conteo

Cada video recibió:

1. Un protagonista principal exclusivo, determinado por la entidad con mayor presencia al inicio del título/caption y su posición en el texto.
2. Todas las menciones secundarias reconocibles.
3. Un ecosistema que agrupa proyectos relacionados sin mezclarlos en el inventario. Por ejemplo:
   - Chris Cornell, Soundgarden, Audioslave y Temple of the Dog permanecen separados.
   - Para medir concentración temática también se suman bajo el ecosistema `Cornell`.
4. Indicadores de cobertura: total, últimos 90 días, mediana de vistas, share rate, hits dentro del 10% superior, mejor video y enfoques dominantes.

El análisis de ángulos se basa en captions, no en inspección visual cuadro por cuadro. La API disponible tampoco trae curvas de retención por segundo.

## Ecosistemas con mayor cobertura

| Ecosistema | Videos principales | Últimos 90 días | Mediana vistas | Mediana reciente | Hits top 10% | Lectura |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pearl Jam | 18 | 1 | 10,502 | 2,174 | 1 | Catálogo profundo; reciente débil |
| Pink Floyd | 18 | 0 | 10,636 | — | 2 | Catálogo profundo, especialmente técnica e historia |
| Weiland | 16 | 5 | 10,880 | 13,134 | 2 | Concentración reciente y fatiga de serie |
| Cerati / Soda Stereo | 14 | 1 | 3,870 | 19,032 | 1 | Mucho histórico, pero la señal reciente revivió |
| Guns N' Roses | 14 | 1 | 6,001 | 16,884 | 2 | Profundo, pero todavía responde con conexiones nuevas |
| Cornell | 13 | 1 | 8,052 | 7,524 | 0 | Profundo; faltan hits top 10% propios |
| Led Zeppelin | 13 | 0 | 31,892 | — | 4 | Profundo y excepcionalmente productivo |
| Alice in Chains / Layne / Mad Season | 12 | 5 | 7,520 | 10,033 | 1 | Concentración reciente; un gran outlier de Layne |
| Grohl / Foo Fighters | 10 | 2 | 2,640 | 2,025 | 2 | Catálogo amplio, retorno reciente bajo |
| RHCP / Frusciante | 8 | 4 | 21,218 | 28,930 | 2 | Concentrado, pero todavía productivo |
| Depeche Mode | 8 | 1 | 16,730 | 4,406 | 3 | Históricamente fuerte; reciente flojo |
| Beatles | 8 | 0 | 10,521 | — | 0 | Amplio, sin hit top 10% |
| Nirvana | 8 | 0 | 7,314 | — | 1 | Buen potencial, pero dependiente de un outlier |
| Nine Inch Nails | 7 | 3 | 1,601 | 1,601 | 2 históricos | Tema agotado en su forma reciente |
| Radiohead / Thom Yorke | 7 | 1 | 2,587 | 507,208 | 1 | Señal reciente extraordinaria que merece réplica |

## Qué está saturado

### Saturación reciente real

**Scott Weiland**

La serie de cinco partes pasó por 38,395; 2,462; 13,134; 15,308 y 4,231 vistas. La mediana es buena, pero el final perdió 89% frente a la primera parte. No conviene publicar otra serie de Weiland de inmediato. El desgaste es del formato serial y del enfoque tragedia/expulsión, no necesariamente del interés por STP.

**Layne Staley / Mad Season / Alice in Chains**

El video aislado de Layne llegó a 935,409. La serie posterior de Mad Season hizo 10,033; 10,571; 8,286 y 6,755. El descenso entre la primera y la última parte fue de 32.7%. Layne no está “agotado”: el ángulo de última entrevista, muerte y descenso personal sí está sobreexplotado, y Mad Season no heredó automáticamente el alcance del outlier.

**John Frusciante / RHCP**

La serie hizo 282,264; 31,115 y 26,745. Las partes 2 y 3 superaron ampliamente la mediana del canal, pero perdieron alrededor de 90% frente al gancho inicial. El ecosistema sigue siendo productivo, aunque no conviene encadenar otra biografía descendente.

**Linkin Park**

La serie hizo 5,425; 30,926; 47,489 y 19,882. No muestra rechazo al tema; muestra que cada parte funcionó casi como video independiente. Es mejor convertir futuras series en episodios autónomos con contexto completo.

**Nine Inch Nails**

Los tres videos recientes hicieron 1,068; 1,601 y 4,274. Aquí sí hay una señal débil consistente. Debe pausarse salvo que Creator Search Insights muestre una búsqueda concreta o exista una noticia fuerte.

**Grohl / Foo Fighters**

Los dos videos recientes quedaron en 1,926 y 2,124. El catálogo tiene dos grandes outliers históricos, pero la propuesta actual no está respondiendo. Pausar y cambiar el enfoque antes de repetir.

### Catálogo profundo que requiere ángulo nuevo

**Cornell**

El ecosistema suma 13 protagonistas, mediana de 8,052 y mejor video de 67,933: buen piso, pero ningún hit dentro del top 10% del canal. Los enfoques más repetidos son instrumento/voz, legado/historia, presentaciones y adversidad. No falta “otro video biográfico de Cornell”; faltan preguntas específicas, controversias verificables, canciones concretas, decisiones creativas y miembros secundarios de Soundgarden.

**Pearl Jam**

Es el ecosistema más cubierto: 18 videos. Su único video reciente hizo 2,174 frente a una mediana histórica de 10,502. Antes de volver, el tema debe tener búsqueda demostrable o una noticia y no otra pieza general de legado.

**Pink Floyd**

También suma 18 videos. Trece tocan instrumento/técnica y once historia/legado. La banda todavía tiene buen share rate, pero esos dos enfoques están repetidos. Sólo vale regresar con una brecha muy específica.

**Guns N' Roses**

Tiene 14 videos, pero el reciente sobre Shannon Hoon llegó a 16,884. El hallazgo fue usar una conexión oculta —un personaje conocido alrededor de una historia menos conocida—, no repetir la biografía de Axl o Slash.

**Cerati / Soda Stereo**

Tiene 14 videos y una mediana histórica modesta, pero la noticia del documental hizo 19,032. No debe considerarse agotado: funciona mejor con actualidad, archivos inéditos y consecuencias concretas que con homenajes generales.

**Led Zeppelin**

Tiene 13 videos, una mediana de 31,892 y cuatro hits top 10%. Es un tema profundo, pero no saturado por rendimiento. Puede volver de manera espaciada con historias nuevas; no necesita una pausa total.

## Dónde falta hablar más: señales internas fuertes

### Prioridad inmediata: señal reciente

1. **Thom Yorke / Radiohead**  
   El video reciente llegó a 507,208. El ecosistema tiene siete videos, pero su mediana baja refleja piezas anteriores débiles. Conviene probar dos videos autónomos que conserven el patrón del ganador: una pieza musical casi perdida, censura/conflicto y un personaje inesperado.

2. **Def Leppard**  
   Cuatro videos, mediana de 19,294 y uno reciente de 35,999. La combinación de regreso, Latinoamérica, espera histórica y ciudades específicas funcionó. Hay espacio para historias locales y decisiones detrás de giras, no sólo clips en vivo.

3. **Billy Corgan / Smashing Pumpkins**  
   Seis videos; el reciente hizo 23,867. El formato de dos figuras analizando una escena o mito funcionó mejor que el catálogo general de la banda.

4. **Cerati / Soda Stereo**  
   Aunque el catálogo es amplio, la actualidad produjo 19,032 frente a una mediana histórica de 3,870. Debe tratarse como franquicia reactiva a noticias y archivos, no como biografía recurrente.

5. **Guns N' Roses mediante personajes periféricos**  
   El video de Shannon Hoon hizo 16,884. La oportunidad no es más Axl/Slash, sino conexiones ocultas, músicos no acreditados y decisiones de estudio.

### Segunda prioridad: pilotos históricos que merecen revalidación

Estos temas tienen muy poca cobertura y al menos una señal fuerte. Deben probarse con un video original de 60–90 segundos antes de producir una serie:

| Tema | Videos del ecosistema | Mediana vistas | Mejor video | Lectura |
| --- | ---: | ---: | ---: | --- |
| The Doors / Jim Morrison | 2 | 85,316 | 164,934 | Muy buen rendimiento y share |
| Alice Cooper | 1 | 124,766 | 124,766 | Piloto ganador, cero repetición |
| Annie Lennox / Eurythmics | 1 | 98,698 | 98,698 | Piloto ganador y buen share |
| Shirley Manson / Garbage | 2 | 50,835 | 100,185 | Buen personaje, baja cobertura |
| Billy Gibbons / ZZ Top | 1 | 79,764 | 79,764 | Cerca del top 10%; historia visual memorable |
| Fito Páez | 1 | 69,868 | 69,868 | Señal latina fuerte y buen share |
| Mark Knopfler / Dire Straits | 1 | 62,462 | 62,462 | Autoridad musical sin saturación |
| Crowded House | 1 | 57,517 | 57,517 | Share muy alto; requiere formato original |
| Pantera / Rex Brown | 1 | 50,673 | 50,673 | Buena primera prueba |
| Kid Rock | 2 | 75,972 | 123,885 | Funciona, aunque debe evaluarse afinidad de marca |

Journey, Poison/Bret Michaels y Marilyn Manson tienen resultados históricos todavía mayores, pero pueden estar dominados por outliers o por formatos de clip antiguos. Antes de priorizarlos hay que comparar duración, originalidad y capacidad real de monetización, no sólo vistas.

## Temas realmente ausentes

Una búsqueda literal en los 469 captions no encontró cobertura de:

- Deftones o Chi Cheng
- Slipknot, Joey Jordison o Paul Gray
- Motörhead o Lemmy
- Type O Negative o Peter Steele
- Lynyrd Skynyrd
- Rush
- The Who
- Bruce Springsteen
- Ramones
- Mötley Crüe, Vince Neil o Razzle
- Cliff Burton
- Randy Rhoads

Esto demuestra un hueco de catálogo, no una oportunidad de demanda. Ninguno debe producirse sólo porque falta. El siguiente filtro debe ser Creator Search Insights: volumen, crecimiento, brecha de contenido y ajuste con audiencia en México/Latinoamérica.

Jeff Buckley y Tom Petty aparecen como menciones, pero nunca como protagonistas. Taylor Hawkins sólo tiene un protagonista antiguo de 590 vistas; por ahora es una prueba débil, no un ganador.

## Recomendación editorial

Durante los próximos 10 videos:

- 4 pruebas sobre señales recientes: Radiohead/Thom Yorke, Def Leppard, Corgan/Smashing Pumpkins, Cerati o una conexión periférica de Guns N' Roses.
- 3 revalidaciones de pilotos históricos: The Doors/Jim Morrison, Alice Cooper, Annie Lennox, Shirley Manson/Garbage, Fito Páez, Mark Knopfler o Pantera.
- 2 huecos confirmados primero en Creator Search Insights.
- 1 regreso a una franquicia profunda sólo si el ángulo es nuevo y autocontenido.

No publicar por ahora otra serie consecutiva de Weiland, Mad Season/Layne, Frusciante o Linkin Park. Si se vuelve a ellos, cada entrega debe poder entenderse sin “Parte 1/2/3” y separarse con otros artistas entre publicaciones.

## Validación inicial en Creator Search Insights

Capturas recibidas el 26 de julio de 2026, dentro de `Brecha de contenido`.

### Deftones: validación parcial positiva

La búsqueda sí devuelve un ecosistema grande, pero la mayor parte de la demanda visible es estética, fandom o cruce cultural: `deftones jersey` (245K), `dbz deftones` (352K), `deftones fans` (292K), `deftones tattoos` (283K), `deftones mustang` (280K; +516.7%) y `deftones nick diaz` (224K; +158.9%).

La oportunidad narrativa más compatible con Rockwise Tales es `is deftones demonic`: 225K de popularidad mostrada por TikTok. También merecen exploración `deftones top` (29.4K; +1000%+) y `deftones 2026`, aunque esta última sólo muestra 700 y no justifica producción todavía.

Conclusión: **Deftones queda en amarillo/verde**. Existe demanda, pero no está validada una biografía tradicional ni Chi Cheng. Antes de producir hay que buscar por separado `Chi Cheng`, `Deftones historia`, `Deftones canciones significado` y `is Deftones demonic`, y revisar si los resultados corresponden realmente a la banda.

### Slipknot: no validado todavía

El resultado está contaminado por otros significados de “slip knot”, productos, tutoriales, videojuegos y cosplay: `slipknot shoes`, `slip knots`, `slipknot tutorial`, `How To Do A Slip Knot`, `slipknot costume`, `slipknot aov`, `smite slipknot`, `slipknot fortnite`, `slip knot tutorial tinsel` y `Slipknot braid`.

Hay demanda alrededor de la marca, pero esta captura no demuestra demanda por historias musicales. Conclusión: **Slipknot queda en amarillo**, no en verde. Las búsquedas correctas para la siguiente ronda son `Joey Jordison`, `por qué despidieron a Joey Jordison`, `Paul Gray Slipknot`, `Slipknot historia` y `Slipknot canciones significado`.

### Lemmy: búsqueda inválida por ambigüedad

Los resultados visibles pertenecen principalmente a homónimos, personajes o frases: `Oh please Lemmy`, `Lemmy Koopa`, `Lemmy P W Y P`, `Scotty and Lemmy`, `Lemmy has 2 babies`, `Lemmy funny moments` y otros.

No existe señal suficiente de Motörhead en esta captura. Conclusión: **Lemmy sigue sin validar**. Debe repetirse con `Lemmy Kilmister`, `Motörhead`, `Lemmy última entrevista`, `Lemmy historia` y `Lemmy documental`.

### Regla confirmada

La cifra de popularidad sólo es útil después de comprobar la intención de búsqueda. No se sumarán resultados de productos, memes, personajes, videojuegos o tutoriales como demanda musical.

### Ampliación de las capturas

La lista extendida de Deftones confirma que el cluster dominante es una estética cultural: parejas, tatuajes, edits, Berserk, Dragon Ball, autos, ropa y fandom. No aparecen nuevas preguntas biográficas claras. `is deftones demonic` continúa siendo el único ángulo narrativo de volumen alto visible en estas capturas.

La lista extendida de Slipknot continúa dominada por productos, cosplay, videojuegos, tutoriales y el significado literal de “slip knot”. Aparece contenido musical de reacción, pero no una brecha documental suficiente para Rockwise Tales. La banda no queda descartada; debe validarse mediante nombres propios como Joey Jordison o Paul Gray.

La pantalla general de brechas sí descubre una línea editorial distinta:

- `IndieRockMusic`: 108K.
- `Art rock`: 93.6K y crecimiento de 1000%+.
- `Postpunk`: 35.2K y crecimiento de 1000%+.
- `deathmetal`: 579K.
- `a punk`: 223K y crecimiento de 1000%+.

Son brechas de género, no de artista. Pueden servir para videos informativos rápidos —por ejemplo, “qué hace que una banda sea post-punk”—, pero antes deben buscarse variaciones con intención clara: `post punk bands`, `art rock bands`, `historia del post punk`, `qué es art rock` y equivalentes en español.

## Archivos generados

- Inventario completo: `tiktok_artist_catalog_audit_2026-07-26.csv`
- Datos, clasificación por video y ecosistemas: `tiktok_artist_catalog_audit_2026-07-26.json`
- Script reproducible: `scripts/tiktok_artist_catalog_audit.py`
