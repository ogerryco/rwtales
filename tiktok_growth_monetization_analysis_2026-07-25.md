# Diagnóstico de crecimiento y monetización de TikTok — Rockwise Tales

Fecha de corte: 2026-07-25  
Plataforma única: TikTok  
Cuenta: @rockwisetales

## Alcance y evidencia

Este análisis usa únicamente:

1. API oficial de TikTok: `tiktok_own_videos.json`, 469 videos.
2. TikTok Studio live de @rockwisetales, consultado el 2026-07-25.
3. Creator Search Insights de las capturas entregadas por Geruka.
4. TikTok Studio `Inspiration` y perfiles públicos de TikTok.
5. Fuentes oficiales de TikTok y un benchmark externo de 2.31 millones de
   publicaciones de TikTok.

No se usaron datos de YouTube ni `rwt_keyword_trends.json`. No existe todavía
evidencia CSI limpia suficiente para ordenar artistas por “los más buscados”.

- `HECHO`: dato visible en API o TikTok Studio.
- `INFERENCIA`: explicación más compatible con varios hechos.
- `PENDIENTE`: requiere una métrica que la API pública no entrega.

## Diagnóstico ejecutivo

### No hay evidencia de shadowban

`HECHO`: el video largo de Soundgarden recibió 95.9% de su tráfico desde Para
ti. Layne Staley recibió 96.3%. TikTok sí está probando ambos con audiencia de
Para ti.

`INFERENCIA`: el problema actual no es entrar al FYP, sino conseguir que la
prueba inicial se expanda a grupos mucho más grandes de audiencia fría.

### La caída semanal no demuestra un cambio de algoritmo

TikTok Studio, últimos siete días:

| Métrica | Valor | Cambio |
| --- | ---: | ---: |
| Views | 105.8K | -43.9% |
| Profile views | 899 | -61.5% |
| Likes | 6.6K | -40.2% |
| Comments | 112 | -53.9% |
| Shares | 409 | -36.4% |

En los siete días actuales se publicó un video; en los siete anteriores se
publicaron cinco. La producción cayó 80%, mientras las views cayeron 43.9%.

`INFERENCIA`: parte sustancial de la caída semanal se explica por cadencia. No
se puede atribuir al algoritmo sin normalizar publicaciones, edad, duración y
tema.

### Search ya es una palanca real

Tráfico global de los últimos siete días:

| Fuente | Participación |
| --- | ---: |
| Para ti | 75.5% |
| Search | 19.8% |
| Perfil | 4.4% |
| Siguiendo | 0.3% |

El benchmark Metricool 2026 reporta 73% FYP y 4% Search. Rockwise Tales está
aproximadamente en línea con FYP y muy por encima en Search durante esta
ventana. Esto no significa que todos los videos estén optimizados para
búsqueda: Soundgarden recibió solo 1.8% desde Search.

`HECHO`: videos antiguos siguen aportando descubrimiento. En los últimos siete
días, Layne Staley añadió 12K espectadores nuevos y 20K views; Prince/Radiohead
añadió 1.8K espectadores nuevos dos meses después de publicarse.

### Calidad de respuesta y escala son problemas diferentes

| Mediana | Top 10% viral | Resto |
| --- | ---: | ---: |
| Views | 178,757 | 3,862 |
| Engagement | 4.862% | 3.842% |
| Share rate | 0.418% | 0.221% |

Soundgarden tiene 8.28% de engagement y 0.425% de shares: la audiencia expuesta
respondió bien. Aún no recibió el volumen suficiente para acercarse a un
breakout.

La decisión correcta para casos así no es descartar el tema. Es conservar la
revelación, reconstruir la entrada para audiencia fría y mejorar el encaje con
una consulta concreta.

## Comparación de piezas clave

| Video | Duración | Views | Avg watch | % duración | Completo | FYP | Search | Shares | Seguidores | Rewards |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Layne Staley | 2:39 | 936K | 37.22s | 23.4% | 5.2% | 96.3% | 0.9% | 3,610 | 7.5K | $190.7 |
| Soundgarden | 12:12 | 8,342 | 73.18s | 10.0% | 1.4% | 95.9% | 1.8% | 33 | 39 | $0.4 |
| Prince / Radiohead | 7:39 | 507K | N/D | N/D | N/D | N/D | N/D | 9,458 | N/D | $175.79 |
| Frusciante Parte 1 | 1:27 | 283K | N/D | N/D | N/D | N/D | N/D | 555 | N/D | $31.11 |

