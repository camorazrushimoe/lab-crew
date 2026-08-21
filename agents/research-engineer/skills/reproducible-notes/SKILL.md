# Skill: reproducible-notes

## Purpose

Leave enough scripts, commands and notes so another agent (or human) can re-run or audit the experiment.

## When to use

- After any non-trivial experiment or analysis
- Before handing results to Evaluation Specialist or Research Lead

## Minimum bar

For each experiment folder:

1. Entry-point script or notebook that can be re-run
2. Short `NOTES.md` with:
   - what was done
   - key parameters / filters
   - how to re-run
   - known quirks
3. Clear separation of raw data vs derived outputs

## Discipline

- Prefer boring clarity over clever one-liners
- Record random seeds and important thresholds when they affect results
- If something was done manually, say so explicitly

## Anti-patterns

- Analysis that only exists in chat history
- Notebooks that cannot be executed top-to-bottom
- Hidden filters that change the conclusion
