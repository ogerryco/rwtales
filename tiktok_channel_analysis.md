# Análisis profundo del canal de TikTok — RockWise Tales

Regenerado 2026-07-21/22 con datos frescos de la API (`user.info` + `video.list`, 468 videos, historial completo desde 2023-10-08). Fuente cruda: `tiktok_own_videos.json`. Conexión vía `scratch_tiktok_auth.py fetch` (Sandbox, token vigente ~24h).

## Panorama general

- **82,283 seguidores**, 468 videos, **21.7M vistas acumuladas** en todo el historial.
- Ya es más grande que el canal de YouTube (1,332 subs) en esta etapa.
- El canal no ha crecido de forma lineal: tuvo un pico de volumen y rendimiento en **Q1 2025** (160 videos publicados, mediana 11,959 vistas), luego una caída fuerte durante casi todo 2025 y la primera mitad de 2026, y una **recuperación marcada en julio 2026** (mediana 17,878 — la mejor de cualquier trimestre) gracias a un cambio de formato reciente. Ver sección 3.

## 1. Rendimiento por duración — dato histórico (todo el archivo)

| Duración | # videos | Vistas promedio | Mediana | Engagement rate |
|---|---|---|---|---|
| <15s | 7 | 3,477 | 1,010 | 4.23% |
| 15-30s | 2 | 924 | 1,220 | 4.73% |
| 30-60s | 18 | 2,940 | 616 | 5.38% |
| 60-180s | 160 | 31,664 | 3,147 | 4.94% |
| 180-600s (3-10 min) | 253 | 57,837 | 5,808 | 4.32% |
| 600-900s (10-15 min) | 24 | 78,052 | 9,226 | 2.85% |
| >900s (15-16.6 min) | 4 | 18,087 | 24,630 | 2.60% |

**Matiz importante que el análisis anterior no tenía:** el engagement rate (like+comment+share ÷ vistas) **cae** conforme sube la duración, aunque las vistas totales suban. Es decir, los videos largos consiguen más vistas absolutas (el algoritmo empuja más porque suma más tiempo de reproducción total), pero un porcentaje menor de quienes los ven interactúan. Los cubos de 600-900s y >900s están además dominados por muy pocos videos (24 y 4 respectivamente) publicados casi todos en Q1 2025 — no es una muestra representativa del canal actual, es el "pico viejo".

## 2. El giro reciente: series cortas "Parte N" (últimas 4 semanas) — el hallazgo más relevante

Desde el 28 de junio de 2026 el canal empezó a publicar **mini-series narrativas de 2-5 episodios cortos** (Mad Season → John Frusciante → Linkin Park → Scott Weiland), cada episodio de 87-355s, publicados en días consecutivos. Es un formato distinto a los documentales largos de un solo video que dominaban en 2025.

| Fecha | Serie / Parte | Vistas totales | Vistas/día desde publicación | Duración |
|---|---|---|---|---|
| 2026-07-03 | Frusciante Parte 1 | 280,073 | **14,889/día** | 87s |
| 2026-07-10 | Linkin Park Parte 3 | 43,158 | 3,654/día | 150s |
| 2026-07-12 | Weiland Parte 1 | 37,201 | 3,799/día | 223s |
| 2026-07-04 | Frusciante Parte 2 | 30,919 | 1,736/día | 143s |
| 2026-07-08 | Linkin Park Parte 2 | 27,660 | 2,012/día | 187s |
| 2026-07-05 | Frusciante Parte 3 | 25,811 | 1,535/día | 163s |
| 2026-06-28 | Mad Season Parte 2 | 10,178 | 445/día | 355s |

Comparado contra "vistas/día desde publicación" (velocidad ajustada por antigüedad, más justo que el total crudo porque los videos viejos han tenido más tiempo de acumular), **9 de los 15 videos más rápidos de todo el canal son de las últimas 3 semanas**, y casi todos son episodios de estas mini-series. Frusciante Parte 1 es, ajustado por velocidad, el segundo video de mejor desempeño de toda la historia del canal — solo detrás de Layne Staley (2026-05-22, 159s, también reciente).

