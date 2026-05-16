## Day 1 — Tuesday, May 15, 2026

### Topics covered
- Variables, types, f-strings
- List operations (built-ins, filtering)
- String methods and slicing
- Conditionals (if/elif/else)
- References vs copies (deep concept)

### Mistakes I made
- Forgot parentheses on method calls
- Misread questions (skipped filtering, did 2 checks instead of 1)
- Used capitalize() instead of title()
- Used Currently_working_fintech (wrong casing convention)

### Wins
- Predicted reference/copy behavior correctly on second try
- Caught my own bugs in the rewrite

### Concepts that clicked
- enumerate() vs zip() — when to use which
- The "collect first, output later" pattern
- Silent bugs: code runs but output is wrong (expenses vs expense)

### Question I now know to ask
- "Would this code still work if the input were slightly different?"
- "Code ran without error ≠ code did what I intended"

- ## Day 2 — May 16, 2026

### Topics covered
- Matplotlib: line, bar, subplots, figsize, conditional colors
- Reading Python error tracebacks (bottom-up)
- Dictionaries (preview, starting Day 9)
- input() and while loops with validation
- continue vs nested input — control flow gotcha
- Method calls need parentheses (recurring pattern)

### Bugs I debugged today
- Wrong chart type (hist instead of bar) — error message clarified it
- Subplot placement (called after plot instead of before)
- Missing parentheses on .isdigit (silent bug, my recurring weak spot)
- Nested input + continue = lost data (silent bug)

### Decisions made
- Dropping DataCamp; using Angela Yu + Real Python + targeted YouTube
- Will revisit DataCamp option in Phase 2 (SQL) if needed

### What I want to remember
- "Code ran without error ≠ code did what I intended" — still my biggest blind spot
- Stack traces: bottom line first, ignore the middle wall of text
- continue in a while loop restarts from the top — any work done before continue gets overwritten
