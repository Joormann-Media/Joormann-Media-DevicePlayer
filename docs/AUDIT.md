# Audit: Joormann-Media-DevicePlayer

Stand: 2026-03-08

## Ergebnis

Der Player ist jetzt als lauffähiger MVP umgesetzt.

## Abgedeckte Funktionen

- lokales `manifest.json` laden und validieren
- Modi: `full`, `split`
- Layoutparameter: `orientation`, `direction`, `ratioA`
- Transitionen: `crossfade`, `slide-left`
- lokale Assets laden (`jpg/png/webp`, abhängig von SDL/Pygame Build)
- Endlosschleife für Playlist
- robuste Fehlerbehandlung pro Asset (kein Komplettabsturz)
- Manifest-Reload via Dateizeit-Änderung (Polling)
- Service-Betrieb via `systemd/joormann-media-deviceplayer.service`

## Wichtige Dateien

- `run.py`
- `src/deviceplayer/app.py`
- `src/deviceplayer/plan_loader.py`
- `src/deviceplayer/renderer.py`
- `src/deviceplayer/transitions.py`
- `systemd/joormann-media-deviceplayer.service`

## Bekannte Grenzen

- Fokus aktuell auf Bild-Assets (keine Videodekodierung in diesem MVP)
- effektive WebP-Unterstützung hängt von lokalem SDL_image/Pygame Build ab
- keine externe Telemetrie-Schnittstelle im Player-Prozess

## Fazit

Der Player ist nicht mehr Scaffold, sondern als eigenständiger HDMI-Renderer im vorgesehenen Manifest-Format nutzbar.
