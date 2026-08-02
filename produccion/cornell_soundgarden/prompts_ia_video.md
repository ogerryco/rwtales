# Cornell/Soundgarden — Prompts de video IA + revisión del teaser

## Revisión del teaser (Cornell teaser.mp4, 1:29, revisado 2026-07-17)

**Audio/narración:** correcto — transcripción con Whisper confirma que corresponde línea por línea al gancho + presagio de Nirvana (guion líneas 17-59), sin discrepancias de contenido.

**Visuales — problemas encontrados y resueltos:**
- ~45s (durante "siete canciones que nadie ha escuchado"): apareció una captura de una página de "net worth" de celebridades (con Taylor Swift en el carrusel) — **NO usar**, probablemente proviene de un video de comentario/análisis de otro canal (ej. "Chris Cornell's Wealth Who Profited the Most and Why.mp4"), no es footage de archivo real.
- ~70-80s (bloque de Nirvana/Courtney Love/Dave Grohl): apareció video stock genérico de mazo de juez + una foto "cara a cara estilo UFC" de Courtney Love/Dave Grohl (`2.jfif`, real pero de tono equivocado, parece meme) — **reemplazado** por:
  - `foto_courtney_love_dave_grohl.jpg` (ya existía, compuesto editorial serio) — 0-5s, zoom lento hacia la cara de ella
  - `3.jfif` (foto de prensa clásica de Nirvana: Cobain/Novoselic/Grohl, B&N) — 5-10s, zoom lento hacia Cobain
  - Ambas con animación Ken Burns (zoom/pan) en CapCut, NO usar el clip `09_PRESAGIO_nirvana_reading_1992.mp4` (real pero visualmente no comunica nada de la disputa legal — solo muestra una banda tocando bajo luz roja, sin conexión con la narración).
- Otros archivos descargados hoy y verificados como buenos: `1.jfif` (alfombra roja Rock Hall 2025 — Cameron/Thayil/Shepherd/Yamamoto), `4.jfif` (foto de prensa Soundgarden joven, B&N).

**Apertura (primer minuto):** decisión de la editora de meter la voz en off inmediatamente sobre el clip de Cornell cantando (sin los 2-3s de silencio que sugería la guía original) — confirmado que funciona bien para retención de YouTube (evita "dead air" en los primeros segundos), sin perder el eco narrativo con Toni al final (que depende de repetir la canción/plano, no del silencio inicial).

**Copyright:** verificación inicial de YouTube (paso "Verificación inicial" al subir como privado) no encontró problemas.

---

## Prompts de video IA generados (2026-07-17)

Todos diseñados para escenas que nunca se filmaron (sesiones de estudio privadas 2015-2017) — sin caras reconocibles de ningún integrante, usando solo siluetas/sombras desenfocadas, consistente con la política del canal de no generar rostros de personas reales con IA.

### VIDEO 1 — Consola de mezcla con el tracklist (8s)

**Imagen inicial:**
```
Close-up of a vintage analog mixing console in a dim recording studio, a handwritten tracklist sheet taped to the console, clearly reading a numbered list:
1. Road Less Traveled
2. Orphans
3. At Orphan's Door
4. Cancer
5. Ahead of the Dog
6. Merrmas
7. Stone Age Mind
red recording light glowing softly, warm amber lighting, shallow depth of field, out-of-focus silhouette of a musician standing blurred in the background, cinematic documentary photography, no visible faces, legible clean handwriting
```

**Imagen final:**
```
Same mixing console now closer in frame, the handwritten tracklist sheet with the seven song titles now fully readable and centered in frame, red recording light still glowing, the blurred silhouette now leaning over the console in soft focus, dust particles floating in the amber light beam, cinematic depth of field, no visible faces, legible clean handwriting
```

**Prompt de movimiento:**
```
Slow cinematic dolly-in push toward the mixing console, ending centered on the handwritten tracklist sheet with the seven song titles clearly legible, shallow depth of field throughout, subtle handheld camera breathing, red light flickers gently, silhouette figure shifts slightly in the background, no faces revealed, moody atmospheric recording studio
```

### VIDEO 2 — Estantería de cintas analógicas, una por canción (8s)

