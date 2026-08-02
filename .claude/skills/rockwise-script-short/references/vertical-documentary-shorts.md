# Vertical documentary shorts - aprendizaje reusable Rockwise

Leer esta referencia cuando el usuario pida convertir, derivar o adaptar un
documental largo de Rockwise Tales a TikTok vertical. No usarla como regla para
YouTube long; esa linea vive en `rockwise-script`.

## Principio central

Un documental largo no se convierte bien a TikTok solo recortandolo.

El largo puede acumular contexto, capas y tension lenta. TikTok necesita una
pieza nativa: una promesa inmediata, evidencia temprana, micro-payoffs
frecuentes y frases grabables para consumo vertical.

Regla:

> El video largo es fuente de verdad y archivo; el short necesita guion propio.

## Flujo obligatorio

1. Identificar el cold open real.
2. Escribir una primera frase de voz que conecte directamente con ese cold
   open.
3. Crear guion TikTok nativo, no solo una lista de parrafos del largo.
4. Separar narracion limpia de inserts, notas, timestamps y decisiones de
   edicion.
5. Entregar el script de grabacion con acentos, comas y puntuacion natural.
6. Mantener el control fino de subtitulos y crops en CapCut cuando el usuario
   asi lo prefiera.

## Cold open

El short debe abrir con evidencia emocional o factual, no con explicacion.

Ejemplos de evidencia:

- entrevista vulnerable del artista;
- frase del artista que contradice su personaje publico;
- momento visual de quiebre;
- documento, llamada, declaracion o escena que pruebe la premisa.

Despues del cold open, la voz en off debe reinterpretar lo que acabamos de ver.

Ejemplo de funcion:

```text
[clip vulnerable del artista]
Narrador: "Parecia una roca."
```

No abrir con backstory si existe un archivo vulnerable capaz de probar la
tension.

## Escritura nativa para TikTok

No reciclar la voz del largo salvo que el usuario lo pida explicitamente como
experimento.

El guion TikTok debe tener:

- frases mas cortas;
- menos subordinadas;
- tension cada 10-20 segundos;
- datos ocultos o giros verificables;
- avance por revelaciones;
- oralidad natural;
- una pregunta emocional que cierre con payoff.

El objetivo no es "resumir el documental"; es crear una pieza autosuficiente
que haga que alguien quiera ver o compartir la historia.

## Puntuacion y acentos

Para Rockwise, los scripts de grabacion deben entregarse con acentos, tildes y
comas.

Motivo: el usuario narra con intencion. Sin acentos y puntuacion, la lectura se
vuelve torpe, se pierden pausas y aumenta el retrabajo.

Regla:

- los archivos de produccion tecnica pueden estar en ASCII si el repo lo exige;
- los scripts finales de locucion en espanol deben tener acentos.

## Separacion de capas

Nunca mezclar notas internas dentro de la narracion.

Malo:

```text
[microdato musical] Aqui esta el morbo verificable...
```

Bueno:

```text
## Narracion limpia
...

## Inserts sugeridos
...
```

La seccion grabable debe poder leerse de corrido sin que el usuario tenga que
filtrar instrucciones.

## Formato vertical

Para TikTok Rockwise:

- video fullscreen 9:16;
- evitar fondo blur como salida final;
- crop manual siguiendo emocion y sujetos, no centro geometrico;
- priorizar ojos, rostro, manos, instrumento o gesto colectivo;
- si el gesto vulnerable no se ve, el clip no sostiene el hook.

El render automatico puede servir para prototipo, pero no sustituye una
decision editorial de CapCut.

### Precision de crop para TikTok

En TikTok hay menos tiempo para captar atencion. Un mal crop vertical puede
destruir una escena aunque el clip sea correcto.

No usar por defecto un crop centrado del video horizontal. Antes de aprobar un
corte vertical, revisar:

1. Rostro: ojos, boca y expresion no deben quedar cortados.
2. Personaje: el artista o musico relevante debe aparecer completo cuando la
   escena lo exige.
3. Instrumento/manos: si la frase habla de tocar, riff, bateria o guitarra, no
   cortar manos ni instrumento clave.
4. Accion: si hay abrazo, quiebre, mirada o gesto de apoyo, el crop debe cubrir
   la accion completa.
5. Dinamismo: si el sujeto se mueve, dividir el clip en subcortes con crops
   distintos o ajustar manualmente en CapCut.
6. Hook: en los primeros 3 segundos, el encuadre debe ser fuerte sin que el
   usuario tenga que "buscar" al personaje.

Si el crop automatico corta al artista, deja personas incompletas o centra un
espacio vacio, el clip queda como `RECHAZADO_PARA_VERTICAL` aunque sirva en
16:9.

## Subtitulos

Regla de canal: los shorts de Rockwise llevan subtitulos.

Pero no quemar subtitulos automaticos malos. Si Whisper o cualquier transcriptor
genera errores evidentes, entregar sin subtitulos y dejar que el usuario los
haga en CapCut.

Un subtitulo incorrecto destruye autoridad, especialmente con audiencia
melomana.

## Copyright y archivo ajeno

El archivo ajeno es evidencia, no la pieza completa.

Para documentales, DVDs, entrevistas o clips de terceros:

- usar microfragmentos cuando haya riesgo de reclamacion;
- alternar con fotos, stills, zooms, articulos, archivo propio o recreaciones;
- evitar que un documental ajeno corra como base visual continua;
- revisar derechos antes de publicar si el objetivo es monetizacion.

## Musica generada

Para musica instrumental en Suno u otra herramienta:

- separar `Lyrics` y `Style` si la herramienta tiene ambos campos;
- en `Lyrics`, escribir instrucciones de instrumental sin letra;
- indicar explicitamente: `Instrumental only. No vocals. No lyrics.`;
- pedir que deje espacio para narracion;
- evitar leads melodicos o solos que compitan con la voz.

## Checklist antes de entregar el script

- [ ] Hay cold open real y no solo idea de apertura.
- [ ] La primera frase de voz conecta con el cold open.
- [ ] El guion no es recorte literal del largo.
- [ ] La narracion esta separada de notas/inserts.
- [ ] El script de grabacion tiene acentos y comas.
- [ ] Cada 10-20 segundos aparece nueva tension, dato o giro.
- [ ] El cierre reinterpreta la escena inicial.
- [ ] Se indico que el video final debe ser fullscreen 9:16.
- [ ] Los crops verticales no cortan rostros, artistas, manos, instrumentos ni
      gestos clave.
- [ ] Se definio si los subtitulos van en CapCut o automatizados revisados.
- [ ] Se marco riesgo de copyright en clips de archivo.

## Postmortem origen

Este protocolo nace del aprendizaje del documental de James Hetfield
documentado en:

`produccion/james_hetfield/reference/postmortem/tiktok_vertical_learning_2026-08-02.md`
