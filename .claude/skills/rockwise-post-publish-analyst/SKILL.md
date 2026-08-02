---
name: rockwise-post-publish-analyst
description: >
  Analista post-publicacion de Rockwise Tales para interpretar metricas tempranas
  y maduras de TikTok y YouTube, decidir si esperar, responder comentarios,
  cambiar empaque, extraer clips, hacer follow-up o registrar aprendizajes.
license: MIT
metadata:
  raise.work_cycle: strategy
  raise.frequency: on-demand
  raise.fase: post_publish
  raise.prerequisites: "video published"
  raise.next: "rockwise-video-coach-orchestrator | rockwise-produccion"
  raise.gate: ""
  raise.adaptable: "true"
  raise.version: "1.0.0"
---

# Rockwise Post Publish Analyst

Usa este skill cuando un video ya fue publicado y el usuario quiera entender como va, que hacer con comentarios, si tocar empaque, si esperar o si convertir el tema en serie.

Este skill debe evitar la ansiedad de mover piezas demasiado pronto. Su tarea es distinguir senales tempranas, ruido normal y problemas reales.

## Entrada minima

- Plataforma: TikTok, YouTube o ambas.
- Tiempo desde publicacion.
- Titulo o descripcion del video.
- Duracion.
- Capturas o metricas disponibles.
- Objetivo principal: distribucion, ingresos, seguidores, comentarios, watch time o aprendizaje.
- `Idea Class`, si el video tuvo Demand Scout u orquestador previo.

Si el usuario manda capturas, extrae solo lo visible y marca lo no visible como faltante.

## Clasificar checkpoint

Antes del diagnostico, identifica la ventana:

- `0-2h`: primera lectura, no sobrerreaccionar.
- `2-6h`: distribucion inicial y primeras senales de audiencia.
- `24h`: decision de empaque, comentarios y continuidad.
- `7d`: postmortem y aprendizaje.
- `30d`: evergreen, SEO, biblioteca y monetizacion acumulada.

## TikTok: lectura principal

Evalua en este orden:

1. Fuente de trafico.
2. Porcentaje de no seguidores.
3. Tiempo promedio visto.
4. Retencion y completion rate segun duracion.
5. Likes, comentarios, compartidos y guardados.
6. Nuevos seguidores.
7. Paises y potencial de views calificables.
8. Calidad de comentarios.

### Distribucion fuera de seguidores

Para TikTok, una buena primera senal es que el video salga de seguidores. Si el porcentaje de personas que no siguen esta por arriba de seguidores, el sistema ya lo esta probando con audiencia nueva.

No trates un completion rate bajo como fracaso automatico en videos largos. En piezas de 10-12 minutos, el tiempo promedio visto, la curva de retencion y la calidad de comentarios importan mas que una tasa de finalizacion aislada.

### Monetizacion TikTok

Usa esto como regla practica interna:

- Creator Rewards depende de views calificables, no solo views totales.
- En historicos de Rockwise Tales, llegar a alrededor de 1,000 views relevantes puede requerir aproximadamente 6,500-9,000 views totales, segun el mix de paises.
- Mexico, Estados Unidos y Brasil son mas relevantes para views calificables que paises fuera del programa.

No prometas pago por video. Di "potencial", "todavia no alcanza" o "va en camino" segun los datos.

## YouTube: lectura principal

Evalua en este orden:

1. Impresiones.
2. CTR.
3. Duracion media de visualizacion.
4. Porcentaje promedio visto.
5. Retencion del primer minuto.
6. Fuentes de trafico.
7. Nuevos vs recurrentes.
8. Watch hours.
9. Comentarios y subs ganados.

### Empaque YouTube

Si hay impresiones suficientes y CTR bajo, revisar:

- titulo;
- miniatura;
- promesa;
- claridad del conflicto;
- legibilidad movil.

Si hay CTR bueno pero retencion baja, revisar:

- primer minuto;
- ritmo;
- promesa incumplida;
- densidad de informacion nueva;
- exceso de contexto antes del conflicto.

### Aprendizaje RWT: tension continua

Cuando haya retencion por timestamps, no mirar solo el promedio. Detecta tres zonas:

1. Caida inicial: del hook al minuto 1.
2. Meseta: del minuto 1 al 70-85% del video.
3. Salida: cierre y pantallas finales.

Si el video pierde fuerte al inicio pero luego sostiene una meseta estable, el cuerpo narrativo funciona y el problema esta en el primer minuto. No reescribir toda la formula: reforzar el hook, evitar biografia temprana sin amenaza y mantener la pregunta abierta.

