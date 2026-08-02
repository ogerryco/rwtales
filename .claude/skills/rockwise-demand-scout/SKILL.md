---
name: rockwise-demand-scout
description: >
  Scout estrategico de demanda para Rockwise Tales. Valida temas, artistas,
  canciones y angulos antes del research profundo usando competencia en YouTube,
  senales de busqueda, contexto actual, datos propios y potencial de monetizacion
  en YouTube y TikTok.
license: MIT
metadata:
  raise.work_cycle: strategy
  raise.frequency: on-demand
  raise.fase: scouting
  raise.prerequisites: ""
  raise.next: "rockwise-research"
  raise.gate: "demand_score >= 70 or explicit override"
  raise.adaptable: "true"
  raise.version: "1.0.0"
---

# Rockwise Demand Scout

Usa este skill antes de comprometer produccion fuerte en un tema de Rockwise Tales.

Su objetivo es responder si el tema merece investigacion profunda, si hay una brecha real frente a la competencia y cual es el mejor angulo para monetizar atencion.

## No negociar

- No publiques ni expongas llaves API, tokens, client secrets ni credenciales.
- Si usas datos de APIs, reporta metodologia y limites, no secretos.
- Si una fuente es dudosa, marcala como senal debil.
- No confundas videos oficiales, videoclips, lyrics o presentaciones en vivo con competencia editorial.
- No declares ingresos esperados como certeza; trabaja con potencial y condiciones.

## Entrada minima

- Tema candidato: artista, banda, album, cancion, conflicto o pregunta.
- Plataforma objetivo: YouTube, TikTok o ambas.
- Formato tentativo: longform, TikTok largo, short, serie, clip o experimento.
- Objetivo: monetizacion, crecimiento, autoridad, prueba de formato o backlog.

Si el usuario no especifica plataforma, asume multiplataforma y separa la recomendacion.

## Fuentes locales sugeridas

Cuando existan, revisa:

- `tiktok_channel_analysis.md`
- `tiktok_own_videos.json`
- `rwt_real_analytics_longform.json`
- `rwt_demand_fit_results.json`
- `youtube_salud_mental_competencia_api_filtered.md`
- `youtube_salud_mental_competencia_api_report.md`
- Scripts o reportes previos de YouTube Data API.

Si existen credenciales en archivos `.env` o `.secrets`, usalas solo a traves de scripts/herramientas seguras. Nunca copies su contenido en reportes.

## Proceso

### 1. Normalizar el tema

Convierte la idea en 3-6 consultas comparables.

Ejemplo:

- `[artista] historia`
- `[artista] documental`
- `[artista] entrevista personal`
- `[artista] salud mental`
- `[artista] adicciones`
- `[artista] canciones no publicadas`

Incluye variantes en espanol e ingles cuando el tema lo amerite.

### 2. Mapear competencia en YouTube

Usa YouTube Data API cuando este disponible. Si no lo esta, usa busqueda web o busqueda manual y marca la limitacion.

Para cada resultado util, captura:

- Link.
- Titulo.
- Canal.
- Fecha.
- Views si estan disponibles.
- Duracion si esta disponible.
- Idioma.
- Tipo: editorial, entrevista, clip oficial, reaccion, podcast, noticia, short.
- Relevancia para Rockwise Tales.

Filtra o separa:

- videos musicales oficiales;
- lyrics;
- lives completos;
- shorts no comparables;
- noticias de baja profundidad;
- contenido sin narrativa.

### 3. Buscar brecha editorial

Evalua:

- Hay mucho contenido en ingles y poco en espanol?
- Hay contenido en espanol, pero superficial?
- Falta un angulo humano, economico, historico o de industria?
- El tema esta atomizado en entrevistas que nadie ha conectado?
- Hay una promesa fuerte que se pueda contar en 12-20 minutos?
- Hay potencial de serie?

### 4. Revisar actualidad

Busca ganchos recientes:

- aniversario;
- estreno;
- documental;
- reunion;
- gira;
- controversia;
- muerte o efemeride;
- entrada o salida de integrantes;
- tendencia organica en comentarios.

Si no hay actualidad, el tema aun puede valer si tiene busqueda evergreen y brecha narrativa.

### 5. Comparar con datos propios

Cruza el tema con senales conocidas de Rockwise Tales:

- Temas que ya funcionaron.
- Paises con mejor fit.
- Edad y genero de audiencia.
- Distribucion fuera de seguidores.
- Duracion que la audiencia tolera.
- Comentarios que piden expansion.
- Temas que activan conversacion y no solo views.

Para TikTok, recuerda que la distribucion fuera de seguidores importa mucho. Un video largo puede estar vivo si conserva audiencia no seguidora y comentarios, aunque la tasa de finalizacion sea baja por duracion.

### 6. Evaluar monetizacion

#### YouTube

Pondera:

