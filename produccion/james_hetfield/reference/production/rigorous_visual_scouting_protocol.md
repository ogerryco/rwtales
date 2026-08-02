# Protocolo riguroso de scouting visual

Fecha: 2026-08-01

## Objetivo

Reducir retrabajo en la fase mas costosa del documental: encontrar contenido real que encaje con el script, la voz, la epoca y la emocion. El objetivo no es llenar carpetas; es construir una secuencia que parezca investigada, confiable y premium.

## Principio

Cada asset debe justificar su lugar con una frase:

> "Este asset va aqui porque cubre esta frase exacta, de esta epoca, con esta emocion, y aporta esta autoridad visual."

Si no puede responder eso, no entra.

## Fase 1 - Beat sheet desde voz real

Antes de buscar visuales:

1. Escuchar la voz del bloque.
2. Marcar beats de 5-12 segundos.
3. Escribir la frase exacta de cada beat.
4. Definir funcion visual:
   - prueba directa;
   - contexto historico;
   - album/era;
   - conflicto;
   - vulnerabilidad;
   - tension/misterio;
   - transicion;
   - respiracion.
5. Definir necesidad visual: entrevista, documental, album, performance, foto, still, recreacion o IA.

Gate: no se busca nada hasta tener beat sheet.

## Fase 2 - Busqueda real por capas

Buscar en este orden:

1. Artista/persona diciendolo.
2. Documental o making-of.
3. Entrevista de la misma era.
4. Performance real de la misma era.
5. Album, press, foto historica o archivo publico.
6. Still del material real.
7. Recreacion sobria sin personas reconocibles.
8. IA como ultimo recurso.

Gate: si una capa superior existe y sirve, no saltar a IA.

## Fase 3 - Asset log

Registrar cada candidato, incluido lo rechazado. Campos obligatorios:

- bloque;
- beat_time;
- script_quote;
- visual_need;
- candidate_title;
- source_url_or_path;
- source_type;
- source_year;
- useful_timestamp;
- technical_quality;
- narrative_fit;
- risk;
- decision;
- rejection_reason;
- backup_option.

Gate: no se descarga ni se corta en lote sin asset log minimo.

## Fase 4 - Verificacion narrativa

Cada asset debe pasar:

1. Frase exacta.
2. Epoca correcta o contexto declarado.
3. Emocion correcta contra la voz.
4. Autoridad visual.
5. Calidad TV.
6. Riesgo de uso.
7. Plan B.

Gate: si falla frase exacta o autoridad, se rechaza aunque sea atractivo.

## Fase 5 - Verificacion tecnica

Para video:

- verificar resolucion;
- verificar duracion audio/video con `ffprobe`;
- extraer frame del timestamp exacto;
- confirmar que el contenido del timestamp coincide con el guion;
- si es vertical o baja calidad, decidir composicion antes de aprobar.

Para imagen:

- verificar dimensiones;
- decidir si va full screen o en composicion;
- evitar estirar imagenes historicas pequenas;
- etiquetar origen.

Gate: nada entra al pack CapCut sin revisar calidad.

## Fase 6 - Ensamble CapCut

Solo despues de aprobar assets:

1. Crear carpeta `00_CAPCUT_SECUENCIA_COMPLETA`.
2. Numerar por orden de montaje.
3. Mezclar fotos/videos en una sola secuencia.
4. Incluir README con:
   - rango de voz;
   - frase por asset;
   - duracion sugerida;
   - source_type;
   - notas de riesgo/uso.

Gate: el pack debe poder montarse sin adivinar.

## Fase 7 - Revision de mezcla real/IA

Antes de cerrar:

- calcular porcentaje de assets IA;
- si supera 40%, justificar imposibilidad documental;
- revisar si falta album/era/foto real;
- revisar repeticion visual contra bloques previos;
- validar que no hay banda/personajes genericos cuando deberian ser reconocibles.

Gate: pack no cerrado si parece slideshow generico.

## Regla de oro

La IA no es un atajo para terminar rapido. Es una herramienta para:

- huecos imposibles;
- recreaciones honestas;
- transiciones atmosfericas;
- respiracion visual.

El alma documental debe venir de archivo real.