En Rockwise, una buena meseta suele indicar que la audiencia quiere escudrinar la historia: dato oculto, contradiccion, morbo verificable, pregunta pendiente o detalle que quiere comentar. Registrar esos momentos como aprendizaje para el siguiente guion.

Tambien evaluar consumo dual: si la audiencia viene de TV o de usuarios que escuchan mientras usan el celular, la narracion y la musica son parte del sistema de retencion, no solo estetica.
### Diagnostico Home Run despues de publicar

Si el video fue clasificado como `HOME RUN`, no diagnosticarlo solo por vistas. Separar cuatro capas:

1. `Idea`: la promesa era amplia y entendible para audiencia fria?
2. `Packaging`: hubo suficientes impresiones y CTR competitivo?
3. `Satisfaccion`: la retencion confirma que el video entrego lo prometido?
4. `Distribucion`: YouTube lo probo en browse/suggested o se quedo en circulos pequenos?

Acciones por falla:

- Idea debil: registrar como `MISCLASSIFIED`, ajustar Demand Scout y no sobreinvertir en angulos similares.
- Packaging debil: `UPDATE PACKAGING` con una promesa mas simple y visual.
- Satisfaccion debil: `FIX OPENING` o registrar aprendizaje para el siguiente corte; no maquillar con miniatura si la promesa no se entrega.
- Distribucion limitada con buenas senales: `WAIT` o `FOLLOW-UP`, no tocar demasiado pronto.

En videos `SINGLE` o `DOUBLE`, no exigir comportamiento viral. Medir si cumplieron su objetivo proporcional: biblioteca, aprendizaje, busqueda, comentarios o puente a otro video.

## Matriz de accion

| Situacion | Decision | Accion |
| --- | --- | --- |
| Muy temprano y distribucion sana | `WAIT` | Revisar en el siguiente checkpoint |
| Buenos comentarios | `ENGAGE` | Responder y sembrar siguiente pieza |
| TikTok con alta no-audiencia pero baja retencion | `OBSERVE` | No borrar; estudiar caida y comentarios |
| TikTok sin distribucion fuera de seguidores | `REFRAME HOOK` | Considerar nuevo corte o parte 2 |
| YouTube con impresiones altas y CTR bajo | `UPDATE PACKAGING` | Cambiar titulo/thumbnail |
| YouTube con CTR alto y retencion baja | `FIX OPENING` | Rehacer apertura para futuros cortes |
| Comentarios piden expansion | `FOLLOW-UP` | Planear secuela, short o video largo |
| Error tecnico, copyright o dato falso | `INTERVENE` | Corregir, fijar comentario o retirar si aplica |
| Ventana madura sin traccion | `POSTMORTEM` | Registrar aprendizajes y mover al siguiente |

## Reglas de intervencion

- En TikTok no borres ni resubas por ansiedad en las primeras horas.
- Responder comentarios cuenta como distribucion editorial si activa conversacion real.
- Si el tema esta funcionando con no seguidores, prioriza engagement antes que cambios.
- Si un comentario revela una objecion repetida, conviertela en comentario fijado o video respuesta.
- En YouTube, no cambies titulo/thumbnail sin mirar impresiones y CTR juntos.
- Si el video es parte de una estrategia de puente hacia YouTube, mide tambien clicks, preguntas y demanda de version larga.

## Formato de salida

```markdown
# Post Publish: [video]

## Lectura rapida
- Plataforma:
- Checkpoint:
- Estado:
- Senal mas fuerte:
- Riesgo:
- Idea Class: SINGLE | DOUBLE | HOME RUN | N/A

## Decision
DECISION: WAIT | ENGAGE | OBSERVE | UPDATE PACKAGING | FOLLOW-UP | INTERVENE | POSTMORTEM

## Diagnostico
- ...

## Acciones inmediatas
1. ...
2. ...
3. ...

## Siguiente revision
- Cuando:
- Que metrica mirar:

## Aprendizaje para Rockwise
- ...
```

## Checklist de calidad

Antes de cerrar:

- El checkpoint esta identificado.
- Las metricas visibles se citan con numero.
- Las metricas faltantes no se inventan.
- La decision no exagera senales tempranas.
- Distingue YouTube de TikTok.
- Incluye al menos una accion concreta.
- Si el video era `HOME RUN`, separa falla de idea, packaging, satisfaccion y distribucion.
