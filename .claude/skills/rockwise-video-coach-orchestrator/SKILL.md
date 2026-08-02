---
name: rockwise-video-coach-orchestrator
description: >
  Orquestador estrategico de Rockwise Tales para decidir que video conviene producir,
  como empacarlo, cuando publicarlo y como reaccionar despues de verlo en datos.
  Coordina scouting, research, QA, produccion y analisis post-publicacion con foco
  en monetizacion, retencion y crecimiento multiplataforma.
license: MIT
metadata:
  raise.work_cycle: strategy
  raise.frequency: on-demand
  raise.fase: orchestrator
  raise.prerequisites: ""
  raise.next: "rockwise-demand-scout | rockwise-research | rockwise-produccion | rockwise-post-publish-analyst"
  raise.gate: ""
  raise.adaptable: "true"
  raise.version: "1.0.0"
---

# Rockwise Video Coach Orchestrator

Usa este skill cuando el usuario quiera decidir, auditar o corregir la estrategia de un video de Rockwise Tales antes, durante o despues de publicarlo.

Este skill no reemplaza a los especialistas. Su trabajo es diagnosticar la situacion, elegir el siguiente skill correcto, pedir o inferir el minimo contexto necesario y devolver una decision accionable.

## Principio central

Cada video debe responder tres preguntas antes de consumir produccion:

1. Hay demanda real o una brecha clara?
2. El angulo puede sostener retencion y conversacion?
3. La pieza tiene una ruta concreta hacia monetizacion o aprendizaje reutilizable?

Si una de estas respuestas no esta clara, el orquestador debe pausar la produccion y mandar el caso al especialista adecuado.
## Home Run Gate (YouTube LONG)

Aprendizaje 2026-07-25 basado en el playbook publico de Paddy Galloway y en los casos propios Weiland/James/Soundgarden: no todas las ideas deben recibir el mismo nivel de produccion. YouTube distribuye por power law; una idea mucho mejor ejecutada puede multiplicar el canal completo. El orquestador debe clasificar cada idea LONG antes de pasar a research profundo.

Clasificacion:

- `SINGLE`: idea normal, util para biblioteca o aprendizaje. Produccion ligera.
- `DOUBLE`: buena idea con potencial por encima del promedio. Produccion completa, sin sobredimensionar.
- `HOME RUN`: idea amplia, visual, emocional y verificable que merece inversion premium.

Una idea YouTube LONG solo puede ser `HOME RUN` si cumple la mayoria de estos criterios:

- Artista o banda reconocible para audiencia amplia, no solo fans duros.
- Conflicto entendible en una frase por alguien que no conoce el lore.
- Escena-prueba o documento visual que pueda aparecer en los primeros 5-15 segundos.
- Promesa emocional concreta, no solo tema general.
- Curiosity gap claro sin resolver el remate.
- Potencial de titulo y miniatura entendible en medio segundo.
- Suficiente sustancia para sostener 12-20 minutos con micro-intrigas.
- Comentabilidad: una pregunta que la audiencia pueda responder sin ser experta.
- Fit con patrones propios del canal o una razon estrategica explicita para probarlo.

Inversion por clase:

- `SINGLE`: 1-2 rutas de titulo, 1 paquete visual, research acotado.
- `DOUBLE`: 3-5 rutas de titulo, 3 miniaturas A/B, research completo.
- `HOME RUN`: 6-10 rutas de titulo/thumbnail antes de elegir 3 para A/B, apertura auditada cuadro a cuadro, prueba estricta de satisfaccion en los primeros 30 segundos, y mayor inversion de assets/edicion.

El orquestador debe pasar `Idea Class` a los siguientes skills. Si un tema no es `HOME RUN`, no debe tratarse como fracaso; solo debe recibir una inversion proporcional.

## Entrada minima

Cuando falte contexto, intenta inferirlo desde el repo antes de preguntar.

- Tema, artista, album, cancion o conflicto propuesto.
- Plataforma principal: YouTube longform, TikTok longform, Shorts/Reels o multiplataforma.
- Estado del video: idea, scouting, research, guion, assets, publicacion, post-publicacion.
- Objetivo dominante: ingresos, crecimiento, autoridad, prueba de formato o aprendizaje.
- Datos disponibles: links, capturas, metricas, reportes previos o analytics exportados.

## Contexto local que debe revisar

Cuando existan, revisa estos artefactos antes de emitir decision:

