import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const projectDir = process.argv[2];

if (!projectDir) {
  throw new Error("Uso: node build_youtube_short.mjs <carpeta-del-proyecto>");
}

if (path.basename(projectDir) !== "Prueba Cornell TT Largo") {
  throw new Error(`Proyecto inesperado: ${projectDir}`);
}

const contentPath = path.join(projectDir, "draft_content.json");
const templatePath = path.join(projectDir, "template-2.tmp");
const metaPath = path.join(projectDir, "draft_meta_info.json");

const draft = JSON.parse(fs.readFileSync(contentPath, "utf8"));
const meta = JSON.parse(fs.readFileSync(metaPath, "utf8"));

const expectedOriginalDuration = 732_966_666;
if (draft.duration !== expectedOriginalDuration || meta.tm_duration !== expectedOriginalDuration) {
  throw new Error(
    `El proyecto no está en su estado largo esperado: content=${draft.duration}, meta=${meta.tm_duration}`,
  );
}

if (!Array.isArray(draft.tracks) || draft.tracks.length !== 12) {
  throw new Error(`Estructura de pistas inesperada: ${draft.tracks?.length}`);
}

// Orden narrativo del tráiler:
// 1) cifra y doble rechazo; 2) conflicto; 3) canciones retenidas; 4) remate.
const ranges = [
  { start: 360_500_000, end: 372_566_666, label: "doble rechazo de 21 millones" },
  { start: 35_200_000, end: 61_033_333, label: "siete canciones y conflicto" },
  { start: 388_533_333, end: 398_900_000, label: "canciones retenidas" },
  { start: 404_500_000, end: 413_366_666, label: "no como música, como prueba" },
];

const clone = (value) => structuredClone(value);
const uuid = () => crypto.randomUUID().toUpperCase();

function interpolateValues(left, right, ratio) {
  return left.map((value, index) => value + (right[index] - value) * ratio);
}

function valueAt(keyframes, time) {
  if (time <= keyframes[0].time_offset) return clone(keyframes[0].values);
  if (time >= keyframes.at(-1).time_offset) return clone(keyframes.at(-1).values);

  for (let index = 1; index < keyframes.length; index += 1) {
    const right = keyframes[index];
    const left = keyframes[index - 1];
    if (time <= right.time_offset) {
      const span = right.time_offset - left.time_offset;
      const ratio = span === 0 ? 0 : (time - left.time_offset) / span;
      return interpolateValues(left.values, right.values, ratio);
    }
  }

  return clone(keyframes.at(-1).values);
}

function boundaryKeyframe(template, timeOffset, values) {
  const result = clone(template);
  result.id = uuid();
  result.time_offset = timeOffset;
  result.values = values;
  return result;
}

function trimCommonKeyframes(commonKeyframes, offsetStart, duration) {
  if (!Array.isArray(commonKeyframes) || commonKeyframes.length === 0) return commonKeyframes;
  if (offsetStart === 0 && duration === null) return commonKeyframes;

  return commonKeyframes.map((property) => {
    const trimmedProperty = clone(property);
    const sourceKeys = [...property.keyframe_list].sort(
      (left, right) => left.time_offset - right.time_offset,
    );

    if (sourceKeys.length === 0) return trimmedProperty;

    if (sourceKeys.length === 1) {
      const only = clone(sourceKeys[0]);
      only.time_offset = 0;
      trimmedProperty.keyframe_list = [only];
      return trimmedProperty;
    }

    const offsetEnd = offsetStart + duration;
    const first = boundaryKeyframe(sourceKeys[0], 0, valueAt(sourceKeys, offsetStart));
    const middle = sourceKeys
      .filter((keyframe) => keyframe.time_offset > offsetStart && keyframe.time_offset < offsetEnd)
      .map((keyframe) => {
        const adjusted = clone(keyframe);
        adjusted.time_offset -= offsetStart;
        return adjusted;
      });
    const last = boundaryKeyframe(
      sourceKeys.at(-1),
      duration,
      valueAt(sourceKeys, offsetEnd),
    );

    trimmedProperty.keyframe_list = [first, ...middle, last];
    return trimmedProperty;
  });
}

let outputCursor = 0;
const mappedRanges = ranges.map((range) => {
  const mapped = {
    ...range,
    outputStart: outputCursor,
    duration: range.end - range.start,
  };
  outputCursor += mapped.duration;
  return mapped;
});
const newDuration = outputCursor;

const selectedByTrack = [];

