import os
import subprocess
import platform
import logging
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
from pydub.playback import play

# Get ElevenLabs API key from environment
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# -------------------------------
# gTTS function without autoplay (old version)
def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

# -------------------------------
# ElevenLabs function without autoplay (old version)
def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

# -------------------------------
# gTTS function with autoplay using pydub playback
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    try:
        # Load the MP3 file using pydub and play it
        audio_segment = AudioSegment.from_mp3(output_filepath)
        play(audio_segment)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# ElevenLabs function with autoplay using pydub playback
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    try:
        # Load the MP3 file using pydub and play it
        audio_segment = AudioSegment.from_mp3(output_filepath)
        play(audio_segment)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# -------------------------------
# Testing the functions
if __name__ == "__main__":
    test_text = "Hi, this is Ridham's model, autoplay testing"
    
    # Test gTTS with autoplay using pydub's playback
    #text_to_speech_with_gtts(input_text=test_text, output_filepath="gtts_testing_autoplay.mp3")
    
    # Uncomment the following line to test ElevenLabs TTS with autoplay:
    # text_to_speech_with_elevenlabs(input_text=test_text, output_filepath="elevenlabs_testing.mp3")