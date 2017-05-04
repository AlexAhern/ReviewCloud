from wordcloud import WordCloud
from PIL import Image
import numpy as np
import pandas
import string

file="netflix.csv"
wordlist=""
data = pandas.read_csv(file)
reviews = data['Content']
reviews=[x.translate(None, string.punctuation).lower().split() for x in reviews]
for review in reviews:
	wordlist+=" ".join(review)

wordcloud = WordCloud(width=1680, height=1050).generate(wordlist)

wordcloud.to_file("netflixios.png")

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
