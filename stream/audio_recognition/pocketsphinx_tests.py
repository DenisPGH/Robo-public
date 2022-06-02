# from pocketsphinx import LiveSpeech
# """
# pip install Cmake
# pip install pyaudio
# in cmd :pip install pocketsphinx-0.1.15-cp310-cp310-win_amd64.whl
# """
# for phrase in LiveSpeech():
#     print(phrase)

import os
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()


speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'en-us'),
    lm=os.path.join(model_path, 'en-us.lm.bin'),
    dic=os.path.join(model_path, 'cmudict-en-us.dict')
)

"""
fst = voxforge-de.fst
hmm folder = model_parameters/voxforge.cd_cont_6000
dictionary = cmusphinx-voxforge-de.dic
language model = cmusphinx-voxforge-de.lm.gz
"""

print('Start recording....')
for phrase in speech:
    print(phrase)

print('STOP recording!!!')

