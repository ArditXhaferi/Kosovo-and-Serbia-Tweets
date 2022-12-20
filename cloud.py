import networkx as nx
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from langdetect import detect
import random

def create_cloud(text, colors = ['red', 'blue'], filename="test"):

    wc = WordCloud(background_color='white', width=1080, height=1080, font_path='font.ttf')
    wc.generate(' '.join(text))

    def word_to_color(word, font_size, position, orientation, random_state=None, **kwargs):
        return colors[random.choice([0, 1])]

    wc.recolor(color_func=word_to_color)

    plt.imshow(wc)
    plt.savefig(f"./images/{filename}.png")