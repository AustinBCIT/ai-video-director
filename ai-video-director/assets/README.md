# AI Video Director

Two distinct Codex skill invocations share the same video-production rules:

| Invoke | Purpose |
|---|---|
| `$ai-video-director` | Work on your actual video: plan, write prompts, prepare assets, execute authorized production and review results |
| `$ai-video-director-tutorial` | Learn step by step: explanations, simple choices, recommendations and guided exercises |

The director does not start a lesson by default. Both begin with a Director's Project Guideline and reuse your existing decisions.

The opening overview recommends a model and reasoning effort for your current stage, plus whether to continue, compact or propose a fresh task. It distinguishes recommended settings from verified active settings and measures savings only when usage evidence supports them. See [model and conversation economics](ai-video-director/references/model-and-context.md).

**[Download the complete ZIP](https://github.com/AustinBCIT/ai-video-director/raw/refs/heads/main/ai-video-director-download.zip)** · **[Beginner start guide](START-HERE.md)**

This is a public download; no Git or GitHub account is needed. The repository also includes all editable skill source files.

## Install

1. Download and extract the ZIP.
2. Open `ai-video-director-download` and copy both complete folders, **ai-video-director** and **ai-video-director-tutorial**, into your Codex skills folder:
   - Windows: `%USERPROFILE%\.codex\skills\`
   - macOS/Linux: `~/.codex/skills/`
   - Custom `CODEX_HOME`: its `skills` folder.
3. Confirm `skills/ai-video-director/SKILL.md` and `skills/ai-video-director-tutorial/SKILL.md` exist side by side. Keep their supporting folders intact. Back up personal modifications before replacing an older installation.
4. Start a new Codex task and paste:

```text
Use $ai-video-director-tutorial. I'm a beginner.
Show the Director's Project Guideline, then start Step 1.
Give me one decision at a time, simple choices and your recommendation.
Explain when, why and how to use the relevant tools.
Start with a planning exercise without paid generation.
```

For actual production, invoke the director instead:

```text
Use $ai-video-director to create my video. Here is the result I want:
[describe the scene, duration, references and constraints].
Write the prompts and carry out the available authorized work.
```

In the tutorial you can say **recommend**, **explain more**, **go back**, **pause** or **resume**. You do not need to fill every template or write technical prompts yourself. Switching skills carries accepted project decisions forward; it does not authorize new charges.

## What the tutorial covers

- A Director's Project Guideline first, followed by Step 1 and only the questions needed next.
- Model/effort recommendations before work and at meaningful stage changes; cache-aware comparisons that include handoff costs and preserve accepted decisions.
- Choosing the viewer's experience, camera viewpoint and reference requirements.
- Story, dialogue, pronunciation, music/no-music decisions and sound review.
- Character sheets with front, both profiles, back and relevant three-quarter/detail views.
- Real-location photos/video, product/prop evidence, realism and continuity checks.
- Tool choices and small guided exercises for Blender, Resolve and After Effects.
- Reference preparation, camera-motion previews, supported generation inputs and bounded trials.
- Editing, color, captions, sound mixing, full audiovisual review and delivery.
- Practice without paid generation and a saved place for resuming the lesson.

The lesson adapts: editing phone clips does not require creating character sheets, building a Blender scene or generating new footage. A user who specifically wants to learn a tool can choose a small learning exercise.

Read the [tutorial instructions](ai-video-director/references/guided-tutorial.md) or [tool-selection guide](ai-video-director/references/tool-routing.md). Other references load only when needed.

## Included files

- `ai-video-director/`: the complete installable skill, tool guides, templates and worked examples.
- `ai-video-director-tutorial/`: the separate teaching entry point; keep it beside the director folder because it loads the shared curriculum there.
- [START-HERE.md](START-HERE.md): beginner installation and starting prompts.
- [video-project-brief.md](video-project-brief.md): optional standalone brief; describe your idea and let the assistant help fill it.
- `ai-video-director-download.zip`: the ready-to-share package.
- `SHA256SUMS.txt`: download checksum.
- `scripts/build_package.py`: standard-library Python script to rebuild the ZIP from the repository source.

## Tools, costs and limits

Installing this skill does not install creative applications, connect accounts, buy credits or grant permission to spend or publish. Each person supplies their own assets and uses their own available tools. Specialist plugins are optional and are not bundled.

Blender is useful for controlled 3D scenes and cameras; Resolve for editing, color and sound; After Effects for specific motion graphics or compositing. These are options, not a requirement to use every app. Actual features, editions, model inputs and prices are checked when needed. See the individual tool references for official sources.

Instructions and extra references reduce avoidable errors but cannot guarantee generated fidelity. Screenshots and transcripts do not establish full motion or pronunciation quality. Failed or unverified required checks remain visible; an attractive still or user approval does not erase them.

The download includes reusable instructions, blank templates and fictional examples. It does not include private project media, account credentials, local audit logs, third-party plugin code or software installers. Example plans are not rendered or audience-tested videos.
