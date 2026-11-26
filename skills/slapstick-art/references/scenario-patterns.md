# Scenario Patterns

## Cache-Aside Read Path

Use this for Redis performance scenes.

- The request comes in from the left or foreground.
- Tango shows the app or request path.
- Nib can act as the fast cache helper.
- Redis is the quick middle layer.
- The database is a larger, slower object in the background.
- On a cache hit, show the database sleeping or staying untouched.
- On a cache miss, show the database being consulted once, then the cache being filled.
- Avoid a simple Tom-and-Jerry chase layout; use a systems metaphor with clear action instead.

## Before and After

Use this when the user wants a direct contrast.

- Left side: direct database hit, slow and heavy.
- Right side: Redis hit, fast and light.
- Make the difference obvious with expression and motion.

## Comparison

Use this when the user wants two paths or two strategies.

- One side shows the expensive path.
- The other side shows the cached path.
- Keep the same framing so the contrast is easy to read.

## Reaction Beat

Use this when the point is surprise or speed.

- One character expects a slow database wait.
- The other character appears with the answer immediately.
- End with a clear aha moment.
