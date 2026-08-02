# Timeline real por voz - B01 a B05

Fecha: 2026-07-31

Fuente usada:

- `F:\Google Drive GOG MH\A Videos Backup\RWTLat Youtube Long\S107 James Hetfield\10_Approval_Previews\Intro_V7_GO_V2\S107_INTRO_V2_GO_MASTER_clean.wav`
- `F:\Google Drive GOG MH\A Videos Backup\RWTLat Youtube Long\S107 James Hetfield\01_Script\Voz\Voces V2\Voz parte 2.mp3`
- `F:\Google Drive GOG MH\A Videos Backup\RWTLat Youtube Long\S107 James Hetfield\01_Script\Voz\Voces V2\Voz parte 3.mp3`

Transcripciones temporales:

`F:\Google Drive GOG MH\A Videos Backup\RWTLat Youtube Long\S107 James Hetfield\01_Script\Voz\timeline_whisper_parts`

Nota: Whisper tiny no es confiable para texto final, pero si es util para ubicar entradas, cortes y duraciones aproximadas.

## Audio maestro V2

Duracion aproximada:

- Intro GO master: 00:40.9
- Voz parte 2: 04:54.8
- Voz parte 3: 04:59.9
- Voz parte 4: 04:59.9
- Voz parte 5: 04:59.9
- Voz parte 6: 01:48.9
- Total voz V2 aproximado: 22:24

## Correccion de offset

El usuario confirmo que `Voz parte 2.mp3` entra despues de la intro editada de aproximadamente 1 minuto, no inmediatamente despues del master limpio de 40 segundos. Por tanto:

- la carpeta `Voces V2` contiene la narracion principal por partes;
- `Voz parte 2.mp3` debe tratarse como continuacion posterior a la intro ya editada;
- los packs visuales deben mapearse contra el audio real en CapCut, usando el inicio de `Voz parte 2.mp3` como punto de arranque narrativo posterior a la intro.

Este ajuste es importante para no sobrecontar ni subcontar cobertura visual en el arranque.

## Bloques ya creados

| Bloque | Rango aproximado en audio maestro | Duracion voz aprox. | Visual actual aprox. con imagenes a 4s | Estado |
|---|---:|---:|---:|---|
| B01 | 00:40.9-03:38.2 | 02:57 | 01:07 | Corto |
| B02 | 03:38.2-05:09.7 | 01:31 | 00:34 | Corto |
| B03 | 05:09.7-07:30.5 | 02:21 | 00:38 | Muy corto |
| B04 | 07:30.5-08:51.4 | 01:21 | 00:46 | Corto |
| B05 | 08:51.4-10:33.1 | 01:42 | 00:28 | Muy corto |

## Nuevo criterio de cobertura

Para cada bloque, el pack debe cubrir la voz real, no solo el texto del guion.

Primero se analiza la voz y el ritmo. Despues se buscan, bajan, recortan o generan los visuales.

Objetivo minimo:

- visual base >= 100% de la voz del bloque;
- visual recomendado >= 120% de la voz del bloque;
- si hay clips candidatos, no contarlos como cobertura segura hasta que sean aprobados.

Targets recomendados:

| Bloque | Voz aprox. | Target visual minimo | Target recomendado 120% |
|---|---:|---:|---:|
| B01 | 02:57 | 02:57 | 03:33 |
| B02 | 01:31 | 01:31 | 01:49 |
| B03 | 02:21 | 02:21 | 02:49 |
| B04 | 01:21 | 01:21 | 01:37 |
| B05 | 01:42 | 01:42 | 02:02 |

## Implicacion directa

B06 en adelante debe salir mucho mas robusto. Un bloque de 90-120 segundos de voz necesita normalmente:

- 18-28 imagenes si duran 4-5 segundos;
- o 12-16 imagenes premium si se planean con movimiento de 6-8 segundos;
- mas 2-4 clips reales breves cuando aporten autoridad;
- mas 4-6 visuales de colchon por si algo no encaja.

## Ajuste para B01-B05

No conviene estirar todo de manera pareja. Para completar sin que se sienta lento:

- agregar planos de detalle entre frases largas;
- usar paneos/zoom suave en imagenes premium;
- alternar espacios, objetos, manos, escenario, archivos reales mudos y recreaciones;
- dejar las entrevistas solo como acentos de autoridad, no como relleno.
