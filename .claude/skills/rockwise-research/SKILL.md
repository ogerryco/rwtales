---
name: rockwise-research
description: >
  Skill 1 de 6 del pipeline Rockwise Tales. Investiga la historia, identifica
  el patrón narrativo, verifica cada hecho con mínimo 3 fuentes independientes
  reales, y detecta los gaps que la audiencia no conoce. Produce el brief
  completo para el script. Obliga a formular hipótesis, procedencia, sesgo,
  nivel de certeza y diferencia entre hecho, versión, interpretación y mito.

license: MIT

metadata:
  raise.work_cycle: production
  raise.frequency: on-demand
  raise.fase: research
  raise.prerequisites: "rockwise-demand-scout"
  raise.next: "rockwise-script"
  raise.gate: ""
  raise.adaptable: "true"
  raise.version: "1.6.0"
---

# Rockwise Research

## Purpose

Investigar la historia del video, construir el timeline verificado, identificar los gaps narrativos poco conocidos, y producir el brief completo que alimenta el script.

**Canal:** Rockwise Tales (@rockwisetales) — 70K+ seguidores, 1M+ likes, NO FACE (voz en off únicamente)

## Mastery Levels (ShuHaRi)

- **Shu**: Buscar el hecho principal, verificar año y fuente, listar lo que pasó
- **Ha**: Identificar 2-3 gaps con fuente primaria, reconocer el patrón emocional
- **Ri**: Elegir el gap que maximiza tensión narrativa y tiene material visual disponible

## Context

**When to use:** Al iniciar un nuevo video. Siempre antes de escribir una sola línea de script.

**When to skip:** Si el Skill 1 ya está completo y documentado en el journal de sesión.

**Inputs:**
- Historia o artista propuesto por el usuario
- Demand Scout con `Idea Class: SINGLE | DOUBLE | HOME RUN` cuando el formato sea YouTube LONG
- Patrón emocional identificado (ej: "Genio Incomprendido", "La Traición", "El Regreso")

## Steps

### Step 0: Scouting con datos reales — ANTES de elegir el tema/patrón (OBLIGATORIO)

Antes de hacer research profundo, ejecutar `rockwise-demand-scout` o documentar un Demand Scout equivalente. Este paso decide si el tema merece investigación, cuál es el ángulo ganador y qué brecha concreta existe frente a la competencia.

> ⚠️ APRENDIZAJE REAL (Cornell/Soundgarden): lo que realmente hizo funcionar ese video no fue solo un buen patrón narrativo — fue meterse a fondo con datos reales ANTES de decidir de qué iba a tratar. Elegir el tema/ángulo sin este paso es pensamiento mágico, no proceso.

Tres búsquedas obligatorias, con la API de YouTube (o búsqueda directa) y web search — no opinión ni intuición:

1. **Scouting de competencia en YouTube:** buscar ampliamente qué videos YA existen sobre este artista/tema en YouTube. ¿Qué tan saturado está? ¿Qué ángulos ya cubrieron otros canales? ¿Qué le falta a la cobertura existente — cuál es el gap real que tu video puede llenar? No elegir un ángulo sin saber qué ya se contó mil veces.

2. **Scouting de relevancia actual ("tema candente"):** buscar en Google/prensa si hay algo pasando AHORA MISMO con este artista/tema — no solo interés histórico. El caso Cornell: encontrar que la banda estaba en ese momento terminando de grabar las 7 canciones inéditas le dio urgencia real al video, algo que nadie sabía y que estaba pasando en tiempo presente. Un tema histórico sin gancho de actualidad compite peor que uno con desarrollo reciente real.

3. **Análisis continuo del propio canal:** revisar con YouTube Analytics/API los videos anteriores del canal — cuáles se viralizaron y cuáles no — para identificar qué tipo de tema, artista o ángulo predice éxito real en ESTE canal específico, no en teoría general. Esto no es un análisis de una sola vez: se revisa cada vez que se elige un tema nuevo, porque el patrón de qué funciona puede cambiar con el tiempo.

**Verification:** Demand Scout adjunto o equivalente con score, competencia, brecha, actualidad y fit del canal. Las 3 búsquedas documentadas con hallazgos concretos (no "ya lo revisé" sin evidencia) antes de pasar al Step 1.



### Step 0.1: Análisis de competencia real por guion/transcript (OBLIGATORIO para YouTube LONG)

