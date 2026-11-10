# JUST RUN / JUST RAN — Motion Poster Builder

A browser tool for making 6-second thermal motion posters in the JUST RUN / JUST RAN series by Tony Han (KOMA Media). It's a speculative campaign, not affiliated with Nike.

## Use

Download `just-ran-poster-builder.html` and open it in Chrome. Everything is embedded in the file, so it works offline.

- **Format:** 1920×1080 (16:9), 1080×1920 (9:16), 1080×1440 (3:4), 1080×1350 (4:5), 1080×1080 (1:1)
- **Headline:** free text, one line per row. The 16:9 size has its own headline; the four vertical sizes share one.
- **Lockup:** vertical or horizontal tagline, tagline size, logo size
- **Image:** upload or drop a photo, then zoom, pan, softness, heat low/high/curve, invert
- **Render MP4:** 30fps H.264. **Save frame PNG:** a still of the current frame.

Shortcuts: `Space` plays or pauses, `←`/`→` step one frame, `H` hides the panel.

Locked: typeface (Futura Std Extra Bold Condensed, 150px, 129px leading, −30 tracking), layout, palettes, timing, grain and vignette.

## Rebuild

```
python3 src/build.py
```

This puts `src/template.html` and `src/assets/` back together into `just-ran-poster-builder.html`.

## Notes

- `src/assets/futura.otf` is a licensed Adobe font. Keep this repo private.
- `src/assets/*.mp4` are the tagline and logo animations exported from After Effects, cropped down.
- MP4 export uses [mp4-muxer](https://github.com/Vanilagy/mp4-muxer) (MIT).
