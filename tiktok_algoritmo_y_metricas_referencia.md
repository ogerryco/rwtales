# TikTok: algoritmo, métricas y Creator Rewards — referencia de trabajo

Investigación 2026-07-22 para entender a fondo cómo funciona la plataforma detrás de los números que vemos en `tiktok_channel_analysis.md`. Separado por nivel de confianza: **[OFICIAL]** viene de TikTok directamente (Transparency Center, Creator Academy, Legal/Terms, Support); **[NO OFICIAL]** es interpretación de terceros (blogs de marketing, guías de 2026) — útil pero no verificado por TikTok, se marca explícitamente para no confundirlo con hechos confirmados.

## 1. Cómo funciona el algoritmo del "Para ti" (FYP)

**[OFICIAL — TikTok Transparency Center]**
- El sistema de recomendación usa modelos de machine learning en varios pasos: primero recupera un conjunto grande de videos que ya pasaron moderación de contenido, luego los clasifica por relevancia a tus intereses.
- Antes de rankear, TikTok analiza la pista de audio (incluyendo transcripción automática de voz), el texto en pantalla, la descripción, los hashtags, el sonido usado, y el contenido visual de los frames — esto decide contra qué "clusters de interés" se prueba un video.
- Señales de ranking confirmadas: likes, shares, saves, comentarios, y **tiempo de reproducción (watch time)** — TikTok dice textualmente: *"un indicador fuerte de interés, como terminar de ver un video largo de principio a fin, recibe más peso que un indicador débil."*
- El sistema predice la probabilidad de que interactúes con un video (like, share, comentario, o skip) y combina esas predicciones en un puntaje general.

**[NO OFICIAL, pero ampliamente reportado — cambio de 2026]**
- **Cambio clave de 2026: los videos nuevos se muestran primero a tus propios seguidores, no al público general.** TikTok usa a tus seguidores como "audiencia de prueba" durante las primeras horas — evalúa tasa de finalización, shares y saves entre ellos antes de decidir si expande el video a no-seguidores. Si los seguidores responden fuerte, el video se empuja a audiencias cada vez más grandes de no-seguidores. Si no responden, el video se queda encerrado dentro de tu propia base y no crece más.
- Compartidos y guardados ("saves") pesan más que los likes desde una actualización de 2025.
- Se reporta que el umbral de tasa de finalización para "volverse viral" subió a ~70% (contra ~50% en 2024) — dato de fuentes no oficiales, tomar con cautela.

**Por qué esto importa para tu canal — conecta directo con lo que medimos en la sección 12 de `tiktok_channel_analysis.md`:** todas las partes de la serie de Weiland tuvieron 94-98% de "espectadores recurrentes" (tu propia audiencia ya fiel) — es exactamente la señal de que esos videos **nunca superaron la prueba con seguidores** lo suficiente para que TikTok los empujara a audiencia nueva. Frusciante Parte 1, en cambio, tuvo 42% de espectadores nuevos — señal de que sí rompió esa barrera y fue empujado ampliamente. Esto explica el mecanismo *detrás* del umbral de 1,000 vistas relevantes que encontramos: sin expansión a no-seguidores, nunca se acumula suficiente volumen bruto como para cruzar ese piso.

## 2. Creator Rewards Program — reglas oficiales completas

**[OFICIAL — TikTok Creator Academy / Legal Terms]**

Elegibilidad de cuenta:
- 10,000+ seguidores
- 100,000+ vistas en los últimos 30 días
- 18+ años (19 en Corea del Sur)
- Cuenta personal (no Business), en buen estado, sin historial de violaciones
- Cuenta registrada en un país elegible

**Países elegibles confirmados:** Estados Unidos, Reino Unido, Alemania, Japón, Corea del Sur, Francia, **México** y **Brasil**. (Esto confirma exactamente lo que encontramos empíricamente en la sección 12 — el "91-94% México + 4-6% EEUU + 1-2% Brasil" de las vistas relevantes de tus videos corresponde 1:1 a esta lista oficial.)

Requisitos por video:
- Contenido original, filmado/diseñado/producido enteramente por el creador
- Duración mínima de **60 segundos**
- Publicado *después* de unirse al programa
- **Al menos 1,000 vistas calificadas del feed "Para ti"** — esto es el piso duro que confirmamos en TikTok Studio con las 5 partes de Weiland ("Menos de 1000" = sin cálculo de recompensa)
- Cada vista calificada debe durar **más de 5 segundos** para contar
- **NO debe estar vinculado a un "Series" de TikTok** (la función de contenido de pago/suscripción de TikTok) — esto es distinto de simplemente titular tus videos "Parte 1, 2, 3..."; el "Series" oficial de TikTok es un producto de suscripción de pago separado. Tus partes de Weiland/Frusciante/Linkin Park NO usan esa función, así que no aplica esta exclusión — puedes descartar por completo la hipótesis de "descalificación" que investigamos antes.
- No debe incluir publicidad, desinformación, contenido patrocinado o promociones pagadas

Aplicación y pago: respuesta en ~3 días tras aplicar; se requiere completar información fiscal antes de recibir pagos.

## 3. Qué significan las métricas que ves en TikTok Studio

**[OFICIAL, con matices de interpretación]**

