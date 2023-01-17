#
# Author: Christopher Minson 
# www.christopherminson.com
# 
#

import os
import numpy as np
import matplotlib.pyplot 
import sklearn.manifold
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import gensim
import textinput

RS = 25111993
CHART_PATH = './CHARTS/'
MODEL_PATH = './MODELS/'

def plot_similar_books(matrix, chart_name):

    coordinates2D = sklearn.manifold.TSNE(random_state=RS).fit_transform(matrix)
    x = coordinates2D[:,0]
    y = coordinates2D[:,1]
    print('coord books', coordinates2D.shape, 'matrix', matrix.shape)

    colors = []
    sizes = []

    for book in textinput.ALL_BOOKS:
        if book in textinput.BOOKS_OLD_TESTAMENT: color = 'red'
        if book in textinput.BOOKS_NEW_TESTAMENT: color = 'green'
        if book in textinput.BOOKS_APOCRYPHA: color = 'grey'

        colors.append(color)
        sizes.append(1600)

    matplotlib.pyplot.scatter(x, y, s=sizes, alpha=0.4, color=colors)

    for book_index, book_name in enumerate(textinput.ALL_BOOKS):
        matplotlib.pyplot.text(x[book_index], y[book_index], book_name, fontsize=6, ha='center', va='center')

    cur_axes = matplotlib.pyplot.gca()
    cur_axes.axes.get_xaxis().set_ticklabels([])
    cur_axes.axes.get_yaxis().set_ticklabels([])

    print(chart_name)
    matplotlib.pyplot.savefig(chart_name, dpi=120)

def plot_word_vectors(word_list, matrix, chart_name):

    coordinates2D = sklearn.manifold.TSNE(random_state=RS).fit_transform(matrix)
    x = coordinates2D[:,0]
    y = coordinates2D[:,1]
    print('x', x)
    print('y', y)
    print('coord words', coordinates2D.shape, 'matrix', matrix.shape)

    colors = []
    sizes = []

    for i in range(len(x)):
        colors.append('green')
        sizes.append(2500)

    matplotlib.pyplot.scatter(x, y, s=sizes, alpha=0.4, color=colors)

    for word_index, word_name in enumerate(word_list):
        matplotlib.pyplot.text(x[word_index], y[word_index], word_name, fontsize=6, ha='center', va='center')

    cur_axes = matplotlib.pyplot.gca()
    cur_axes.axes.get_xaxis().set_ticklabels([])
    cur_axes.axes.get_yaxis().set_ticklabels([])

    matplotlib.pyplot.savefig(chart_name, dpi=120)


if __name__ == '__main__':

    MODEL_BOOKS = 'model.books.npy'

    matrix  = np.load(MODEL_PATH + MODEL_BOOKS)
    plot_similar_books(matrix, CHART_PATH + 'biblebooks.png')



