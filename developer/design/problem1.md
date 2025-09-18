# Problem 1

Make auto-generated MID fields deterministic based on node content (e.g., TITLE or UID, and STATEMENT)

## Current behavior

MID auto-generation uses random values (opaque, non-deterministic) with the python built-in uuid.uuid4().hex

## Proposed changes

### MID generation function

Replace or supplement random MID generation with a deterministic hash-based method.
Might consider using uuid.uuid5() with inputs from at least the node.statement, and probably the uid and title if either exists.

### Configuration option

Introduce a config flag in OPTIONS section of the document.

Pipeline logic: if deterministic mode is enabled, use deterministic hash-based generation; else, fallback to python's built-in random uuid with uuid.uuid4().

### Backwards compatibility implications

If content changes, the MID will change. Document this behavior clearly.

Only compute MID (deterministic or otherwise) when node did not already have a MID.

### Tests

Write tests:
1. two identical nodes produce same MID
2. differing content yields different MID
3. options flag to disable deterministic MID results in a random MID field value
