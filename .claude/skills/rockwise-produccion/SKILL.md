---
name: rockwise-produccion
description: >
  Skill 6 de 6 del pipeline Rockwise Tales. Genera el paquete de publicación:
  título, descripción, hashtags, horario, comentario de fuentes y checklist
  de configuración para TikTok y YouTube.

license: MIT

metadata:
  raise.work_cycle: production
  raise.frequency: on-demand
  raise.fase: publish
  raise.prerequisites: "rockwise-audio"
  raise.next: "rockwise-post-publish-analyst"
  raise.gate: ""
  raise.adaptable: "true"
  raise.version: "1.3.0"
---

# Rockwise Produccion

## Purpose

Empaquetar el video para publicación con metadata optimizada. Incluye configuración de privacidad, horario óptimo, comentario de fidelización fijado y comentario de fuentes.

**Canal:** @rockwisetales — TikTok (Shorts) + YouTube (Long-form exclusivo)
**Monetización activa:** TikTok Creator Rewards Program
**Meta activa YouTube:** 4,000 horas de watch time — formato long-form 12–20 min, sin Shorts en YouTube

> Ver `youtube_strategy.md` para las reglas completas del canal en YouTube.

**Mecánica real de monetización YouTube (verificado, no asumido):**
- El watch time de Shorts NO cuenta para las 4,000 horas del umbral long-form — son dos rutas de monetización separadas (Shorts: 10M vistas en 90 días; long-form: 4,000 horas). Un Short puede tener excelente desempeño y aportar cero a esta meta.
- Un video puesto en "no listado" deja de contar sus horas de reproducción PÚBLICAS hacia el umbral mientras esté así — y esas horas específicas del período no-listado no se recuperan retroactivamente al volver a ponerlo público (las horas de ANTES de que se ocultara si siguen contando). Cuidado especial si se usan videos "no listados" para separar contenido (ej. música original vs. documentales) — revisar el impacto en el conteo de horas antes de cambiar el estado de un video con tráfico real.
- El contador de horas en la pestaña de monetización de Studio puede tardar en reflejar cambios recientes (más lento que las estadísticas del video individual) — no asumir que algo se perdió si el número no sube de inmediato.

## Mastery Levels (ShuHaRi)

- **Shu**: Completar título, hashtags y checklist de publicación
- **Ha**: Optimizar el título para el patrón de búsqueda del nicho rock history
- **Ri**: El título cumple la promesa emocional del hook del video

## Context

**When to use:** Video montado y listo para subir.

**When to skip:** No se salta. Sin metadata el algoritmo no sabe a quién mostrar el video.

**Inputs:** Script aprobado + patrón narrativo del Skill 1

## Steps

### Step 0: Heredar Idea Class y definir inversion de empaque (YouTube LONG)

Antes de escribir titulo/miniatura, revisar si el orquestador o Demand Scout marco `Idea Class`.

- `SINGLE`: 1-2 titulos, 1 concepto principal de miniatura, empaque correcto sin sobreproducir.
- `DOUBLE`: 3-5 titulos, 3 conceptos de miniatura para A/B nativo.
- `HOME RUN`: 6-10 rutas de titulo/thumbnail antes de elegir las 3 variantes finales para A/B. Las variantes deben probar conceptos distintos, no solo cambios cosmeticos.

Para `HOME RUN`, el empaque debe pasar estas tres etapas:

1. `Scroll stop`: algo visible en milisegundos, normalmente rostro, emocion, cifra o objeto/documento claro.
2. `Interest`: curiosity gap entendible en segundos.
3. `Click`: propuesta de valor creible y alineada con el video.

No aprobar empaque `HOME RUN` si el titulo/miniatura requieren conocer lore previo para entender la promesa.

### Step 1: Escribir título

**Fórmulas que funcionan en RWT:**
- Fórmula A: `[Lo que nadie sabe] + [artista] + [consecuencia]`
- Fórmula B: `[Dato impactante] + [artista]`
- Fórmula C: `Por qué [artista] [acción dramática]`