**Imagen inicial:**
```
Stack of seven analog reel-to-reel tape boxes on a studio shelf, each box individually labeled by hand with one song title: "Road Less Traveled," "Orphans," "At Orphan's Door," "Cancer," "Ahead of the Dog," "Merrmas," "Stone Age Mind" — labels clearly legible, dim moody backlight, out-of-focus silhouette of a guitarist mid-strum blurred in the background, warm amber and red tones, cinematic documentary photography, no visible faces, legible clean handwriting
```

**Imagen final:**
```
Camera has panned across the shelf, revealing all seven labeled tape boxes in sequence clearly readable, a drum kit silhouette visible in soft focus behind them, dust particles drifting through a beam of light, same warm amber and red tones, cinematic depth of field, no visible faces, legible clean handwriting
```

**Prompt de movimiento:**
```
Slow cinematic horizontal pan across the seven labeled tape boxes from left to right, each title becoming legible as the camera passes, shallow depth of field, dust particles floating through the light beam, silhouette shifts subtly in the background, moody atmospheric lighting, no faces revealed
```

### VIDEO 3 — "Summer Tiger" se convierte en "Ahead of the Dog" (duración a definir)

Para la línea: *"Una de ellas ni siquiera era nueva: 'Ahead of the Dog' había nacido años antes, durante el álbum King Animal, de 2012, con otro nombre — 'Summer Tiger' — y la reciclaron para esto."*

**Imagen inicial:**
```
A dusty, aged analog tape box sitting on an archive shelf among other boxes, handwritten label clearly reading "SUMMER TIGER — King Animal sessions, 2012," faded ink, thin layer of dust visible, warm sepia-toned archival lighting, shallow depth of field, cinematic documentary photography, no visible faces, legible clean handwriting
```

**Imagen final:**
```
Same tape box now in close-up, the old title "SUMMER TIGER" has a single diagonal line struck through it, with "AHEAD OF THE DOG" handwritten just below in fresh, slightly different ink, an out-of-focus blurred hand visible at the edge of frame having just finished writing, lighting shifts subtly cooler and more modern than the sepia tone before, dust particles floating, cinematic depth of field, no visible faces, legible clean handwriting
```

**Prompt de movimiento:**
```
Slow cinematic dolly-in from a wide shot of a dusty archive shelf toward a close-up of one specific tape box, ending on a blurred out-of-focus hand crossing out "Summer Tiger" with a single pen stroke and handwriting "Ahead of the Dog" just beneath it in fresh ink, shallow depth of field throughout, dust particles drifting in the light, poignant documentary tone, no faces revealed
```

### VIDEO 4 — Títulos conocidos, música sellada (duración a definir)

Para la línea: *"Los títulos ya existían. La música, todavía no la había escuchado nadie."*

**Imagen inicial:**
```
Wide shot of a dim table with several analog tape boxes lined up, each clearly labeled by hand with a song title, one box has an official legal exhibit tag attached with a case number, dust settled undisturbed on the surfaces, single spotlight from above, deep shadows, cinematic documentary photography, still and silent atmosphere, no visible faces, legible clean handwriting
```

**Imagen final:**
```
Close-up on one specific tape box, its handwritten song title clearly legible, red "SEALED" evidence tape strips crossing over the opening of the box, untouched dust undisturbed on the seal, the legal exhibit tag visible at the edge of frame, dim single-source lighting, cinematic shallow depth of field, still and silent atmosphere, no visible faces, legible clean handwriting
```

**Prompt de movimiento:**
```
Slow cinematic dolly-in push from a wide shot of the table toward a close-up on one sealed tape box, camera movement is the only motion — no hands, no people, ending centered on the red evidence seal strip across the box, dust particles drifting faintly in the spotlight beam, mournful and still tone, no faces revealed, no sound implied
```

**Nota técnica (aplica a los 4 videos):** los generadores de video IA (Kling, Runway, Luma) suelen fallar al renderizar texto legible con precisión. Es probable necesitar 2-3 intentos para que los títulos salgan legibles y sin errores de ortografía. Si el texto sigue saliendo distorsionado, generar el video sin texto y añadir los títulos como overlay animado en CapCut.

---

