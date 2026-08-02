# Diagnóstico de canal, competencia y monetización TikTok

Leer esta referencia cuando el usuario pida analizar rendimiento, encontrar
patrones/gaps, comparar competencia, evaluar un supuesto cambio de algoritmo o
maximizar Creator Rewards.

## Jerarquía de evidencia

1. TikTok Studio live de la cuenta.
2. API oficial del catálogo propio.
3. Creator Search Insights live.
4. TikTok Studio `Inspiration` y perfiles públicos de TikTok.
5. Fuentes oficiales de TikTok.
6. Estudios externos con metodología y muestra declaradas.
7. Foros o X, únicamente como señal anecdótica.

No usar YouTube, Google Trends ni archivos de autocomplete de origen
desconocido para concluir demanda dentro de TikTok.

## Auditoría obligatoria por video

Ejecutar:

```powershell
python scripts/channel_diagnostic.py `
  --catalog tiktok_own_videos.json `
  --csv tiktok_video_audit.csv `
  --summary tiktok_video_audit.json
```

El CSV debe conservar una fila por video. Comparar por edad, duración y cohorte;
no ordenar únicamente por views acumuladas.

La API pública no entrega retención, fuentes, espectadores nuevos,
visualizaciones relevantes, RPM ni ingresos. Completar esas columnas con
TikTok Studio antes de concluir por qué un video monetizó o dejó de hacerlo.

## Embudo de diagnóstico

Separar cuatro capas:

1. `DISTRIBUCIÓN`: views, FYP, nuevos espectadores y velocidad por edad.
2. `RESPUESTA`: average watch, porcentaje de duración visto, finish, shares,
   saves y follows.
3. `SEARCH`: porcentaje de tráfico, queries exactas y satisfacción de
   intención.
4. `DINERO`: views relevantes, RPM y reward.

No usar engagement como sinónimo de distribución o monetización.

### Matriz de decisión

| Señal | Lectura | Acción |
| --- | --- | --- |
| Views bajas + ER/share altos | gustó, pero no se expandió | reempaquetar el ángulo |
| FYP alto + retención baja | sí fue probado | acortar entrada y adelantar evidencia |
| Search bajo + queries distintas | promesa poco buscable | responder una consulta exacta |
| Secuela baja + buena respuesta | fricción de audiencia fría | relanzar subángulo autosuficiente |
| Views altas + share bajo | hit por exposición | validar retención antes de copiar |
| <1K views relevantes | no cruza piso económico | resolver escala/audiencia elegible |
| RPM bajo con volumen | menor valor económico | revisar play duration, search y originalidad |

## Gate para declarar cambio de algoritmo

No declarar que TikTok cambió el algoritmo por una caída semanal.

Exigir:

1. normalizar cantidad de publicaciones;
2. comparar videos de edad y duración semejantes;
3. revisar FYP, Search, nuevos espectadores y tráfico de perfil;
4. descartar inelegibilidad o restricciones;
5. observar al menos dos cohortes consecutivas;
6. contrastar con fuente oficial o estudio externo;
7. etiquetar foros/X como anecdóticos.

Usar `CAMBIO CONFIRMADO`, `CAMBIO PROBABLE`, `SIN EVIDENCIA` o
`DATOS INSUFICIENTES`.

## Competencia

Comparar solo dentro de TikTok:

- `Inspiration > Recommended > Similar posts`;
- `Similar creators`;
- resultados públicos para una consulta exacta;
- perfiles y videos comparables por fecha, formato e idioma.

No comparar solo los fijados o el mayor viral. Tomar también publicaciones
recientes y anotar varianza. Extraer:

```text
CUENTA:
FECHA:
SEGUIDORES:
PROMESA DEL PERFIL:
MUESTRA RECIENTE:
OUTLIERS:
GANCHO:
DURACIÓN:
EMOCIÓN:
PRUEBA:
SEARCH INTENT:
QUÉ IMITAR:
QUÉ NO IMITAR:
```

No copiar afirmaciones sensacionalistas o no verificadas aunque tengan millones
de views.

## Benchmarks internos vigentes

Catálogo: 469 videos, corte 2026-07-25.

- top 10%: al menos 85,225 views;
- share mediano viral: 0.418%;
- engagement mediano viral: 4.862%;
- resto: share 0.221%, engagement 3.842%;
- 180-359s en últimos 120 días: n=9, mediana 13,134 views y 77.8% por encima
  de 6,500 views;
- tratar este último dato como cohorte prometedora, no regla universal.

TikTok Studio, últimos siete días al corte:

- FYP: 75.5%;
- Search: 19.8%;
- perfil: 4.4%;
- siguiendo: 0.3%;
- views: 105.8K, -43.9%;
- publicaciones: una, frente a cinco en los siete días anteriores.

Conclusión vigente: no hay evidencia de penalización de cuenta. La caída
semanal coincide con 80% menos publicaciones.

### Comparación validada

| Video | Duración | Views | Avg watch | Completo | FYP | Search | Rewards |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Layne Staley | 2:39 | 936K | 37.22s | 5.2% | 96.3% | 0.9% | $190.7 |
| Soundgarden | 12:12 | 8,342 | 73.18s | 1.4% | 95.9% | 1.8% | $0.4 |

Soundgarden tuvo 8.28% de engagement y 0.425% de shares: buen contenido con
escala limitada, no fracaso creativo ni bloqueo de FYP.

## Tres gates de Creator Rewards

1. `ELEGIBILIDAD`: original, más de 60s y conforme a reglas.
2. `VOLUMEN`: alrededor de 6,500-9,000 views totales es el rango empírico para
   intentar cruzar 1,000 views relevantes en esta cuenta.
3. `VALOR`: RPM depende de play duration, search value, engagement,
   originalidad y valor comercial.

Cruzar volumen no garantiza pago ni RPM alto.

## Diseño de pruebas

Antes de afirmar una nueva regla, probar una cohorte de al menos 12 piezas:

- 6 narrativas autosuficientes de 90-240s;
- 3 respuestas a gaps CSI confirmados;
- 2 narrativas de 3-6 minutos;
- 1 video de 7-10 minutos que supere viral-fit.

Mantener estable voz, calidad y frecuencia. Variar una sola dimensión:
gancho, duración, ángulo o search intent. Medir 2h, 6h, 24h, 72h, 7d y 30d.

