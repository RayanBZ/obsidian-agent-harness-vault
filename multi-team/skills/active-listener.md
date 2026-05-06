# Active Listener Skill

## Purpose
Read the conversation log before every response for full context.

## Protocol
1. Read `{{CONVERSATION_LOG}}` — full session JSONL
2. Identify: Who said what? What was decided? What's open?
3. Track: Which agents involved? What did they report?
4. Avoid: Repeating answered questions. Contradicting prior decisions.
