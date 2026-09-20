# Start your guided video tutorial

You can start with an idea, phone clips, photographs, or no project at all. You do not need to write technical prompts, know filmmaking terms, or own every application.

**To make a video:** invoke `$ai-video-director` and describe your project. **To learn with guided choices:** invoke `$ai-video-director-tutorial`. The director does not automatically start a tutorial. Both use the same quality checks and preserve accepted decisions when you switch.

## 1. Install the complete skill

Download [the package](https://github.com/AustinBCIT/ai-video-director/raw/refs/heads/main/ai-video-director-download.zip) and extract it. Inside `ai-video-director-download`, copy both complete folders, `ai-video-director` and `ai-video-director-tutorial`, side by side into:

- Windows: `%USERPROFILE%\.codex\skills\`
- macOS or Linux: `~/.codex/skills/`
- Custom Codex home: its `skills` folder.

The result should include both `skills/ai-video-director/SKILL.md` and `skills/ai-video-director-tutorial/SKILL.md`, with supporting folders intact. Do not copy only SKILL.md or nest the folders inside each other. The tutorial loads shared material from the director folder. If updating an existing installation, keep a backup of any personal edits before replacing the folders. Start a new Codex task after copying them.

The package contains instructions, templates and examples. It does not install Blender, DaVinci Resolve or After Effects, connect accounts, or include paid media credits. Each person uses their own files, available tools and authorization.

## 2. Paste one starting prompt

For a fully guided introduction:

```text
Use $ai-video-director-tutorial. I'm a beginner.
Show the Director's Project Guideline, then start Step 1.
Give me one decision at a time, simple choices and your recommendation.
Explain when, why and how each tool helps. Start with a planning exercise
without paid generation. Help me choose a small project.
```

If you already have phone clips:

```text
Use $ai-video-director-tutorial to guide me through making a short family travel
video from my phone clips. I'm a beginner. Use the clips I already have,
ask one useful question at a time and explain the editing and sound steps.
I have no budget for paid generation. First show the project guideline.
```

For your own idea, replace the project sentence with what you want the viewer to see, hear and feel. Mention anything that must remain accurate, such as a person, product, place or wording.

For actual project work without lesson pacing:

```text
Use $ai-video-director to create a short family travel video from my
phone clips. Prepare the project guideline, write the plan and prompts,
and carry out the available authorized work. Ask only for decisions or
assets needed to complete it.
```

## 3. Answer in ordinary language

The assistant explains the current step, offers a few choices, recommends one and writes the prompts or performs available authorized work. You can choose an option or type your own answer. You should not receive a long form to fill in.

Useful replies:

- **Recommend** — let the assistant choose and explain.
- **Explain more** or **show an example** — slow down the lesson.
- **Go back** or **change my answer** — revise a decision.
- **Pause** and later **resume the tutorial** — keep your place.
- **Switch to production mode** — spend less time teaching and focus on the result; this does not by itself authorize charges.

Expect a Director's Project Guideline first, followed by Step 1. After that, only the current step should expand. The assistant should reuse your earlier answers.

The opening overview also recommends a model and reasoning effort, explains why they suit this stage, and says whether to keep working in this task. A recommendation does not change your active model: use Codex's model/effort controls if a change is needed. The assistant should identify any setting it cannot verify. You do not need to understand token billing to start.

As the work changes, the assistant should reassess these choices. Staying can retain useful context and eligible cached computation; a fresh task can reduce irrelevant history but needs a prepared handoff. Neither is automatically cheaper. If exact cache/usage information is unavailable, the recommendation should say so instead of promising a percentage saving. The assistant proposes a fresh task and prepares the handoff; it creates one only when you explicitly ask. Read [the detailed guide](ai-video-director/references/model-and-context.md) if you want the accounting rules and examples.

## 4. Learn only the tools your project needs

| Tool | What you would learn | Good reason to use it |
|---|---|---|
| Blender | Set up a 3D camera, preview a move, light and render a scene | A stable scene, repeated angles or controlled objects/camera movement |
| DaVinci Resolve | Arrange clips, balance dialogue/music, match color and export | Editing and finishing recorded or generated footage |
| After Effects | Animate editable text and layered graphics; export to an editor | A specific graphics/compositing task, or learning AE itself |
| Image/video tools | Prepare supported references/prompts and inspect a trial | Creating suitable new imagery when existing footage does not meet the brief |

A phone-footage edit may need only an editor. A lesson can also be a plan without producing media. Software-specific steps depend on what you have installed and what the assistant can actually operate. You can explicitly ask to learn a tool even when it is optional for the final video.

## 5. Review picture and sound

The assistant should explain what to look and listen for: believable motion, consistent faces/products, stable signs and backgrounds, correctly pronounced words, natural lip-sync, audible dialogue and appropriate music. Real photos or walking footage may be needed for accurate places; a generated reference image is not proof of real geography.

If the assistant cannot watch continuous playback or hear the audio, it should say which checks need a capable reviewer. A good-looking still does not prove the video is correct. Your answer to a creative choice is not a substitute for checking the result.

## Optional: use the brief without installing

Attach [video-project-brief.md](video-project-brief.md) to your preferred assistant with a plain-language idea. The brief contains a compact guided-learning instruction too. The installed skill includes the fuller tutorial and tool branches.
