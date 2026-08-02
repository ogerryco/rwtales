# Scouting YouTube LONG — Jonathan Davis, Trent Reznor, Andrew Wood

Fecha: 2026-08-01

Objetivo: dejar guardada la decisión editorial para producir, en este orden:

1. Jonathan Davis / Korn
2. Trent Reznor / Nine Inch Nails
3. Andrew Wood / Mother Love Bone

## Método

Scouting ejecutado con YouTube Data API (`search.list` + `videos.list`) y criterio del skill `rockwise-research`:

- competencia existente en YouTube;
- saturación en español;
- videos largos comparables;
- ángulos ya cubiertos;
- hueco editorial real para Rockwise Tales;
- potencial narrativo y fit con los videos que mejor han funcionado en el canal.

Archivos de datos:

- `youtube_three_favorites_research_scout_strict_20260801.json`
- `youtube_three_favorites_research_scout_20260801.json`

## Keywords usadas

### Trent Reznor / Nine Inch Nails

- `"Trent Reznor" documental`
- `"Nine Inch Nails" documental español`
- `"Trent Reznor" adicción`
- `"Trent Reznor" Hurt Johnny Cash`
- `"Nine Inch Nails" historia español`
- `"Trent Reznor" depression addiction`

Filtro estricto: `trent reznor`, `nine inch nails`, `nin`.

### Andrew Wood / Mother Love Bone

- `"Andrew Wood" "Mother Love Bone"`
- `"Andrew Wood" documental`
- `"Mother Love Bone" historia español`
- `"Andrew Wood" "Temple of the Dog"`
- `"Malfunkshun" "Andrew Wood"`
- `"Mother Love Bone" documentary`

Filtro estricto: `andrew wood`, `mother love bone`, `malfunkshun`, `temple of the dog`.

### Jonathan Davis / Korn

- `"Jonathan Davis" Korn documental`
- `"Jonathan Davis" abuso Korn`
- `"Jonathan Davis" Daddy Korn`
- `"Korn" historia español Jonathan Davis`
- `"Jonathan Davis" meth addiction`
- `"The Abused Kid Who Reinvented Metal"`

Filtro estricto: `jonathan davis`, `korn`.

## Criterio de demanda

La demanda no se definió solo por keywords. Se ponderó:

- cantidad de resultados relevantes;
- vistas de videos existentes;
- número de videos largos comparables;
- número de videos largos comparables en español;
- señales de interés en clips/canciones/documentales;
- saturación del ángulo;
- fit con Rockwise Tales y con el patrón de Scott Weiland / James Hetfield / Layne Staley.

Se consideró “largo comparable” cuando:

- duraba al menos 8 minutos;
- no era lyric video, cover, reaction, karaoke, topic, video oficial, subtitulado suelto o clip musical;
- trataba directamente al artista, banda o historia nuclear.

## Resultado

| Ranking | Tema | Saturación | Potencial | Veredicto |
| ---: | --- | --- | --- | --- |
| 1 | Jonathan Davis / Korn | Baja-media en documental español específico | Alto | Mejor hueco para viral emocional |
| 2 | Trent Reznor / Nine Inch Nails | Media-alta en inglés, baja-media en español | Alto | Mejor tema premium/current |
| 3 | Andrew Wood / Mother Love Bone | Baja en español, menor demanda general | Medio-alto | Video de culto fuerte, menos masivo |

## 1. Jonathan Davis / Korn

Datos API estrictos:

- resultados únicos: 45;
- largos comparables: 3;
- largos comparables en español: 1;
- señales en español: 8;
- top 5 comparables: 1.72M vistas.

Videos/ángulos existentes:

- `The Abused Kid Who Reinvented Metal: Jonathan Davis` — 606k vistas, inglés.
- `Jonathan Davis - Steve-O's Wild Ride!` — 798k vistas, entrevista larga.
- `La Historia de Korn` — 323k vistas, español.
- `Infierno en casa: la perturbada infancia de Jonathan Davis` — 296k vistas, español corto.
- `Korn - Daddy historia detrás de la canción` — 198k vistas, español corto.

Hueco:

No hay suficiente documental largo en español centrado en Jonathan Davis como persona. Hay historia de Korn, subtítulos, clips y piezas cortas sobre `Daddy`, pero falta un documental emocional completo.

Ángulo recomendado:

> La canción que Jonathan Davis no podía cantar sin romperse.

Alternativa:

> Korn nació del sonido de un niño que nadie protegió.

Idea Class: `HOME RUN` si el research encuentra una escena-prueba fuerte y verificable alrededor de `Daddy`.

## 2. Trent Reznor / Nine Inch Nails

Datos API estrictos:

- resultados únicos: 52;
- largos comparables: 18;
- largos comparables en español: 7;
- señales en español: 11;
- top 5 comparables: 3.28M vistas.

Videos/ángulos existentes:

- `The Downward Spiral Of Trent Reznor` — 647k vistas, inglés.
- `Pretty Hate Machine - The Nine Inch Nails Story` — 359k vistas, inglés.
- `Nine Inch Nails - The Fragile (Documentary)` — 300k vistas, inglés.
- `La Trágica Historia De Nine Inch Nails` — 37k vistas, español.
- `La HISTORIA COMPLETA de NINE INCH NAILS` — 32k vistas, español.
- `Trent Reznor y su espiral descendente` — 20k vistas, español.

Hueco:

Está más saturado que Jonathan, pero hay hueco para un enfoque humano en español: autodestrucción, sobriedad, `Hurt`, Johnny Cash, legitimación cultural y regreso actual.

Ángulo recomendado:

> Trent Reznor escribió la canción más rota de los 90… y Johnny Cash se la devolvió como despedida.

Alternativa:

> El hombre que convirtió su espiral descendente en una segunda vida.

Idea Class: `DOUBLE alto / HOME RUN` si se amarra a `Hurt + Johnny Cash + sobriedad + actualidad`.

## 3. Andrew Wood / Mother Love Bone

Datos API estrictos:

- resultados únicos: 51;
- largos comparables: 16;
- largos comparables en español: 4;
- señales en español: 6;
- top 5 comparables: 7.69M vistas, inflado por videos musicales/documentales no necesariamente equivalentes.

Videos/ángulos existentes en español:

- `LA HISTORIA DE ANDREW WOOD - EL INICIO DE LA MALDICION DEL GRUNGE` — 17k vistas.
- `La Tragedia que dio Origen a Pearl Jam: Temple Of The Dog` — 4.6k vistas.
- `El desconocido padre del Grunge - Biografia de Andrew Wood` — 4k vistas.
- `Andrew Wood: Historia y legado` — 2.6k vistas.

Hueco:

Muy poca saturación documental en español, pero también menor demanda masiva. El tema debe venderse por su conexión con Pearl Jam, Chris Cornell y Temple of the Dog, no solo por el nombre de Andrew Wood.

Ángulo recomendado:

> El cantante que tuvo que morir para que nacieran Pearl Jam y Temple of the Dog.

Idea Class: `DOUBLE`. Fuerte como video de culto; menor probabilidad de explosión que Jonathan o Trent.

## Decisión editorial guardada

Orden recomendado de producción:

1. Jonathan Davis / Korn
2. Trent Reznor / Nine Inch Nails
3. Andrew Wood / Mother Love Bone

Siguiente paso para otro chat: iniciar `rockwise-research` profundo de Jonathan Davis, empezando por:

- escena-prueba de apertura;
- hipótesis narrativa;
- claim ledger de infancia, abuso, `Daddy`, adicción y salud mental;
- fuentes primarias;
- clips verificables con los 5 puntos del skill.
