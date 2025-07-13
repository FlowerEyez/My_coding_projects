import pvporcupine
import pyaudio
import struct

def wait_for_wake_word():
    access_key = "qNgF6G5GhyyEXPHEcp+dyGqshh6V5vcHcHyHKYhPS39l+XfedwNTFw=="
    porcupine = pvporcupine.create(
        access_key=access_key,
        keywords=["computer"] # or any other wake word.
        )

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate = porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🎤 Listening for wake word...")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm_unpacked)
            if keyword_index >= 0:
                print("👋 Wake word detected!")
                return # Goes back to main.py
    finally:
        stream.stop_stream()
        stream.close()
        porcupine.delete()
        pa.terminate()