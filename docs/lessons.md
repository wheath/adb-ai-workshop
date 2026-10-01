# Lessons: what human review caught

Both commercials took several review rounds. The AI did the first pass quickly; a person found what it missed.

## Problems review caught

| Problem | Cause | Fix |
|---|---|---|
| Children out of the camera frame | Checks used the viewport, not the camera frame | Verify with `world_to_camera_view` at several frames |
| Tiny specks over the river before the bridge appears | Planks were scaled to almost zero instead of hidden | Keyframe visibility; never rely on tiny scale |
| Children "in frame" but too small to see | The check passed, but it measured the wrong thing | Ask for what matters: clearly visible, not just inside the frame |
| Scene end silently cut from frame 852 to 264 | Side effect of building one shot | Restate global settings in the brief (`AGENTS.md`) |
| Unrequested house moves broke an earlier shot | Fixing one thing changed another | Recheck earlier shots after every fix |
| Flickering mountain peaks and text | Overlapping surfaces ("z-fighting") | Separate the surfaces; copy settings from text that works |
| Road laid over the bridge; road under a house | Paths drawn without checking what's there | Describe what must not overlap |
| A summary that didn't add up ("12 units, down from 12") | Generated text, not checked | Read AI output; don't skim it |

## What this means for using AI at work

1. **Write the brief once.** A file like `AGENTS.md` makes results repeatable and survives the AI's memory limits.
2. **Ask for evidence, not "done".** Screenshots, measurements, citations.
3. **Expect the last 10% to be human work,** and budget time for it.
4. **Read every permission and data-sharing prompt.** We declined the Blender add-on's data collection.
5. **Choose tools by data sensitivity.** Voice and music ran locally; nothing left the laptop.
6. **One MCP server adds a capability to any agent.** Claude and Copilot used the same Blender server and got different, valid results.