## Hueco de audio sin video: min 11:59-14:00 (auditoría 2026-07-18, corregida)

Video "Cornell y su legado (semicompleto).mp4" (20:19) tiene un hueco real de **107 segundos**
sin visual (pantalla negra), en dos tramos, verificado con extracción de frames cada 2-5s + Whisper.
**Corrección importante:** una primera pasada detectó solo 46s (desde 13:00) — al escanear desde
antes se confirmó que el negro en realidad empieza a los 11:59, casi el doble de lo estimado.

- **Gap A: 11:59-13:12 (73s)** — cubre desde "¿Qué es lo que de verdad estaban protegiendo?"
  hasta justo antes del anuncio de abril 2023.
- (13:12-13:22 ya cubierto por la captura de Instagram del anuncio de abril 2023 — no tocar)
- **Gap B: 13:22-13:56 (34s)** — desde "no revelaron los términos" hasta "terminar las siete
  grabaciones."
- (13:56 en adelante ya cubierto por la foto de Terry Date en la consola — no tocar)

**IMPORTANTE — flujo de generación corregido (2026-07-18):** cada imagen se generaba de forma
independiente y Flow creaba su propio cuarto/objetos que no encajaban con la imagen anterior.
Flujo correcto: 1) genera la Imagen inicial normal. 2) Para la Imagen final, usa esa MISMA
imagen ya generada como base/referencia (edición de imagen sobre ella, no generación nueva desde
cero) y aplica solo el cambio descrito abajo. 3) Con las dos imágenes ya consistentes entre sí,
genera el movimiento. Todos los prompts de "Imagen final" de aquí en adelante ya están escritos
como instrucciones de edición ("using this same image as the base...").

**Flow/Veo generan clips de 8s fijos. Reparto real:**
- **Gap A (73s):** 73 ÷ 8 = 9.1 → **9 clips de 8s** (Videos 5-13) = 72s + congelar el último
  frame de Video 13 un 1s extra = 73s
- **Gap B (34s):** 34 ÷ 8 = 4.25 → **4 clips de 8s** (Videos 14-17) = 32s, los 2s sobrantes se
  absorben con transiciones cruzadas de ~0.5s entre cada corte (4 cortes × 0.5s = 2s) = 34s

**Total: 13 clips nuevos de 8s + los 4 ya existentes (Video 1-4) = 17 clips de IA en todo el video.**

### VIDEO 5 — La pregunta sin responder (8s) — Gap A, beat 1 de 9

Para: *"Pero ¿qué es lo que de verdad estaban protegiendo?"*

**Imagen inicial:**
```
Empty spotlight on a bare stage, three microphone stands standing empty in the dark, a single
beam of light center stage, no performers, dust particles visible in the light beam, cinematic
documentary photography, no visible faces
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: narrow the spotlight beam until only one microphone stand
catches the last of the light before the scene fades to near total darkness. Do not change
anything else about the stage.
```

**Prompt de movimiento:**
```
Slow cinematic pull-back from the empty spotlit stage as the light beam gradually narrows and
dims, three empty microphone stands remaining in near-darkness, contemplative and unresolved
tone, no faces revealed
```

### VIDEO 6 — El juez desestima, la demanda sigue viva (8s) — Gap A, beat 2 de 9

Para: *"En marzo de 2021, un juez recomendó desestimar dos de los reclamos de Vicky Cornell. La
demanda seguía viva, pero ya no completa."*

**Imagen inicial:**
```
Close-up of an official legal document on a dark wooden desk, completely unstamped and intact,
an out-of-focus blurred hand holding a rubber stamp reading "DISMISSED" poised just above the
top of the page, warm desk lamp light, cinematic documentary photography, no visible faces,
legible clean print
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: the "DISMISSED" stamp is now pressed down firmly onto the
top two lines of the document, ink still fresh, and the blurred hand is lifting away. The rest
of the document remains exactly the same, intact and legible.
```

**Prompt de movimiento:**
```
Slow cinematic push toward the legal document as a blurred hand lowers a "DISMISSED" stamp and
presses it firmly onto only the top portion of the page, ink glistening fresh where it lands,
then the hand lifts away leaving the rest of the document intact and unresolved below, warm
still lamp light, no faces revealed
```

