# Joormann-Media-DevicePlayer

Eigenständiger HDMI-Player für kompakte Runtime-Manifeste aus dem Adminpanel.

## Unterstütztes Manifest

- `layout.mode`: `full` | `split`
- `layout.orientation`: `landscape` | `portrait`
- `layout.direction`: `horizontal` | `vertical` (bei split)
- `layout.ratioA`: 1..99 (bei split)
- `defaults.durationMs`
- `defaults.transition.type`: `none` | `crossfade` | `slide-left`
- `defaults.transition.ms`
- `assets` Mapping
- `playlist`:
  - full: `[{ "asset": "assetX" }]`
  - split: `[{ "zones": { "A": {"asset":"..."}, "B": {"asset":"..."} } }]`

## Start

```bash
cd /home/djanebmb/projects/Joormann-Media-DevicePlayer
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python run.py --manifest runtime/plan.json
```

## Service

```bash
sudo cp systemd/joormann-media-deviceplayer.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now joormann-media-deviceplayer.service
sudo systemctl status joormann-media-deviceplayer.service
```

Standard-Manifestpfad im Service:
- `/mnt/deviceportal/media/stream/current/manifest.json`

## Lokaler Dateiaufbau

Der Player erwartet lokal:
- `manifest.json`
- `assets/<dateien>`

Das Device Portal schreibt atomar:
- `<storage>/stream/staging/build-*/...`
- danach Umschalten auf `<storage>/stream/current/...`