- `tiktok_channel_analysis.md`
- `youtube_strategy.md`
- `rwt_real_analytics_longform.json`
- `rwt_demand_fit_results.json`
- `tiktok_own_videos.json`
- Reportes `youtube_*scouting*`, `youtube_*competencia*` o similares.
- Reportes de skills anteriores dentro del repo.

No expongas secretos, tokens, llaves API ni rutas sensibles completas en el resultado final.

## Clasificacion del caso

Determina primero en que punto esta el trabajo.

### Idea o tema nuevo

Ruta:

1. Ejecutar o solicitar `rockwise-demand-scout`.
2. Si el score pasa el umbral, pasar a `rockwise-research`.
3. Si no pasa, recomendar reencuadre, espera o descarte.

Decision posible:

- `PRODUCE`
- `REFRAME`
- `HOLD`
- `WAIT`

### Tema validado pero sin historia

Ruta:

1. Usar `rockwise-research`.
2. Exigir brecha narrativa, fuentes independientes y clips verificables.
3. Convertir el hallazgo en promesa editorial clara.

Decision posible:

- `PRODUCE`
- `SPLIT`
- `REFRAME`

### Guion o corte en proceso

Ruta:

1. Usar `rockwise-qa-audit` para verdad factual y claims delicados.
2. Auditar manualmente retencion si no existe un skill dedicado:
   - primer minuto;
   - promesa no resuelta;
   - cambios de energia;
   - escenas con informacion nueva;
   - densidad de assets;
   - momentos comentables.
3. Mandar cambios concretos al guion o edicion.

Decision posible:

- `PRODUCE`
- `REFRAME`
- `SPLIT`

### Publicacion y empaque

Ruta:

1. Usar `rockwise-produccion`.
2. Revisar titulo, descripcion, hashtags, thumbnail y plan de comentarios.
3. Si es YouTube, priorizar CTR, promesa y watch time.
4. Si es TikTok, priorizar distribucion fuera de seguidores, retencion temprana y comentario detonador.

Decision posible:

- `PUBLISH`
- `UPDATE PACKAGING`
- `HOLD`

### Video ya publicado

Ruta:

1. Usar `rockwise-post-publish-analyst`.
2. Clasificar checkpoint: primeras 2 horas, 6 horas, 24 horas, 7 dias.
3. Decidir si esperar, responder comentarios, cambiar empaque, extraer clips, hacer follow-up o registrar aprendizaje.

Decision posible:

- `WAIT`
- `ENGAGE`
- `UPDATE PACKAGING`
- `FOLLOW-UP`
- `POSTMORTEM`

## Matriz de decision

Usa esta matriz para cerrar cada consulta.

| Decision | Cuando aplica | Siguiente paso |
| --- | --- | --- |
| `PRODUCE` | Demanda, brecha y fit son claros | Iniciar research o guion |
| `REFRAME` | Hay tema, pero el angulo actual no compite | Proponer 2-3 angulos mejores |
| `SPLIT` | Hay demasiado material para una sola pieza | Separar longform, TikTok y shorts |
| `HOLD` | La evidencia aun no justifica produccion | Guardar backlog con condicion de activacion |
| `WAIT` | Es temprano o los datos aun no son concluyentes | Definir siguiente checkpoint |
| `UPDATE PACKAGING` | El contenido puede funcionar pero titulo/thumbnail/hook fallan | Cambiar empaque especifico |
| `ENGAGE` | Hay senales de conversacion | Responder comentarios y sembrar siguiente video |
| `FOLLOW-UP` | El publico pide expansion o serie | Definir parte 2 o video relacionado |
| `POSTMORTEM` | Ya paso la ventana principal | Registrar aprendizajes y accion reutilizable |

## Formato de salida

Entrega siempre un diagnostico breve y una decision clara.

```markdown
## Diagnostico
- Estado:
- Plataforma:
- Objetivo:
- Senal mas importante:
- Riesgo principal:

## Decision
DECISION: PRODUCE | REFRAME | SPLIT | HOLD | WAIT | UPDATE PACKAGING | ENGAGE | FOLLOW-UP | POSTMORTEM

## Por que
- ...

## Siguiente skill
- Skill:
- Input que debe recibir:

## Acciones
1. ...
2. ...
3. ...
```

## Checklist de calidad

Antes de responder, verifica:

- La decision no es generica.
- El siguiente skill esta nombrado.
- La recomendacion distingue YouTube de TikTok.
- La monetizacion esta considerada sin inventar ingresos.
- Las incertidumbres estan marcadas como incertidumbre.
- No se revelan secretos ni credenciales.
