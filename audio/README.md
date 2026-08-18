# Audio Annotation Tasks

This category contains annotation task designs for audio and speech processing research, including transcription, speaker identification, and audio classification.

> Run these designs in [Potato](https://www.potatoannotator.com). See the [audio annotation documentation](https://www.potatoannotator.com/docs/features/audio-annotation) to configure waveform playback and transcription tasks.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [audio-transcription](https://github.com/davidjurgens/potato-showcase/tree/main/audio/audio-transcription) | Review and correct automatic speech recognition transcriptions with waveform visualization | Template |
| [audiohate-speech-detection](https://github.com/davidjurgens/potato-showcase/tree/main/audio/audiohate-speech-detection) | Audio hate speech detection with explanations | An et al., SIGDIAL 2024 |
| [clotho-audio-captioning](https://github.com/davidjurgens/potato-showcase/tree/main/audio/clotho-audio-captioning) | Audio captioning and quality assessment based on the Clotho dataset | Drossos et al., ICASSP 2020 |
| [covost-speech-translation](https://github.com/davidjurgens/potato-showcase/tree/main/audio/covost-speech-translation) | Speech translation quality evaluation based on the CoVoST 2 dataset | Wang et al., arXiv 2020 |
| [displace-speaker-diarization](https://github.com/davidjurgens/potato-showcase/tree/main/audio/displace-speaker-diarization) | Speaker and language diarization in multilingual conversational audio | Kalluri et al., INTERSPEECH 2024 |
| [doreco-language-documentation](https://github.com/davidjurgens/potato-showcase/tree/main/audio/doreco-language-documentation) | DoReCo is a cross-linguistic corpus of 53 spoken languages with over 100 hours of narrative speech… | Paschen et al., LREC 2020 |
| [emobox-multilingual-speech-emotion](https://github.com/davidjurgens/potato-showcase/tree/main/audio/emobox-multilingual-speech-emotion) | Multilingual speech emotion recognition across multiple languages and corpora | Ma et al., INTERSPEECH 2024 |
| [emotion-recognition](https://github.com/davidjurgens/potato-showcase/tree/main/audio/emotion-recognition) | Classify emotional states from speech audio including happiness, sadness, anger, fear, and more | Template |
| [librispeech-transcription](https://github.com/davidjurgens/potato-showcase/tree/main/audio/librispeech-transcription) | Audio transcription quality assessment based on the LibriSpeech corpus | Panayotov et al., ICASSP 2015 |
| [miami-code-switching](https://github.com/davidjurgens/potato-showcase/tree/main/audio/miami-code-switching) | Multi-tier annotation of Spanish-English bilingual speech for code-switching analysis | Deuchar & Parafita Couto, TalkBank 2011 |
| [music-genre-classification](https://github.com/davidjurgens/potato-showcase/tree/main/audio/music-genre-classification) | Classify music clips into genres and subgenres with mood and instrumentation tags | Template |
| [podcastfillers-disfluency-tagging](https://github.com/davidjurgens/potato-showcase/tree/main/audio/podcastfillers-disfluency-tagging) | Per-segment tagging of filler words and other audio events on podcast audio with time-aligned transcripts,… | Zhu et al., Interspeech 2022 |
| [speaker-diarization](https://github.com/davidjurgens/potato-showcase/tree/main/audio/speaker-diarization) | Identify and label different speakers in audio recordings with timestamp-based segment annotation | Template |
| [speech-accent-classification](https://github.com/davidjurgens/potato-showcase/tree/main/audio/speech-accent-classification) | Classify speaker accents from audio recordings and assess speech quality | Ardila et al., LREC 2020 |
| [speech-commands-recognition](https://github.com/davidjurgens/potato-showcase/tree/main/audio/speech-commands-recognition) | Google Speech Commands is a corpus of one-second spoken-word audio clips for training keyword spotting… | Warden, arXiv 2018 |
| [sporc-podcast-turn-annotation](https://github.com/davidjurgens/potato-showcase/tree/main/audio/sporc-podcast-turn-annotation) | Speaker-role labeling and diarization validation for podcast episodes, based on the Structured Podcast… | Litterer et al., ACL 2025 |
| [tobi-prosody-annotation](https://github.com/davidjurgens/potato-showcase/tree/main/audio/tobi-prosody-annotation) | Multi-tier prosodic annotation following the Tones and Break Indices (ToBI) framework | Silverman et al., ICSLP 1992 |
| [voicemos-quality-assessment](https://github.com/davidjurgens/potato-showcase/tree/main/audio/voicemos-quality-assessment) | Speech quality assessment using Mean Opinion Score (MOS) | Huang et al., IEEE SLT 2024 |
| [wavcaps-audio-captioning](https://github.com/davidjurgens/potato-showcase/tree/main/audio/wavcaps-audio-captioning) | Audio captioning - write natural language descriptions of audio content | Mei et al., IEEE TASLP 2024 |

## Quick Start

```bash
# Navigate to a specific task
cd audio/speaker-diarization

# Run with Potato
potato start config.yaml
```

## Annotation Features

Potato draws the waveform so annotators can see amplitude over time, and gives them play, pause, seek, and speed controls. Annotators mark start and end times for speech turns, and the player handles files with more than one audio channel.

## Task Count

**Total: 19 audio annotation tasks**
