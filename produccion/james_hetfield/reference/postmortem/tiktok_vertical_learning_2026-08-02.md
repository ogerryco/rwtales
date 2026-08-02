# Aprendizaje minucioso - James Hetfield TikTok vertical

Fecha: 2026-08-02

Proyecto: Rockwise Tales / James Hetfield

Contexto: despues de publicar el documental largo de YouTube, se intento derivar una version vertical de 3-4 minutos para TikTok. El primer enfoque automatico no funciono editorialmente. Este documento guarda el aprendizaje operativo para evitar retrabajo en futuros videos.

## Decision principal

No conviene convertir un documental largo de YouTube a TikTok solo recortando fragmentos del render final.

Para TikTok, especialmente en videos de 3-4 minutos, el contenido necesita guion nativo de short:

- Frases mas cortas.
- Tension mas frecuente.
- Menos contexto acumulativo.
- Mas avance por revelaciones.
- Mas claridad oral.
- Un cold open audiovisual que pruebe la emocion antes de explicarla.

El video largo tiene densidad documental. El TikTok necesita respiracion de scroll: cada 10-20 segundos debe aparecer una razon para quedarse.

## Error detectado: render automatico desde video final

Se genero un borrador vertical automatico desde el documental final:

- Primer intento: fondo blur con video horizontal centrado.
- Segundo intento: crop vertical fullscreen por segmentos.

Problemas:

1. El fondo blur no respeta el lenguaje de TikTok de Rockwise Tales. En los mejores videos del canal, el video ocupa toda la pantalla.
2. El crop automatico no puede entender intencion dramatica. Puede centrar mal rostros, cortar expresiones o perder personajes.
3. Cortar segmentos del render largo produce continuidad rara: la voz original fue grabada para YouTube, no para TikTok.
4. La narracion larga mantiene subordinadas y explicaciones que en vertical se sienten lentas.
5. El archivo automatico no sustituyo la edicion de CapCut; solo sirvio como prueba de que el proceso debe ser editorial, no mecanico.

Regla nueva: si se deriva TikTok desde un documental largo, usar el render final solo como fuente visual/audio de referencia. No asumir que el render automatico sera publicable.

## Regla de formato vertical

Para TikTok Rockwise:

- El video debe llenar pantalla 9:16.
- Evitar blur background como salida final.
- Usar zoom/crop manual, cuidando que no se pierdan rostros, manos, instrumentos o gestos clave.
- El crop debe seguir al sujeto y a la emocion, no solo al centro geometrico.
- En entrevista vulnerable, priorizar ojos y expresion facial.
- En escenas de banda, priorizar gesto colectivo o personaje principal.

El usuario normalmente hace fit vertical acercando la imagen en CapCut. Ese metodo debe respetarse.

## Subtitulos

Regla de canal: siempre llevan subtitulos.

Pero para este caso se decidio no quemarlos con ffmpeg porque:

- Whisper tiny genero transcripcion muy mala.
- Los subtitulos malos destruyen autoridad.
- El usuario prefiere hacerlos en CapCut con su estilo.

Regla nueva:

- Si se automatizan subtitulos, usar un modelo suficientemente preciso y revisar manualmente.
- Si no hay tiempo para revision, entregar video sin subtitulos y dejar que el usuario los haga en CapCut.
- Nunca quemar subtitulos defectuosos solo por cumplir el paso.

## Apertura correcta para TikTok

El TikTok debe abrir con evidencia, no con explicacion.

Orden recomendado:

1. Cold open: 8-12 segundos de James vulnerable.
2. Subtitulo/traduccion de esa frase.
3. Entra la voz del narrador.
4. La primera frase del narrador debe reinterpretar lo que acabamos de ver.

Ejemplo aprobado como direccion:

> James Hetfield parecia una roca.

El cold open no lo narra el usuario. Se edita antes de su voz.

## Por que no basta con tomar parrafos del guion largo

Se creo un mapa del script largo marcando parrafos para TikTok. Ese mapa es util para saber que partes de la historia entran, pero no debe ser la version final de locucion.

Motivo:

- El largo explica.
- El short empuja.
- El largo puede acumular contexto por minutos.
- El short necesita micro-payoffs constantes.

Decision: grabar un script nuevo para TikTok.

Archivo creado:

`produccion/james_hetfield/tiktok_vertical_3_4min/script_tiktok_v3_grabacion_acentos.md`

Esta version ya incluye acentos, comas y respiracion para lectura.

## Escritura para locucion

Aprendizaje importante: los scripts de locucion deben venir con acentos, tildes y puntuacion natural.

El usuario necesita leer con musicalidad. Sin acentos, la grabacion se vuelve mas dificil y aumenta la probabilidad de pausas incorrectas.

Reglas nuevas:

