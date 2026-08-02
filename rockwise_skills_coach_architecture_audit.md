# Auditoria de skills Rockwise Tales: hacia un coach de monetizacion

Fecha: 2026-07-22

## Diagnostico ejecutivo

La idea es viable y el set actual ya tiene una base fuerte: `rockwise-research`, `rockwise-script`, `rockwise-script-short`, `rockwise-qa-audit`, `rockwise-assets`, `rockwise-visuals`, `rockwise-audio` y `rockwise-produccion` cubren bien el pipeline de produccion de un video.

El hueco no esta en producir videos. El hueco esta antes y despues:

- Antes: decidir que video conviene producir para maximizar monetizacion real.
- Durante: auditar si el guion/titulo/miniatura estan optimizados para watch time, CTR, retencion y dinero, no solo para calidad narrativa.
- Despues: interpretar resultados 2h/24h/7d y convertirlos en aprendizaje operativo.

Por eso hace falta un skill orquestador y varios expertos de estrategia, no reemplazar los skills existentes.

## Skills actuales auditados

| Skill | Estado | Fortalezas | Hueco para la idea nueva |
|---|---|---|---|
| `rockwise-research` | Solido | Ya exige scouting de competencia, relevancia actual y analisis del canal antes de elegir tema | Debe delegar ese Step 0 a un experto de demanda/monetizacion con APIs y scorecard, no dejarlo como checklist manual |
| `rockwise-script` | Muy solido | Tiene principios narrativos, lecciones reales de retencion y reglas para LONG YouTube | No calcula potencial economico ni riesgo de abandono por estructura antes de escribir |
| `rockwise-script-short` | Solido | Diferencia bien short/long y protege contra mecanica de listas | Necesita separarse mas entre TikTok monetizable y YouTube Shorts, porque sus incentivos no son iguales |
| `rockwise-qa-audit` | Muy solido como gate factual | Excelente doble verificacion independiente | No audita performance, retencion, promesa de titulo, ni monetizacion |
| `rockwise-assets` | Solido | Tiene aprendizajes reales de clips, frame exacto, audio/video y densidad visual | No prioriza assets segun potencial de retencion o riesgo de Content ID economico |
| `rockwise-visuals` | Correcto | Resuelve gaps de IA visual con prompts | No evalua si la IA ayuda o perjudica percepcion de originalidad/monetizacion |
| `rockwise-audio` | Solido | Muy buena regla sobre Voice Changer, WPM y pausas reales | Falta integrarlo con auditoria de retencion: ritmo de audio como factor de abandono |
| `rockwise-produccion` | Bueno | Metadata, A/B thumbnails, comentarios, horarios, reglas TikTok/YouTube | Es pre-publicacion. El seguimiento post-publicacion es muy corto y no tiene protocolo de decision |

## Arquitectura recomendada

Crear un orquestador principal:

`rockwise-video-coach-orchestrator`

Mandato:

Maximizar monetizacion real de Rockwise Tales combinando demanda, retencion, watch time, CTR, riesgo de copyright, distribucion TikTok y aprendizaje historico del canal.

Subskills/expertos sugeridos:

| Skill nuevo | Proposito |
|---|---|
| `rockwise-video-coach-orchestrator` | Decide que experto activar segun etapa: idea, guion, metadata, publicacion o analisis post-publicacion |
| `rockwise-demand-scout` | Usa YouTube Data API, busqueda web y datos historicos RWT para decidir si una idea merece producirse |
| `rockwise-youtube-monetization-expert` | Evalua potencial de watch hours, CTR, retencion, evergreen/search y elegibilidad de monetizacion |
| `rockwise-tiktok-distribution-expert` | Evalua For You, followers vs no followers, duracion, paises relevantes, Creator Rewards y umbral de vistas relevantes |
| `rockwise-retention-auditor` | Audita hook, estructura, midpoint, intro, ritmo y posibles caidas antes de grabar/editar |
| `rockwise-title-thumbnail-auditor` | Genera y evalua promesa de titulo/miniatura, separando CTR de retencion |
| `rockwise-post-publish-analyst` | Interpreta metricas 2h/24h/7d y decide: esperar, responder comentarios, cambiar miniatura/titulo, recortar, repostear o convertir en serie |

## Integracion con pipeline actual

Flujo recomendado:

1. Idea nueva
   - `rockwise-video-coach-orchestrator`
   - `rockwise-demand-scout`
   - `rockwise-youtube-monetization-expert`
   - `rockwise-tiktok-distribution-expert`

2. Si la idea pasa el gate
   - `rockwise-research`
   - `rockwise-script` o `rockwise-script-short`

3. Antes de produccion
   - `rockwise-qa-audit`
   - `rockwise-retention-auditor`
   - `rockwise-title-thumbnail-auditor`

4. Produccion
   - `rockwise-assets`
   - `rockwise-visuals`
   - `rockwise-audio`
   - `rockwise-produccion`

5. Despues de publicar
   - `rockwise-post-publish-analyst`
   - actualiza memoria/patrones del canal

## Gates nuevos recomendados

| Gate | Pregunta |
|---|---|
| Demand Gate | Hay suficiente demanda o hueco competitivo para producir este video |
| Monetization Gate | El formato elegido maximiza dinero real, no solo views |
| Retention Gate | El hook siembra la pregunta sin resolverla y no causa abandono temprano |
| Packaging Gate | Titulo/miniatura prometen exactamente lo que el video entrega |
| Platform Fit Gate | TikTok y YouTube no estan recibiendo el mismo empaque si sus incentivos divergen |
| Post-Publish Gate | La decision posterior se basa en metricas, no ansiedad de las primeras horas |

## Recomendacion inmediata

No editar todos los skills existentes de golpe.

Primero crear `rockwise-video-coach-orchestrator` y `rockwise-demand-scout`, porque son los que desbloquean la decision mas valiosa: elegir el siguiente video con base en datos antes de invertir 12+ horas en investigacion, assets y edicion.

Segundo crear `rockwise-post-publish-analyst`, porque ya hay datos reales de TikTok y YouTube que se estan revisando manualmente en chat; convertir eso en protocolo evitara decisiones impulsivas.

Tercero actualizar `rockwise-research` para que su Step 0 apunte al nuevo `rockwise-demand-scout` como prerequisito formal.

## Decision recomendada para la siguiente iteracion

Crear tres skills:

1. `rockwise-video-coach-orchestrator`
2. `rockwise-demand-scout`
3. `rockwise-post-publish-analyst`

Despues de probarlos con un candidato real (James Hetfield, Anthony Kiedis o Jonathan Davis), ajustar `rockwise-research` y `rockwise-produccion` para integrarlos.
