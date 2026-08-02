---
name: rockwise-script-short
description: >
  Skill de guion nativo para TikTok de Rockwise Tales. Escribe piezas
  monetizables y autosuficientes para audiencia fria, tanto narrativas de un
  protagonista como mosaicos o votaciones cuando el concepto lo exige. Aplica
  el patron viral real del canal, Creator Search Insights, search value,
  retencion, shareability, Creator Rewards y reglas para series. No usar para
  YouTube LONG; usar rockwise-script.

license: MIT

metadata:
  raise.work_cycle: production
  raise.frequency: on-demand
  raise.fase: script-short
  raise.prerequisites: "rockwise-research"
  raise.next: "rockwise-assets"
  raise.gate: ""
  raise.adaptable: "true"
  raise.version: "2.3.0"
---

# Rockwise Script TikTok

## Purpose

Tomar hechos verificados del research y escribir un guion nativo para TikTok
que pueda descubrir una audiencia fria, sostener atencion, provocar shares y
entregar una historia completa.

**Plataforma unica:** TikTok. No producir YouTube Shorts con este skill.
**Canal:** Rockwise Tales (@rockwisetales), NO FACE, voz en off o grabacion
directa del usuario.
**Objetivo primario:** distribucion y Creator Rewards sin sacrificar verdad
factual.

> El TikTok no es un resumen del video de YouTube. Debe funcionar por si solo.

## Separacion obligatoria respecto a YouTube

Usar `rockwise-script` para YouTube LONG. Se pueden reutilizar hechos y la
historia real, pero no el mismo guion ni la misma apertura.

| Decision | TikTok â€” este skill | YouTube â€” `rockwise-script` |
| --- | --- | --- |
| Audiencia inicial | Fria, decide en segundos | Puede tolerar desarrollo mayor |
| Unidad narrativa | Momento/revelacion autosuficiente | Arco documental de 12-20 min |
| Payoff | Micro-payoffs frecuentes | Midpoint y resolucion larga |
| Empaque | Gancho verbal y caption | Titulo, thumbnail, CTR |
| Monetizacion | Views relevantes de Creator Rewards | Watch hours y ads |
| Series | Cada pieza compite desde cero | Biblioteca y sesiones de canal |

Importar del skill de YouTube solamente:

- historia real frente a tema superficial;
- protagonista claro cuando el formato es narrativo;
- empezar en tension, no con biografia;
- atribucion y verdad factual;
- claridad para consumo audio-only.

No importar midpoint obligatorio, cinco actos, conteo de 1,400-1,800 palabras,
apertura lenta, miniatura, CTR ni reglas de watch hours.

## Base empirica obligatoria

Leer `tiktok_viral_pattern_playbook.md` antes de elegir el angulo o escribir.
Para decidir demanda o keywords, leer tambien
`references/creator-search-insights.md`. Si el playbook tiene mas de 30 dias,
cambiaron los formatos o entraron al menos 10 videos nuevos, actualizar la API
y recalcular el patron.

Si el pedido es derivar, adaptar, recortar o convertir un documental largo de
Rockwise a TikTok vertical, leer tambien
`references/vertical-documentary-shorts.md` antes de escribir. En ese caso, no
entregar un simple recorte del guion largo: crear guion nativo para TikTok con
cold open, primera frase conectada, puntuacion de locucion y notas de edicion
separadas.

Para diagnosticar rendimiento, competencia, cambios del algoritmo o
monetizacion, leer `references/channel-diagnostics.md` y ejecutar
`scripts/channel_diagnostic.py`. Conservar una fila por video y separar
distribucion, respuesta, Search y dinero.

Hallazgo vigente del canal:

> artista reconocible + momento especifico e irreversible + revelacion
> verificable + consecuencia emocional + razon para compartir

En 469 videos:

- top 10% viral: al menos 85,225 views;
- share rate mediano viral: 0.418%, frente a 0.221% en el resto;
- engagement mediano viral: 4.862%, frente a 3.842%;
- comment rate casi no cambia; no escribir para comentarios a costa de shares;
- `nadie`, cifras, preguntas, hashtags y duracion no producen viralidad por si
  solos;
- `Parte N` no transfiere alcance y puede frenar audiencia fria.

