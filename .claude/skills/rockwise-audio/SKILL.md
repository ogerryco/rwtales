---
name: rockwise-audio
description: >
  Skill 5 de 6 del pipeline Rockwise Tales. Genera el prompt para Suno AI
  (música de fondo), configura ElevenLabs para la voz, y define la arquitectura
  de 4 pistas para el montaje en CapCut.

license: MIT

metadata:
  raise.work_cycle: production
  raise.frequency: on-demand
  raise.fase: audio
  raise.prerequisites: "rockwise-script"
  raise.next: "rockwise-produccion"
  raise.gate: ""
  raise.adaptable: "true"
  raise.version: "1.1.0"
---

# Rockwise Audio

## Purpose

Producir el prompt de música para Suno AI y la arquitectura de audio para CapCut. La voz siempre es lo principal; la música es textura, no protagonista.

## Mastery Levels (ShuHaRi)

- **Shu**: Completar los dos campos de Suno (LYRICS y STYLE) correctamente
- **Ha**: Elegir tags de estilo que correspondan al período y al mood del video
- **Ri**: La música refuerza la tensión narrativa — sube en los picos, baja en los momentos íntimos

## Context

**When to use:** Después de que el script está aprobado (Skill 2).

**When to skip:** No se salta. Sin audio no hay video.

**Inputs:** Script del video + patrón emocional del Skill 1

## Steps

### Step 1: Construir prompt de Suno AI

Suno tiene DOS campos separados. Nunca mezclarlos.

**Campo LYRICS — solo instrucciones en [corchetes]:**
- Cualquier texto FUERA de corchetes se vocaliza como letra de canción
- ✅ `[instrumental only, no vocals, melancholic intro 8 bars]`
- ❌ `Start with melancholic guitar` → Suno lo cantará como letra

**Campo STYLE — tags separados por comas:**
- Género, mood, instrumentos, era, tempo
- Ejemplo: `post-grunge, melancholic, cinematic, slow tempo, electric guitar, no vocals, 90s rock`

**Verification:** Campo LYRICS tiene solo contenido entre [corchetes]. Campo STYLE tiene solo tags.

### Step 2: Definir arquitectura de 4 pistas para CapCut

| Pista | Contenido | Nivel de volumen |
|-------|-----------|-----------------|
| 1 | Voz en off (ElevenLabs) | Principal — referencia |
| 2 | Riff o melodía icónica del artista | -12 a -15 dB |
| 3 | Textura Suno AI | -18 dB |
| 4 | Ambiente (crowd, sala, estática) | -24 dB |

La pista 1 nunca se comprime por las otras. Si hay conflicto, bajan las pistas 2, 3 y 4.

> ⚠️ Pista 2 (riff del artista) — Content ID SÍ detecta audio/música (a diferencia de las fotos, que no escanea). Nunca usar una grabación real del artista como música de fondo — generar en Suno un riff ORIGINAL que evoque el estilo/época (ej. "grunge, heavy guitar riff, drop tuning, 90s alternative rock, instrumental"), nunca una copia.

**Verification:** Los 4 niveles definidos. Pista 2 confirmada como generación original, no audio real de la banda.

### Step 3: Configurar ElevenLabs

Ajustes del canal Rockwise Tales:
- Voz: masculina profunda
- Stability: 55%
- Similarity: 75%
- Style: 30%

Pausas en el script:
- `[...]` = pausa aproximada de 1.2 segundos
- `<break time="1.2s"/>` = equivalente SSML (usar si ElevenLabs acepta SSML)

**Verification:** Configuración anotada para uso en grabación.

### Step 4: QA de la toma grabada (ritmo y naturalidad)

> ⚠️ Voice Changer vs. Text-to-Speech: el canal usa Voice Changer (grabar con tu voz real y convertir el timbre) precisamente porque preserva tu ritmo/pausas naturales — a diferencia de Text-to-Speech, que sí tiene controles de velocidad y pausa (`<break time="Xs"/>`) pero sacrifica la voz natural. **Voice Changer NO corrige el ritmo después** — si la toma se grabó rápido o con pausas cortas, el resultado sonará igual de rápido. El ajuste tiene que pasar en la grabación misma, no en la herramienta.

Antes de dar una toma por buena, analizar (Whisper + librosa, o de oído):
- **Ritmo (WPM):** comparar contra el ritmo natural ya medido del canal (~122 palabras/min). Una toma notablemente más rápida (+30-40%) suele sonar mecánica aunque el tono varíe bien.
- **Varianza de pausas:** la señal más reveladora de "suena a IA" no es el tono ni el volumen — es que TODAS las pausas duren parecido. El habla humana real varía mucho: pausas casuales de una décima de segundo, pausas dramáticas reales de 1-3 segundos. Si ninguna pausa de la toma pasa de ~0.5 segundos, los momentos marcados "pausa larga" en el guion no se están honrando — hay que volver a grabar sosteniendo la pausa de verdad (contar "uno-mil, dos-mil" en el momento).

**Verification:** WPM de la toma dentro de rango del canal; al menos las pausas marcadas como "larga" en el guion duran 1+ segundo real en la grabación.

## Output

```
SUNO LYRICS:
[instrucción 1]
[instrucción 2]
[instrucción 3]

SUNO STYLE:
tag1, tag2, tag3, tag4, tag5

ARQUITECTURA CAPCUT:
Pista 1 — Voz ElevenLabs: referencia
Pista 2 — [nombre del riff/canción]: -XX dB
Pista 3 — Suno AI texture: -18 dB
Pista 4 — Ambiente [descripción]: -24 dB

NOTAS DE MEZCLA:
[instrucciones específicas de timing si aplica]
```

## Quality Checklist

- [ ] Campo LYRICS de Suno: solo contenido entre [corchetes]
- [ ] Campo STYLE de Suno: solo tags separados por comas
- [ ] Arquitectura de 4 pistas definida con niveles
- [ ] Pista 2 (riff) confirmada como generación Suno original, no audio real del artista
- [ ] Configuración ElevenLabs anotada
- [ ] Toma grabada revisada: WPM en rango del canal, pausas "largas" del guion duran 1+ segundo real
- [ ] Journal add ejecutado antes de pasar al Skill 6

## References

- Previous: `/rockwise-visuals`
- Next: `/rockwise-produccion`
