# Creator Search Insights para Rockwise Tales

Usar esta referencia al elegir temas, keywords o ángulos para TikTok. Creator
Search Insights (CSI) es una señal de demanda, no un generador automático de
temas.

## Principio central

No preguntar primero qué quiere contar el canal. Preguntar qué busca la
audiencia dentro del universo rock y después comprobar si Rockwise Tales puede
resolver esa intención con una historia verificable.

Una fila visible en CSI solo es evidencia si:

1. corresponde semánticamente a música rock;
2. conserva el significado de la consulta;
3. encaja con una historia que el canal puede producir;
4. no repite sin novedad un tema ya saturado en el catálogo propio.

## Limitación de acceso

La API pública de TikTok no expone Creator Search Insights ni su volumen. Usar
la vista live de la app, capturas o una exportación manual. Registrar siempre
fecha, cuenta, idioma, región, consulta escrita, pestaña y filtro.

No describir el número junto al icono de popularidad como búsquedas mensuales.
TikTok lo presenta como popularidad o señal de demanda; conservar el valor tal
como aparece y no extrapolarlo. Tratar el porcentaje azul como cambio mostrado
por la interfaz, sin inventar su periodo o denominador.

## Evidencia propia: falsos positivos semánticos

Capturas de @rockwisetales del 2026-07-25:

- La consulta `soundgarden` devolvió `soundcore select go 4`, `8d Sound`,
  `Soundgsm`, `AcousticCovers`, `Soundwaves` y `SoundEffect`. Ninguna fila
  demostraba demanda por la banda Soundgarden.
- La consulta `secretos del rock` devolvió términos como `the rock and the
  usos`, `NEW ROCKS`, `el secreto del casco`, `rock moving`, `rock and stone` y
  ubicaciones o productos. La coincidencia lexical con `rock` no implicaba
  música.

Conclusión: nunca sumar popularidad, crecimiento o `content gap` antes de
pasar el filtro semántico.

## Captura mínima

Guardar una tabla por sesión:

```text
FECHA:
CUENTA/REGIÓN/IDIOMA:
CONSULTA ESCRITA:
PESTAÑA: SUGERENCIA | POPULAR | MODA | OTRA
FILTRO: TODO | BRECHA DE CONTENIDO | OTRO

TÉRMINO | VALOR MOSTRADO | CAMBIO MOSTRADO | GAP VISIBLE | RELEVANCIA | NOTA
```

Usar `N/D` cuando un dato no sea legible. No reconstruir números borrosos.

## Filtro semántico obligatorio

Clasificar cada fila antes de puntuar:

- `EXACTA`: artista, banda, canción, álbum, género, escena o historia musical
  inequívoca.
- `ADYACENTE`: comunidad o identidad musical útil, pero la intención necesita
  investigación adicional; por ejemplo `metalhead guy`.
- `AMBIGUA`: podría ser música u otra cosa. Abrir la fila y revisar videos
  antes de usarla.
- `FALSO_POSITIVO`: producto, ubicación, objeto, luchador, efecto de sonido,
  juego o frase sin intención musical.

Solo `EXACTA` pasa directamente. `ADYACENTE` y `AMBIGUA` requieren validación
con resultados reales. Descartar `FALSO_POSITIVO`.

## Buscar por clusters, no por una sola palabra

Explorar de lo amplio a lo específico:

1. Historia: `historia del rock`, `historia del grunge`, `historias de
   canciones`.
2. Género y escena: `grunge`, `metal`, `rock latino`, `rock mexicano`,
   `rock alternativo`.
3. Artista o banda: nombre exacto y variantes naturales.
4. Canción o álbum: nombre + `historia`, `significado`, `origen` o `secreto`.
5. Momento: `última entrevista`, `por qué dejó la banda`, `canción inédita`,
   `concierto histórico`, `rechazó millones`.
6. Identidad: `metalhead`, `rockero`, `underground music`, únicamente si la
   intención observada es musical.

Buscar en español e inglés cuando el artista tenga demanda bilingüe, pero
escribir el video para una sola intención primaria.

## Auditoría de cobertura propia

Antes de recomendar un tema, cruzar la consulta con
`tiktok_own_videos.json`:

```text
VIDEOS DEL MISMO ARTISTA: total / últimos 90 días
VIDEOS DEL MISMO ÁNGULO: total / últimos 90 días
ÚLTIMO VIDEO RELACIONADO:
MEDIANA DE VIEWS DEL CLUSTER:
MEJOR RESULTADO DEL CLUSTER:
NOVEDAD REAL DEL ÁNGULO:
```

Muchos videos previos no prohíben un artista. Exigen una consulta o momento
nuevo. Para artistas ya cubiertos repetidamente —como Layne Staley o
Soundgarden— no recomendar otra biografía general; exigir evidencia de demanda
para un subtema no repetido.

## Topic Priority Score

Puntuar únicamente filas que pasaron el filtro semántico:

| Dimensión | Rango | Criterio |
| --- | ---: | --- |
| Evidencia CSI | 0-4 | De plausible a demanda/gap visible |
| Relevancia rock | 0-3 | De adyacente a intención musical exacta |
| Encaje Rockwise | 0-3 | Existe momento, revelación y consecuencia |
| Crecimiento visible | 0-2 | Ninguno, positivo o acelerado |
| Brecha visible | 0-2 | No visible, sugerida o confirmada |
| Novedad de catálogo | 0-3 | Repetido, ángulo nuevo o cluster nuevo |

Reglas de decisión:

- `14-17`: prioridad alta para research.
- `10-13`: validar resultados y competencia antes de producir.
- `0-9`: no priorizar.
- Relevancia rock menor de 2: descartar sin importar el total.
- Novedad 0: exigir un subángulo nuevo; no producir otra pieza equivalente.

El score prioriza research, no autoriza escribir sin Fact Sheet.

## Handoff obligatorio

```text
CSI SOURCE + DATE:
PRIMARY QUERY:
SEARCH INTENT:
SEMANTIC CLASS:
DISPLAYED POPULARITY:
DISPLAYED CHANGE:
CONTENT GAP: CONFIRMADO | NO CONFIRMADO
RELATED QUERIES:
OWN-CATALOG COVERAGE:
TOPIC PRIORITY SCORE:
WHY THIS TOPIC NOW:
```

## Fuentes oficiales

- https://newsroom.tiktok.com/creator-search-insights
- https://support.tiktok.com/en/using-tiktok/growing-your-audience/creator-search-insights
- https://newsroom.tiktok.com/introducing-the-new-creator-rewards-program
- https://ads.tiktok.com/help/article/how-to-use-trends

TikTok confirma que CSI muestra temas buscados con frecuencia, permite filtrar
`content gaps` y conecta search value con Creator Rewards. Creative Center
sirve para tendencias y hashtags; no sustituye CSI ni prueba volumen de
búsqueda orgánica.
