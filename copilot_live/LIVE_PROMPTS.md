# Live build: prompts to paste into the GitHub Copilot app

Model: Claude Sonnet 5 (fast). Project: `adb_bank/copilot_live`. Blender open with "MCP for Blender" started.
Target time: 15-20 minutes. Backup if anything stalls: open `adb_bank/adb_commercial.blend` (tonight's version).

---

**0. Warm-up (1 min)**
> Check the Blender connection and tell me what is in the scene. Then start a new empty scene following the project instructions and save it.

**1. Shot 1 - the village (3 min)**
> Build shot 1: a low-poly village of 8 houses with red roofs and trees beside a river, rolling green hills behind, distant mountains filling the horizon, and a dawn sky (orange at the horizon, blue above) with a low warm sun. Add the camera push-in for frames 1-120. Show me a screenshot through the camera.

**2. Shot 2 - the bridge (4 min)**
> Build shot 2 (frames 121-264): an arched wooden bridge across the river that builds plank by plank, then railing posts. Two simple children, one blue and one yellow, wait on the near bank in frame, then walk across after the last plank. Use a low side-on camera over the water. Hide each plank until it appears. Verify with world_to_camera_view that the children and both bridge ends stay in frame for the whole shot.

**3. Shot 3 - clean power (3 min)**
> Build shot 3 (frames 265-408): blue solar panels unfold on each roof one after another, then the windows light up warmly one by one while the sun dims a little. Camera at rooftop height gliding across the village.

**4. Shot 4 - roads (4 min)**
> Build shot 4 (frames 409-576): add four small neighbouring villages, two across the river. The camera rises to a high aerial view by frame 490, then roads grow one at a time from the village to each neighbour, the two southern ones via the bridge. Verify all four villages stay in frame from frame 470.

**5. Shot 5 - title and sound (3 min)**
> Build shot 5 (frames 577-852): sunset colours, slow orbit, then the title, tagline and concept-demo label over a soft dark band, timed as in the project instructions. Then add the voice and music strips exactly as listed in the project instructions, smooth-shade the ground and hills, save, and play from frame 1.

---

**If something looks wrong, say what you see** (that is the human-review lesson):
- "The children are outside the camera frame around frame 200 - fix it and verify with world_to_camera_view."
- "I can see tiny specks over the river before the bridge builds - hide them until they appear."
- "The hills look faceted - smooth-shade the terrain only."

**Talking points while it works**
- Same MCP server, different agent: Claude built tonight's version; Copilot builds this one.
- The agent writes Blender Python, checks its own work, and a person approves each shot.
- Voice (Kokoro) and music (Stable Audio 3) are local open models - nothing leaves the laptop.
