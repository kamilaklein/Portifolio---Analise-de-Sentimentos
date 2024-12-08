# Índice:

- [Objetivo Principal:](#objetivo-principal)
- [Escopo:](#escopo)  
- [Requisitos:](#requisitos)  
- [Pacotes de entregas:](#pacotes-de-entregas)    
- [Tecnologias utilizadas:](#tecnologias-utilizadas)    
- [Bibliotecas:](#bibliotecas)  
- [Diagramas](#diagramas)  

# Análise de sentimentos e comportamento no mercado artesanal de velas aromáticas  

## Objetivo Principal:

O objetivo principal é investigar e entender o comportamento dos consumidores e analisar sentimentos sobre velas aromaticas no YouTube. Este estudo visa identificar padrões de engajamento e as preferências dos usuários ao terem o contato com conteúdos educacionais e de "faça você mesmo", relacionados ao mercado artesanal de velas. Através das informações obtidas pode-se apoiar artesãos e empresas a criar produtos e conteúdos alinhados às expectativas do público.

## Escopo:

O projeto foca na coleta de dados de videos no YouTube, especialmente tutoriais sobre velas aromaticas. Nesta análise incluimos:

• Coleta dos comentarios, curtidas e outras interações em vídeos de tutoriais;

• Processamento dos dados coletados para identificar sentimentos (positivos, neutros e negativos) e emoções específicas como (alegria, surpresa, raiva, tristeza ou desgosto).

• Identificação de temas e técnicas mais valorizados e aspectos onde os usuários demonstram maior interesse ou necessidade de esclarecimento.

## Requisitos do projeto:

### Requisitos Funcionais

**RF01:** A aplicação deve ser capaz de coletar informações de vídeos tutoriais sobre velas aromáticas, incluindo título, descrição, data de publicação, número de visualizações, curtidas e comentários.  
**RF02:** Deve acessar a API do YouTube para capturar comentários e metadados relevantes.  
**RF03:** A aplicação deve utilizar técnicas de PLN para analisar o conteúdo textual dos comentários, identificando sentimentos expressos pelos usuários.  
**RF04:** Deve classificar os sentimentos em categorias (positivos, negativos e neutros) e explorar sentimentos mais específicos, como emoções (felicidade, raiva, surpresa, etc.).  
**RF05:** A aplicação deve identificar padrões e tendências nos comentários, como termos frequentemente usados e temas relevantes relacionados aos tutoriais.  
**RF06:** A aplicação deve apresentar os resultados da análise por meio de gráficos interativos e visualizações dinâmicas, acessíveis em uma interface gráfica.  
**RF07:** Deve incluir visualizações como nuvens de palavras, gráficos de sentimentos e tendências temporais.  
**RF08:** Deve permitir a exportação dos resultados da análise para formatos como CSV.  


### Requisitos não Funcionais:

**RF01:** A aplicação deve ser capaz de lidar com a análise de comentários de até 25 vídeos por vez, garantindo desempenho consistente.  
**RF02:** A aplicação deve atingir pelo menos 85% de precisão na análise de sentimentos para evitar erros significativos de classificação.  
**RF03:** Os dados coletados devem ser tratados de forma anônima, sem associar informações pessoais aos usuários.  
**RF04:** A aplicação deve apresentar os resultados da análise por meio de gráficos interativos e visualizações dinâmicas, acessíveis em uma interface gráfica.  
**RF05:** A aplicação deve seguir as políticas de privacidade e uso da API do YouTube, garantindo conformidade com as regulamentações de dados.  
**RF06:** A interface deve ser intuitiva, permitindo fácil navegação entre diferentes visualizações e exportações.  
**RF07:** Deve suportar diferentes navegadores (Chrome, Firefox, Edge) e ser responsivo em desktops.  

## Pacotes de entregas:

**Pacote 1: Preparação do Projeto**  
**Pacote 2: Coleta de Dados do YouTube**   
**Pacote 3: Análise de Sentimentos**  
**Pacote 4: Visualização de Resultados**    
**Pacote 5: Documentação e Relatórios**       
**Pacote 6: Trabalhos Futuros**  

[Mais informações sobres os pacotes](PacotesEntrega.md)  



## Tecnologias Utilizadas:

- **Linguagem de Programação:** Python
- **Banco de Dados:** PostgreSQL
- **Ferramentas de Desenvolvimento:**
  - Visual Studio Code
  - Docker (gerenciar o ambiente de desenvolvimento)
  - DBeaver (consulta no banco de dados)
- **Ferramentas de Gerenciamento e Controle:**
  - Jira
  - GitHub
  

## Bibliotecas Utilizadas:

#### Processamento de Linguagem Natural (PLN):
- **NLTK**: Tokenização, remoção de stop words, manipulação de sentenças.
- **spaCy**: Manipulação de textos, análise gramatical, extração de informações.
- **Langdetect**: Detecção de idiomas.
- **Emoji**: Remoção ou análise de emojis.
- **Hugging Face Transformers**: Ferramentas para modelos pré-treinados.
- **BERT**: Modelo de linguagem baseado em Transformers.

#### Manipulação de Dados:
- **Pandas**: Manipulação de dados estruturados, tabelas, e arquivos CSV.
- **re**: Módulo nativo do Python para limpeza e processamento de textos dos comentários.

#### Visualização de Dados:
- **Streamlit**: Framework para criação de interfaces web interativas.
- **Plotly Express**: Criação de gráficos interativos.
- **Matplotlib**: Gráficos estáticos e visualizações de dados.
- **Wordcloud**: Ferramenta para criar nuvens de palavras.  

#### Machine Learning:
- **Scikit-learn**: Implementação de modelos de aprendizado supervisionado.  


## Diagramas:  

- [Diagrama de Atividades](Diagramas/Diagramadeatividade.md)
- [Diagrama ER](Diagramas/DiagramaER.md)    



