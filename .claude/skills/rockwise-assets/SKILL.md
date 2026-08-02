---
name: rockwise-assets
description: >
  Skill 3 de 6 del pipeline Rockwise Tales. Mapea los assets visuales por
  bloque narrativo del script. Busca footage real en YouTube, verifica con
  5 puntos, y marca los bloques sin footage para generacion AI en Skill 4.

license: MIT

metadata:
  raise.work_cycle: production
  raise.frequency: on-demand
  raise.fase: assets
  raise.prerequisites: "rockwise-script"
  raise.next: "rockwise-visuals"
  raise.gate: ""
  raise.adaptable: "true"
  raise.version: "1.3.0"
---

# Rockwise Assets

## Purpose

Encontrar footage real para cada bloque narrativo del script. Solo recurrir a IA visual (Skill 4) cuando no existe material de archivo.

**Principio operativo:** este skill no busca "material bonito"; busca evidencia visual que encaje con una frase especifica del guion. Cada asset debe tener razon narrativa, fuente, timestamp, calidad tecnica, descarte documentado y nivel de confianza. El objetivo es reducir retrabajo en edicion.

## Mastery Levels (ShuHaRi)

- **Shu**: Buscar en YouTube, verificar que el video existe y tiene personas reales
- **Ha**: Identificar el minuto exacto relevante, rechazar compilaciones de creadores
- **Ri**: Construir contraste visual entre bloques sin perder autoridad documental

## Context

**When to use:** Despues de que el script LONG esta aprobado.

**When to skip:** No se salta. Sin assets el Skill 4 no sabe que generar con IA.

**Inputs:** Script LONG con bloques narrativos identificados y voz real/transcripcion por partes cuando el usuario ya grabo.

> APRENDIZAJE CRITICO (James Hetfield, 2026-08-02): si ya existe voz grabada, NO buscar visuales solo desde el texto del script. Primero escuchar la voz real, medir ritmo, pausas, respiraciones, enfasis y duracion por bloque. El sourcing visual debe seguir el audio que se editara en CapCut, no una lectura teorica del parrafo. En James se perdio tiempo porque algunos bloques visuales se armaron por tema, pero no cubrian la duracion ni la energia real de la narracion.

## Steps

### Step 0: Gate audio-first si ya existe voz grabada

Antes de buscar videos o imagenes, verificar si el usuario ya grabo la voz.

Si existe voz grabada:

1. Escuchar el audio completo o la parte correspondiente.
2. Medir duracion real por bloque, no estimarla solo por palabras.
3. Detectar pausas largas destinadas a inserts de entrevista.
4. Marcar enfasis de voz: tension, vulnerabilidad, dato oculto, cambio de energia, remate.
5. Convertir la narracion real en beats de edicion con tiempos aproximados.
6. Solo despues buscar visuales para esos beats.

Si no existe voz grabada:

- usar el script como referencia provisional;
- marcar el asset plan como `PRE-VOICE`;
- advertir que debe recalibrarse despues de grabar.

**Verification:** El asset log indica `audio_basis: REAL_VOICE | SCRIPT_ESTIMATE` y, si hay voz real, cada bloque tiene duracion escuchada.

### Step 1: Listar bloques narrativos que necesitan visual

Recorrer el script y marcar cada momento que necesita imagen o video. Un bloque = una escena o periodo de tiempo en la historia.

**Verification:** Lista completa de bloques con descripcion de que debe mostrarse.

### Step 1bis: Dividir por beats exactos de voz y guion

Antes de buscar, convertir cada bloque en beats visuales de 5-12 segundos:

- Frase exacta del guion o rango de voz.
- Duracion real escuchada si existe voz grabada.
- Pausas donde entran entrevistas, archivo o respiracion visual.
- Funcion visual: `prueba directa`, `contexto historico`, `album/era`, `conflicto`, `emocion`, `transicion`, `respiracion`.
- Necesidad real: entrevista, documental, album, performance, foto, still o recreacion.
- Tension que debe sostener: pregunta, dato oculto, morbo verificable, conflicto, vulnerabilidad.

No aprobar un asset si solo "se ve bien" pero no responde a una frase/beat concreto o si se queda corto/largo frente al ritmo real de la voz.

**Verification:** Cada beat tiene una necesidad visual concreta y una duracion objetivo antes de abrir YouTube/Google.

### Step 2: Buscar footage primario en YouTube y fuentes oficiales

Para cada bloque, buscar:

- Entrevistas originales de la epoca
- Performances en vivo
- Documentales oficiales
- Making-of / behind the scenes
- Videos musicales de la epoca
- Fotos historicas, press, albumes y stills del propio material

**Herramienta para timestamps:** YouTube tiene transcripcion automatica. Usarla para encontrar el minuto exacto sin ver todo el video completo, pero verificar visualmente el timestamp antes de aprobar.

