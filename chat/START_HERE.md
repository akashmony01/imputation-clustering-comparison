# Getting Started — Project Context Recovery

Copy and paste the following prompt into Claude Code when you open this project on a new machine:

---

```
I'm continuing work on a capstone project that was previously developed on another machine. I've saved my past conversation history and project memory in the `chat/` directory.

Please do the following:

1. Read `chat/MEMORY.md` (or `chat/memory_backup/MEMORY.md`) to understand the project context, known issues, and current status.
2. Read `chat/session_1_2c910dd1.md` and `chat/session_2_6a5f53f8.md` to understand what was discussed and decided in previous sessions.
3. Briefly explore the project structure (notebooks, datasets, report files) to verify what's currently on disk.

After reading everything, give me:
- A summary of where the project stands
- What was completed vs what still needs work
- Any known issues or fixes that were identified but not yet applied

Then save all of this understanding to your memory so future conversations don't need to re-read the chat files.
```

---

## What's in this directory

| File | Description |
|------|-------------|
| `session_1_2c910dd1.md` | First conversation — full project analysis, report assessment, LaTeX setup discussion |
| `session_2_6a5f53f8.md` | Second conversation — about transferring project between machines |
| `claude_settings.json` | Claude Code settings (was empty on original machine) |
| `memory_backup/MEMORY.md` | Project memory index — key facts, known issues, file locations |
