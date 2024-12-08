# Análise de sentimentos e comportamento no mercado artesanal de velas aromáticas

# Índice:

- [Objetivo Principal:](#objetivo-principal)
- [Escopo:](#escopo)  
- [Requisitos:](#requisitos)  
- [Pacotes de entregas:](#pacotesdeentregas)    
- [Tecnologias utilizadas:](#tecnologiasutilizadas)    
- [Bibliotecas:](#bibliotecas)

## Objetivo Principal:

O objetivo principal é investigar e entender o comportamento dos consumidores e analisar sentimentos sobre velas aromaticas no YouTube. Este estudo visa identificar padrões de engajamento e as preferências dos usuários ao terem o contato com conteúdos educacionais e de "faça você mesmo", relacionados ao mercado artesanal de velas. Através das informações obtidas pode-se apoiar artesãos e empresas a criar produtos e conteúdos alinhados às expectativas do público.

## Escopo:

O projeto foca na coleta de dados de videos no YouTube, especialmente tutoriais sobre velas aromaticas. Nesta análise incluimos:

• Coleta dos comentarios, curtidas e outras interações em vídeos de tutoriais;

• Processamento dos dados coletados para identificar sentimentos (positivos, neutros e negativos) e emoções específicas como (alegria, surpresa, raiva, tristeza ou desgosto).

• Identificação de temas e técnicas mais valorizados e aspectos onde os usuários demonstram maior interesse ou necessidade de esclarecimento.

## Requisitos:

### Requisitos Funcionais

RF01: A aplicação deve ser capaz de coletar informações de vídeos tutoriais sobre velas aromáticas, incluindo título, descrição, data de publicação, número de visualizações, curtidas e comentários.  
RF02: Deve acessar a API do YouTube para capturar comentários e metadados relevantes.  
RF03: A aplicação deve utilizar técnicas de PLN para analisar o conteúdo textual dos comentários, identificando sentimentos expressos pelos usuários.  
RF04: Deve classificar os sentimentos em categorias (positivos, negativos e neutros) e explorar sentimentos mais específicos, como emoções (felicidade, raiva, surpresa, etc.).  
RF05: A aplicação deve identificar padrões e tendências nos comentários, como termos frequentemente usados e temas relevantes relacionados aos tutoriais.  
RF06: A aplicação deve apresentar os resultados da análise por meio de gráficos interativos e visualizações dinâmicas, acessíveis em uma interface gráfica.  
RF07: Deve incluir visualizações como nuvens de palavras, gráficos de sentimentos e tendências temporais.  
RF08: Deve permitir a exportação dos resultados da análise para formatos como CSV.  


### Requisitos não Funcionais:

RF01: A aplicação deve ser capaz de lidar com a análise de comentários de até 25 vídeos por vez, garantindo desempenho consistente.  
RF02: A aplicação deve atingir pelo menos 85% de precisão na análise de sentimentos para evitar erros significativos de classificação.  
RF03: Os dados coletados devem ser tratados de forma anônima, sem associar informações pessoais aos usuários.  
RF04: A aplicação deve apresentar os resultados da análise por meio de gráficos interativos e visualizações dinâmicas, acessíveis em uma interface gráfica.  
RF05: A aplicação deve seguir as políticas de privacidade e uso da API do YouTube, garantindo conformidade com as regulamentações de dados.  
RF06: A interface deve ser intuitiva, permitindo fácil navegação entre diferentes visualizações e exportações.  
RF07: Deve suportar diferentes navegadores (Chrome, Firefox, Edge) e ser responsivo em desktops.  

## Pacotes de entregas:

[Mais informações sobres os pacotes](PacotesEntrega.md)

**Pacote 1: Preparação do Projeto**  
**Pacote 2: Coleta de Dados do YouTube**   
**Pacote 3: Análise de Sentimentos**  
**Pacote 4: Visualização de Resultados**    
**Pacote 5: Documentação e Relatórios**       
**Pacote 6: Trabalhos Futuros**     


## Tecnologias utilizadas:

Linguagens de programação: **Python**  
Banco de dados: **PostgreSQL**  
Ferramentas:  
 • Jira  
 • Visual Studio Code  
 • Docker (gerenciar o ambiente de desenvolvimento)  
 • Dbeaver (consulta no banco de dados)  
 • GitHub   

## Bibliotecas:
 
• NLTK (PLN, tokenização, remoção de stop words, sentenças);  
• spaCy (PLN, p/ manipulação de textos, analise gramatical, extração de informações);  
• Pandas (p/ manipulação de dados estruturados, tabelas e dados em formato CSV);  
• Langdetect (detectar idioma);  
• Streamlit (framework p/ interfaces web interativas);  
• Plotly.express (gráficos interativos);  
• Matplotlib (gráficos estáticos e visualizações de dados);  
• Scikit-learn (modelos de aprendizado supervisionado);  
• Wordcloud (ferramenta p/ criar nuvem de palavras);   
• re (módulo da biblioteca Python, limpa e processa textos dos comentários);  
• Emoji (remover ou analisa-los);  
• Hugging Face Transformers (fornece ferramentas p/ modelos pré-treinados);  
• BERT (modelo de linguagem baseado em Transformers);  




