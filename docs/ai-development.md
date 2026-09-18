# AI-Assisted Development

RaceSim is intentionally built with AI assistance, but the developer remains responsible for every technical choice and must be able to explain the system in an interview or operational setting.

## Roles

ChatGPT is used primarily for architecture discussion, project planning, explanations, milestone specifications, review, and interview preparation.

Codex is used primarily for repository changes, implementation, tests, and refactoring within an explicitly requested milestone.

The developer, Kareem, reviews the output, runs or verifies the relevant checks, makes final decisions, and develops an understanding of the resulting architecture and code.

## Working principles

- Start each task from a bounded milestone with clear acceptance criteria.
- Read the persistent project documentation before making architectural changes.
- Preserve the locked architecture unless an explicit, documented decision changes it.
- Generate only work that belongs to the current milestone.
- Prefer code and designs that are straightforward to read, test, and explain.
- Test meaningful business behavior instead of accepting generated output on appearance alone.
- Review generated code for correctness, security, maintainability, and scope.
- Never place secrets or private credentials in prompts, source control, logs, or generated documentation.
- Use Architecture Decision Records to make significant choices and their tradeoffs visible.
- End implementation tasks with a summary of changed files, commands, tests, decisions, and unresolved issues.

## Transparency

AI assistance is part of the project's documented engineering process, not a substitute for engineering judgment. Commit and pull-request descriptions should accurately describe the work. Important decisions should be traceable to project documentation or ADRs, and generated changes should receive the same review and testing expected of manually authored changes.

This approach makes RaceSim evidence of both technical implementation skills and the ability to use AI tools deliberately, safely, and accountably.

