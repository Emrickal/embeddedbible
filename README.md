# embeddedbible

Solutions to issues encountered with original code:

Within genwordmodel.py - size parameter needs to be changed to (line 20):
    vector_size = WORD2VEC_SIZE

Within analyzemodel.py - the most_similar tag needs updated to: model.wv.most_similar for lines 56 and 58 only.
    result = model.most_similar(positive=['god'], negative=['jesus'], topn=20)
    print('god - jesus\n', result)
    result = model.most_similar(positive=['jesus'], negative=['god'], topn=20)
    print('jesus - god\n', result)

Within genphrasemodels.py - Needed to uncomment line 150 to build the book model.

I am running Python3 - Python 3.10.4 and had to pip install the following packages to allow all programs to work:

  tensorflow
  tensorflow-hub
  nltk
  sklearn
  gensim
  numpy
  matplot
  spacy
 
Once NLTK was installed, I had to import nltk stopwords and punkt. I did this my accessing python3 console and running the following commands:

    import nltk
    nltk.download('stopwords')
    import nltk
    nltk.download('punkt')

Finally, I had to manually create the following folders for the output of the code to work:
    Models
    Charts


This project is discussed <a href="https://www.christopherminson.com/articles/aibible.html">here</a>
<p>

File Descriptions
<p>
genwordmodel - generates the Word2Vec model.
<br>
genphrasemodels - generates the Sentence2Vec models, for all books and sentences
<br>
gencharts - generates the books similarity chart
<br>
textinput - reads and parses the Bible's text
<br>
analyzemodels  - reads in models and runs various test queries
<p>