**Verification:** Link encontrado y verificado visualmente.

### Step 2bis: Busqueda por capas, no por una sola query

Para cada beat, buscar en este orden:

1. Fuente primaria donde el artista lo dice o lo muestra.
2. Documental/making-of oficial o de epoca.
3. Entrevista de la misma era.
4. Performance real de la misma era.
5. Album/press/foto historica de la misma era.
6. Still extraido de los videos anteriores.
7. Recreacion representativa sin personas reconocibles.
8. IA visual solo si las capas 1-7 fallan o son inviables.

Usar multiples queries:

- `[artista] [tema] interview`
- `[artista] [album] making of`
- `[banda] [ano] interview`
- `[album] documentary`
- `[cancion] meaning interview`
- `[evento/conflicto] documentary clip`
- `site:youtube.com [terminos]`
- `site:[sitio oficial] [terminos]`

**Verification:** Registrar al menos 3 busquedas o fuentes consideradas para beats importantes, incluyendo descartes si no sirven.

### Step 3: Aplicar criterios de rechazo

Rechazar automaticamente cualquier video cuyo titulo contenga:

- "reaction" / "reaccion"
- "breakdown" / "explained" / "explicado"
- "disaster" / "worst" / "fails"
- emojis en el titulo
- signos de exclamacion
- nombres de creadores como protagonistas del titulo

Estos filtros no aplican a fuentes oficiales, entrevistas primarias, archivos historicos o material que se use solo como referencia interna, pero si debe quedar registrado el motivo.

**Verification:** Ningun asset rechazado aparece en la lista final sin justificacion.

### Step 4: Verificar con 5 puntos

Para cada asset que pasa el filtro de titulo:

1. **Origen**: programa, evento, canal o procedencia.
2. **Ano/era**: confirmado con fuente o marcado como aproximado/contexto.
3. **Naturaleza**: entrevista, documental, performance, clip oficial, fan shot, foto, still, recreacion.
4. **Staged o real**: actuado vs. footage genuino.
5. **Coherencia**: el contexto del clip corresponde al bloque del script.

**Verification:** Los 5 puntos completados por escrito para cada asset.

### Step 4a: Verificar encaje narrativo antes de descargar

Cada asset candidato debe pasar esta prueba:

1. **Frase exacta:** que linea del script cubre.
2. **Epoca:** corresponde al ano/album/evento del relato o se marca como contexto.
3. **Emocion:** sostiene la intencion de la voz: vulnerabilidad, tension, control, perdida, escala, etc.
4. **Autoridad:** aporta prueba o contexto real, no solo decoracion.
5. **Calidad TV:** aguanta 16:9 en pantalla grande o necesita composicion.
6. **Riesgo:** video/audio oficial, entrevista, fan shot, foto fija, still, IA.
7. **Plan B:** que se usara si falla por calidad o derechos.

Si falla en frase exacta o autoridad, descartarlo aunque sea visualmente atractivo.

**Verification:** Asset log completado con `decision: APROBADO`, `CANDIDATE` o `RECHAZADO`.

### Step 4bis: Verificacion tecnica post-descarga (OBLIGATORIO)

Dos bugs reales encontrados en produccion:

1. **Audio cortado antes que el video**: al cortar un segmento directo de YouTube, a veces el audio termina segundos antes que el video, justo donde pasa lo importante. Verificar SIEMPRE con `ffprobe` que la duracion de audio y video coincidan despues de cortar. Si no coinciden: descargar el video completo o un tramo mas largo y cortar localmente con ffmpeg.
2. **Contenido no coincide con el titulo**: extraer un frame del timestamp EXACTO usado antes de dar un clip por bueno.

**Verification:** Cada clip final tiene audio/video con misma duracion, y un frame verificado del segmento exacto usado.

### Step 4ter: Fotos vs. video - calibracion de riesgo real

Content ID de YouTube detecta huellas de AUDIO y VIDEO. El riesgo real de bloqueo esta en clips de video/audio, no en fotos fijas.

- **Para fotos:** buscar libremente en Google Images, fotos de prensa, archivos de bandas, Wikimedia, etc. No restringirse solo a licencias dominio publico o Creative Commons salvo que el proyecto lo requiera explicitamente. Evitar imagenes marcadas explicitamente como "fair use" de Wikipedia porque esa licencia es solo para uso dentro de Wikipedia.
- **Para video/audio:** mantener filtro estricto. Preferir fragmentos breves, transformativos, con voz en off y sin audio original cuando convenga.

### Step 5: Marcar bloques sin footage

Si despues de buscar no existe material real, marcar como `[REQUIERE AI VISUAL]` para Skill 4.

No marcar `[REQUIERE AI VISUAL]` por cansancio, prisa o busqueda superficial. Debe existir un descarte minimo:

