# Prompt Template

Use this as the base prompt for image generation.

```text
Generate one original 16:9 cartoon illustration.

Visual DNA:
Hand-drawn slapstick cartoon energy with slightly wobbly black line art.
Clean, readable composition. Simple shapes. Expressive poses.
Not Tom and Jerry, not Disney, not anime, not photorealistic.

Characters:
Tango, a blue-charcoal cat with an angular body, one nicked ear, a longer muzzle, and big paws.
Nib, a small mouse with a triangular head, asymmetrical ears, quick hands, and a compact body.
They must feel original and franchise-safe.

Scene:
{core idea or technical scenario}

Composition:
{where the characters are, what action is happening, and what the viewer should notice first}

Text:
Use at most 3 to 6 short handwritten labels if they help the explanation.

Constraints:
One clear idea only.
Keep Tango and Nib active, not decorative.
No crowded background.
No copied franchise poses or expressions.
No classic cat-and-mouse chase framing on a blank white stage.
No red scarf, white gloves, or other recognizable slapstick franchise signals.
Make the scenario readable in a few seconds.
```

## Redis Version

For Redis scenes, fill the core idea like this:

```text
Show a cache-aside read path: the request checks Redis first, gets a fast hit, and skips the database; if the cache misses, the database fills Redis once and future reads stay fast.
```