- **Fuentes de tráfico:** de dónde vino cada vista — "Para ti" (descubrimiento algorítmico), "Perfil personal" (alguien fue directo a tu perfil, normalmente audiencia ya existente), "Siguiendo", "Buscar", "Sonido". Un video con % alto de "Perfil personal" suele ser señal de que la mayoría son fans ya existentes revisitando, no descubrimiento nuevo.
- **Espectadores nuevos vs. recurrentes:** % de gente que nunca había visto tu contenido vs. gente que ya te conocía. Es la métrica más directa para saber si un video rompió la barrera de "solo llegó a mis seguidores" — la confirmamos como predictor fuerte de monetización en la sección 12.
- **Tasa de retención / "dejaron de ver tras X segundos":** el punto donde ocurre la mayor caída de audiencia. En nuestro dataset esto resultó ser casi idéntico en todos los videos de una misma serie (caída en 1-2 segundos) — no fue una variable que explicara diferencias de pago, aunque sigue siendo relevante para el algoritmo en general.
- **"Visualizaciones relevantes" (Cálculo de recompensas):** la métrica clave para dinero — vistas que cumplen los 3 filtros oficiales a la vez: (1) del feed "Para ti", (2) de un país elegible (México/EEUU/Brasil para tu caso), (3) duración de vista mayor a 5 segundos. Es un subconjunto mucho más chico que las vistas totales (en tu canal, ronda 11-18% del total).
- **"Calidad del contenido" / "Valor comercial" (Buena/Excelente):** son etiquetas propias de TikTok Studio, poco documentadas públicamente — no encontré una definición oficial exacta de sus umbrales. Empíricamente, en tu canal aparecieron "Excelente"/"Buena" en todos los videos que sí llegaron a tener datos suficientes para calcular RPM (nunca las vimos en los videos con "Menos de 1000" vistas relevantes, que ni siquiera llegan a mostrar la etiqueta) — así que no está claro si es una señal *causal* de mejor pago o simplemente aparece una vez que hay suficiente data para evaluar. Tratarla como referencia, no como verdad absoluta (la misma pantalla de TikTok lo advierte: *"esta valoración es solo de referencia, la precisión puede variar"*).

## 4. Video de larga duración — postura oficial de TikTok

**[OFICIAL — TikTok Creator Academy]**
- TikTok permite subir videos pregrabados de hasta 60 minutos (10 minutos si se grava directo en la app).
- Cita textual: *"un video de dos minutos que mantiene a alguien viendo acumula mucho más tiempo total de reproducción que un clip de 30 segundos, y parece ser ese tiempo acumulado — no la tasa de finalización — lo que se recompensa con más alcance."* Esto valida directamente lo que encontramos con Frusciante Parte 1: no necesitas 70%+ de finalización, necesitas volumen absoluto de minutos vistos.
- TikTok explícitamente dice que los videos largos (1min+) existen para "no tener que partir tu historia en varias partes" — es decir, la plataforma misma sugiere que fragmentar en series es una solución de compromiso, no la recomendación por defecto.

## 5. Síntesis: el modelo completo, de principio a fin

1. Publicas un video → TikTok lo prueba primero con tus **seguidores existentes** (cambio de 2026).
2. Si tus seguidores lo completan/comparten/guardan con fuerza en las primeras horas → TikTok lo expande a **no-seguidores** progresivamente (esto es lo que separó a Frusciante Parte 1 del resto de las partes de Weiland).
3. Esa expansión determina el **volumen total de vistas** que el video termina acumulando.
4. De ese volumen total, solo cuenta para dinero la fracción que es (a) desde "Para ti", (b) de México/EEUU/Brasil, y (c) vista más de 5 segundos — las **"vistas relevantes."**
5. Si las vistas relevantes no llegan a **1,000**, el video no genera ni un centavo, sin importar qué tan bueno sea. Si las superan, el pago escala con el volumen de vistas relevantes × un RPM que en tu canal ronda $0.5-0.9 por cada 1,000.

**La palanca real, entonces, no es ajustar el guion video por video — es lo que pasa en las primeras horas con tus propios seguidores.** Si el gancho no los detiene de inmediato, el video nunca sale de tu propia base y nunca cruza el piso de las 1,000 vistas relevantes.

## Fuentes

- [Introduction to the TikTok recommendation system — TikTok Transparency Center](https://www.tiktok.com/transparency/en/recommendation-system)
- [Join the TikTok Creator Rewards Program — TikTok Creator Academy](https://www.tiktok.com/creator-academy/article/creator-rewards-program)
- [Creator Rewards Program: How to Qualify and Enroll — TikTok Creator Academy](https://www.tiktok.com/creator-academy/article/eligibility)
- [Creator Rewards Program Terms — TikTok Legal](https://www.tiktok.com/legal/page/global/creator-rewards-program-us/en)
- [TikTok Support — Creator Rewards Program](https://support.tiktok.com/en/business-and-creator/creator-rewards-program/creator-rewards-program)
- [Longer video content strategy — TikTok Creator Academy](https://www.tiktok.com/creator-academy/en/article/longer-video-content-strategy)
- [Acerca del estándar de calidad de TikTok para contenido comercial — TikTok Ads Help](https://ads.tiktok.com/help/article/about-tiktoks-content-quality-standard-for-creator-commercial-content?lang=es)
- Cambio de "follower-first" 2026: reportado por múltiples fuentes no oficiales de marketing (SyncStudio, Mickyweis, Opus.pro) — consistente entre ellas pero sin confirmación textual directa de TikTok Newsroom encontrada; tratar como razonablemente confiable pero no 100% oficial.
