# Contexto de Sesión — Videos RWT
## Fecha: 2026-06-03 | PC → continuar en Mac

---

## Estado actual

### Videos en producción
1. **Canciones Malditas del Rock** — SHORT → lanzar **jueves tarde-noche**
2. **Shannon Hoon (Blind Melon)** — SHORT → lanzar **sábado**

Layne Staley → reservado para video LONG la semana siguiente (ya hay un SHORT previo que funcionó bien).

### Lo que está completo
- [x] Research brief con hechos verificados y fuentes
- [x] Script con marcadores de tono ElevenLabs
- [x] Shot list con clips mapeados a narración
- [x] Lista de clips a descargar con URLs de YouTube

### Lo que falta
- [ ] Generar audios en ElevenLabs (pegar script directamente)
- [ ] Descargar clips de YouTube (usar yt-dlp)
- [ ] Editar en laptop durante viaje

---

## Configuración ElevenLabs
- Voz: masculina profunda
- Stability: 55%
- Similarity: 75%
- Style: 30%

---

## Decisiones tomadas esta sesión

### Scouting
- Se hizo demand-fit analysis con YouTube Data API (20 keywords, resultados en `rwt_demand_fit_results.json`)
- Se hizo análisis de saturación profundo de "Club de los 27" → **SATURADO** (29 videos 2024+, 15 con >50K views, competidor más reciente 3.5M views a 46K views/día)
- Trending keywords extraídas vía autocomplete: `layne staley muerte`, `shannon hoon muerte`, `canciones malditas en español`, `historias del rock korn/megadeth` son las señales más fuertes

### Estrategia de lanzamiento
- Jueves tarde-noche → calienta overnight → revienta viernes
- Sábado → el fin de semana la gente tiene tiempo para historia profunda → revienta domingo
- Canciones Malditas va jueves: Metallica + Ozzy = nombres que cualquiera reconoce, genera comentarios rápidos
- Shannon Hoon va sábado: historia más profunda y emocional, mejor para fin de semana

---

## Archivos de datos generados
- `rwt_demand_fit_results.json` — análisis demand-fit 20 keywords
- `rwt_deep_scout.json` — saturación Club 27 + trending autocomplete
- `scratch/rwt_demand_fit.py` — script reutilizable para análisis futuro
- `scratch/rwt_deep_scout.py` — script reutilizable para scouting profundo

---

## Próximos videos (backlog)
- **Layne Staley** — LONG documental (semana siguiente al viaje)
- **Dimebag Darrell** — descartado por saturación reciente (video de enero 2025 con tracción)
- **Canciones prohibidas en tiendas de guitarra** — señal activa en autocomplete, muy poca cobertura en español, buen candidato para después del viaje