**Reglas:**
- Sin clickbait vacío — el título debe cumplir lo que promete
- TikTok y YouTube tienen títulos distintos (pacing de audiencia diferente)
- No usar: signos de exclamación, emojis, palabras como "shocking" o "increíble" aisladas

> ⚠️ APRENDIZAJE REAL (datos de YouTube Studio, no teoría): el título/miniatura y la retención del guion son DOS PALANCAS SEPARADAS. Un video real del canal despegó (91 → 4,000+ vistas en 48h, empujado por "Funciones de exploración" de YouTube) con un CTR de miniatura de 7.35% — arriba del promedio típico (2-6%) — a pesar de que su guion seguía teniendo un problema real de retención en el gancho (confirmado con la curva real de audiencia). El título consigue el clic; la estructura del guion determina cuánto se queda la gente después. No asumas que un video con buen alcance algorítmico tiene automáticamente un guion óptimo — revisa las dos cosas por separado. Si tienes acceso a YouTube Studio → Analytics → pestaña "Alcance", ahí está el CTR real para confirmar.

**Verification:** El título describe exactamente lo que el video entrega.

### Step 1bis: Prueba A/B de título y miniatura — SIEMPRE (YouTube)

> ⚠️ APRENDIZAJE REAL: una buena miniatura impulsa muchísimo, y YouTube tiene su propia función nativa de prueba A/B ("Test & Compare") que no requiere adivinar cuál gana — deja que los datos reales de TU audiencia decidan.

Preparar siempre 3 variantes de miniatura (y opcionalmente de título) para la prueba A/B nativa de YouTube antes de publicar, no solo cuando parezca un video importante. Si la idea es `HOME RUN`, generar primero 6-10 rutas conceptuales y elegir las 3 mas fuertes para la prueba.

**Cómo funciona (verificado):**
- YouTube reparte tráfico real entre hasta 3 variantes.
- El ganador se decide por **watch time share (tiempo de retención), NO solo por CTR/clics** — gana la que retiene mejor a quien llega por ella, no la que más clics saca.
- Tarda entre unos días y ~2 semanas en declarar un ganador, dependiendo del volumen de impresiones del canal (canales con menos tráfico diario tardan más en llegar a una muestra confiable — apuntar a 1,000-5,000 impresiones por variante como referencia).
- Al final, la variante ganadora se vuelve automáticamente la que ve todo el mundo.

**Diseño de las 3 variantes — no hagas 3 iguales:** varía el concepto real (ej. protagonista solo vs. composición "versus"/conflicto vs. un misterio/dato específico), no solo el color o la tipografía — así la prueba realmente aprende qué gancho conceptual funciona mejor para el canal, no solo qué paleta se ve mejor.

**Verification:** 3 variantes de miniatura (mínimo) cargadas en la prueba A/B antes de publicar, ninguna es una copia cosmética de otra.

### Step 2: Escribir descripción (YouTube)

- Párrafo 1: contexto de la historia (2-3 oraciones)
- Párrafo 2: keywords naturales integradas
- Timestamps si el video es de 8+ minutos
- CTA al final: suscripción + notificaciones

**Verification:** Keywords relevantes presentes de forma natural.

### Step 3: Hashtags (TikTok) / Tags (YouTube)

TikTok: 3-5 hashtags máximo, mezcla nicho + masivo
- Ejemplo nicho: #rockhistory #grunge #alternativerock
- Ejemplo masivo: #rock #music #historia

YouTube: 10-15 tags, incluir variaciones del nombre del artista y del álbum

**Verification:** Hashtags/tags aplicados.

### Step 4: Configurar privacidad TikTok

Basado en análisis de los top performers del canal (user_data_tiktok.json):

| Setting | Valor óptimo |
|---------|-------------|
| Allow Stitches | ❌ OFF |
| Allow Stickers | ❌ OFF |
| Allow Sharing to Story | ❌ OFF |

**Verification:** Los 3 settings desactivados antes de publicar.

### Step 5: Programar horario

