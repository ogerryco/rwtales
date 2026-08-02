# Auditoria de cobertura visual - B01 a B05

Fecha: 2026-07-31

Objetivo: evitar que los bloques de imagenes/videos se queden cortos frente a la narracion grabada.

## Hallazgo principal

Los packs B01-B05 fueron armados con buena coherencia visual, pero no todos tienen suficiente duracion base si las imagenes se usan a 3-4 segundos. Para este documental, el criterio correcto no debe ser "numero de assets", sino "duracion estimada de voz + colchon visual".

## Regla operativa desde B06

- Antes de buscar, bajar o generar imagenes/videos, analizar primero la voz real del bloque.
- La voz manda la secuencia: ritmo, pausas, intencion, velocidad y duracion real.
- Los visuales se preparan despues, ya calculados contra ese timeline de voz.
- Pero la cobertura no debe resolverse principalmente con imagenes generadas. La nueva jerarquia es: voz real -> archivo real -> stills del archivo real -> foto historica/album/press -> recreacion representativa -> IA como ultimo recurso.
- Si el bloque habla de un album, una era, un conflicto o una entrevista, buscar primero material real de esa fuente.
- Un pack no debe considerarse cerrado si mas del 40% de su secuencia principal es IA, salvo que el tramo sea imposible de documentar visualmente.
- Calcular duracion estimada por palabras antes de cerrar cada pack.
- Usar como referencia 125-135 palabras por minuto para la voz.
- Entregar visuales para al menos 120-140% de la duracion estimada.
- Si el bloque es emocional o conceptual, agregar mas imagenes de transicion, detalles, objetos y espacios.
- Si una imagen es fuerte y premium, puede planearse a 5-7 segundos con movimiento en CapCut.
- No depender de clips candidatos para completar duracion, porque pueden caerse por calidad, derechos o falta de encaje.

## Aprendizaje confirmado

El flujo incorrecto no es solo:

1. leer el script;
2. buscar imagenes/videos;
3. intentar que encajen.

Tampoco es:

1. escuchar la voz;
2. generar imagenes bonitas;
3. cubrir duracion.

El flujo correcto es:

1. escuchar la voz real;
2. detectar ritmo, pausas y puntos de enfasis;
3. dividir el bloque por beats narrativos reales;
4. buscar archivo real por beat;
5. usar stills del propio archivo si el clip no encaja;
6. completar con fotos historicas, albumes o material publico;
7. solo al final usar recreaciones o IA como respiracion visual.

Esto evita que el pack se quede corto, pero tambien evita visuales que "describen el texto" sin aportar autoridad documental.

## Estimacion rapida

| Bloque | Visuales actuales aprox. con imagenes a 4s | Riesgo |
|---|---:|---|
| B01 | 66.6 s | Alto: ya se observo corto en edicion |
| B02 | 34.0 s | Medio/alto si cubre todo el texto asignado |
| B03 | 38.0 s | Alto |
| B04 | 46.0 s | Medio/alto |
| B05 | 28.0 s | Alto |

## Ajuste recomendado

Para los siguientes bloques, cada folder debe incluir:

1. Secuencia principal: visuales en orden directo para pegar en CapCut.
2. Colchon visual: 4-8 assets extra numerados al final o integrados como alternativas.
3. README con duracion estimada, duracion base de assets y rango recomendado de uso.

## Nota para B01-B05

Si al montar alguno queda corto, no estirar todos los clips de forma pareja. Es mejor agregar:

- close-ups de manos, guitarras, escenarios, cuartos, maletas, luces, recortes visuales;
- planos de transicion entre ideas;
- 1-2 imagenes abstractas narrativas por cada pregunta o giro emocional;
- clips reales mudos solo cuando el look visual lo soporte.