Modelo oficial complementario:

- For You pondera interacciones, tiempo visto, finalizacion y skips;
- Search pondera que el contenido responda claramente a la consulta;
- Creator Rewards evalua originalidad, play duration, search value y
  engagement;
- no existe un porcentaje universal de retencion: comparar por duracion,
  edad y cohorte del canal.

Senal live al corte 2026-07-25:
- FYP global 75.5% y Search 19.8% en los ultimos siete dias;
- Soundgarden recibio 95.9% FYP: no hay evidencia de bloqueo de cuenta;
- una caida semanal no prueba cambio de algoritmo si tambien cambio la
  frecuencia de publicacion;
- engagement alto con views bajas significa buena respuesta, no
  necesariamente buena distribucion.

## Reglas no negociables

- No inventar citas ni hechos. Usar solo el Fact Sheet verificado.
- Atribuir toda cita textual antes de citarla.
- No usar "les", "vamos a", "hoy vemos" ni "te cuento".
- No confundir misterio con ocultar el tema: declarar artista, momento y
  contradiccion desde el inicio.
- No abrir con contexto biografico.
- No prometer que engagement alto implica monetizacion.
- No inventar volumen, ranking ni `content gap` de Creator Search Insights.
  Registrar siempre fuente y fecha, y marcar cualquier aproximacion como
  `PROXY`.
- No hacer keyword stuffing. La consulta debe sonar natural y describir la
  promesa real del video.
- No declarar cambio de algoritmo sin normalizar cadencia, edad, duracion,
  FYP, Search y nuevos espectadores. Marcar foros o X como anecdota.
- Comparar competidores solo dentro de TikTok y contra una muestra reciente;
  no usar un viral fijado como rendimiento tipico.
- No copiar sensacionalismo, muertes, citas o hechos no verificados aunque el
  competidor tenga millones de views.
- Para Creator Rewards, exigir contenido original de mas de un minuto. El
  archivo ajeno es evidencia, no el producto: agregar tesis propia, narracion,
  contexto y edicion transformativa.
- Mantener la frase final literal:
  "Si quieres seguir explorando la boveda de los archivos ocultos de las
  leyendas, sigueme, esto es Rockwise Tales."
- Ejecutar journal add antes de pasar a `rockwise-assets`.

## Modos

### Modo A â€” Narrativa viral autosuficiente (default)

Usar para una persona, banda, cancion, decision, entrevista o momento central.
Es el modo preferido para alcance y Creator Rewards.

Duracion orientativa:

- 90-240 s para un momento concentrado;
- 4-8 min cuando la evidencia y escalada lo justifican;
- hasta 12 min solo si cada bloque agrega informacion nueva.

No alargar para monetizar. Si el concepto se agota antes de 60 segundos, buscar
un angulo con mayor sustancia o tratarlo como experimento no monetizable.

### Modo B â€” Mosaico o votacion (excepcion)

Usar solo cuando el valor depende de comparar varias menciones, presentar una
lista o pedir una seleccion. No usar mosaico por defecto para historias que
tienen un protagonista y un momento potente.

Cada mencion necesita un dato gancho verificado y una frase puente narrativa.
Evitar la mecanica "Banda X: dato. Banda Y: dato".

## Proceso

### Ruta de diagnostico
Si el pedido es analizar el canal, patrones, gaps, competencia, algoritmo o
monetizacion:

1. Leer `references/channel-diagnostics.md`.
2. Actualizar la API si el catalogo esta vencido.
3. Ejecutar `scripts/channel_diagnostic.py`.
4. Completar desde TikTok Studio FYP, Search, nuevos espectadores, retencion,
   views relevantes, RPM y rewards de las piezas comparadas.
5. Separar `HECHO | INFERENCIA | PENDIENTE`.
6. Entregar hallazgos antes de proponer temas o escribir guiones.

No entrar a la ruta de YouTube ni usar sus reportes de competencia.

### Step 0: Construir el Search Brief

Investigar demanda antes de fijar el angulo. Prioridad de fuentes:

1. Creator Search Insights: `Popular searches`, `Content gap`, `Searches by
   followers` y `Search analytics`.
2. TikTok Studio > Inspiration: `Trending`, `Recommended` y publicaciones
   similares.