### Layne frente a Soundgarden

- Ambos entraron con fuerza a Para ti.
- Soundgarden acumuló más segundos por reproducción, pero solo 10% de sus
  12:12; Layne sostuvo 23.4% de 2:39.
- Layne ofrece una promesa instantánea y humana: última respuesta, felicidad,
  momento final. Soundgarden exige entender una disputa legal, siete
  grabaciones, una viuda, tres integrantes y seis años de conflicto.
- Soundgarden no es un mal video: convirtió 8,342 views en 39 seguidores y
  cruzó el perfil viral de shares. Es una buena historia con demasiada
  fricción para escalar rápido en su empaque actual.

### Prince / Radiohead

El video de 7:39 prueba que una historia larga puede viralizar y pagar cuando
su mecanismo es inmediatamente compartible: una gema musical casi perdida,
Prince intentando censurarla y Thom Yorke recuperándola. Tiene el share rate
más alto del catálogo: 1.865%.

La duración larga no es la ventaja. La ventaja es sostener durante varios
minutos una conexión cultural que la audiencia necesita enviar a otra persona.

## Series: el número de parte no determina el resultado

### John Frusciante

| Episodio | Views | Share rate |
| --- | ---: | ---: |
| Parte 1 | 282,264 | 0.197% |
| Parte 2 | 31,115 | 0.145% |
| Parte 3 | 26,745 | 0.202% |

Parte 1 concentró el breakout; las secuelas conservaron menos de 12% de sus
views.

### Linkin Park

| Episodio | Views | Share rate |
| --- | ---: | ---: |
| Parte 1 — volvió sin avisar | 5,425 | 0.590% |
| Parte 2 — fundador que desapareció | 30,926 | 0.346% |
| Parte 3 — la madre se enteró por Google | 47,489 | 0.166% |
| Parte 4 — frase de Shinoda | 19,882 | 0.080% |

La Parte 3 superó ampliamente a la Parte 1 porque “su madre se enteró por
Google” es una contradicción autosuficiente y comprensible sin contexto.

### Scott Weiland

| Episodio | Views | Engagement | Share rate |
| --- | ---: | ---: | ---: |
| Parte 1 | 38,395 | 6.32% | 0.313% |
| Parte 2 | 2,462 | 8.61% | 0.406% |
| Parte 3 | 13,134 | 5.28% | 0.152% |
| Parte 4 | 15,308 | 4.83% | 0.222% |
| Parte 5 | 4,231 | 7.68% | 0.284% |

Parte 2 es el ejemplo más claro de “gustó, pero no se distribuyó”: tiene el
mejor engagement de la serie y casi el share rate viral, pero quedó en 2,462
views.

### Conclusión de series

`Parte N` no mata automáticamente un video, pero tampoco transfiere alcance. El
ángulo de cada episodio domina. Cada pieza debe:

1. omitir `Parte N` en el primer texto y la primera frase;
2. explicar por sí sola artista, momento y contradicción;
3. resolver una consulta independiente;
4. mencionar la serie solo después del gancho o en playlist.

## Patrones ganadores

La fórmula con mejor respaldo interno es:

> artista reconocible + momento específico e irreversible + revelación
> verificable + consecuencia emocional + razón para compartir

Arquetipos confirmados:

1. Confesión o verdad tardía.
2. Pérdida, herida o supervivencia.
3. Momento raro o colisión de iconos.
4. Conexión cultural oculta.
5. Decisión que contradice la imagen pública.

Las muertes y pérdidas aparecen cerca de 2 veces más en el decil viral, pero
solo funcionan cuando existe una consecuencia humana verificable. La palabra
`historia` aparece 1.68 veces más. `Nadie`, preguntas, cifras, dinero y hashtags
no tienen lift suficiente por sí solos.

## Gaps del canal

### Search intent no integrado desde el guion

El canal obtiene 19.8% de tráfico semanal desde Search, pero muchos videos
nacen como una premisa editorial, no como una respuesta a una intención.

Soundgarden:

- `chris cornell que le paso`: 33.3% de sus queries;
- `chris cornell`: 14%;
- `soundgarden`: 7%.

