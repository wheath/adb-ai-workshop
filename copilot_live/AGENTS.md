# Project: ADB concept commercial (live build in Blender via MCP)

You are building a 35-second low-poly animated concept commercial in Blender, using the Blender MCP tools.
Work in small steps: one `execute_blender_code` call per logical step, then check with `get_viewport_screenshot`.

## Scene conventions (always follow)
- Render engine Eevee, 1280x720, 24 fps, frames 1-852. Save the file after every shot (`bpy.ops.wm.save_mainfile()`).
- Save as `~/Documents/work/adb_bank/copilot_live/adb_commercial_copilot.blend` on the first save.
- Low-poly style: houses, roofs and trees keep flat shading; ground, hills and characters use smooth shading.
- One camera named `Camera` with a Track To constraint on an empty named `CamTarget`. Animate both; use CONSTANT interpolation on the last key of a shot so cuts are clean.
- Objects that "build" or "appear" must be hidden (keyframe `hide_render` and `hide_viewport`) until their start frame. Never rely on scaling to 0.01 - tiny specks stay visible.
- Before finishing any shot, verify framing with `bpy_extras.object_utils.world_to_camera_view` on the key objects at several frames: x and y must stay between 0.1 and 0.9. Viewport screenshots are not proof of what the camera sees.
- Keep the viewport looking through the camera in Rendered shading so the presenter can see progress.

## Shot list (frames)
1. 1-120: dawn village by a river, slow push-in.
2. 121-264: wooden bridge builds plank by plank; two children (blue and yellow) wait on the near bank, then cross after the last plank (about frames 214-262). Low side-on camera over the water.
3. 265-408: solar panels unfold on the roofs, then windows light up warmly.
4. 409-576: camera rises to a high aerial view by about frame 490; roads grow (one at a time) to four neighbouring villages; every village visible in frame while the roads grow.
5. 577-852: sunset, slow orbit, then title "Asian Development Bank", tagline "Building a prosperous, inclusive, resilient Asia and the Pacific", and a small label "Concept demo · not an official ADB production" over a soft dark band.

## Audio (already generated - do not regenerate)
- Voice lines: `~/Documents/work/adb_bank/audio/kokoro/bm_george/line_1.wav` ... `line_5.wav`; place at frames 1, 199, 329, 454, 589 on channel 2.
- Music: `~/Documents/work/adb_bank/audio/sa3/sa3_take_seed44.wav` at frame 61 on channel 3, volume 0.32, dipping to 0.14 under each voice line.
- Set `scene.sync_mode = 'AUDIO_SYNC'`.
