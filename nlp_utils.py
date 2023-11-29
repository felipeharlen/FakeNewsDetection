import numpy as np
import nltk
import re
import urlextract
import unicodedata
import fasttext

from glob import glob
from tqdm.notebook import tqdm
from nltk.tokenize import word_tokenize

def extract_data(data_path, label):
    dir_data = glob(data_path + label + '/*.txt')
    array = []

    # Capturando dados das notícias
    for path in tqdm(dir_data):
        with open(path, encoding='utf-8') as file:
            text = file.read()
        array.append([text, label])   
         
    return array

def preprocessing(data, remove_stopwords=True, remove_sc=True):

    pattern_words = re.compile(r'\b[a-zà-ÿ-]+\b') if remove_sc else re.compile(r'[^a-zà-ÿ- ,.:;?!()]')
    extractor = urlextract.URLExtract()
    preprocessed_texts = []

    for text in tqdm(data):
        # Verificando se o texto é nulo ou vazio
        if text is not None and isinstance(text, str) and text.strip() != "":
            text = text.lower()
            text = re.sub(r'["\']', '', text)
            text = ''.join(c for c in unicodedata.normalize('NFC', text) if unicodedata.category(c) != 'Mn')
            text = ' '.join([word for word in text.split() if not extractor.has_urls(word)])
            tokens = pattern_words.findall(text)
            
            if remove_stopwords:
                stopwords = set(nltk.corpus.stopwords.words("portuguese"))
                tokens = [token for token in tokens if token not in stopwords]
            
            preprocessed_texts.append(' '.join(tokens))

    return preprocessed_texts


def word_vec_matrix(embedding, word_index, vocabulary_size, embedding_dims):
    word_vector_matrix = np.zeros((vocabulary_size, embedding_dims))

    for word, index in word_index.word_index.items():
        vector = None

        if type(embedding) == fasttext.FastText._FastText:
            vector = embedding.get_word_vector(word)
        elif word in embedding:
            vector = embedding.get_vector(word)

        if vector is not None:
            word_vector_matrix[index] = vector
        else:
            print(word)
    
    return word_vector_matrix

def word_count(textos):
    # Baixe o recurso necessário para tokenização (se ainda não tiver baixado)
    # Lista para armazenar o número de palavras em cada texto
    num_palavras_por_texto = []

    # Itera sobre os textos e conta as palavras
    for texto in tqdm(textos):
        palavras_tokenizadas = word_tokenize(texto)
        num_palavras_por_texto.append(len(palavras_tokenizadas))

    return np.array(num_palavras_por_texto)