- Probabilidad de CTR por titulo/thumbnail.
- Watch time potencial.
- Retencion narrativa.
- Riesgo de copyright por clips o musica.
- Posibilidad de longform 12-20 minutos.
- Potencial de videos derivados.

#### TikTok

Pondera:

- Views calificables, no solo views totales.
- Audiencia fuera de seguidores.
- Paises relevantes para monetizacion.
- Tiempo promedio visto.
- Comentarios, compartidos y guardados.
- Posibilidad de convertir en serie.

Regla practica: si el objetivo es Creator Rewards, el video necesita acercarse a suficientes views relevantes. En datos previos de Rockwise Tales, alrededor de 1,000 views relevantes suele requerir aproximadamente 6,500-9,000 views totales, dependiendo del mix de paises. Usalo como referencia interna, no como promesa.



### 6bis. Clasificar potencial Home Run para YouTube LONG

Si la plataforma incluye YouTube LONG, clasificar la idea antes de recomendar produccion. Esta clasificacion no reemplaza el score de demanda; decide cuanta inversion merece.

Usar:

- `SINGLE`: tema valido pero de alcance limitado, con promesa poco visual o interes principalmente de fans duros.
- `DOUBLE`: buena oportunidad con demanda/brecha clara, pero sin suficiente amplitud o escena-prueba para apostar produccion premium.
- `HOME RUN`: idea amplia, emocional, visual y verificable que puede levantar el piso del canal completo.

Score Home Run, 0-2 por criterio:

| Criterio | Pregunta |
| --- | --- |
| Amplitud | Lo entiende/clickea audiencia fria del nicho, no solo fans expertos? |
| Reconocimiento | El artista/banda tiene senal fuerte de interes evergreen o masivo? |
| Escena-prueba | Hay imagen, entrevista, documento o momento que prueba la promesa en 5-15s? |
| Conflicto simple | La tension se explica en una frase clara? |
| Curiosity gap | Abre una pregunta fuerte sin revelar el remate? |
| Packaging | Puede producir titulo + miniatura legibles en medio segundo? |
| Sustancia LONG | Aguanta 12-20 min con micro-intrigas reales? |
| Comentabilidad | La audiencia puede opinar sin conocimiento tecnico? |
| Fit RWT | Se parece a patrones ganadores propios o justifica una prueba estrategica? |

Decision por Home Run score:

- 16-18: `HOME RUN`.
- 12-15: `DOUBLE`, o `HOME RUN` solo con evidencia extraordinaria.
- 8-11: `SINGLE` o reencuadre.
- 0-7: `HOLD` salvo experimento explicito.

Si una idea tiene score de demanda alto pero Home Run bajo, recomendar produccion proporcional, no inversion premium.

## Scorecard

Califica de 0 a 5 cada dimension y calcula sobre 100.

| Dimension | Peso | Pregunta |
| --- | ---: | --- |
| Demanda observable | 20 | Hay busqueda, views o competencia suficiente? |
| Brecha editorial | 20 | Falta una version Rockwise clara? |
| Fit de audiencia | 15 | Encaja con la audiencia actual? |
| Potencial de retencion | 15 | Hay historia, misterio, conflicto o revelacion? |
| Monetizacion | 15 | Puede generar watch time, views calificables o serie? |
| Factibilidad | 10 | Hay fuentes, clips y assets posibles? |
| Riesgo controlable | 5 | Copyright, sensibilidad o saturacion son manejables? |

Umbral recomendado:

- 80-100: producir pronto.
- 70-79: producir si el angulo queda muy fino.
- 55-69: guardar o reencuadrar.
- Menos de 55: no producir ahora salvo razon estrategica externa.

## Formato de salida

```markdown
# Demand Scout: [tema]

## Recomendacion
DECISION: PRODUCE | REFRAME | HOLD | WAIT
Score: __/100
Plataforma prioritaria:
Formato recomendado:
Idea Class: SINGLE | DOUBLE | HOME RUN | N/A
Home Run score: __/18

## Angulo ganador
- Promesa:
- Pregunta central:
- Por que ahora:

## Scorecard
| Dimension | Score | Evidencia |
| --- | ---: | --- |

## Competencia util
| Idioma | Canal | Video | Link | Observacion |
| --- | --- | --- | --- | --- |

## Home Run Fit
- Clase recomendada:
- Inversion recomendada:
- Por que no es mayor/menor:

## Brecha Rockwise
- ...

## Riesgos
- ...

## Siguiente paso
- Skill recomendado:
- Input:
```

## Checklist de calidad

Antes de cerrar:

- Incluye links de competidores cuando sea posible.
- Distingue competencia editorial de material oficial.
- Explica la brecha concreta, no solo que "hay oportunidad".
- Incluye recomendacion diferente para TikTok y YouTube si aplica.
- Si aplica YouTube LONG, incluye `Idea Class` y Home Run score.
- Marca limites de datos y supuestos.
- No revela credenciales.
