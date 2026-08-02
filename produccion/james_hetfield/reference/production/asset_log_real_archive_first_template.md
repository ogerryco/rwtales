# Asset log real archive first - template

Usar esta plantilla antes de armar carpetas CapCut. Cada fila debe cubrir un beat real de voz/script, no un asset suelto.

## Reglas

- No aprobar assets sin frase exacta.
- No marcar IA sin busqueda real documentada.
- Todo asset debe tener decision: `APROBADO`, `CANDIDATE` o `RECHAZADO`.
- Si una foto/video no aguanta TV, marcarlo y proponer composicion o plan B.
- Si aparece una banda/artista real, evitar recreaciones que puedan parecer evidencia historica.

## Tabla

| bloque | beat_time | script_quote | visual_need | candidate_title | source_url_or_path | source_type | source_year | useful_timestamp | technical_quality | narrative_fit | risk | decision | rejection_reason | backup_option |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BXX | 00:00-00:08 | "..." | entrevista/documental/album/performance/foto/still/recreacion/IA | ... | ... | REAL_CLIP/REAL_STILL/REAL_PHOTO/ALBUM_REF/RECREACION/IA_ATMOSFERA | ... | ... | ... | ... | bajo/medio/alto | APROBADO/CANDIDATE/RECHAZADO | ... | ... |

## Checklist por asset

- [ ] Frase exacta del guion identificada.
- [ ] Funcion visual clara: prueba/contexto/album/conflicto/emocion/transicion.
- [ ] Fuente real priorizada antes de IA.
- [ ] Ano/era verificada o marcada como contexto.
- [ ] Calidad tecnica revisada: resolucion, horizontal/vertical, audio si aplica.
- [ ] Encaje emocional revisado contra la voz.
- [ ] Riesgo de uso identificado.
- [ ] Plan B registrado.

## Taxonomia `source_type`

- `REAL_CLIP`: video real que puede entrar como clip.
- `REAL_STILL`: still extraido de video real.
- `REAL_PHOTO`: foto historica, prensa, Wikimedia, archivo publico.
- `ALBUM_REF`: portada, press de album, promo de era.
- `RECREACION`: imagen/video representativo no presentado como evidencia.
- `IA_ATMOSFERA`: imagen/video IA solo para respiracion o transicion.
- `CANDIDATE`: material que requiere aprobacion visual o legal antes de usar.

## Niveles de decision

- `APROBADO`: encaja con frase, epoca, emocion, autoridad y calidad.
- `CANDIDATE`: puede servir, pero tiene problema de calidad, riesgo o encaje parcial.
- `RECHAZADO`: no usar; registrar razon para no volver a perder tiempo.