El scouting de competencia no termina con títulos, thumbnails y número de vistas. Para YouTube LONG, identificar cuáles videos son competencia real y analizar qué dicen por dentro.

Proceso obligatorio:

1. **Separar competencia real de ruido**
   - Competencia real: documentales, ensayos, historias de canción, biografías o videos largos/cortos con el mismo conflicto central, promesa emocional o búsqueda del espectador.
   - Ruido: listicles superficiales, transformaciones por edad, shorts reusados, curiosidades aisladas, lyric videos, reacciones sin investigación o videos que solo comparten palabra clave pero no intención narrativa.

2. **Extraer o reconstruir el script**
   - Si hay transcript disponible, guardarlo y analizarlo.
   - Si no hay transcript, usar capítulos, descripción, comentarios fijados, timestamps visibles, lectura manual del video o resumen por segmentos.
   - Si no se pudo acceder al guion/transcript, marcarlo como `NO ANALIZADO A FONDO` y no sacar conclusiones fuertes sobre su contenido.

3. **Analizar cada competidor real con esta tabla**

| Video | Tipo | Tesis/promesa | Estructura | Claims sensibles | Fuentes visibles | Fortalezas | Debilidades | Hueco para Rockwise |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

4. **Detectar saturación por ángulo**
   - ¿Qué parte de la historia ya contaron todos?
   - ¿Qué escena usan como gancho?
   - ¿Qué mito repiten?
   - ¿Qué pregunta emocional dejan sin responder?
   - ¿Qué claim delicado manejan mal o sin fuente?
   - ¿Qué parte de la transformación musical, humana o cultural nadie articula?

5. **Convertir huecos en oportunidad editorial**
   - `Oportunidad de guion`: qué enfoque narrativo permitirá que el video sea distinto.
   - `Oportunidad de título`: qué promesa puede decirse sin repetir el mismo packaging de la competencia.
   - `Oportunidad de miniatura`: qué contraste visual/emocional falta en la competencia y puede hacer que el espectador entienda el valor en 1 segundo.

Formato de salida obligatorio:

```
COMPETENCIA REAL:
- [video] - por qué compite realmente

RUIDO / NO COMPITE:
- [video] - por qué no define el estándar del tema

SATURACIÓN:
- Lo que ya contaron todos:
- Lo que casi nadie explicó:
- Mitos o claims peligrosos detectados:

OPORTUNIDAD ROCKWISE:
- Guion:
- Título:
- Miniatura:
```

**Verification:** Para cada competidor marcado como real debe existir transcript, resumen por segmentos o justificación explícita de por qué no pudo analizarse. El brief no puede pasar a script si la oportunidad editorial solo se basa en metadata externa.

**Idea Class obligatorio para YouTube LONG:** si el Demand Scout clasifica la idea como `HOME RUN`, el research debe buscar una escena-prueba fuerte para los primeros 5-15 segundos, 2-3 rutas de promesa editorial y suficiente material para micro-intrigas cada 1-2 minutos. Si la idea es `SINGLE` o `DOUBLE`, mantener rigor factual pero ajustar el alcance de produccion a la clase; no sobredimensionar una idea que no tiene amplitud suficiente.

### Step 1: Identificar el patrón narrativo

Definir el patrón emocional central del video. Ejemplos del canal:
- "Genio Incomprendido y la Fragilidad" (Layne Staley)
- "La Renuncia y el Respeto entre Gigantes" (Frusciante)

Formato de salida:
```
PATRÓN: [nombre]
PREMISA: [1 oración que resume la historia]
```

**Verification:** El patrón tiene nombre y premisa en 1 línea.

### Step 2: Formular hipótesis y mapa epistemológico (OBLIGATORIO)

Antes de construir el timeline final, declarar explícitamente qué hipótesis está investigando el video y qué tipo de evidencia podría confirmarla, debilitarla o descartarla.

Una hipótesis no es un dato. Es una propuesta narrativa que debe sobrevivir a la evidencia.

Ejemplos:

- "La entrada de Emily no fue solo un reemplazo vocal, sino una relectura pública del duelo de Linkin Park."
- "La caída de [artista] no se explica por un solo evento, sino por una cadena de decisiones industriales, personales y médicas."
- "Las canciones inéditas de Cornell importan no por morbo, sino porque cambian la lectura del cierre artístico de Soundgarden."

Para cada hipótesis, crear esta tabla:

| Hipótesis | Evidencia a favor | Evidencia en contra | Fuente primaria | Fuente secundaria | Sesgo probable | Certeza |
| --- | --- | --- | --- | --- | --- | --- |

