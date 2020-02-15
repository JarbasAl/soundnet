from soundnet import SoundNet

s = SoundNet()
s.model_summary()


def my_callback(prediction):
    places = s.predictions_to_places(prediction)
    print(places)


s.set_callback(my_callback)
s.run()