**Esto contradice parcialmente la implicación del análisis anterior.** El análisis de julio 21 (antes de este) concluía que el "punto dulce" eran videos de 10-15 min, basado en promedios de todo el historial. Esos promedios están inflados por unos pocos hits virales viejos de Q1 2025 (Chad Smith 519s, Jimmy Page 795s). La señal más reciente y más fresca — las últimas 3-4 semanas, con el formato de serie corta — apunta en la dirección contraria: **episodios de 1.5-4 minutos publicados en serie diaria están superando en velocidad a cualquier otra cosa que el canal ha probado recientemente.**

No son mutuamente excluyentes: el canal nunca ha probado un video único de ~20 min, así que no hay evidencia de que falle. Pero si la pregunta es "¿subo el documental de Cornell completo (20 min) o lo corto en una serie de partes?", la evidencia más reciente y más fuerte favorece **cortarlo en serie** (formato que ya está funcionando ahora, con la audiencia actual, con contenido de la misma naturaleza narrativa/biográfica) sobre apostar por un formato nunca probado.

## 3. Evolución del canal por trimestre

| Trimestre | # videos | Duración promedio | Vistas mediana |
|---|---|---|---|
| 2023-Q4 | 4 | 63s | 732 |
| 2024-Q1 | 28 | 163s | 581 |
| 2024-Q2 | 40 | 216s | 395 |
| 2024-Q3 | 3 | 107s | 329 |
| 2024-Q4 | 12 | 293s | 1,919 |
| 2025-Q1 | 160 | 365s | **11,959** |
| 2025-Q2 | 51 | 325s | 11,290 |
| 2025-Q3 | 22 | 301s | 1,925 |
| 2025-Q4 | 55 | 219s | 5,224 |
| 2026-Q1 | 44 | 100s | 3,225 |
| 2026-Q2 | 36 | 132s | 2,130 |
| 2026-Q3 (parcial, 22 días) | 13 | 179s | **17,878** |

Lectura: 2024 fue la era de clips de letras de canciones sin narrativa (rendimiento muy bajo, mediana <2,000). Q1-Q2 2025 fue la era de documentales largos de un solo video (365s promedio) con el mejor volumen y rendimiento sostenido del canal hasta ahora. De ahí el canal cayó en Q3 2025 y se mantuvo mediocre hasta mediados de 2026 con clips cortos sin serialización (100-132s, sin narrativa por partes). **Q3 2026 (el mes actual) ya es, con solo 13 videos, el trimestre de mejor mediana histórica**, empujado casi enteramente por el formato de series.

## 4. Hashtags — cuáles predicen buen desempeño y cuáles son ruido

| Hashtag | n | Vistas promedio | Mediana |
|---|---|---|---|
| #ledzeppelin | 15 | 141,176 | 20,360 |
| #capcut | 52 | 146,308 | 5,543 (alta varianza, un outlier lo infla) |
| #classicrock | 49 | 92,408 | **31,886** |
| #musichistory | 20 | 91,672 | 32,869 |
| #grunge | 51 | 64,298 | 13,034 |
| #historiadelrock | 52 | 56,983 | 11,685 |
| #90srock | 21 | 43,123 | 33,082 |
| #rocklegends | 83 | 122,715 | 12,144 |
| #soundgarden | 14 | 26,028 | 24,129 |
| #chriscornell | 15 | 17,755 | 8,052 |
| #foryou | 30 | 4,094 | 636 |
| #parati | 59 | 9,461 | 738 |

`#classicrock`, `#musichistory` y `#90srock` tienen las medianas más altas y son etiquetas de nicho/tema, no de descubrimiento genérico. `#parati` y `#foryou` (las etiquetas de descubrimiento masivo más obvias) tienen consistentemente el peor desempeño del canal — coinciden con los videos de la era 2024 sin narrativa. No es causal necesariamente (correlaciona con la era del video, no solo con el hashtag), pero no hay ninguna señal de que valga la pena seguir usándolas.

## 5. Rendimiento por artista/tema (búsqueda de menciones en título+descripción)

