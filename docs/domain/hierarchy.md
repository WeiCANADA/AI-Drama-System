# Domain Hierarchy

## Initial Production Hierarchy

The current system models the early production structure as:

- Project
  - Story
    - Episode
      - Scene
        - Shot

## Ordering

Stories, episodes, scenes, and shots use explicit `order` fields so production sequencing does not depend on database insertion order.

## Current Shot Scope

The `Shot` model is intentionally limited to foundational scheduling and identification data:

- UUID primary key
- scene reference
- production code
- order
- title
- duration in seconds
- lifecycle status
- timestamps