Reglas:

- Si no hay evidencia en contra buscada activamente, la hipótesis todavía no está auditada.
- Si la hipótesis depende de una sola entrevista, marcarla como frágil aunque la entrevista sea buena.
- Si el artista lo dijo directamente, sigue existiendo sesgo posible: memoria, autoprotección, marketing, dolor, conflicto legal o retrospectiva.
- Si lo dijo un periodista, preguntar si cita material primario o si está interpretando.
- Si lo repiten varios medios pero todos parecen venir de la misma nota original, cuenta como una sola cadena de transmisión.

**Verification:** Al menos una hipótesis principal con evidencia a favor, evidencia en contra o ausencia explícita de contraevidencia, procedencia y sesgo antes de pasar al timeline.

### Step 3: Clasificar fuentes, procedencia y nivel de certeza (OBLIGATORIO)

Cada claim delicado debe clasificarse antes de entrar al script. No basta con tener un link.

Usar esta jerarquía:

1. **Fuente primaria fuerte:** entrevista en video/audio, comunicado oficial, liner notes, créditos, court docs, archivo de época, declaración directa verificable.
2. **Fuente primaria republicada:** transcripción, reedición o archivo de una entrevista original; usable si conserva contexto, fecha y atribución.
3. **Fuente secundaria fuerte:** medio confiable que entrevista, cita directamente o contrasta fuentes.
4. **Fuente secundaria débil:** artículo que resume sin links claros, notas de efeméride, listas, blogs.
5. **Fuente terciaria:** Wikipedia, wikis, fan pages, videos de otros creadores, posts no documentados.
6. **Mito/fandom:** afirmación repetida sin origen rastreable.

Para cada claim importante, crear esta tabla:

| Claim | Quién lo dijo | Fuente original | Fecha original | Medio consultado | Cadena | Sesgo | Usable como |
| --- | --- | --- | --- | --- | --- | --- | --- |

Valores para `Usable como`:

- `HECHO CONFIRMADO`: suficiente evidencia primaria o corroboración independiente real.
- `HECHO ATRIBUIDO`: usable solo con "según..." o "en entrevista con...".
- `VERSIÓN`: una persona o bando lo afirma, pero hay otras versiones o falta corroboración.
- `INTERPRETACIÓN`: lectura editorial permitida, nunca narrada como hecho.
- `DISPUTADO`: usar solo si la disputa es parte de la historia.
- `MITO / NO USAR`: no entra al script salvo para desmontarlo explícitamente.

Preguntas obligatorias por claim:

- ¿Quién lo dijo originalmente?
- ¿Desde cuándo existe esa afirmación?
- ¿El medio consultado vio la fuente primaria o está copiando a otro?
- ¿Hay una entrevista completa, o solo una frase recortada?
- ¿La traducción cambia el sentido?
- ¿Qué interés o sesgo podría tener quien lo dijo?
- ¿Qué diría un fan melómano para tumbar este dato?

**Verification:** Ningún claim de fecha, causa, crédito, salud mental, conflicto, muerte, entrada/salida de integrantes o atribución de canción entra al script sin clasificación de fuente, cadena y certeza.

### Step 4: Construir timeline verificado

Listar los hechos clave en orden cronológico. Cada hecho debe tener:
- Fecha (año como mínimo)
- Mínimo 3 fuentes independientes y reales que corroboren el mismo dato
  (ej. Wikipedia + un medio especializado como Louder/Ultimate Classic Rock/
  Rolling Stone + una entrevista o nota de prensa original). No cuenta como
  fuente independiente un sitio que claramente copia a otro (fan wikis que
  citan Wikipedia palabra por palabra no suman como fuente aparte).
- Si dos de las 3 fuentes se contradicen entre sí (fechas, nombres,
  integrantes), marcar el dato como [DISCREPANCIA] y no usarlo en el script
  hasta resolverlo con una fuente primaria (entrevista directa, sitio
  oficial de la banda, documento de la época).

> ⚠️ Esto es una barra más alta que "una fuente por hecho" — el canal tiene
> 80,000+ seguidores con público melómano que detecta errores factuales de
> inmediato. Un solo dato mal verificado puede dañar la credibilidad de todo
> el canal. No negociable, aplica incluso a datos que "todo el mundo sabe".