- 3-5 queries probadas;
- fuentes reales revisadas;
- razon de descarte documentada;
- alternativa representativa considerada.

**Verification:** El bloque sin footage tiene mini informe de busqueda fallida.

## Output

```text
BLOQUE [N] - [descripcion del momento]
Asset: [titulo del video/foto/still]
Link o ruta: [URL/ruta]
Minuto util: [si aplica]
Verificado: [5 puntos completados]
Encaje: [frase exacta + funcion visual + nivel de confianza]
Decision: [APROBADO / CANDIDATE / RECHAZADO]

BLOQUE [N+1] - [descripcion del momento]
[REQUIERE AI VISUAL] - no existe footage real disponible
Busqueda fallida: [queries/fuentes descartadas + motivo]
```

## Asset log obligatorio

Cada proyecto LONG debe mantener un archivo `asset_log_real_archive_first.md` o `.csv` con estas columnas:

| Campo | Descripcion |
| --- | --- |
| bloque | Numero/nombre del bloque |
| beat_time | Rango estimado de voz o montaje |
| audio_basis | REAL_VOICE/SCRIPT_ESTIMATE |
| audio_duration | Duracion escuchada del beat o bloque |
| audio_emphasis | tension/vulnerabilidad/dato/remate/respiracion |
| script_quote | Frase exacta que cubre |
| visual_need | entrevista/documental/album/performance/foto/still/recreacion/IA |
| candidate_title | Titulo o descripcion del asset |
| source_url | Link o ruta local |
| source_type | REAL_CLIP/REAL_STILL/REAL_PHOTO/ALBUM_REF/RECREACION/IA_ATMOSFERA |
| source_year | Ano o era |
| useful_timestamp | Minuto util o rango |
| technical_quality | resolucion, horizontal/vertical, audio ok |
| narrative_fit | por que encaja |
| risk | bajo/medio/alto |
| decision | APROBADO/CANDIDATE/RECHAZADO |
| rejection_reason | si aplica |
| backup_option | plan B |

Sin asset log, no cerrar el skill.

## Densidad visual - evitar que se sienta lento

Para un video de 15-20+ minutos, un solo clip por bloque narrativo grande suele sentirse estatico. Dato real de produccion: un documental Rockwise de ~20 min termino usando alrededor de 135 imagenes/clips. Eso equivale a ~6-7 assets por minuto de video, o un corte visual nuevo cada ~9 segundos en promedio.

**Implicacion practica:** al hacer el Step 1, calcular duracion total esperada del guion y multiplicar por ~6-7 assets/minuto para un numero de referencia realista.

Si ya existe voz grabada, la densidad se calcula sobre la duracion real del audio, no sobre palabras del script. Un bloque puede necesitar mas assets si el usuario narra lento, deja pausas para inserts o subraya emocionalmente una frase.

**Presupuesto de tiempo real:** buscar/verificar manualmente esa cantidad de assets puede tomar 8-12 horas en un video LONG. Avisar esto por adelantado evita que el sourcing se sienta como un cuello de botella inesperado.

## Quality Checklist

- [ ] Todos los bloques del script tienen asset o marcador AI
- [ ] Si existe voz grabada, se escucho antes de buscar assets
- [ ] Cada bloque tiene `audio_basis` y duracion real o estimada
- [ ] Cada asset cubre una frase/beat exacto del guion
- [ ] Cada asset cubre el ritmo real de la narracion, no solo el tema del parrafo
- [ ] Asset log completado con aprobados, candidatos y rechazados
- [ ] Para beats importantes se probaron varias queries/fuentes antes de rendirse
- [ ] Criterios de rechazo aplicados
- [ ] 5 puntos verificados para cada asset
- [ ] Encaje narrativo verificado: frase, epoca, emocion, autoridad, calidad, riesgo
- [ ] Minutos utiles identificados donde aplica
- [ ] Audio y video verificados con misma duracion con `ffprobe` en cada clip final
- [ ] Frame verificado del timestamp exacto usado, no solo el titulo del video
- [ ] Densidad de assets revisada: bloques largos tienen mas de un corte visual
- [ ] Menos de 40% de la secuencia principal depende de IA, salvo imposibilidad documentada
- [ ] Journal add ejecutado antes de pasar al Skill 4

## Jerarquia de assets

1. Footage original de la epoca: entrevistas, conciertos, behind the scenes.
2. Fuente primaria posterior donde el artista explica el hecho.
3. Documentales, making-of o trailers oficiales.
4. Albumes, press photos, fotos historicas y Wikimedia.
5. Stills extraidos del propio material real.
6. Recreacion representativa sin personas reconocibles.
7. AI visual generado (Skill 4) solo si no existe footage real viable o como respiracion visual menor.

## References

- Previous: `/rockwise-script`
- Next: `/rockwise-visuals`