### VIDEO 7 — Pasan los años, nada cambia (8s) — Gap A, beat 3 de 9

Para: *"Pasó 2021, pasó 2022."*

**Imagen inicial:**
```
Dim office interior, soft blurred daylight coming through a window in the background, an empty
wooden desk in the foreground with a thin layer of dust, nothing in the room moves, warm dim
light, cinematic documentary photography, no visible faces, no text anywhere in frame
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: the light coming through the window is now noticeably dimmer
and grayer, as if much more time has passed. The desk below has a visibly thicker layer of
dust. Nothing else in the room changes.
```

**Prompt de movimiento:**
```
Extremely slow, continuous and unbroken cinematic shot as the light through the window gradually
dims from bright to gray, one single uninterrupted transition with no cuts and no scene changes,
the desk below remaining perfectly static and undisturbed throughout, dust thickening almost
imperceptibly, quiet and stagnant tone, no faces revealed, no text anywhere in frame
```

### VIDEO 8 — Las cintas, todavía guardadas (8s) — Gap A, beat 4 de 9

Para: *"Las canciones seguían guardadas, ni terminadas, ni destruidas, ni escuchadas por nadie
fuera de un estudio y un juzgado."*

**Imagen inicial:**
```
A shelf of seven labeled analog tape boxes, each individually labeled by hand with one song
title: "Road Less Traveled," "Orphans," "At Orphan's Door," "Cancer," "Ahead of the Dog,"
"Merrmas," "Stone Age Mind" — labels clearly legible, now with a thicker layer of undisturbed
dust, sitting in near total darkness, only a faint sliver of light from under a door far in the
background, cinematic documentary photography, no visible faces, legible clean handwriting
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: no change at all to the tape boxes, only the faint light
under the far door flickers slightly, as if time is passing outside. Emphasize complete
stillness.
```

**Prompt de movimiento:**
```
Extremely slow, almost imperceptible cinematic push toward the untouched shelf of sealed tape
boxes, nothing moves except a faint flicker of distant light under a far door, emphasizing
total stillness and suspended time, no faces revealed, no resolution implied
```

**Nota:** este clip es el "antes" del Video 16 (las cintas reciben luz) — mismo encuadre,
deliberadamente sin cambios, para que el contraste con el Video 16 se sienta más fuerte.

### VIDEO 9 — Evidencia, no música (8s) — Gap A, beat 5 de 9

Para: *"Cada demo, cada voz grabada de Chris Cornell existía solo como evidencia dentro de una
carpeta legal. No como música. Como prueba."*

**Imagen inicial:**
```
Extreme close-up on one single analog tape box, a small printed legal exhibit tag tied to it
reading "EXHIBIT — CASE NO." with the rest of the number out of focus, dust on the box, dim
single-source light, cinematic documentary photography, no visible faces, legible clean print
on the tag only
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: the camera moves closer to the legal exhibit tag, which now
fills most of the frame, while the handwritten song title on the box behind it falls out of
focus and becomes secondary.
```

**Prompt de movimiento:**
```
Slow deliberate cinematic push ending on the legal exhibit tag in sharp focus while the
handwritten song title on the box behind it falls out of focus, visually prioritizing
"evidence" over "music," somber tone, no faces revealed
```

### VIDEO 10 — Compañeros de banda, técnicamente (8s) — Gap A, beat 6 de 9

Para: *"Kim Thayil, Matt Cameron y Ben Shepherd seguían siendo, técnicamente, sus compañeros de
banda desde hacía más de tres décadas."*

**Imagen inicial:**
```
Wide shot of an empty rehearsal room, three separate instrument cases (guitar, bass, drum
hardware case) closed and standing apart from each other against different walls, thin dust on
each, warm dim light from a single window, cinematic documentary photography, no visible faces
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: the camera is slightly closer, the three cases remain closed
and untouched, but a thin ray of light now crosses the empty space between them, emphasizing
the physical distance between the three.
```

**Prompt de movimiento:**
```
Slow cinematic pan across the empty rehearsal room connecting the three separate closed
instrument cases in one continuous motion, emphasizing the distance between them despite being
in the same room, quiet and melancholic tone, no faces revealed
```