**Verification:** Ningún hecho con menos de 3 fuentes independientes reales.
Si no se alcanzan 3 fuentes = marcar como [NO VERIFICADO] y no usar en script.

### Step 5: Identificar los gaps narrativos

Buscar 2-3 momentos poco conocidos que enriquecen la historia. Un gap es:
- Algo que el público general no conoce
- Que tiene material de archivo disponible (video, foto, audio)
- Que agrega profundidad emocional al patrón

**Verification:** Cada gap tiene descripción + fuente + confirmación de que existe material visual.

### Step 6: Verificación de clips de archivo (5 puntos — OBLIGATORIO)

Antes de incluir cualquier clip en el brief, verificar los 5 puntos:

1. **Origen** — ¿De qué programa/evento proviene exactamente?
2. **Año** — ¿Confirmado con fuente? No usar "circa" sin advertirlo
3. **Naturaleza** — ¿Entrevista seria, documental, comedia, mockumentary?
4. **Staged o real** — ¿Es actuado o footage real?
5. **Coherencia narrativa** — ¿El contexto del clip corresponde a lo que el script dirá?

> ⚠️ ERROR CRÍTICO DE REFERENCIA (aprendizaje canal): El video de apertura del Layne Staley/"Died" fue identificado como "MTV Headbangers Ball 1993". Era The Nona Tapes (1995), un mockumentary de comedia. Generó error de año Y de contexto en el script publicado (130K+ vistas). Los 5 puntos no son opcionales.

> ⚠️ SEGUNDO ERROR CRÍTICO (aprendizaje canal, Cornell/Soundgarden): título y descripción del video correctos NO garantizan que el timestamp/segmento específico usado corresponda. Dos casos reales: (1) un video correctamente titulado "Fell On Black Days Live" tenía 30 segundos de entrevista hablada ANTES de que empezara la canción — el segmento 0:00-0:15 elegido mostraba la entrevista, no a Cornell cantando; (2) un video titulado "Louder Than Live (1990)" mostraba la portada del VHS y logos de la disquera en sus primeros 20 segundos, no metraje de la banda tocando. Ambos se descubrieron extrayendo un frame real del segmento exacto — nunca asumir contenido por el título solo.

**Verification:** Los 5 puntos completados para cada clip propuesto. Para cada clip, extraer al menos un frame del timestamp EXACTO que se usará (no del video en general) y confirmar visualmente que corresponde — si hay diálogo/voz relevante, verificar también con una transcripción rápida del segmento.

## Output

| Item | Destino |
|------|---------|
| PATRÓN + PREMISA | Brief del video |
| HIPÓTESIS + MAPA EPISTEMOLÓGICO | Define qué se puede afirmar, atribuir o interpretar |
| ANÁLISIS DE COMPETENCIA POR SCRIPT | Define huecos reales para guion, título y miniatura |
| CLAIM LEDGER | Alimenta QA factual y evita errores melómanos |
| TIMELINE verificado | Alimenta el script |
| GAPS (2-3) con fuentes | Alimenta el script |
| CLIPS verificados (5 puntos) | Alimenta rockwise-assets |

## Quality Checklist

- [ ] Para YouTube LONG, `Idea Class` heredada del Demand Scout y alcance de research ajustado a esa clase
- [ ] Scouting de competencia en YouTube documentado (qué ya existe, qué gap llena el video)
- [ ] Competidores reales separados de ruido/listicles/reacciones superficiales
- [ ] Scripts/transcripts de competidores reales extraídos, resumidos por segmentos o marcados como no analizables
- [ ] Huecos de competencia traducidos en oportunidad de guion, título y miniatura
- [ ] Scouting de relevancia actual documentado (¿hay algo pasando ahora con este tema?)
- [ ] Análisis de videos propios (viralizados vs. fallidos) revisado antes de elegir el tema
- [ ] Patrón nombrado y premisa en 1 línea
- [ ] Hipótesis principal declarada con evidencia a favor, evidencia en contra, procedencia y sesgo
- [ ] Claims delicados clasificados como hecho confirmado, hecho atribuido, versión, interpretación, disputado o mito/no usar
- [ ] Cadena de transmisión revisada: fuente primaria vs redactor vs repetición de otro medio
- [ ] Timeline con fechas y fuentes
- [ ] 2-3 gaps identificados con material visual confirmado
- [ ] 5 puntos verificados para cada clip propuesto
- [ ] Journal add ejecutado antes de pasar al Skill 2

## References

- Previous: `/none`
- Next: `/rockwise-script`
