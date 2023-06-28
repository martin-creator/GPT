# How my alexa works in Africa
# The user asks a question using their microphone. We will use Python SpeechRecognition⁴⁶.
# • OpenAI Whisper automatically transcribes the question into a text.
# • The text is passed to OpenAI GPT completions endpoints
# • The OpenAI API returns an answer
# • The answer is saved to an mp3 file and passed to Google Text to Speech (gTTS) to create a
# voice response.



# Recording the audio
# We will use the Python SpeechRecognition library to record the audio

def record_audio(audio_queue, energy, pause, dynamic_energy):
    """
        • audio_queue: a queue object where the recorded audio will be saved.
        • energy: an initial energy threshold for detecting speech.
        • pause: a pause threshold for detecting when speech has ended.
        • dynamic_energy: a Boolean indicating whether the energy threshold should be adjusted
          dynamically based on the surrounding environment
    """
    # load the speec recognizer and set the intial energy threshold snd pause threshold
    r = sr.Recognizer()
    r.energy_threshold = energy
    r.pause_threshold = pause
    r.dynamic_energy_threshold = dynamic_energy


    # use the microphone as source for input
    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        i = 0

        while True:
            # get and save audio to wav file
            audio = r.listen(source)

        # Using: https://github.com/openai/whisper/blob/9f7016 532bd8c21d/whisper/audio.py
            torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
            # we use 32768.0 becasue the audio is 16 bit and we want to normalize it to -1 to 1
            audio_data = torch_audio
            audio_queue.put_nowait(audio_data)
            i += 1


# Transcribing the audio
# OpenAI Whisper automatically transcribes the question into a text.

def transcribe_forever(audio_queue, result_queue, audio_model, english, wake_word, verbose):
    while True:
        audio_data = audio_queue.get()
        if english:
            result = audio_model.transcribe(audio_data, language="english", verbose=verbose)
        else:
            result = audio_model.transcribe(audio_data)

        predicted_text = result["text"]

        if predicted_text.strip().lower().startswith(wake_word.strip().lower()):
            pattern = re.comile(re.escape(wake_word), re.IGNORECASE)
            predicted_text = pattern.sub("", predicted_text).strip()
            punc = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
            predicted_text.translate({ord(char): None for char in punc})
            if verbose:
                print("You said the wake word ... Processing {}".format(predicted_text))
            result_queue.put_nowait(predicted_text)
        else:
            if verbose:
                print("You did not say the wake word .. Ignoring")