### VIDEO 11 — Hablar solo a través de abogados (8s) — Gap A, beat 7 de 9

Para: *"Durante esos años, la única forma en que podían hablar de las canciones que habían
escrito juntos era a través de sus abogados."*

**Imagen inicial:**
```
Two separate wooden desks in dim law offices, shown side by side in frame, each with a closed
envelope addressed only with a case number, a rotary telephone on each desk untouched, warm
lamp light on each side, cinematic documentary photography, no visible faces, no legible text
beyond case numbers
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: a blurred hand on the left side places a sealed envelope
into an outbox tray; the telephone remains untouched. On the right side, an identical envelope
now appears arriving into its own inbox tray, implying indirect communication.
```

**Prompt de movimiento:**
```
Slow cinematic split-focus movement between two separated desks as a sealed envelope moves from
one outbox to the other's inbox, telephones on both sides remaining untouched throughout,
emphasizing indirect, formal-only communication, no faces revealed
```

### VIDEO 12 — Dos demandas, una retirada (8s) — Gap A, beat 8 de 9

Para: *"Para ese punto, llevaban dos demandas activas por separado, una contrademanda
retirada, y veintiún millones de dólares rechazados dos veces."*

**Imagen inicial:**
```
A growing stack of thick legal case folders on a desk, three visible folders each labeled only
with a case number and year, one folder set slightly apart with a "WITHDRAWN" stamp on its
cover, dim warm lamp light, cinematic documentary photography, no visible faces, legible clean
print only on the stamp
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: a fourth folder is added to the stack. The folder with the
"WITHDRAWN" stamp remains visibly separate from the rest, and the stack now looks noticeably
taller and heavier.
```

**Prompt de movimiento:**
```
Slow cinematic overhead push as folders accumulate one by one onto the desk, the "WITHDRAWN"
folder remaining visibly separate from the growing stack, emphasizing accumulation without
resolution, somber tone, no faces revealed
```

### VIDEO 13 — Ocho años, llegó el final (8s) — Gap A, beat 9 de 9

Para: *"Ocho años desde su muerte. Y entonces, después de todo eso, llegó el final."*

**Imagen inicial:**
```
Close-up of a stack of thick legal folders on a wooden desk, still loose and untied, a red
ribbon lying beside them, warm desk lamp light, dust visible in the beam, cinematic documentary
photography, no visible faces, no text anywhere in frame
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: the red ribbon is now tied firmly in a bow around the stack
of folders, and the desk lamp light dims softly, as if closing for the last time.
```

**Prompt de movimiento:**
```
Slow cinematic push as an out-of-focus blurred hand gathers the loose stack of legal folders
and ties them shut with a red ribbon in one final motion, the desk lamp dimming gently at the
end as if closing this chapter for good, quiet and conclusive tone, no faces revealed, no text
anywhere in frame
```

**Nota:** congelar el último frame de este clip 1 segundo más antes de cortar al anuncio de
Instagram (13:12) — completa el Gap A (73s) exacto.

### VIDEO 14 — El acuerdo silencioso (8s) — Gap B, beat 1 de 4

**Imagen inicial:**
```
Close-up of a single sheet of paper on a wooden desk, mostly blank except for a signature line
at the bottom, an out-of-focus blurred hand holding a pen just above it, warm single-source
lamp light, deep shadows around the edges of frame, cinematic documentary photography, no
visible faces, no legible text on the page except a small "CONFIDENTIAL" stamp in the corner
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: the signature is now complete at the bottom of the page, the
blurred hand sets the pen down beside it, and the page is slowly closing into a plain folder
with no label.
```

**Prompt de movimiento:**
```
Slow cinematic close-up push as the blurred hand signs the page in silence, then sets the pen
down and closes the folder, no other movement in frame, warm still lamp light throughout,
quiet and unceremonious tone — no triumphant music implied, just quiet finality, no faces
revealed
```

### VIDEO 15 — Cuatro años guardados en un cajón (8s) — Gap B, beat 2 de 4

Para: *"Después de cuatro años de acusaciones públicas — de cifras filtradas, de cartas de
abogados, de declaraciones a la prensa — el final llegó sin una sola palabra sobre quién tenía
razón."*