draft.tracks.forEach((track, trackIndex) => {
  const outputSegments = [];
  const usedOriginalIds = new Set();

  for (const range of mappedRanges) {
    for (const original of track.segments) {
      const originalStart = original.target_timerange.start;
      const originalEnd = originalStart + original.target_timerange.duration;
      const intersectionStart = Math.max(originalStart, range.start);
      const intersectionEnd = Math.min(originalEnd, range.end);

      if (intersectionStart >= intersectionEnd) continue;

      const intersectionDuration = intersectionEnd - intersectionStart;
      const offsetStart = intersectionStart - originalStart;
      const segment = clone(original);

      if (usedOriginalIds.has(original.id)) {
        segment.id = uuid();
      } else {
        usedOriginalIds.add(original.id);
      }

      segment.target_timerange.start =
        range.outputStart + (intersectionStart - range.start);
      segment.target_timerange.duration = intersectionDuration;

      if (segment.source_timerange) {
        const ratio =
          original.source_timerange.duration / original.target_timerange.duration;
        const sourceOffset = original.reverse
          ? originalEnd - intersectionEnd
          : offsetStart;
        segment.source_timerange.start =
          original.source_timerange.start + Math.round(sourceOffset * ratio);
        segment.source_timerange.duration = Math.round(intersectionDuration * ratio);
      }

      const wasClipped =
        offsetStart !== 0 || intersectionDuration !== original.target_timerange.duration;
      if (wasClipped && Array.isArray(segment.common_keyframes)) {
        segment.common_keyframes = trimCommonKeyframes(
          segment.common_keyframes,
          offsetStart,
          intersectionDuration,
        );
      }

      outputSegments.push(segment);
    }
  }

  outputSegments.sort(
    (left, right) => left.target_timerange.start - right.target_timerange.start,
  );
  track.segments = outputSegments;
  selectedByTrack.push({
    track: trackIndex,
    type: track.type,
    segments: outputSegments.length,
  });
});

// CTA final, en una pista de texto que quedó libre tras el recorte.
const ctaText = "¿POR QUÉ DIJERON QUE NO?\nVIDEO COMPLETO VINCULADO";
const ctaDuration = 2_000_000;
const ctaStart = newDuration - ctaDuration;
const textTrack = draft.tracks[2];
const originalTextSegment = JSON.parse(
  fs.readFileSync(contentPath, "utf8"),
).tracks[2].segments[0];
const originalTextMaterial = draft.materials.texts.find(
  (material) => material.id === originalTextSegment.material_id,
);

if (!originalTextMaterial) {
  throw new Error("No se encontró el material base para el CTA.");
}

const ctaMaterial = clone(originalTextMaterial);
ctaMaterial.id = uuid();
ctaMaterial.name = "CTA YOUTUBE SHORT";
ctaMaterial.recognize_text = ctaText;
ctaMaterial.group_id = "cornell-youtube-short-cta";
ctaMaterial.words = { start_time: [], end_time: [], text: [] };
ctaMaterial.current_words = { start_time: [], end_time: [], text: [] };

const ctaContent = JSON.parse(ctaMaterial.content);
ctaContent.text = ctaText;
if (ctaContent.styles?.[0]) {
  ctaContent.styles[0].range = [0, ctaText.length];
  ctaContent.styles[0].size = 13;
}
ctaMaterial.content = JSON.stringify(ctaContent);
ctaMaterial.font_size = 13;

const ctaSegment = clone(originalTextSegment);
ctaSegment.id = uuid();
ctaSegment.material_id = ctaMaterial.id;
ctaSegment.target_timerange = { start: ctaStart, duration: ctaDuration };
ctaSegment.clip.scale = { x: 1.0, y: 1.0 };
ctaSegment.clip.transform = { x: 0.0, y: 0.55 };
ctaSegment.render_index = 20_000;
ctaSegment.common_keyframes = [];
ctaSegment.keyframe_refs = [];
textTrack.segments.push(ctaSegment);
textTrack.segments.sort(
  (left, right) => left.target_timerange.start - right.target_timerange.start,
);
draft.materials.texts.push(ctaMaterial);

draft.duration = newDuration;
draft.update_time = Date.now() * 1000;
meta.tm_duration = newDuration;
meta.tm_draft_modified = Date.now() * 1000;

const serializedDraft = JSON.stringify(draft);
const serializedMeta = JSON.stringify(meta);

// Validación estructural antes de reemplazar los archivos activos.
const reparsed = JSON.parse(serializedDraft);
if (reparsed.duration !== 57_133_332) {
  throw new Error(`Duración final inesperada: ${reparsed.duration}`);
}
if (reparsed.tracks[0].segments.length === 0 || reparsed.tracks[5].segments.length === 0) {
  throw new Error("El Short quedó sin video principal o sin narración.");
}
for (const track of reparsed.tracks) {
  for (const segment of track.segments) {
    const end = segment.target_timerange.start + segment.target_timerange.duration;
    if (segment.target_timerange.start < 0 || end > reparsed.duration) {
      throw new Error(`Segmento fuera de rango: ${segment.id}`);
    }
  }
}

fs.writeFileSync(contentPath, serializedDraft, "utf8");
fs.writeFileSync(templatePath, serializedDraft, "utf8");
fs.writeFileSync(metaPath, serializedMeta, "utf8");

console.log(
  JSON.stringify(
    {
      projectDir,
      duration: newDuration,
      durationSeconds: newDuration / 1_000_000,
      ranges: mappedRanges,
      selectedByTrack,
      cta: { start: ctaStart, duration: ctaDuration, text: ctaText },
    },
    null,
    2,
  ),
);