La promesa habla de $21 millones y el disco final, pero la búsqueda dominante
es biográfica. La siguiente pieza relacionada debería resolver una consulta
más exacta sobre el conflicto por el último álbum, sin convertirse en otra
biografía general.

### Formato monetizable intermedio

En los últimos 120 días, los videos de 180-359 segundos tienen:

- n=9;
- mediana de 13,134 views;
- 77.8% superó 6,500 views.

Es la cohorte reciente más consistente para cruzar el piso empírico de
monetización. La muestra es pequeña; usarla como formato de prueba preferente,
no como ley universal.

Los videos de 600s+ recientes son solo dos. No forman una muestra suficiente
para declarar que 10-15 minutos funciona o falla.

### Audiencia nueva frente a recurrente

Los videos que siguen descubriéndose meses después son promesas autosuficientes:

- Layne: última respuesta.
- Prince/Radiohead: gema censurada y recuperada.
- Linkin Park: madre informada por Google.

La estrategia debe optimizar `nuevos espectadores por 1,000 views`, no solo
views acumuladas.

### Historias buscables con emoción comprimida

TikTok Studio recomendó como publicaciones similares:

| Tema | Views | Likes | Mecanismo visible |
| --- | ---: | ---: | --- |
| Bunbury / canción triste | 2.4M | 284K | identificación emocional |
| Chris Cornell | 2.1M | 230K | éxito frente a dolor interno |
| Cerati / Soda Stereo | 517K | 96K | nostalgia e identidad |
| Lista de canciones | 1.1M | 280K | colección guardable |

No prueban volumen de búsqueda. Sí muestran que emoción, identidad y utilidad
se comprenden antes que una explicación compleja.

La oportunidad de Rockwise Tales es combinar esa compresión con research
verificable y narración original de más de un minuto.

### Auditoría económica por video

La API no entrega visualizaciones relevantes, RPM ni ingresos. Para cada video
se necesitan cuatro capas:

1. Distribución: FYP, nuevos espectadores y fuentes.
2. Respuesta: average watch, finish rate, shares y saves.
3. Search: porcentaje y queries exactas.
4. Dinero: visualizaciones relevantes, RPM y recompensa.

## Competencia

### Antes De La Gloria

TikTok Studio lo clasifica como creador similar. Al 2026-07-25:

- 105.7K seguidores;
- 853.8K likes;
- promesa: historias de artistas, caídas, fe y gloria en 90 segundos;
- tres fijados con 1.1M, 1.4M y 3.1M.

Su patrón:

- celebridad reconocible;
- giro irreversible;
- una emoción dominante;
- duración/promesa consistente;
- texto que puede entenderse sin contexto.

Sus publicaciones recientes oscilan aproximadamente entre 1.2K y 63.2K, con
varios resultados bajos. Los fijados no representan el rendimiento típico.

El perfil contiene afirmaciones sensacionalistas o aparentes escenarios no
verificados. No imitar ese recurso. La ventaja competitiva de Rockwise Tales es
producir el mismo nivel de claridad emocional con hechos comprobados.

### La CornellPedia

En búsquedas actuales de Chris Cornell aparece repetidamente con fragmentos de
entrevistas, fechas, fuente y audio original. Su ventaja es profundidad de
archivo y especificidad. Su debilidad visible es depender de clips y usar
metadatos/hashtags excesivos.

Rockwise Tales puede diferenciarse con:

- una tesis propia;
- narración transformativa;
- contexto que cambie el significado del archivo;
- una sola intención de búsqueda, sin stuffing.

## ¿Está cambiando el algoritmo?

TikTok confirma que:

- tiempo visto, finalización y skips influyen en Para ti;
- Search pondera el encaje con la consulta;
- el peso de los factores puede cambiar;
- Creator Rewards usa originalidad, play duration, search value y engagement.

Metricool analizó 2,314,756 publicaciones de 92,000 cuentas:

- el volumen publicado creció cerca de 72-80%;
- views por publicación cayeron 31%;
- reach cayó 29%;
- FYP se mantuvo dominante con 73%;
- 96% de las views ocurre en los primeros diez días.

La explicación externa más sólida no es un “nuevo algoritmo secreto”, sino más
competencia por cada impresión.