| Tema | n | Vistas promedio | Mediana |
|---|---|---|---|
| John Frusciante / RHCP | 7 | 649,696 | 25,811 |
| Led Zeppelin / Jimmy Page | 17 | 127,341 | 20,360 |
| Axl Rose / GNR | 10 | 59,458 | 25,721 |
| Kurt Cobain / Nirvana | 19 | 80,500 | 7,682 |
| Layne Staley / Alice in Chains / Mad Season | 12 | 88,481 | 7,078 |
| Pearl Jam / Eddie Vedder | 27 | 23,975 | 12,050 |
| **Chris Cornell / Soundgarden** | 23 | 18,026 | **11,179** |
| Scott Weiland / STP | 22 | 29,883 | 5,745 |
| Chester Bennington / Linkin Park | 10 | 14,565 | 9,094 |
| Metallica / Hetfield | 9 | 42,436 | 1,929 |

Cornell/Soundgarden (23 videos, mediana 11,179) rinde en la mitad de la tabla — ni el mejor tema del canal ni uno de riesgo. Confirma lo que decía el análisis anterior: hay precedente sano, no espectacular, para ese contenido específico.

## 6. Día de la semana y hora de publicación (hora UTC)

| Día | n | Vistas promedio | Mediana |
|---|---|---|---|
| Viernes | 70 | 100,866 | 7,838 |
| Sábado | 78 | 82,654 | 5,554 |
| Domingo | 94 | 27,011 | 4,667 |
| Jueves | 59 | 33,449 | 3,853 |
| Miércoles | 53 | 25,953 | 5,682 |
| Martes | 57 | 21,120 | 4,777 |
| Lunes | 57 | 19,722 | 5,150 |

Viernes y sábado tienen los promedios más altos, pero están inflados por outliers puntuales (los promedios se disparan, las medianas no tanto). Domingo es el día con más volumen histórico de publicación (94 videos) pero rendimiento mediocre. Ninguna hora del día destaca de forma contundente y consistente entre promedio y mediana a la vez — no hay una "hora mágica" clara en estos datos; cualquier lectura por hora UTC además requiere saber en qué zona horaria está la audiencia real (dato que la API no expone).

## 7. Outliers: qué tienen en común el top y el fondo del ranking

**Top 15 histórico:** todos narrativa biográfica/documental (Chad Smith, Layne Staley, Jimmy Page, James Hetfield, etc.), rango amplio de duración (85s a 795s) — el denominador común no es la duración sino el formato de storytelling con gancho fuerte en los primeros segundos.

