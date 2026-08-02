# Playbook de patron viral de TikTok â€” Rockwise Tales

Actualizado: 2026-07-25.

Fuente: API oficial de TikTok (`tiktok_own_videos.json`, 469 videos accesibles)
y analisis reproducible (`scratch_tiktok_viral_patterns.py`). Recalcular cuando
hayan pasado 30 dias, cambie el formato editorial o entren al menos 10 videos
nuevos.

## Patron central

La unidad viral de Rockwise Tales no es un hashtag, una duracion ni una palabra
aislada. Es:

> artista reconocible + momento especifico e irreversible + revelacion
> verificable + consecuencia emocional + razon para compartir

No prometer una biografia general. Prometer resolver un momento concreto que
cambie como el espectador entiende al artista, una cancion o una decision.

## Evidencia del canal

Definicion historica: top 10% = 47 videos con al menos 85,225 views.

| Mediana | Top 10% viral | Resto |
| --- | ---: | ---: |
| Views | 178,756 | 3,862 |
| Duracion | 384 s | 216.5 s |
| Engagement total | 4.862% | 3.842% |
| Like rate | 4.558% | 3.473% |
| Comment rate | 0.078% | 0.080% |
| Share rate | 0.418% | 0.221% |
| Titulos/captions con `Parte N` | 4.3% | 5.7% |

La diferencia conductual mas fuerte es el share rate: casi 1.9 veces el resto.
El comment rate no separa a los virales. Usar comentarios como insight
cualitativo, no como predictor principal de alcance.

## Arquetipos ganadores observados

1. **Confesion o verdad tardia**
   - La ultima respuesta de Layne Staley.
   - Steve Perry explica por que abandono Journey.
   - Jimmy Page revela el origen de su sonido.
2. **Perdida, herida o supervivencia**
   - Robert Plant despues de perder a su hijo.
   - James Hetfield admite sentirse roto.
   - Eddie Vedder y la verdad sobre su infancia.
3. **Momento raro o colision de iconos**
   - Chad Smith escucha una cancion por primera vez.
   - Reunion de Nirvana con Violet Grohl.
   - Cerati vuelve al escenario mediante tecnologia.
4. **Conexion cultural oculta**
   - La gema que Prince intento censurar y Thom Yorke recupero.
   - Trent Reznor explica el origen de `Hurt`.

Los temas de muerte, perdida o transformacion aparecen aproximadamente dos
veces mas en el decil viral. La palabra `historia` aparece 1.68 veces mas. Esto
no autoriza morbo vacio: debe existir consecuencia humana y evidencia.

## Caso de estudio: Prince versionando `Creep`

Video principal, publicado el 13 de mayo de 2026:

- 507,208 views.
- 36,083 likes en el corte API; 36.1K visibles en TikTok.
- 1,592 comentarios visibles.
- 9,468 shares visibles.
- 9,068 favoritos visibles.
- Share rate aproximado: 1.867%.
- Comment rate aproximado: 0.314%.
- Interaccion sin favoritos: aproximadamente 9.30%.

La explicacion posterior del mismo tema, publicada 14 dias despues, obtuvo
4,045 views, 138 likes, 3 comentarios y 8 shares:

- Share rate: 0.198%.
- Comment rate: 0.074%.
- Interaccion: 3.684%.

El primer video no gano por "ser polemico" en abstracto. Combino:

1. Una prueba audiovisual completa que permite juzgar sin confiar en el
   narrador: Prince interpretando la cancion.
2. Dos comunidades con identidad fuerte: fans de Prince y de Radiohead.
3. Un veredicto discutible: genio y obra maestra frente a desafinacion,
   mediocridad o preferencia por la original.
4. Un conflicto factual adicional: quien bloqueo o libero el video.
5. Espacio para demostrar conocimiento musical explicando cambios de armonia,
   ritmo, letra, feeling y arreglos.
6. Descubrimiento real: muchos espectadores no conocian la version.
7. Humor, testimonios de asistentes a Coachella y defensa del legado.

Los comentarios visibles se reparten entre admiracion, rechazo, comparacion
con la original, analisis tecnico, correcciones factuales, humor y testimonio.
Por eso la conversacion no depende de una sola pregunta binaria.

### Patron: polemica con evidencia

```text
dos identidades reconocibles
+ una ejecucion/decision que se puede ver u oir
+ una afirmacion levemente discutible
+ dos o mas lecturas defendibles
+ una pregunta que no necesita inventarse
```

La polemica debe dejar que la audiencia juzgue. No fabricar errores ni acusar
sin respaldo. La tension ideal divide interpretaciones, no hechos basicos.
Si existe disputa factual, el guion debe distinguir evidencia, version de las
partes e inferencia.

Aplicado a videos de generos:

- No: `Que es el post-punk`.
- Si: `El post-punk no es musica triste: es musica para bailar sin fingir que
  todo esta bien`.
- No: `Que genero toca Deftones`.
- Si: `Deftones no volvio por nostalgia: una generacion nueva reconocio en esa
  musica algo que los adultos dejaron de escuchar`.
- No: `Diferencia entre art rock y rock progresivo`.
- Si: `El art rock queria convertir la cancion en arte; el progresivo queria
  demostrar hasta donde podia llevarla. No es exactamente lo mismo`.

Estas aperturas son hipotesis editoriales. Deben investigarse y ajustarse a la
evidencia antes de publicarse.

## Lo que no predice viralidad por si solo

- `Nadie`: aparece con la misma frecuencia en virales y no virales. Solo sirve
  si introduce una revelacion concreta.
- Preguntas, cifras o dinero: pueden fortalecer un caso especifico, pero no
  presentan lift historico suficiente por si solos.
- Hashtags genericos: describen tema o epoca; no confundir correlacion con
  causalidad. Priorizar claridad de nicho.
