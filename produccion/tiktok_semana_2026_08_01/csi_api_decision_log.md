# CSI + API Decision Log: TikTok semana 2026-08-01

Fecha de trabajo: 2026-08-01
Canal: Rockwise Tales TikTok
Skill usado: `.claude/skills/rockwise-script-short/SKILL.md`

## Principio operativo

Creator Search Insights no decide temas por si solo. CSI genera hipotesis de
demanda. Antes de producir, cada hipotesis debe pasar:

1. filtro semantico;
2. revision de resultados reales en TikTok cuando sea ambigua;
3. cruce con API/catalogo propio;
4. viral-fit editorial de Rockwise Tales;
5. decision explicita: producir, reencuadrar o descartar.

## Clasificacion semantica

| Clase | Criterio | Decision |
| --- | --- | --- |
| EXACTA | Banda, artista, cancion, album, genero, escena o historia musical inequivoca. | Puede pasar a cobertura propia y viral-fit. |
| ADYACENTE | Identidad, estetica, formato o comunidad util, pero no necesariamente rock. | Requiere abrir resultados reales antes de producir. |
| AMBIGUA | Puede ser musica rock u otra intencion. | No producir sin verificar resultados reales. |
| FALSO_POSITIVO | Meme, cancion de otro genero, producto, anime, videojuego, frase random o homonimo. | Descartar como evidencia CSI para Rockwise. |

Regla nueva: ninguna keyword con `rock`, `rockstar`, `metal`, `punk` o nombre
parcial pasa sin revisar intencion real. Puede ser moda, anime, urbano,
producto, meme o estetica.

## Tabla de decision

| Tema | Query CSI | Clase semantica | Evidencia real | Cobertura propia | Saturacion 90d | Viral-fit | Riesgo | Decision |
| --- | --- | --- | --- | ---: | ---: | --- | --- | --- |
| Los rockstars no van al cielo | `los rockstars no van al cielo` | FALSO_POSITIVO | La frase corresponde a una cancion urbana/trap/reggaeton de Ovi ft. Hanzel La H, no a una busqueda de historia del rock. | 17 videos cluster rockstar/rockeros/cielo | 1 | Debil para Rockwise porque la intencion de busqueda no es rock. | Alto: atraer audiencia equivocada y parecer que no se verifico el trend. | DESCARTAR |
| Tu gusto musical si te delata | `videos identificarse`, `estilo punk hombre`, `mis gustos musicales rock` | ADYACENTE | `videos identificarse` es mecanismo de formato, no demanda musical exacta. El usuario ya probo un video similar y no funciono. | 114 videos cluster identidad musical | 9 | Medio como formato de identidad, bajo como documental factual. | Alto: horoscopo musical repetido o sin novedad. | DESCARTAR |
| Deftones no volvio por nostalgia | `deftones`, `deftones fans`, `is deftones demonic` | PENDIENTE | Requiere revisar resultados reales: separar banda/musica de estetica, anime, tattoos, edits y fandom. | 0 videos cluster Deftones | 0 | Potencial si se formula como cultura musical: por que Deftones se volvio lenguaje emocional para otra generacion. | Medio: demanda contaminada por estetica TikTok. | VALIDAR |

## Handoff para validar Deftones

```text
CSI SOURCE + DATE:
PRIMARY QUERY: deftones
SEARCH INTENT: entender por que Deftones volvio a circular entre una audiencia nueva
SEMANTIC CLASS: PENDIENTE
DISPLAYED POPULARITY:
DISPLAYED CHANGE:
CONTENT GAP: CONFIRMADO | NO CONFIRMADO
RELATED QUERIES:
  - deftones fans
  - deftones trend
  - is deftones demonic
  - deftones tattoos
  - deftones mustang
  - dbz deftones
OWN-CATALOG COVERAGE:
  - videos del cluster: 0
  - ultimos 90 dias: 0
  - mediana views: 0
  - share mediana: 0
TOPIC PRIORITY SCORE: pendiente hasta filtrar semantica real
WHY THIS TOPIC NOW:
  Es un cluster nuevo para Rockwise. La oportunidad no es biografia general,
  sino explicar por que una banda de metal alternativo/shoegaze/nu metal se
  convirtio en lenguaje emocional y estetico para otra generacion.
```

## Protocolo antes de escribir guion

Para cada nueva fila de CSI:

```text
FECHA:
CUENTA/REGION/IDIOMA:
CONSULTA ESCRITA:
PESTANA:
FILTRO:
TERMINO:
VALOR MOSTRADO:
CAMBIO MOSTRADO:
GAP VISIBLE:
RELEVANCIA: EXACTA | ADYACENTE | AMBIGUA | FALSO_POSITIVO
NOTA DE INTENCION REAL:
COBERTURA PROPIA:
DECISION:
```

No producir hasta que `RELEVANCIA` sea EXACTA, o hasta que una fila ADYACENTE
tenga resultados reales que prueben intencion musical compatible con Rockwise
Tales.