Foros de julio de 2026 contienen relatos de caídas bruscas y Search menos
preciso. Son evidencia anecdótica: sirven para vigilar, no para afirmar que
TikTok cambió una regla específica.

### Lectura para Rockwise Tales

No hay evidencia suficiente de una penalización:

- FYP actual: 75.5%, alineado con el benchmark.
- Soundgarden: 95.9% FYP.
- caída de producción semanal: 80%.
- el catálogo antiguo sigue recibiendo nuevos espectadores.

Hipótesis vigente: más saturación general + menor cadencia + piezas recientes
con dificultad desigual para expandirse a audiencia fría.

## Sistema para viralizar y monetizar cada video

### Antes de producir

1. Confirmar demanda con CSI exacto o marcar la fuente como proxy.
2. Auditar cobertura propia del artista y del ángulo.
3. Exigir momento, contradicción, revelación, consecuencia y share trigger.
4. Definir una consulta primaria.
5. Elegir duración por densidad narrativa:
   - 90-240s: opción base;
   - 180-359s: cohorte reciente más consistente;
   - 5-8m: solo con varios payoffs;
   - 10m+: experimento explícito, no default.

### Durante el guion y edición

1. 0-2s: artista + momento irreversible + contradicción.
2. 2-15s: prueba concreta de que existe evidencia.
3. Cada 20-40s: dato nuevo, micro-payoff o consecuencia.
4. Voz, texto en pantalla y caption responden a la misma consulta.
5. Nunca abrir con `Parte N`.
6. Archivo ajeno como evidencia; tesis, voz y edición propias.

### Después de publicar

Registrar checkpoints 2h, 6h, 24h, 72h, 7d y 30d.

| Señal | Diagnóstico | Acción |
| --- | --- | --- |
| Views bajas + ER/share altos | buen contenido, poca expansión | reempaquetar; no abandonarlo |
| FYP alto + retención baja | sí fue probado, no escaló | acortar entrada y adelantar prueba |
| Search bajo + queries desalineadas | promesa poco buscable | responder una query exacta |
| Parte 2 baja + buena respuesta | fricción de serie | relanzar subángulo autosuficiente |
| Views altas + share bajo | hit por exposición | validar retención antes de copiar |
| Share ≥0.418% | perfil histórico viral | replicar mecanismo, no artista |
| <1K views relevantes | no cruza piso económico | resolver escala y audiencia elegible |
| RPM bajo con volumen | menor valor económico | revisar play duration, search y originalidad |

## Archivos de auditoría

- `tiktok_video_audit_2026-07-25.csv`: 469 filas, una por video, con métricas,
  cohorte, índice de rendimiento, proxy económico y siguiente acción.
- `tiktok_video_audit_2026-07-25.json`: resumen reproducible.
- `.claude/skills/rockwise-script-short/scripts/channel_diagnostic.py`.

El CSV permite filtrar:

- `buen_contenido_baja_distribucion_reempaquetar`;
- `replicar_mecanismo_no_tema`;
- `hacerlo_autosuficiente_sin_parte_n`;
- `probable_bajo_piso`;
- `volumen_suficiente_no_garantizado`.

## Próxima prueba controlada

Producir una cohorte de 12 piezas antes de volver a declarar un cambio del
algoritmo:

1. Seis narrativas autosuficientes de 90-240s.
2. Tres respuestas de 60-120s a gaps CSI confirmados.
3. Dos narrativas de 3-6 minutos con al menos cuatro micro-payoffs.
4. Un video largo de 7-10 minutos, solo si supera el viral-fit gate.

Mantener estable voz, calidad y frecuencia. Variar una sola dimensión por
prueba: gancho, duración, ángulo o search intent.

## Fuentes externas

- TikTok, cómo recomienda contenido:
  https://support.tiktok.com/es/using-tiktok/exploring-videos/how-tiktok-recommends-content/
- TikTok, Creator Rewards:
  https://newsroom.tiktok.com/introducing-the-new-creator-rewards-program
- TikTok, Creator Rewards México:
  https://newsroom.tiktok.com/programa-recompensas-creadores-tiktok-mexico
- TikTok Next 2026 Trend Report:
  https://ads.tiktok.com/business/library/TikTok_Next_2026_Trend_Report.pdf
- Metricool TikTok Study 2026:
  https://metricool.com/wp-content/uploads/tiktok-study-2026-EN.pdf
