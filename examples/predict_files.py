from soundnet import SoundNet

s = SoundNet()
s.model_summary()

prediction = s.predict_from_audio_file('Forest Track 2.mp3')
print(s.predictions_to_places(prediction))
# [('forest_path', 1.0)]

prediction = s.predict_from_audio_file('railroad_audio.wav')
print(s.predictions_to_places(prediction))
# [('railroad_track', 0.46153846153846156),
# ('train_station/platform', 0.41025641025641024),
# ('highway', 0.1282051282051282)]

prediction = s.predict_from_audio_file('storm.mp3')
print(s.predictions_to_places(prediction))
# [('aquarium', 0.321875),
# ('sky', 0.24875),
# ('rainforest', 0.23),
# ('ocean', 0.089375),
# ('train_station/platform', 0.034375),
# ('beach', 0.02125),
# ('ski_slope', 0.013125),
# ('catacomb', 0.011875),
# ('railroad_track', 0.011875),
# ('train_railway', 0.01),
# ('underwater/coral_reef', 0.005625),
# ('crosswalk', 0.00125),
# ('art_gallery', 0.000625)]