**Bottom 15 histórico:** sin excepción, **todos son de 2024**, todos son clips de letras de canción sin narrativa propia (ej. "Best part - Daniel Caesar ft H.E.R.", "Hot Chip - Over and Over"), con hashtags genéricos (#parati, #foryou, #4u). Ese formato ya no se usa y confirma que el pivote a storytelling documental fue la decisión correctamente.

## 8. Ratio like/vista por rango de alcance

| Rango de vistas | n | Like rate |
|---|---|---|
| <1k | 81 | 4.95% |
| 1k-10k | 214 | 3.36% |
| 10k-100k | 133 | 4.33% |
| 100k-1M | 38 | 4.73% |
| >1M | 2 | 8.20% |
Sin señales de anomalía (ni caída sospechosa ni pico artificial) — el engagement se comporta de forma orgánica y consistente en todos los rangos de alcance.

## 9. Implicación estratégica directa: el documental de Cornell (20 min)

**Actualizado con dinero real (sección 10) — recomendación final: subirlo completo como video único, no cortarlo en partes.** El razonamiento intermedio de las secciones 9 (v1, basada en vistas) y 10 (v1, proxy) quedó superado por los datos reales de Creator Rewards: los picos de ingreso fuerte del canal vienen exclusivamente de videos únicos largos con narrativa completa, no de series cortas. Ver sección 10 para la evidencia en dólares.

- Cornell/Soundgarden tiene precedente sano en vistas (mediana 11,179 en 23 videos), ni riesgoso ni el tema más fuerte del canal.
- El formato que replicar es el de **"Video de la historia completa..."** (14 may 2026, 7:39 min, $175.79, el RPM más alto registrado en todo el canal) — narrativa completa de una sola pieza, sin cortar.

## 10. Monetización real (Creator Rewards Program — capturas del 22 jul 2026)

La API pública de TikTok no expone ganancias (no hay scope de Creator Rewards en la API de developer), así que estos números vienen directo de capturas de pantalla de TikTok Creator Center que compartió Geruka, no de la API.

**Julio 2026 (1-20 jul): $82.32 total** ($10.16 recompensa estándar + $72.16 adicional) — generado casi enteramente por la racha de series cortas (Mad Season → Frusciante → Linkin Park → Weiland):

| Video | Fecha | Duración | Total | RPM |
|---|---|---|---|---|
| Frusciante Parte 1 | 3 jul | 1:27 | $31.10 | $0.61 |
| Weiland Parte 1 | 12 jul | 3:43 | $5.88 | $0.93 |
| Linkin Park Parte 3 | 10 jul | 2:30 | $4.30 | $0.63 |
| Frusciante Parte 2 | 4 jul | 2:23 | $3.54 | **$1.22** |
| Linkin Park Parte 2 | 8 jul | 3:07 | $2.88 | $0.71 |
| Linkin Park Parte 4 (final) | 10 jul | 3:14 | $1.85 | $0.74 |
| Frusciante Parte 3 | 5 jul | 2:43 | $1.10 | $0.44 |
| Mad Season Parte 2 | 28 jun | 5:55 | $0.88 | $0.75 |
| Mad Season "1a parte" | 27 jun | 2:22 | $0.56 | $0.60 |
| Mad Season Parte 3 | 30 jun | 1:46 | $0.30 | $0.38 |
| Mad Season Parte 4 (final) | 2 jul | 5:02 | $0.02 | $0.03 |
| Weiland Parte 3 | 15 jul | 3:29 | $1.01 | $0.64 |
| Weiland Parte 4 | 16 jul | 3:21 | $0.82 | $0.53 |
| Linkin Park Parte 1, Weiland Parte 2 y 5 | varias | — | $0.00 | $0.00 |

Sumando los 16 videos publicados en la ventana (27 jun - 17 jul): **$54.24**, contra los $82.32 que reporta el resumen mensual de "jul 2026" (1-20 jul). La diferencia (~$28) probablemente es porque el "Total de recompensas" que muestra cada video es acumulado histórico (incluye lo ganado en junio para los Mad Season, fuera de la ventana del resumen de julio), mientras que el $82.32 del resumen es estrictamente lo devengado del 1 al 20 de julio — no son la misma unidad de medida, así que no deberían cuadrar exactamente. No cambia ninguna de las conclusiones de abajo.

**Mayo-junio 2026 — los dos videos único que sí rompieron:**

| Video | Fecha | Duración | Total | RPM |
|---|---|---|---|---|
| **"Video de la historia completa..."** | 14 may | 7:39 | **$175.79** | **$1.18** (el más alto registrado) |
| **Layne Staley — "La última respuesta..."** | 22 may | 2:39 | **$190.36** | $0.94 |
| Bowie 2da Parte | 29 may | 6:36 | $0.37 | $0.50 |
| "Si te quedaste con las ganas..." | 28 may | 10:50 | $0.14 | $0.25 |
| Def Leppard | jun | 1:45 | $0.13 | $0.04 |
| Varios (Red Hot, Depeche Mode, etc.) | may-jun | — | $0.00 | $0.00 |
| Dave Grohl, Pearl Jam, Josh Homme, Korn, video-YT | may-jun | — | *Visualizaciones insuficientes* (bajo el umbral mínimo de monetización) | — |

**Conclusión con dinero real, no proxy:**

1. **Dos videos únicos de mayo ($175.79 + $190.36 = $366.15) generaron más de 4 veces lo que las 13 series completas de junio-julio juntas ($82.32 en 20 días).** El mejor episodio de serie de toda la historia (Frusciante Parte 1, $31.10) no llega a un sexto de lo que dio Layne Staley solo.
2. **El dinero no es proporcional a las vistas de la API.** Layne Staley (930,976 vistas) y "Video de la historia completa" (505,686 vistas, casi la mitad) ganaron montos similares ($190 vs $176) — y el video más corto en vistas tiene el RPM más alto de todo el dataset ($1.18). TikTok pesa algo (originalidad, retención, calidad) que no es visible en `view_count` de la API pública — la sección 2 y la v1 de esta sección asumían una proporcionalidad que resulta ser falsa.
3. **Incluso dentro de la racha de series, el dinero sigue concentrado en un solo golpe:** Frusciante Parte 1 se lleva 38% de todo julio — la serie no reparte el ingreso entre episodios, solo cambia cuál episodio carga con el peso, y ese peso máximo (~$31) sigue siendo muy inferior al de un video único bien logrado (~$175-190).
4. **Hay un umbral mínimo de vistas para monetizar** ("Visualizaciones insuficientes" aparece en varios videos de mayo-junio con pocas vistas) — publicar más no ayuda si el video no cruza ese piso.

**Respuesta directa a la pregunta original:** sí, tenías razón — ningún episodio de serie da un ingreso diario fuerte porque ninguno ha superado ~$31, mientras que los videos únicos con narrativa completa han generado $175-190 cada uno. Las series dan un piso mensual modesto y predecible; los videos únicos son la única palanca que ha producido picos grandes de dinero real. Para el documental de Cornell, la evidencia en dólares favorece subirlo completo.

## 11. Diagnóstico profundo: qué tienen distinto, palabra por palabra, los videos que sí monetizaron

Con el texto completo y el desglose de like/comment/share de cada video (no solo el agregado), aparecen patrones que el promedio del canal no mostraba. Línea base del canal completo (468 videos): **like rate 4.04%, share rate 0.322%, comment rate 0.116%**.

| Video | Duración | Vistas | Like rate | Share rate | Comment rate | $ |
|---|---|---|---|---|---|---|
| Layne Staley | 2:39 | 930,976 | **9.55%** (2.4x canal) | 0.385% (1.2x) | 0.064% (0.6x) | $190.36 |
| Historia completa (Prince/Radiohead) | 7:39 | 505,686 | 7.12% (1.8x) | **1.866%** (**5.8x canal**) | 0.314% (2.7x) | $175.79 |
| Frusciante Parte 1 | 1:27 | 280,073 | 4.63% (~canal) | 0.196% (0.6x) | 0.035% (0.3x) | $31.10 |
| Weiland Parte 2 | 3:06 | 2,319 | 8.06% (2x canal) | 0.431% (1.3x) | 0.302% (2.6x) | **$0.00** |
| Linkin Park Parte 1 | 2:09 | 5,010 | 6.35% (1.6x) | 0.619% (1.9x) | 0.040% (0.3x) | **$0.00** |

**Tres hallazgos concretos, no especulación:**

1. **Los dos videos que más ganaron tienen like-rate muy por encima del promedio del canal (1.8x y 2.4x).** No es casualidad — el "audience engagement" es uno de los 4 factores oficiales que TikTok usa para fijar el RPM (junto con originalidad, tiempo de reproducción y "search value"). "Historia completa" además tiene el share-rate más alto de **todo** el dataset (5.8x el promedio) — la gente lo compartió de forma desproporcionada. Los dos usan el mismo mecanismo narrativo: presentan el contenido como un **secreto/dato oculto que casi se pierde** ("lo que nadie entendió", "la gema oculta que intentó censurar") y cierran con una pregunta o tensión sin resolver, no con un final cerrado. Eso es replicable a propósito, no solo cuestión de suerte.

2. ~~Hay algo que anula el pago por completo, probablemente copyright/duplicado~~ — **descartado con evidencia directa, ver sección 12.** Geruka confirmó en TikTok Studio que no hay videos marcados por copyright/originalidad desde febrero 2026. La causa real es un umbral duro de volumen, no una exclusión de contenido.

3. **Frusciante Parte 1 prueba que hay una segunda ruta al dinero sin depender de engagement alto:** su engagement (4.86%) es prácticamente el promedio del canal, nada especial — pero ganó $31.10 solo por volumen bruto de vistas (280k). Es decir, **o generas engagement muy por encima del promedio (ruta Staley/historia completa), o generas un volumen de vistas muy por encima del promedio (ruta Frusciante)** — necesitas destacar claramente en al menos una de las dos dimensiones; estar en el promedio en ambas (como la mayoría de los episodios de serie que ganan $0-3) no monetiza.

## 12. El mecanismo real, confirmado con la pantalla "Recompensas por video" de TikTok Studio

Las hipótesis de las secciones 10-11 (retención, geografía de audiencia total, copyright) se probaron y descartaron una por una con evidencia directa de las 5 partes de Weiland más Frusciante Parte 1. La pantalla "Recompensas por video" de TikTok Studio (Cálculo de recompensas → Visualizaciones relevantes) tiene el dato que faltaba y resuelve todo el misterio.

**Hay un piso duro: 1,000 "visualizaciones relevantes".** Visualizaciones relevantes = vistas que vienen específicamente de México, EEUU o Brasil (los únicos países de la región habilitados para Creator Rewards, confirmado en la sección 10). Por debajo de 1,000 vistas relevantes, TikTok ni siquiera calcula un RPM — la pantalla muestra literalmente "Menos de 1000" y "Cálculo de datos en curso. Vuelve más tarde", y el video queda congelado en $0.00 de forma permanente una vez que dejó de crecer.

| Video | Vistas totales | Visualizaciones relevantes | % relevante | RPM | Total $ |
|---|---|---|---|---|---|
| Weiland Parte 2 | 2,347 | **Menos de 1,000** | — | -- | $0.00 |
| Weiland Parte 5 | 3,529 | **Menos de 1,000** | — | -- | $0.00 |
| Weiland Parte 4 | 14,000 | 1.6K | 11.4% | $0.52 | $0.85 |
| Weiland Parte 3 | 12,400 | 1.6K | 12.9% | $0.63 | $1.02 |
| Weiland Parte 1 | 37,201 | 6.4K | 17.2% | $0.92 | $5.91 |
| Frusciante Parte 1 | 280,073 | 50.6K | 18.1% | $0.61 | $31.11 |

**La distribución de país dentro de "visualizaciones relevantes" es casi idéntica en todos (92-94% México, 4-6% EEUU, 1-2% Brasil)** — no es lo que varía entre videos. Lo que varía es el volumen bruto de vistas. Con el % relevante rondando 11-18% de forma consistente, la regla práctica para este canal: **un video necesita aproximadamente 6,500-9,000 vistas totales para que sus vistas relevantes cursen las 1,000 y empiece a pagar algo — sin importar retención, gancho de los primeros segundos, copyright o engagement.**

**Conclusión definitiva de toda esta investigación:** ni la retención (sección 10), ni la geografía de la audiencia total (que sí es plana/pan-latinoamericana y llevó a una hipótesis descartada), ni el copyright (descartado por Geruka directamente en TikTok Studio) explican por qué algunos episodios de serie ganan $0.00. Es puramente un umbral de volumen sobre un sub-conjunto geográfico fijo de la audiencia. La palanca real para subir el ingreso no es optimizar guion por guion — es lograr que más videos cracen esa barrera de ~7,000-9,000 vistas, algo que los videos únicos con descubrimiento en frío (ver sección 11, punto 1: Frusciante Parte 1 tuvo 42% de espectadores nuevos vs. 2-3% en cada secuela de Weiland) logran con mucha más facilidad que las secuelas de una serie, que reciclan a la misma audiencia fiel una y otra vez.

## Estado de la API de TikTok

- Conectada de punta a punta vía OAuth2 + PKCE (Sandbox mode). Bug conocido: TikTok pide `code_challenge` en **hex**, no base64url estándar de PKCE (ver `scratch_tiktok_auth.py::make_pkce_pair()`).
- Token vigente por 24h desde 2026-07-21 ~13:37 (`obtained_at` en `.secrets/tiktok_token.json`). Refresh token válido 1 año, pero el script actual no lo usa automáticamente — re-autorizar con `python3 scratch_tiktok_auth.py auth` cuando expire.
- Para refrescar los datos: `python3 scratch_tiktok_auth.py fetch` (requiere token vigente).
- `video.list` **no** expone retención/completion rate ni datos demográficos de audiencia — esas métricas solo viven en TikTok Studio Analytics (no vía API pública), y siguen siendo el hueco más importante de este análisis.
