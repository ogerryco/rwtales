# Audio — Cornell/Soundgarden: prompts Suno + arquitectura CapCut

**Nota importante:** no podemos usar grabaciones reales de Soundgarden/Cornell como música de fondo (riesgo real de Content ID/baneo de audio — a diferencia de las fotos, esto SÍ te puede bloquear). Todo lo de aquí es generación original en Suno, nunca audio real de la banda.

**6 cues**, una por cada fase emocional real del guion (para tu narración de ~14:33) — no 3, porque la historia tiene más giros de tono de los que una sola pista puede sostener sin sentirse plana.

---

## CUE 1 — El gancho: el dinero rechazado (misterio, tensión contenida)

**Dónde va:** desde "A esos tres hombres les ofrecieron millones de dólares..." hasta "Peleaban por quién tiene derecho a decidir cómo se recuerda a Chris Cornell." — justo antes de la intro animada.

**SUNO LYRICS:**
```
[instrumental only, no vocals]
[cold open, single guitar note ringing out into silence, 4 bars]
[low sustained drone enters underneath, almost imperceptible]
[no drums, no resolution, tension held throughout]
[ends abruptly, unresolved, cut to silence]
```

**SUNO STYLE:**
```
dark ambient, cinematic tension, minor key, sparse, single guitar note, low drone, no drums, no vocals, mystery, documentary cold open, unresolved
```

---

## CUE 2 — Origen: la historia de la banda (nostálgico, en ascenso)

**Dónde va:** desde "Soundgarden se formó en Seattle en 1984..." hasta "...esas grabaciones serían las últimas." (incluye Superunknown, la separación, la reunión de 2010, y las sesiones de 2015-17).

**SUNO LYRICS:**
```
[instrumental only, no vocals]
[clean electric guitar arpeggio, nostalgic and warm, 90s alternative feel]
[bass enters, driving but restrained]
[light drums with brushed cymbals, mid tempo, building gradually]
[builds in energy toward the end but never fully resolves]
```

**SUNO STYLE:**
```
90s alternative rock, nostalgic, cinematic documentary score, clean electric guitar, warm bass, restrained drums, mid tempo, building energy, no vocals, hopeful undertone
```

---

## CUE 3 — Duelo: la muerte y el silencio (sombrío, frío)

**Dónde va:** desde "El 18 de mayo de 2017... murió en su hotel" hasta "...sin nadie que decidiera qué hacer con ellas."

**SUNO LYRICS:**
```
[instrumental only, no vocals]
[solo cello, slow and mournful, minimal vibrato]
[long silences between phrases]
[no drums, no bass, no guitar — cello alone]
[fades to near silence, never fully resolving]
```

**SUNO STYLE:**
```
solo cello, mournful, minimal, minor key, very slow tempo, no drums, no vocals, grief, documentary score, sparse, cold
```

---

## CUE 4 — Tributo: el concierto benéfico (agridulce, comunal)

**Dónde va:** desde "Ocho meses después de su muerte... I Am The Highway" hasta justo antes de "Para finales de ese mismo año, Vicky Cornell ya había demandado a la banda."

**SUNO LYRICS:**
```
[instrumental only, no vocals]
[warm acoustic guitar, gentle fingerpicking]
[distant crowd murmur texture underneath, very low]
[strings enter softly in the second half]
[warm but tinged with sadness, no clear resolution]
```

**SUNO STYLE:**
```
warm acoustic guitar, bittersweet, tribute concert atmosphere, gentle strings, soft dynamics, no vocals, communal warmth, melancholic undertone, documentary score
```

---

## CUE 5 — El Abismo: la guerra legal (fría, escalando)

**Dónde va:** desde "Su argumento: las siete grabaciones inéditas..." hasta "...la única forma en que podían hablar de las canciones que habían escrito juntos era a través de sus abogados." — cubre las dos demandas, la contrademanda, la de las contraseñas, y el estancamiento 2021-2022.

**SUNO LYRICS:**
```
[instrumental only, no vocals]
[tense pulsing bass, steady rhythmic pulse like a ticking clock]
[distorted guitar swells enter and recede, unresolved dissonant chords]
[restrained drums enter mid-section, like a heartbeat, not a full beat]
[intensity increases gradually toward the end, no release]
```

**SUNO STYLE:**
```
suspense, courtroom drama score, dark cinematic, distorted guitar swells, pulsing bass, restrained drums, minor key, escalating tension, no vocals, post-rock influence, cold
```

---

## CUE 6 — Resolución: el acuerdo y el Rock Hall (triunfo agridulce)

**Dónde va:** desde "En abril de 2023, sin previo aviso público, apareció un comunicado" hasta el final del guion (incluye Rock Hall, Toni cantando, y el cierre).

**SUNO LYRICS:**
```
[instrumental only, no vocals]
[warm strings enter first, hopeful but restrained]
[clean electric guitar melody enters, bittersweet not triumphant]
[builds gradually to a fuller arrangement by the middle]
[ends on a sustained, unresolved-feeling final chord — not a full resolution]
```

**SUNO STYLE:**
```
bittersweet, cinematic strings, hopeful but melancholic, slow build, clean electric guitar, orchestral rock, no vocals, documentary score, emotional, restrained triumph
```

> El acorde final "sin resolver" es intencional en las 3 cues que terminan así (1, 5 y 6) — hace eco de que el disco todavía no ha salido.

---

## ARQUITECTURA CAPCUT (4 pistas — sin audio real de la banda)

```
Pista 1 — Voz ElevenLabs: referencia (nunca se comprime)
Pista 2 — Riff original grunge (generación Suno aparte, NO Soundgarden real): -12 a -15 dB
Pista 3 — Cue de Suno correspondiente (1 a 6 según la sección): -18 dB
Pista 4 — Ambiente (público de concierto en Cue 4/Rock Hall, estática de sala en Cue 5): -24 dB
```

**Prompt para el riff original de Pista 2 (generación separada, se usa de fondo constante y sutil en todo el video):**

SUNO LYRICS:
```
[instrumental only, no vocals]
[single guitar riff, repeating, drop-D tuning feel]
[heavy but simple, four chords, grunge era]
```

SUNO STYLE:
```
grunge, heavy guitar riff, drop tuning, 90s alternative rock, instrumental, no vocals, simple repeating motif, raw production
```

## NOTAS DE MEZCLA

- Transiciones (usa un fade cruzado de 2-3 seg entre cues, no un corte seco):
  - Cue 1 → Cue 2: al entrar la intro animada
  - Cue 2 → Cue 3: en "El 18 de mayo de 2017..."
  - Cue 3 → Cue 4: en "Ocho meses después de su muerte..."
  - Cue 4 → Cue 5: en "Su argumento: las siete grabaciones inéditas..."
  - Cue 5 → Cue 6: en "En abril de 2023, sin previo aviso público..."
- Baja Pista 3 casi a silencio durante las citas textuales largas (Dave Grohl, Ben Shepherd, Jerry Cantrell) para que la voz en off no compita.
- La Cue 3 (duelo) es la más sparse a propósito — es el único momento del video donde la música casi desaparece; no la satures con la Pista 2 (riff) encima, bájala a -20dB o quítala en ese tramo.

## CONFIGURACIÓN ELEVENLABS (canal Rockwise Tales)
- Voz: masculina profunda (tu voz clonada + voice changer)
- Stability: 55%
- Similarity: 75%
- Style: 30%
- Pausas largas en el guion: usa `<break time="1.5s"/>` o cuenta "uno-mil, dos-mil" en vivo
