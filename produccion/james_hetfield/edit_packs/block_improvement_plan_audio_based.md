# Plan de mejoras por bloque basado en voz real

Fecha: 2026-07-31

Regla: la voz manda. Cada bloque se mejora despues de escuchar su duracion real, ritmo, pausas e intencion.

## Prioridad

1. B01: ya se comprobo en CapCut que queda corto.
2. B03: el bloque tiene mucha narracion y pocos visuales.
3. B05: el bloque Black Album tiene alto riesgo de quedarse corto.
4. B04: riesgo medio; necesita mas colchones emocionales.
5. B02: riesgo medio; se puede reforzar despues de B01/B03/B05.

## Gaps aproximados

| Bloque | Voz aprox. | Visual actual aprox. | Gap minimo | Objetivo mejora |
|---|---:|---:|---:|---|
| B01 | 02:57 | 01:07 | +01:50 | crear version extendida con 3:20-3:40 de cobertura |
| B02 | 01:31 | 00:34 | +00:57 | crear version extendida con 1:45-2:00 de cobertura |
| B03 | 02:21 | 00:38 | +01:43 | crear version extendida con 2:50-3:10 de cobertura |
| B04 | 01:21 | 00:46 | +00:35 | crear version extendida con 1:35-1:50 de cobertura |
| B05 | 01:42 | 00:28 | +01:14 | crear version extendida con 2:00-2:15 de cobertura |

## Criterio de carpeta

No modificar las carpetas aprobadas directamente. Crear versiones extendidas:

- `B01_v3_audio_timed_extended_coverage`
- `B02_v2_audio_timed_extended_coverage`
- `B03_v2_audio_timed_extended_coverage`
- `B04_v2_audio_timed_extended_coverage`
- `B05_v2_audio_timed_extended_coverage`

Cada carpeta debe tener:

- `00_CAPCUT_SECUENCIA_COMPLETA`
- README con duracion objetivo y frase/beat de cada shot
- assets numerados en orden de montaje
- assets candidatos marcados como `CANDIDATE`

## Principio visual

No agregar relleno decorativo. Cada visual extra debe servir para una de estas funciones:

- sostener una frase larga;
- crear pausa emocional;
- conectar dos ideas;
- reforzar un dato musical;
- evitar repeticion de una imagen que ya aparecio;
- dar margen si un clip real no funciona.
