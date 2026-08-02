---
name: rockwise-qa-audit
description: >
  Verificación factual independiente (QA Expert + Auditor) de cualquier
  guion del pipeline Rockwise Tales (LONG o SHORT) antes de pasar a assets.
  Corre dos agentes separados que re-verifican cada dato contra fuentes
  reales — nunca confían ciegamente en el Fact Sheet previo. Gate
  obligatorio: ningún guion pasa a producción sin las 2 verificaciones limpias.

license: MIT

metadata:
  raise.work_cycle: production
  raise.frequency: on-demand
  raise.fase: qa-audit
  raise.prerequisites: "rockwise-script,rockwise-script-short"
  raise.next: "rockwise-assets"
  raise.gate: "true"
  raise.adaptable: "true"
  raise.version: "1.0.0"
---

# Rockwise QA Audit

## Purpose

Verificación factual independiente de un guion terminado (LONG o SHORT)
antes de pasar a producción de assets. Dos roles separados, con
instrucciones independientes entre sí, para que uno no herede los puntos
ciegos del otro:

- **QA Expert**: re-verifica cada afirmación factual del guion línea por
  línea contra fuentes reales — no contra el Fact Sheet (que pudo tener un
  error de origen), sino contra la web actual.
- **Auditor**: revisión adversarial — busca activamente ambigüedades,
  fechas/nombres que se prestan a confusión (ej. "Rolling Stone" revista
  vs. banda), datos que suenan a suposición o generalidad no verificada, y
  cualquier frase que un espectador melómano pudiera cuestionar en comentarios.

> "El canal tiene una audiencia melómana de más de 80,000 seguidores. Un
> solo dato mal verificado en un short puede dañar la credibilidad de todo
> el canal — no hay margen de error."

## Mastery Levels (ShuHaRi)

- **Shu**: Ejecutar las 2 verificaciones completas, documentar cada hallazgo
- **Ha**: Priorizar qué afirmaciones son de mayor riesgo (nombres propios, fechas, causalidad) sobre las de bajo riesgo (adjetivos, transiciones)
- **Ri**: Detectar patrones recurrentes de error entre guiones y retroalimentar a `/rockwise-research` o `/rockwise-script-short` para prevenir la próxima vez

## Context

**When to use:** Después de que un guion (LONG o SHORT) está escrito y antes de pasar a `/rockwise-assets`. Obligatorio para todo guion que se vaya a publicar.

**When to skip:** Nunca — es un gate, no un paso opcional. Sí se puede omitir una re-verificación completa si el guion no cambió desde la última auditoría limpia.

**Inputs:**
- Guion completo (texto final, tal como se va a grabar)
- Fact Sheet del Skill 1 (para contraste, no como única fuente de verdad)

## Steps

### Step 1: Lanzar QA Expert (independiente)

Un agente separado recibe SOLO el guion (no el Fact Sheet, no el reporte
del Auditor) y re-verifica cada afirmación factual contra fuentes reales
vía búsqueda web — mínimo 2 fuentes por afirmación revisada, priorizando
fuentes primarias sobre wikis derivadas. Reporta, por afirmación:
- CONFIRMADA (con fuente)
- NO VERIFICABLE (sin fuente suficiente)
- INCORRECTA (contradicha por fuentes)

**Verification:** Cada afirmación factual del guion tiene un veredicto explícito.

### Step 2: Lanzar Auditor (independiente, adversarial)

Un segundo agente, separado del QA Expert y sin ver su reporte, recibe el
guion con instrucción de buscar activamente motivos de queja de un
espectador melómano exigente: ambigüedades de nombres, generalizaciones sin
fuente, fechas que podrían estar mal, tono que suene a afirmación cuando en
realidad es especulación. No corrige — solo señala.

**Verification:** Reporte de Auditor entregado sin haber visto el reporte del QA Expert.

### Step 3: Reconciliar hallazgos

Comparar ambos reportes. Cualquier afirmación marcada como INCORRECTA o
NO VERIFICABLE por cualquiera de los dos se corrige o se elimina del guion
— nunca se publica con el beneficio de la duda.

**Verification:** Cero afirmaciones sin resolver antes de aprobar el guion.

### Step 4: Aprobar y continuar

Guion aprobado solo si QA Expert y Auditor no tienen pendientes abiertos.

**Verification:** Ambos reportes limpios antes de pasar a `/rockwise-assets`.

## Output

| Item | Destino |
|------|---------|
| Reporte QA Expert | Journal de sesión |
| Reporte Auditor | Journal de sesión |
| Guion corregido (si aplica) | Reemplaza versión anterior antes de `/rockwise-assets` |

## Quality Checklist

- [ ] QA Expert y Auditor corrieron de forma independiente (uno no vio el reporte del otro antes de terminar)
- [ ] Cada afirmación factual del guion tiene veredicto explícito
- [ ] Toda afirmación NO VERIFICABLE o INCORRECTA fue corregida o eliminada
- [ ] Ambigüedades de nombres (ej. revista vs. banda) resueltas
- [ ] Journal add ejecutado con ambos reportes antes de pasar a `/rockwise-assets`

## References

- Previous: `/rockwise-script` o `/rockwise-script-short`
- Next: `/rockwise-assets`
