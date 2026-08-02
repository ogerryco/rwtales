---
name: rockwise-visuals
description: >
  Skill 4 de 6 del pipeline Rockwise Tales. Genera prompts de imagen y video
  con IA (Flow Labs / Kling) para los bloques marcados como REQUIERE AI VISUAL
  en Skill 3. Cada prompt incluye imagen inicial, imagen final y movimiento.

license: MIT

metadata:
  raise.work_cycle: production
  raise.frequency: on-demand
  raise.fase: visuals
  raise.prerequisites: "rockwise-assets"
  raise.next: "rockwise-audio"
  raise.gate: ""
  raise.adaptable: "true"
  raise.version: "1.1.0"
---

# Rockwise Visuals

## Purpose

Generar prompts de IA para los bloques visuales sin footage real. Rai produce los prompts; el usuario los ejecuta manualmente en Flow Labs o Kling.

**Restriccion importante:** este skill no debe usarse para acelerar el sourcing. Solo se activa despues de que `rockwise-assets` documenta busqueda real suficiente y marca el beat como `[REQUIERE AI VISUAL]` con razon de descarte. IA es ultimo recurso o respiracion visual menor, no sustituto de archivo documental.

## Mastery Levels (ShuHaRi)

- **Shu**: Completar los 3 componentes del prompt (inicio, fin, movimiento)
- **Ha**: Ajustar la atmósfera al período histórico y al patrón emocional del video
- **Ri**: El movimiento de cámara refuerza la emoción del bloque narrativo

## Context

**When to use:** Solo para bloques marcados `[REQUIERE AI VISUAL]` en Skill 3.

**When to skip:** Si todos los bloques tienen footage real (raro pero posible).

**When to reject:** Si el bloque habla de un album, entrevista, documental, conflicto publico, performance o era con archivo probablemente existente y no hay asset log de busqueda fallida. En ese caso volver a `rockwise-assets`.

**Criterio para identificar bloques que GENUINAMENTE no pueden tener footage real** (no es solo "no lo encontré todavía"):
- Reuniones o negociaciones privadas (ej. una conciliación entre partes en disputa) — nunca hubo cámaras ahí
- Sesiones de estudio actuales/en curso, privadas (ej. una banda terminando grabaciones hoy) — no existe metraje público de trabajo en proceso
- Documentos legales o privados que se filtraron (ej. una lista de títulos en un documento de corte) — no hay "video" de eso, solo el hecho
Estos son candidatos naturales y honestos para IA, distinto de un bloque donde probablemente exista footage real y solo falta buscar mejor.

**Inputs:** Lista de bloques `[REQUIERE AI VISUAL]` con descripción del momento narrativo

**Inputs obligatorios adicionales:**
- frase exacta del guion;
- razon por la que no existe/conviene footage real;
- fuentes o queries descartadas;
- etiqueta de uso: `RECREACION`, `IA_ATMOSFERA` o `TRANSICION`;
- advertencia si la escena no debe parecer evidencia historica.

## Steps

### Step 1: Construir prompt de imagen inicial (Start Frame)

Antes del prompt, escribir una linea de control:

`USO: RECREACION/IA_ATMOSFERA/TRANSICION - no presentar como evidencia historica.`

Describir el primer fotograma en inglés:
- Composición (plano general, medio, close-up)
- Sujeto principal y su estado
- Iluminación y atmósfera
- Elementos de época (ropa, ambiente, color)

**Verification:** La descripción es específica, no genérica.

### Step 2: Construir prompt de imagen final (End Frame)

Describir cómo termina la escena:
- Cambio de posición, luz o composición
- Estado emocional al final del movimiento

**Verification:** Es distinto del inicio — hay transformación.

### Step 3: Construir prompt de movimiento

Describir cómo se mueve la cámara o los elementos entre inicio y fin:
- Pan (izquierda, derecha)
- Zoom (in, out)
- Dolly (hacia adelante, atrás)
- Fade (in, out)
- Shake o handheld para tensión

**Verification:** El movimiento refuerza la emoción del bloque.

### Step 4: Verificar coherencia con el período histórico

- ¿La ropa, el ambiente y la paleta de color corresponden a la época?
- ¿La atmósfera corresponde al patrón emocional (oscuro, triunfal, íntimo)?

**Verification:** Nada anacrónco. La imagen podría ser un fotograma real de la época.

## Output

```
VISUAL [N] — [descripción del momento narrativo]

PROMPT IMAGEN INICIAL:
[descripción detallada en inglés]

PROMPT IMAGEN FINAL:
[descripción detallada en inglés]

PROMPT DE MOVIMIENTO:
[descripción del movimiento en inglés]
```

> Todos los prompts en inglés. Flow Labs y Kling responden mejor en inglés.

## Estilo visual del canal RWT

- Estética: oscura, cinematográfica, granulada — rock 90s
- Paletas: desaturadas, altos contrastes, luz lateral o contraluz
- NO: imágenes brillantes, coloridas, hiperrealistas sin atmósfera
- Grano de película: añadir cuando sea posible para autenticidad

## Plataformas

- **Flow Labs** (Google): el usuario ejecuta con su sesión de Google — Rai NO puede conectarse directamente
- **Kling AI**: alternativa para movimientos complejos o escenas de acción

## Quality Checklist

- [ ] Existe asset log de `rockwise-assets` que justifica IA
- [ ] La escena no sustituye un album/entrevista/documental facilmente localizable
- [ ] La salida queda etiquetada como RECREACION, IA_ATMOSFERA o TRANSICION
- [ ] No se presenta como evidencia historica si es recreacion
- [ ] Los 3 componentes presentes en cada prompt (inicio, fin, movimiento)
- [ ] Todos los prompts en inglés
- [ ] Atmósfera coherente con el período histórico
- [ ] Movimiento refuerza la emoción del bloque
- [ ] Journal add ejecutado antes de pasar al Skill 5

## References

- Previous: `/rockwise-assets`
- Next: `/rockwise-audio`