3. Autocomplete, busquedas relacionadas, comentarios y datos propios.

Si Creator Search Insights no esta accesible, usar 2-3 como aproximacion y
marcar `FUENTE: PROXY`; nunca convertir tendencias o recomendaciones en un
volumen de busqueda inventado.

Aplicar completo `references/creator-search-insights.md`:

1. Guardar consulta escrita, pestaña, filtro, fecha, cuenta, region e idioma.
2. Extraer cada valor tal como aparece; no llamarlo busquedas mensuales.
3. Clasificar relevancia `EXACTA | ADYACENTE | AMBIGUA | FALSO_POSITIVO`.
4. Descartar coincidencias lexicales que no sean musica rock.
5. Cruzar el tema con `tiktok_own_videos.json` para medir saturacion propia.
6. Calcular `Topic Priority Score` solo despues del filtro semantico.

Para el cruce de cobertura, ejecutar
`scripts/topic_coverage.py --catalog tiktok_own_videos.json --cluster
"TEMA=alias uno|alias dos"`. No estimar manualmente medianas, share rate ni
cantidad reciente si el catalogo esta disponible.

Una busqueda que contenga `rock` o el nombre parcial de una banda no es
evidencia suficiente. Si `soundgarden` devuelve productos `Soundcore` o
efectos de sonido, esas filas son falsos positivos, no demanda por la banda.

```text
FUENTE: CSI LIVE | TIKTOK STUDIO | PROXY
FECHA:
CONSULTA ESCRITA:
PESTAÑA/FILTRO:
CONSULTA PRIMARIA:
INTENCION:
CLASE SEMANTICA:
POPULARIDAD MOSTRADA:
CAMBIO MOSTRADO:
CONTENT GAP: CONFIRMADO | NO CONFIRMADO
CONSULTAS RELACIONADAS:
COBERTURA PROPIA:
TOPIC PRIORITY SCORE:
EVIDENCIA:
```

Puntuar search-fit de 0 a 4:

- 0: no existe consulta ni intencion clara;
- 1: descripcion plausible, sin evidencia de demanda;
- 2: consulta natural y especifica, demanda desconocida;
- 3: demanda o consultas relacionadas observadas;
- 4: `content gap` confirmado y encaje fuerte con Rockwise Tales.

Para objetivo Creator Rewards, reencuadrar si el score es menor de 2, salvo
experimento For You declarado.

No confundir `search-fit` con prioridad editorial. El primero mide si el guion
responde a una consulta; `Topic Priority Score` decide si esa consulta merece
research frente a otras oportunidades de rock.
### Step 1: Verificar inputs

Exigir:

- Search Brief con fuente y fecha;
- Fact Sheet de `rockwise-research`;
- historia real, no solo tema superficial;
- evidencia primaria o secundaria fuerte para la revelacion;
- clips o assets posibles;
- duracion objetivo;
- objetivo: alcance, Creator Rewards, prueba o votacion.

Si falta una revelacion verificable o una consecuencia humana, volver a
research.

### Step 2: Pasar el viral-fit gate

Puntuar de 0 a 2:

1. Icono reconocible.
2. Momento especifico.
3. Contradiccion clara.
4. Revelacion verificable.
5. Consecuencia emocional.
6. Razon para compartir.

Decision:

- 10-12: escribir.
- 7-9: reencuadrar antes de escribir.
- 0-6: detener salvo experimento explicito.

El score no reemplaza demanda, actualidad, copyright ni disponibilidad de
assets.

### Step 3: Elegir modo

Elegir Modo A salvo que el brief requiera genuinamente comparacion o votacion.
Documentar en una linea:

```text
MODO: NARRATIVA | MOSAICO
PROMESA: [que sabra o entendera el espectador al final]
SEARCH INTENT: [que quiere resolver quien busca]
PRIMARY QUERY: [consulta natural]
SHARE TRIGGER: [por que alguien se lo enviaria a otra persona]
SAVE TRIGGER: [por que alguien lo guardaria]
```

### Step 4A: Escribir narrativa viral

Usar porcentajes, no una duracion rigida:

