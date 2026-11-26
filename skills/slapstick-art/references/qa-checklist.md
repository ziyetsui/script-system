# QA Checklist

## Must Pass

- Is the image 16:9.
- Is the scene built around Tango and Nib.
- Do the characters feel original and not like Tom and Jerry.
- Is one clear idea visible at a glance.
- Do the characters actively drive the explanation.
- Is the composition readable in 3 to 5 seconds.
- Are any labels short and legible.
- Is the background simple enough to support the action.
- Does the Redis scenario clearly show why the cache is useful instead of hitting the database directly.
- Would a casual viewer mistake the duo for Tom and Jerry at first glance? If yes, fail.

## Fail Fast Signals

- The image looks like a copy of a known franchise.
- The characters are just standing there.
- The scene has too many props or labels.
- The database and cache roles are unclear.
- The layout feels like a generic slide or formal diagram.
- The text is too long to read quickly.

## Fixes

- Too generic: make one character do the key action.
- Too busy: remove extra props and labels.
- Too close to Tom and Jerry: change silhouette, pose, and facial design.
- Redis point unclear: show a direct cache hit and a quiet database in the same frame.