- Comentarios: su tasa mediana es casi identica entre virales y resto.
- Duracion: el viral historico es mas largo, pero ganadores recientes van de
  87 a 459 segundos. La historia debe durar lo necesario para pagar la promesa.
- `Parte N`: no transfiere distribucion. Cada episodio vuelve a competir desde
  cero y puede crear friccion para audiencia fria.

## Prueba de viral-fit antes de producir

Puntuar cada dimension de 0 a 2:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Icono reconocible | Nicho debil | Reconocible en el nicho | Reconocible de inmediato |
| Momento especifico | Biografia general | Periodo concreto | Instante/decision verificable |
| Contradiccion | No existe | Implicita | Clara en una frase |
| Revelacion | Resumen conocido | Dato poco conocido | Evidencia que cambia la lectura |
| Consecuencia emocional | Informativa | Humana | Irreversible o transformadora |
| Share trigger | Sin razon de envio | Curiosidad | "Tienes que ver/saber esto" |

- 10-12: fit fuerte; producir si research y factibilidad pasan.
- 7-9: reencuadrar el angulo o reforzar evidencia/consecuencia.
- 0-6: no producir para alcance salvo objetivo experimental explicito.

El score no reemplaza demanda, actualidad, copyright, retencion ni
factibilidad de assets.

## Regla para series

Cada episodio debe pasar la prueba de audiencia fria:

- Entenderse sin haber visto otra parte.
- Tener su propio momento, pregunta y payoff.
- No abrir el titulo/caption con `Parte N`.
- Colocar la continuidad al final del caption, en playlist o despues del
  gancho.
- No recomendar una secuela solo porque hubo comentarios; exigir demanda por
  ese subtema y un nuevo gancho autosuficiente.

## Plantilla de promesa

```text
[ARTISTA] + [HIZO/DIJO/RECHAZO ALGO CONCRETO]
+ [CONSECUENCIA QUE CONTRADICE LO ESPERADO]
```

La apertura debe:

1. Nombrar al artista y el momento.
2. Mostrar la contradiccion antes del contexto.
3. Abrir una pregunta verificable.
4. Retener la evidencia o explicacion central, no ocultar el tema.

El cierre debe entregar la revelacion y dejar una consecuencia interpretable o
una pregunta natural que el espectador quiera compartir o discutir.

## Lectura post-publicacion

Separar calidad de respuesta y volumen de distribucion:

- Share rate cercano o superior a 0.418%: perfil historico viral.
- Engagement cercano o superior a 4.862%: respuesta sana, pero no prueba
  distribucion.
- Buen engagement con pocas views: el contenido gusto al grupo expuesto, pero
  no alcanzo suficiente audiencia nueva.
- Medir velocidad por edad del video y contra cohortes recientes; no comparar
  solo views acumuladas.
- Revisar no seguidores, retencion, tiempo promedio visto, fuentes de trafico
  y nuevos seguidores en TikTok Studio. La API publica no expone todo esto.

No declarar fracaso durante una aceleracion. Definir checkpoints de 2h, 6h,
24h, 72h, 7d y 30d.

## Monetizacion

Creator Rewards depende de views relevantes, no de views totales. Evidencia
interna de TikTok Studio:

- Piso observado: aproximadamente 1,000 views relevantes.
- En Rockwise Tales, suele requerir alrededor de 6,500-9,000 views totales
  cuando 11-18% proviene de Mexico, Estados Unidos o Brasil.
- Cruzar el piso no implica ingreso fuerte; apenas habilita el calculo.
- La API publica no entrega retencion completa, views relevantes ni ingresos.

No prometer monetizacion a partir de engagement o views totales.

## Validacion externa y Search Insights

La evidencia oficial complementa el patron interno:

- For You usa interacciones como tiempo visto, finalizacion, shares, comentarios
  y skips; el peso exacto no es publico.
- Search favorece contenido que coincide con la consulta y satisface su
  intencion.
- Creator Rewards considera originalidad, play duration, search value y
  audience engagement.
- Creator Search Insights permite revisar busquedas populares, `content gaps`,
  busquedas de seguidores y rendimiento en Search cuando la funcion esta
  disponible en la cuenta.

### Acceso disponible para Rockwise Tales

La API publica conectada permite analizar videos propios, pero no ofrece un
endpoint de Creator Search Insights ni volumen de busqueda. TikTok Studio web
si muestra `Inspiration`, tendencias y recomendaciones de publicaciones
similares para @rockwisetales; usarlas como senal cualitativa, no como volumen.

Jerarquia operativa:

1. CSI live en la app, con captura o exportacion de consulta, fecha y
   `content gap`.
2. TikTok Studio > Inspiration > Recommended/Trending.
3. Autocomplete, busquedas relacionadas, comentarios y analitica propia como
   `PROXY`.

Nunca declarar que una keyword es "la mas buscada" sin evidencia visible de
CSI. Para cada tema guardar consulta primaria, intencion, consultas
relacionadas, fuente, fecha y si el `content gap` fue confirmado.

Fuentes oficiales:

- https://support.tiktok.com/en/using-tiktok/growing-your-audience/creator-search-insights
- https://support.tiktok.com/en/using-tiktok/exploring-videos/how-tiktok-recommends-content
- https://www.tiktok.com/creators/creator-portal/en-us/getting-paid-to-create/creator-rewards-program/
- https://developers.tiktok.com/doc/display-api-overview
- https://developers.tiktok.com/products/research-api/
## Datos y comandos

Actualizar API:

```powershell
python scratch_tiktok_auth.py fetch
```

Analizar recientes:

```powershell
python scratch_tiktok_latest_analysis.py
```

Recalcular patron viral:

```powershell
python scratch_tiktok_viral_patterns.py
```
