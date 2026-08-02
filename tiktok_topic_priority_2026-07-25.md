# TikTok Topic Priority — corrección de fuente

Fecha: 2026-07-25  
Cuenta: @rockwisetales

El ranking anterior fue retirado porque usaba `rwt_keyword_trends.json` sin
confirmar que sus sugerencias provinieran exclusivamente de TikTok. Por lo
tanto, no existe en este archivo una prioridad válida entre Héroes del
Silencio, Dolores O'Riordan, Lynyrd Skynyrd, Ozzy Osbourne, David Bowie u otros
artistas.

## Lo confirmado

- El catálogo propio contiene 469 videos obtenidos mediante la API de TikTok.
- TikTok Studio muestra recomendaciones y publicaciones similares, pero esas
  views no equivalen a volumen de búsqueda.
- Creator Search Insights debe capturarse en vivo y filtrarse semánticamente.
- `soundgarden` y `secretos del rock` produjeron falsos positivos en CSI.
- No debe asignarse un `Topic Priority Score` sin demanda CSI válida o un proxy
  TikTok claramente identificado.

## Estado actual

No hay un ranking de temas “más buscados” suficientemente sustentado.

Para el diagnóstico vigente del canal, patrones, competencia, gaps,
distribución y monetización, usar:

`tiktok_growth_monetization_analysis_2026-07-25.md`

Para cada futura prioridad temática:

1. capturar consulta, pestaña, filtro, fecha, región e idioma;
2. eliminar falsos positivos;
3. confirmar intención musical;
4. cruzar cobertura propia;
5. comparar resultados reales dentro de TikTok;
6. puntuar solo después de validar la demanda.
