# Universal Claude Code Project Transfer Prompt

Copy and paste this prompt into Claude Code from **any project directory** you want to transfer to another machine:

---

```
I want to transfer this project to another computer and preserve my Claude Code chat history, memory, and settings. Please do the following:

1. Create a `chat/` directory inside this project.

2. Find my Claude Code conversation history for this project. The conversations are stored as `.jsonl` files in `~/.claude/projects/` under a folder named after this project's absolute path (with slashes replaced by dashes). Extract all human and assistant messages from each `.jsonl` file and save them as readable markdown files in `chat/`, one file per session. Each file should include the session ID, message numbers, and clearly label who said what (USER vs CLAUDE).

3. Copy my Claude Code memory files for this project (from the same `~/.claude/projects/<project>/memory/` directory) into `chat/memory_backup/`.

4. Copy `~/.claude/settings.json` into `chat/` as `claude_settings.json`. Do NOT copy `~/.claude/config.json` as it contains my API key.

5. Create a `chat/START_HERE.md` file that contains:
   - A ready-to-paste prompt I can give Claude on the new machine to read all the chat files and memory, understand the project context, and save it to memory
   - A table listing all the files in the chat directory and what they contain

Make sure the exported chat markdown files are clean and readable, not raw JSON.
```

---

## How to use

1. Open Claude Code in the project you want to transfer
2. Paste the prompt above
3. Claude will create a `chat/` directory with everything exported
4. Copy the entire project to the new machine
5. On the new machine, open `chat/START_HERE.md` and follow the instructions
