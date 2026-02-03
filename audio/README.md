# Audio Annotation Tasks

This category contains annotation task designs for audio and speech processing research, including transcription, speaker identification, and audio classification.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [audio-transcription](./audio-transcription) | Speech transcription review and correction | Template |
| [speaker-diarization](./speaker-diarization) | Speaker identification and turn-taking | Template |
| [emotion-recognition](./emotion-recognition) | Speech emotion classification | Template |
| [music-genre-classification](./music-genre-classification) | Music genre and mood tagging | Template |

## Quick Start

```bash
# Navigate to a specific task
cd audio/speaker-diarization

# Run with Potato
potato start config.yaml
```

## Annotation Features

Audio annotation tasks in Potato support:

- **Waveform visualization**: See audio amplitude over time
- **Playback controls**: Play, pause, seek, and adjust speed
- **Segment marking**: Define temporal boundaries for speech turns
- **Multi-track support**: Handle multiple audio channels

## Task Count

**Total: 4 audio annotation tasks**
