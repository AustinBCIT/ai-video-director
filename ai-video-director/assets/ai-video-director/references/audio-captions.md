# Voice, sound, music and captions

## Audio plan

Determine whether the piece needs dialogue, voiceover, music, sound effects, ambience or intentional silence. Separate story function from acquisition method. Native generated audio, recorded dialogue, stock music and sound designed in the edit are different routes with different control.

For dialogue/VO, establish speaker ID, language, pronunciation, performance and voice continuity. Use appropriately authorized voice assets. Time the actual delivery, including breaths and pauses. For lip-sync, evaluate the face and speech together through the whole shot. If a tool cannot achieve the required performance, offer a narration/reaction-shot edit or another authorized route without pretending the original requirement was met.

## Guideline and preproduction sound checks

In the opening Director's Project Guideline, explicitly state dialogue/VO, background music and ambience as selected, proposed, absent or unresolved. Do not treat a missing music field as an instruction to add a track. For a natural location vlog, location sound without music can be the recommended default; preserve any user's existing no-music direction.

Before picture timing depends on sound, check:

- **Dialogue:** exact or draft words, speaker, language/accent, pronunciation evidence, natural performance, breaths/pauses, actual duration, on-camera versus off-camera delivery and lip-sync route. Do not silently rewrite mandatory copy to fit a shot.
- **Background music:** purpose/mood, instrumental or vocals, intended intensity, source/usage status, cue in/out and fade timing, and whether it competes with speech or realistic location sound. Use an available suitable asset or a proposed direction; do not imply a reference track is licensed or already acquired.
- **Mix:** separate revisable speech/music/ambience where possible, plan level reduction under dialogue when needed, preserve sound continuity across turns/cuts, and identify who can listen to the actual combined result.

After production, listen to dialogue alone and the full mix; check intelligibility, critical words, voice consistency, lip synchronization, music masking, abrupt starts/ends, ambience continuity and clipping. Record evidence/status separately for dialogue and music, including intentional no-music. A waveform, transcript or silent video inspection cannot pass these checks.

## Layers and timing

### Names and pronunciation before video

For place/person names, foreign words or technical terms where accuracy matters, record `exact text / native spelling / language or locale / reliable reference audio or speaker / pronunciation cue / listened-to sample and reviewer / status`. Verify pronunciation with an authoritative or competent native-speaker source; do not invent a phonetic spelling from memory and call it verified. Romanization is not an audio reference.

Test the exact line in the intended voice before an expensive lip-synchronized shot when pronunciation is uncertain. Listen to the sample and time it with breaths, camera turns and pauses. Where supported, bind approved speech as an actual audio input; otherwise use an appropriate recorded/TTS/lip-sync route and verify its capabilities and cost. Pasting an audio filename into the prompt does not bind it. Keep display spelling/captions correct even if a model-specific pronunciation cue is used internally.

Native generated speech without audio control remains an uncertainty, even with phonetic prompting. Do not commit an accuracy-sensitive final to that route without a meaningful audio test or an explicitly scoped diagnostic attempt. A correct automatic transcript does not prove pronunciation; a wrong transcription alone also does not prove mispronunciation. User/native-listener feedback that a name is wrong marks pronunciation failed and requires correction.

If the agent cannot hear audio, disclose that capability gap before the relevant production decision, prepare a playable pronunciation sample for a capable reviewer, and retain `not verified` until listening evidence exists. Do not promise autonomous pronunciation or lip-sync certification through speech-to-text.

| Layer | Purpose | Check |
|---|---|---|
| Dialogue / VO | Carries speech and character | Intelligibility, pronunciation, sync, consistent level and voice |
| Room tone / ambience | Establishes place and bridges edits | No sudden background changes or distracting loops |
| Foley | Makes physical action believable | Contact timing, material, scale and spatial position |
| Designed effects | Supports reveals, transitions or emotion | Appropriate intensity; avoid a whoosh on every cut |
| Music | Supports pacing and emotional development | Leaves room for speech; edit structure fits the piece |
| Silence | Directs attention or creates tension | Intentional pause rather than accidental missing audio |

Write a cue sheet only as detailed as necessary: `time/shot | sound | onset/length | source | mix note`. Separate music, dialogue and effects stems where revisions/localization need them. Check headphones and ordinary speakers, with mono compatibility when relevant.

Set sample rate, channel layout and delivery loudness from the actual destination. 48 kHz is a practical video-production starting point, not a substitute for a delivery spec. Measure final loudness/true peak when required; do not apply one universal LUFS target to every platform. Avoid clipping and excessive music masking speech. Track the actual license for selected music/effects before release; a familiar trending song is not automatically cleared for an ad.

## Followable subtitles

Distinguish dialogue subtitles, accessibility captions including meaningful non-speech sound, and decorative kinetic text. Choose burned-in, separate SRT/VTT, or both according to use. A sidecar can be localized and toggled; a burn-in fixes appearance but cannot be removed from that export.

Start with phrase-level chunks, usually one or two lines for a phone-oriented design, with natural linguistic breaks. This is a layout starting point, not a universal language rule. Set reading speed, maximum lines/characters and timing from the destination and language; preview at actual playback speed. Shorten or retime content when the viewer cannot read it comfortably.

Keep high contrast, adequate size and stable placement. Avoid covering faces, product details, demonstrations and current platform UI. Verify safe areas for each export. Word highlighting can help emphasis, but rapid bouncing every word can hurt readability; keep a stable text block where possible. Do not rely only on color for speaker distinction or meaning.

Build timings from the actual final audio. Review names, technical terms, punctuation, speakers, line breaks and meaningful sounds. Machine transcription is a draft. Avoid duplicate platform captions over burned text, and supply a clean version when needed. If wording is condensed rather than verbatim, preserve meaning and label the caption treatment appropriately.

For formal delivery, use the applicable language/style guide. [Netflix's timing guidance](https://partnerhelp.netflixstudios.com/hc/en-us/articles/360051554394-Timed-Text-Style-Guide-Subtitle-Timing-Guidelines), checked 2026-09-19, emphasizes timing comfortably with speech and editing; its delivery rules should not be imposed on unrelated social content.

## Final review

Listen once without watching for intelligibility and abrupt edits; watch with sound off for visual comprehension where appropriate; then watch normally for synchronization and overload. Record what was actually reviewed. Do not report an audio or full-motion pass based on screenshots.