```text
GANCHO â€” 0-5%
  Artista + momento + contradiccion.
  Integrar la consulta primaria de forma natural en las primeras 1-2 frases.
  Abrir una pregunta verificable.
  Sin backstory, saludo ni numero de parte.

PRUEBA TEMPRANA â€” 5-20%
  Mostrar pronto que existe evidencia real: entrevista, documento, decision,
  llamada, cancion, fecha o testimonio.
  Entregar un micro-payoff sin resolver la consecuencia central.

ESCALADA â€” 20-65%
  Solo contexto que cambie el significado del conflicto.
  Introducir nueva informacion o una consecuencia cada 20-40 segundos.
  Mantener sujeto, fecha y causalidad claros para audio-only.

REVELACION â€” 65-90%
  Entregar la explicacion prometida.
  No reemplazar evidencia por opinion editorial.

CONSECUENCIA + CIERRE â€” 90-100%
  Mostrar como cambia la lectura del artista, la banda o la cancion.
  Cerrar con una pregunta natural o puente relacionado.
  Frase final RWT.
```

La resolucion debe llegar mas rapido que en YouTube. No copiar la regla de
guardar todo hasta un midpoint largo: TikTok necesita micro-payoffs continuos.

### Step 4B: Escribir mosaico

```text
GANCHO DEL FENOMENO
  Presentar la pregunta o mecanismo general, no una lista cerrada.

MENCIONES
  25-45 palabras por tema.
  Dato gancho + por que importa + puente hacia la siguiente mencion.
  Nombrar integrantes y banda de origen cuando sea relevante.
  Incluir rivalidad o ironia solo si esta verificada.

RECORDATORIO
  En votaciones largas, recordar la seleccion al inicio, mitad y final.

CTA + CIERRE RWT
  Pedir favoritos sin fecha limite rigida.
```

Si el flujo requiere 500-600 palabras, conservarlo antes que volverlo
robotico.

### Step 5: Auditar audiencia fria y series

Para cada pieza, comprobar:

- Se entiende sin haber visto otro video.
- Tiene pregunta y payoff propios.
- El primer texto no empieza con `Parte N`.
- La continuidad aparece despues del gancho, al final del caption o en
  playlist.
- Una secuela aporta un nuevo momento, no solo continuacion cronologica.
- Cada pieza pertenece a un cluster de busqueda, pero resuelve una consulta
  independiente.

No producir Parte 2 solo porque Parte 1 recibio comentarios. Exigir un gancho
autosuficiente y demanda por el subtema.

### Step 6: Auditar shareability

Completar antes de entregar:

```text
ALGUIEN LO COMPARTIRIA PORQUE: [razon concreta]
ALGUIEN LO GUARDARIA PORQUE: [valor futuro concreto]
DATO QUE CAMBIA LA LECTURA: [revelacion]
CONSECUENCIA HUMANA: [que costo o transformo]
```

Si la respuesta es solamente "porque es interesante", reescribir el angulo.

### Step 7: Auditar search alignment

La misma intencion debe ser reconocible, sin repeticion mecanica, en:

- voz: consulta primaria o variante natural cerca del inicio;
- texto en pantalla: frase legible que identifique artista y pregunta;
- primera linea del caption: promesa que responde a la misma intencion;
- hashtags: 2-5 terminos especificos en produccion; evitar depender de `#fyp`.

Entregar un `SEARCH HANDOFF` separado del guion:

```text
PRIMARY QUERY:
RELATED QUERIES:
SPOKEN PHRASE:
ON-SCREEN PHRASE:
CAPTION FIRST LINE:
SOURCE + DATE:
```

### Step 8: Auditar originalidad y play duration

Para objetivo Creator Rewards:

- tesis, seleccion de hechos, voz y perspectiva propias;
- clips de archivo usados como evidencia con contexto y edicion transformativa;
- no depender de Duet, Stitch, reupload o contenido patrocinado;
- superar 60 segundos solo cuando la historia sostiene informacion nueva;
- declarar la promesa de visionado y entregar micro-payoffs;
- medir tiempo promedio, finalizacion, skips, rewatches, shares y saves contra
  videos de duracion y edad comparables.

### Step 9: Entregar guion limpio

Entregar solo texto de voz:

- sin timestamps;
- sin titulos de seccion;
- sin notas de produccion;
- sin marcadores `[Tono: ...]`;
- con ritmo oral y frases de longitud variable.

