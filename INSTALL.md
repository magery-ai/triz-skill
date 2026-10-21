# Installing the TRIZ skill

The skill is one folder, [`skills/triz`](skills/triz), in the open
[Agent Skills](https://agentskills.io) format. Any agent that loads skills
from a folder can use it.

## Ask your agent

Paste this into your agent:

```text
Install the TRIZ skill from https://github.com/magery-ai/triz-skill
```

## Claude Code

Plugin marketplace:

```
/plugin marketplace add magery-ai/triz-skill
/plugin install triz@triz-skill
```

To update, run `/plugin marketplace update triz-skill`.

## Claude.ai

Download `triz-skill-<version>.zip` from the
[latest release](https://github.com/magery-ai/triz-skill/releases/latest) and
upload it under Settings > Capabilities > Skills.

## Skills CLI

For any agent the [skills CLI](https://skills.sh) supports:

```bash
npx skills add magery-ai/triz-skill --skill triz
```

## Manual copy

Copy the folder into your agent's skills folder. For Claude Code:

```bash
git clone https://github.com/magery-ai/triz-skill
cp -r triz-skill/skills/triz ~/.claude/skills/
```

Other agents use their own skills folder; check your agent's documentation
for where it is.

## Check that it works

Start a new session and describe a trade-off, for example: *"Our pages need
to be fast, but the cache shows stale prices."* The agent should say it is
using TRIZ and ask up to two clarifying questions.

The matrix lookup script needs Python 3.9 or later and only the standard
library. Without Python, the agent reads the data files directly.