- **TikTok:** 18:00 hora México — mejor promedio histórico del canal (20,593 likes/video en ese slot)
- **YouTube:** publicar simultáneo o con 2 horas de diferencia

**Verification:** Publicación programada, no manual en el momento.

### Step 6: Preparar comentario de fidelización (primer comentario — YouTube)

El primer comentario fijado NO es la lista de fuentes — es una **pregunta de bajo esfuerzo cognitivo** que genere debate o respuesta emocional.

Ejemplos que funcionan:
- "¿Cuál crees que fue el mejor disco de [banda]?"
- "¿Tú hubieras tomado la misma decisión?"
- "¿Cuál es el riff más icónico de [artista]?"

Regla: la pregunta no debe requerir que el espectador piense mucho. Quieres que conteste en 3 segundos.

**Verification:** Comentario de fidelización preparado y distinto del de fuentes.

### Step 7: Preparar comentario de fuentes (segundo comentario — YouTube)

El segundo comentario contiene las fuentes. Va fijado debajo del de fidelización, o como segundo comentario destacado.

```
📚 Fuentes de investigación:
1. [fuente primaria 1]
2. [fuente primaria 2]
3. [fuente primaria 3]
```

**Verification:** Comentario de fuentes preparado antes de publicar.

## Output

```
TÍTULO TIKTOK: [texto]
TÍTULO YOUTUBE: [texto]

DESCRIPCIÓN YOUTUBE:
[párrafo contexto]
[párrafo keywords]
[timestamps si aplica]
[CTA]

HASHTAGS TIKTOK: #tag1 #tag2 #tag3
TAGS YOUTUBE: tag1, tag2, tag3...

HORARIO: [fecha y hora]

COMENTARIO FUENTES:
📚 Fuentes de investigación:
1. [fuente]
2. [fuente]
```

## Quality Checklist

- [ ] `Idea Class` revisada y nivel de inversion de empaque ajustado
- [ ] Título cumple la promesa del hook
- [ ] TikTok y YouTube tienen títulos distintos
- [ ] Video dura 12–20 minutos (YouTube long-form)
- [ ] Cierre del video tiene puente narrativo a otro video ya publicado (no CTA genérico)
- [ ] Stitches/Stickers/Sharing desactivados (TikTok)
- [ ] Publicación programada a 18:00 MX
- [ ] Comentario de fidelización (pregunta debate) listo para pinear como primer comentario
- [ ] Comentario de fuentes listo como segundo comentario
- [ ] Thumbnail preparado con YouTube Studio → Inspeccionar
- [ ] 3 variantes de miniatura (mínimo) cargadas en la Prueba A/B nativa de YouTube — SIEMPRE, no solo en videos "importantes"
- [ ] Si es `HOME RUN`, se exploraron 6-10 rutas de titulo/thumbnail antes de elegir las 3 finales
- [ ] Si el video viene de una serie de TikTok, la apertura fue auditada/reescrita para el corte LONG (no reusada tal cual)
- [ ] Journal add ejecutado — skill 6 completo, video listo

## Seguimiento post-publicación

Después de publicar, usar `rockwise-post-publish-analyst` en checkpoints de 2h, 24h, 7d y 30d cuando haya datos disponibles. Ese skill decide si conviene esperar, responder comentarios, cambiar empaque, extraer clips, hacer follow-up o registrar postmortem.

Revisar en YouTube Studio → Analytics → pestaña "Alcance": impresiones, CTR de miniatura, y de dónde viene el tráfico ("Funciones de exploración" = el algoritmo lo está probando/empujando). Un CTR arriba de ~6-7% es señal de que título/miniatura están funcionando, independiente de qué tan bien retenga el guion.

## Canal — Datos de referencia

- Seguidores TikTok: 70,337
- Likes totales: 1,097,098
- Mejor video: 329,625 likes (enero 2025)
- Meta monetización: $1,000 USD/mes (Creator Rewards activo)
- Formato: NO FACE — voz en off únicamente

## References

- Previous: `/rockwise-audio`
- Next: `/rockwise-post-publish-analyst`