Calcular palabras a 150-160 palabras por minuto segun la duracion elegida. No
forzar todos los TikToks al antiguo rango de 400-480 palabras.

## Monetizacion

Creator Rewards depende de views relevantes, no solo views totales.

Separar tres gates:
1. elegibilidad: original, mas de 60 s y conforme a reglas;
2. volumen: intentar cruzar 1,000 views relevantes;
3. valor: RPM segun play duration, search, engagement, originalidad y valor
   comercial.

Referencia interna verificada en TikTok Studio:

- alrededor de 1,000 views relevantes habilitan el calculo;
- en Rockwise Tales suele requerir aproximadamente 6,500-9,000 views totales
  con el mix geografico observado;
- cruzar el piso no garantiza ingreso fuerte;
- la API publica no entrega views relevantes, retencion completa ni ingresos.

El guion debe buscar audiencia fria y shares, pero nunca prometer pago.

## Output

| Item | Valor |
| --- | --- |
| Plataforma | TikTok |
| Modo | Narrativa viral o mosaico |
| Duracion | Definida por evidencia; normalmente 90 s-8 min |
| Palabras | Duracion x 150-160 ppm |
| Marcadores de tono | Ninguno |
| Gate | Search-fit + viral-fit + audiencia fria + share/save + originalidad |

## Quality Checklist

- [ ] Se leyo `tiktok_viral_pattern_playbook.md`
- [ ] El formato es TikTok, no YouTube resumido
- [ ] Si fue diagnostico, se leyo `references/channel-diagnostics.md`
- [ ] Existe una fila auditable por cada video analizado
- [ ] Se separaron distribucion, respuesta, Search y dinero
- [ ] Un supuesto cambio de algoritmo fue normalizado por cadencia y cohorte
- [ ] La competencia proviene solo de TikTok y usa muestra reciente
- [ ] Search Brief documentado con fuente y fecha
- [ ] No se inventaron volumenes ni `content gaps`
- [ ] Se eliminaron falsos positivos semanticos antes de puntuar demanda
- [ ] Los valores de CSI se conservaron como aparecen, sin llamarlos busquedas
      mensuales
- [ ] Se audito cobertura propia por artista y angulo
- [ ] Topic Priority Score documentado
- [ ] Consulta, voz, texto en pantalla y caption responden a la misma intencion
- [ ] Viral-fit documentado y aprobado
- [ ] Artista, momento y contradiccion aparecen en el gancho
- [ ] La revelacion es concreta y verificable
- [ ] Existe consecuencia emocional, no morbo vacio
- [ ] El share trigger esta escrito en una frase
- [ ] El save trigger esta escrito en una frase
- [ ] No hay backstory antes del conflicto
- [ ] Hay micro-payoff o informacion nueva cada 20-40 segundos
- [ ] La originalidad y el uso transformativo de archivo estan documentados
- [ ] Retencion, finalizacion y skips se compararan por cohorte
- [ ] Si es serie, funciona para audiencia fria y no abre con `Parte N`
- [ ] Todos los quotes tienen atribucion
- [ ] No hay datos fuera del Fact Sheet
- [ ] El texto se entiende solo escuchandolo
- [ ] No contiene marcadores de tono ni notas de produccion
- [ ] Si deriva de un documental largo, se leyo `references/vertical-documentary-shorts.md`
- [ ] Si es script de grabacion en espanol, tiene acentos, comas y puntuacion natural
- [ ] Si usa cold open de archivo, la primera frase de voz conecta con lo que se acaba de ver
- [ ] Frase final RWT presente y literal
- [ ] Journal add ejecutado antes de `rockwise-assets`

## References

- Patron TikTok: `tiktok_viral_pattern_playbook.md`
- Creator Search Insights:
  `references/creator-search-insights.md`
- Shorts verticales derivados de documentales:
  `references/vertical-documentary-shorts.md`
- Cobertura propia: `scripts/topic_coverage.py`
- Diagnostico de canal: `references/channel-diagnostics.md`
- Auditoria por video: `scripts/channel_diagnostic.py`
- Previous: `/rockwise-research`
- Alterno de YouTube: `/rockwise-script`
- Next: `/rockwise-assets`