**Imagen inicial:**
```
Close-up of a wooden desk drawer half-open, containing a messy pile of old newspaper clippings
and printed press articles, headlines blurred and illegible, a pair of reading glasses resting
on top, warm dim lamp light from off-frame, dust visible in the light, cinematic documentary
photography, no visible faces, no legible text on the clippings
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: a blurred hand slowly pushes the drawer closed over the pile
of clippings, the light narrowing to a thin sliver as the drawer shuts.
```

**Prompt de movimiento:**
```
Slow cinematic push toward the open drawer full of blurred press clippings, then a blurred hand
enters frame and slowly pushes the drawer shut, light narrowing to nothing as it closes, quiet
and unceremonious tone, no faces revealed, no triumphant resolution implied — just closure
```

### VIDEO 16 — Las cintas reciben luz de nuevo (8s) — Gap B, beat 3 de 4

**Imagen inicial:**
```
The same shelf of seven labeled analog tape boxes from before (Road Less Traveled, Orphans, At
Orphan's Door, Cancer, Ahead of the Dog, Merrmas, Stone Age Mind), sitting undisturbed in
darkness, thick dust settled on all of them, a single thin beam of light just beginning to
creep across the shelf from off-frame, cinematic documentary photography, no visible faces,
legible clean handwriting on labels
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: the light beam now fully illuminates all seven tape boxes,
the dust visibly disturbed on two of them as if just touched, and a blurred hand reaches toward
one of the boxes.
```

**Prompt de movimiento:**
```
Slow cinematic reveal as a beam of light gradually sweeps across the shelf of seven sealed tape
boxes, ending as a blurred hand reaches toward one of them and disturbs the dust for the first
time in years, shallow depth of field, tone shifts from stillness to quiet hope, no faces
revealed
```

### VIDEO 17 — Hacia la consola (8s) — Gap B, beat 4 de 4, transición a Terry Date

**Imagen inicial:**
```
Close-up on a hand-labeled analog tape box being lifted off the shelf by an out-of-focus
blurred figure, warm amber light, dust particles floating in the light beam, cinematic
documentary photography, no visible faces, legible clean handwriting on the box label
```

**Imagen final (edición sobre la imagen inicial, no generar desde cero):**
```
Using this same image as the base: the same blurred figure is now shown in a wide shot carrying
the tape box toward a vintage mixing console in the distance, studio lights warming up in the
background, with a second blurred figure already seated at the console waiting.
```

**Prompt de movimiento:**
```
Slow cinematic tracking shot following a blurred silhouette carrying a labeled tape box across
a dim studio floor toward a mixing console where another blurred figure waits, warm light
building gradually, hopeful and purposeful tone, ending just before reaching the console (cuts
to the real photo of Terry Date at the board), no faces revealed
```

**Nota:** Video 17 está diseñado para cortar justo antes de la foto real de Terry Date que ya
tienes colocada a los 13:56 — la idea es que el movimiento de cámara "entregue" la escena a esa
foto real de forma fluida, no que la reemplace.

### Resumen de duración final (corregido)

| Clip | Duración generada | Uso en timeline |
|---|---|---|
| Video 5 | 8s | Gap A, beat 1 |
| Video 6 | 8s | Gap A, beat 2 |
| Video 7 | 8s | Gap A, beat 3 |
| Video 8 | 8s | Gap A, beat 4 |
| Video 9 | 8s | Gap A, beat 5 |
| Video 10 | 8s | Gap A, beat 6 |
| Video 11 | 8s | Gap A, beat 7 |
| Video 12 | 8s | Gap A, beat 8 |
| Video 13 | 8s + freeze 1s | Gap A, beat 9 (73s completo) |
| Video 14 | 8s | Gap B, beat 1 |
| Video 15 | 8s | Gap B, beat 2 |
| Video 16 | 8s | Gap B, beat 3 |
| Video 17 | 8s | Gap B, beat 4 (32s + ~2s de transiciones = 34s) |

Total: 73s (Gap A) + 34s (Gap B) = **107s exactos**, cerrando el hueco completo de 11:59 a 14:00.
13 clips nuevos + los 4 ya existentes (Video 1-4) = 17 clips de IA en todo el video.

