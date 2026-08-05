# Audio Annotation Tasks

This category contains annotation task designs for audio and speech processing research, including transcription, speaker identification, and audio classification.

> Run these designs in [Potato](https://www.potatoannotator.com). See the [audio annotation documentation](https://www.potatoannotator.com/docs/features/audio-annotation) to configure waveform playback and transcription tasks.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [audio-transcription](./audio-transcription) | Speech transcription review and correction | Template |
| [audiohate-speech-detection](./audiohate-speech-detection) | Audio hate speech detection with explanations | An et al., SIGDIAL 2024 |
| [clotho-audio-captioning](./clotho-audio-captioning) | Audio captioning and quality assessment based on the Clotho dataset | Drossos et al., ICASSP 2020 |
| [covost-speech-translation](./covost-speech-translation) | Speech translation quality evaluation based on the CoVoST 2 dataset | Wang et al., arXiv 2020 |
| [displace-speaker-diarization](./displace-speaker-diarization) | Speaker and language diarization in multilingual conversational audio | Kalluri et al., INTERSPEECH 2024 |
| [doreco-language-documentation](./doreco-language-documentation) | DoReCo is a cross-linguistic corpus of 53 spoken languages with over 100 hours of narrative speech… | Paschen et al., LREC 2020 |
| [emobox-multilingual-speech-emotion](./emobox-multilingual-speech-emotion) | Multilingual speech emotion recognition across multiple languages and corpora | Ma et al., INTERSPEECH 2024 |
| [emotion-recognition](./emotion-recognition) | Speech emotion classification | Template |
| [librispeech-transcription](./librispeech-transcription) | Audio transcription quality assessment based on the LibriSpeech corpus | Panayotov et al., ICASSP 2015 |
| [miami-code-switching](./miami-code-switching) | Multi-tier annotation of Spanish-English bilingual speech for code-switching analysis | Deuchar & Parafita Couto, TalkBank 2011 |
| [music-genre-classification](./music-genre-classification) | Music genre and mood tagging | Template |
| [podcastfillers-disfluency-tagging](./podcastfillers-disfluency-tagging) | Per-segment tagging of filler words and other audio events on podcast audio with time-aligned transcripts,… | Zhu et al., Interspeech 2022 |
| [speaker-diarization](./speaker-diarization) | Speaker identification and turn-taking | Template |
| [speech-accent-classification](./speech-accent-classification) | Classify speaker accents from audio recordings and assess speech quality | Ardila et al., LREC 2020 |
| [speech-commands-recognition](./speech-commands-recognition) | Google Speech Commands is a corpus of one-second spoken-word audio clips for training keyword spotting… | Warden, arXiv 2018 |
| [sporc-podcast-turn-annotation](./sporc-podcast-turn-annotation) | Speaker-role labeling and diarization validation for podcast episodes, based on the Structured Podcast… | Litterer et al., ACL 2025 |
| [tobi-prosody-annotation](./tobi-prosody-annotation) | Multi-tier prosodic annotation following the Tones and Break Indices (ToBI) framework | Silverman et al., ICSLP 1992 |
| [voicemos-quality-assessment](./voicemos-quality-assessment) | Speech quality assessment using Mean Opinion Score (MOS) | Huang et al., IEEE SLT 2024 |
| [wavcaps-audio-captioning](./wavcaps-audio-captioning) | Audio captioning - write natural language descriptions of audio content | Mei et al., IEEE TASLP 2024 |

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

**Total: 19 audio annotation tasks**
