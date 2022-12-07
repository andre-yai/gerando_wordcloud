#==========
# Este arquivo contém o código utilizado para criar a nuvem de palavras.
# Este código necessita a instalação de bibliotecas python. 
#===========

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def get_dataset(filename):
    # Esta função pega dados da pesquisa
    stack_df = pd.read_csv(filename, sep=';')
    return stack_df

def preprocessamento_palavras(stack_df):
    # Esta função é responsável por normalizar as sentenças colocando tudo em letra minúscula e removendo espaços e caracteres.

    stack_df['stack_usada'] = stack_df['stack_usada'].str.lower()\
    .str.replace('\n', ', ')\
    .str.replace('+', ',')\
    .str.strip().str.replace(' ', '')\
    .str.strip().str.replace('.', '')
    return stack_df

def unindo_sentencas(stack_df):
    # Esta função é responsável por unir as respostas e devolver um único texto para a nuvem de palavras.

    stack_union_sentences = ','.join(stack_df['stack_usada'].values)
    return stack_union_sentences

def gera_wordcloud_grafico(stack_union_sentences, image_path):
    # Esta função gera a nuvem de palavras e salva  a imagem.

    wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
    wordcloud.generate(stack_union_sentences)
    plt.figure( figsize=(20,10) )
    plt.imshow(wordcloud)
    plt.savefig(image_path)

if __name__ == '__main__':
    filename = "data/dataset_respostas.csv"
    image_path = "imagens/wordcloud_stack.png"
    stack_df = get_dataset(filename)
    stack_processado_df = preprocessamento_palavras(stack_df)
    stack_union_sentences = unindo_sentencas(stack_processado_df)
    gera_wordcloud_grafico(stack_union_sentences, image_path)
