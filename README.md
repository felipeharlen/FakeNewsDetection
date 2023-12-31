# FakeNewsDetection

 Proposta de detecção automática de fake news em textos em português usando Aprendizagem de Máquina e Redes Neurais Convolucionais com a base de dados Fake.Br Corpus. Análise de padrões em textos e metadados para identificar conteúdos falsos. Este projeto visa a identificação automática de notícias falsas (fake news) em textos escritos em Língua Portuguesa. Utilizamos algoritmos de Aprendizagem de Máquina e Redes Neurais Convolucionais para analisar padrões em notícias escritas em Português, permitindo a detecção precisa de conteúdos enganosos.

## Visão Geral

A solução utiliza o Fake.Br Corpus, uma base de dados com 7.200 artigos de notícias em Português, para treinamento e validação do modelo. Nesta análise, são utilizados tanto os textos das notícias quanto seus respectivos metadados.

### Características Principais

- **Uso de Redes Neurais Convolucionais**: Utilizamos Redes Neurais Convolucionais (CNN) para análise semântica de textos, permitindo a detecção de padrões complexos.

- **Uso de Algoritmos de Machine Learning**: São aplicados os algoritmos Support Vector Machine (SVM), Multilayer Perceptron (MLP) e Naive Bayes (NB) para reconhecimento de padrões sobre os metadados.

- **Emsemble**: Ao final, os dois modelos (CNN para texto e o modelo com melhor desempenho para os metadados) são combinados, aplicando-se pesos otimizados com Gradiente Descendente, para a classificação final.

---

**Nota**: Este projeto está em constante desenvolvimento e melhorias. Fique à vontade para explorar, contribuir e fazer parte do esforço para combater a disseminação de fake news em Português.