- Los scripts de grabacion deben estar en espanol correcto con acentos.
- Separar notas de produccion de narracion.
- No incluir frases tipo "microdato musical", "morbo verificable" o instrucciones internas dentro del bloque de lectura.
- Mantener encabezados claros:
  - `Cold open antes de voz`
  - `Narracion limpia`
  - `Inserts sugeridos`
- La seccion grabable debe poder leerse sin editar mentalmente.

## Estructura final elegida para TikTok

Duracion objetivo: 3:30-4:00.

Estructura:

1. James vulnerable: prueba emocional.
2. James parecia una roca: contradiccion.
3. Infancia: Christian Science y clase de salud.
4. Padre se va / madre muere.
5. Metallica como segunda familia.
6. Armadura: riffs, voz seca, control.
7. Some Kind of Monster / St. Anger como crisis.
8. Rehabilitacion y comunicacion.
9. Regreso a Brasil como payoff.
10. Cierre: pedir ayuda tambien puede ser poder.

La idea central no es "James sufrio". La idea central es:

> El hombre que parecia invencible habia construido una armadura; cuando por fin admitio que temblaba, no perdio poder, se volvio mas real.

## Musica para reemplazo por copyright

El video largo recibio limitacion por musica entre 0:49 y 4:42 aproximadamente, desde:

> "La primera pista no es una fecha..."

hasta:

> "...una de las voces mas reconocidas del metal"

Aprendizaje:

- Para documentales de rock, la musica debe sostener tension sin competir con la voz.
- No debe sonar a trailer heroico.
- No debe tener lead vocal ni melodia demasiado memorable.
- Debe ser instrumental, dark rock documentary, cinematic, con espacio para narracion.

Para Suno, separar:

- `Lyrics`: instrucciones instrumentales, indicando `Instrumental only. No vocals. No lyrics.`
- `Style`: estilo resumido.

No entregar prompts de Suno como un unico prompt generico si el usuario necesita llenar campos separados.

## Regla de derechos y archivo real

El usuario corrigio derechos de autor en el largo y YouTube aprobo verificaciones. Aun asi:

- Some Kind of Monster debe usarse en microfragmentos.
- No dejar correr DVD/documentales por largos bloques.
- Alternar con fotos, archivo, zooms, stills, articulos y graficos.
- En TikTok monetizado, ser mas cuidadoso con musicas y clips largos.

## Integracion con CapCut

No se logro controlar CapCut de forma confiable desde Codex. Por eso:

- Codex debe entregar guion, secuencia, prompts, assets y mapas de edicion.
- El usuario mantiene el control fino de CapCut.
- No prometer control directo de CapCut si la ventana/app no responde bien.

El mejor handoff para el usuario es:

- Script grabable con acentos.
- Lista de inserts por frase.
- Orden de bloques.
- Reglas de crop.
- Musica sugerida.
- Advertencias de copyright.

## Archivos creados en esta fase

- `produccion/james_hetfield/tiktok_vertical_3_4min/script_tiktok_v2_grabacion.md`
- `produccion/james_hetfield/tiktok_vertical_3_4min/script_tiktok_v3_grabacion_acentos.md`
- `produccion/james_hetfield/tiktok_vertical_3_4min/script_largo_marcado_para_tiktok_v1.md`
- `produccion/james_hetfield/tiktok_vertical_3_4min/secuencia_por_parrafos_v1.md`

Tambien se creo una carpeta local de trabajo para shorts:

`F:\Google Drive GOG MH\A Videos Backup\Tiktok Rockwise Shorts\James Hetfield Docu`

Nota: los renders automaticos generados ahi no son la version recomendada final. Sirven como prueba tecnica, no como corte aprobado.

## Regla para proximos documentales

Flujo recomendado:

1. Publicar o terminar largo.
2. Identificar la escena vulnerable o el clip de evidencia mas fuerte.
3. Escribir script TikTok nativo, no solo extracto del largo.
4. Validar que la primera frase de voz conecte con el cold open.
5. Grabar voz especifica para TikTok.
6. Editar en vertical fullscreen en CapCut.
7. Subtitular en CapCut.
8. Usar musica instrumental propia o generada con prompts por seccion.
9. Revisar derechos antes de publicar.

Si no existe un cold open fuerte, no forzar la historia desde una escena debil. Replantear el eje.

## Criterio de calidad

Un TikTok largo de Rockwise debe pasar estas preguntas:

- En los primeros 3 segundos, hay emocion o contradiccion visible?
- En los primeros 15 segundos, entiendo por que debo quedarme?
- Cada 20 segundos aparece un dato, giro o frase compartible?
- La voz suena como descubrimiento, no como resumen?
- Los subtitulos ayudan a retener incluso si el usuario ve sin audio?
- El video ocupa toda la pantalla vertical?
- El material vulnerable se ve y se siente, no solo se menciona?
- El cierre reinterpreta el inicio?

Si falla alguna de las primeras cuatro, hay que reescribir antes de editar.
