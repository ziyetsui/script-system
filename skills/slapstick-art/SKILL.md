---
name: slapstick-art
description: Generate original cat-and-mouse slapstick illustrations and Redis/cache explainer scenes with a vintage cartoon feel. Use when creating 16:9 artwork, concept art, or technical scenario visuals featuring two original rival characters (not Tom and Jerry), especially cache-aside, before-after, or comparison scenes.
---

# Slapstick Art

## Overview

Create one original 16:9 illustration built around an original cat-and-mouse duo. The image should explain one idea through motion, expression, and a clear visual metaphor, not a dense diagram.

## Characters

- **Tango** - a blue-charcoal cat with an angular body, one nicked ear, a longer muzzle, expressive brows, and oversized paws. He is clever, a little clumsy, and good at carrying the action.
- **Nib** - a small mouse with a triangular head, asymmetrical ears, quick hands, and sharp eyes. He is nimble, mischievous, and good at revealing the trick or shortcut.

Keep them original. They should feel like a fresh slapstick duo with classic cartoon energy, but not a copy of Tom and Jerry or any other franchise. Do not reuse franchise-specific silhouettes, costumes, poses, or signature gags.
Do not use the classic blue-gray cat plus tiny mouse face-off framing, red neck scarves, or white gloves.

## Visual Rules

- Use bold, readable silhouettes and a clean scene hierarchy.
- Keep the duo active. One character must do the key action; the other must react, block, reveal, or carry the explanation.
- Prefer one main prop, one main flow, and at most a few short labels.
- Use a clean background unless the concept needs a simple object or system backdrop.
- If the scene is technical, make the idea visible as a physical system instead of hiding it in text.

## Redis Scenario

For Redis or caching topics, default to a cache-aside story:

- A request arrives.
- Redis answers fast on a hit.
- The database stays quiet on the hit path.
- On a miss, the database fills Redis.
- Updates show invalidate or refresh, not repeated polling.

## Workflow

1. Extract one core idea.
2. Pick one composition from `references/scenario-patterns.md`.
3. Write the prompt with `references/prompt-template.md`.
4. Generate one image with the built-in image tool.
5. Check the result against `references/qa-checklist.md`.
6. Regenerate with one narrow fix if the scene is crowded, unclear, or too close to a franchise look.

## Keep In Mind

- The art should read in 3 to 5 seconds.
- The duo should look original and not franchise-specific.
- Do not overload the canvas with labels, arrows, or extra characters.
- Use `assets/` for final deliverables or example renders.

## References

- `references/characters.md`
- `references/style-dna.md`
- `references/scenario-patterns.md`
- `references/prompt-template.md`
- `references/qa-checklist.md`
