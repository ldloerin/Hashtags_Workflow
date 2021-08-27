# Hashtag generator

Running the source code ./Source/hashtag_generator.py will write a number or random hashtag lists to the output file ./Source/Output/Random/Hashtags.txt

The number of these list can be defined by the value "number_of_random_lists" in the configuration file ./Source/Input/config.json. Each random hashtag list has a length of 30 item, which can not be adjusted.

The hashtag lists contain a list of essential hashtags (./Source/Input/AllEssentialHashtags.txt). These are hashtags that will be included in every output list. This list must not be longer than 30 to avoud a failure of the code. Ideally the essential hashtag should be 10 to 15 expressions. The list ./Source/Input/AllGeneralHashtags.txt is used to fill up the gap between the essentail hashtag list and the desired 30 hashtags.