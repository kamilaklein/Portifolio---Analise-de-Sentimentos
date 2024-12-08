# Análise de sentimentos e comportamento no mercado artesanal de velas aromáticas

## Objetivo Principal:

O objetivo principal é investigar e entender o comportamento dos consumidores e analisar sentimentos sobre velas aromaticas no YouTube. Este estudo visa identificar padrões de engajamento e as preferências dos usuários ao terem o contato com conteúdos educacionais e de "faça você mesmo", relacionados ao mercado artesanal de velas. Através das informações obtidas pode-se apoiar artesãos e empresas a criar produtos e conteúdos alinhados às expectativas do público.

## Escopo:

O projeto foca na coleta de dados de videos no YouTube, especialmente tutoriais sobre velas aromaticas. Nesta análise incluimos:

• Coleta dos comentarios, curtidas e outras interações em vídeos de tutoriais;

• Processamento dos dados coletados para identificar sentimentos (positivos, neutros e negativos) e emoções específicas como (alegria, surpresa, raiva, tristeza ou desgosto).

• Identificação de temas e técnicas mais valorizados e aspectos onde os usuários demonstram maior interesse ou necessidade de esclarecimento.

## Tecnologias utilizadas:

• Python: Linguagem principal para processamento e análise dos dados.
• NLTK

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

**Pacote 1: Preparação do Projeto**  

Configurar o ambiente de desenvolvimento:    

• Criar containers Docker para PostgreSQL;  
• Criar um Docker Compose para orquestrar os serviços;  

Criar banco de dados no PostgreSQL:    

• Estruturar tabelas (videos, comentarios).  

**Pacote 2: Coleta de Dados do YouTube - Desenvolver script de coleta de dados:** 

• Implementar busca de vídeos pela API do YouTube;  
• Coletar informações de vídeos e salvar no banco de dados;  
• Coletar comentários e aplicar filtro de idioma;   

**Pacote 3: Análise de Sentimentos**

Implementar análise de sentimentos:    

• Integrar modelo de análise de polaridade;  
• Integrar modelo de análise de emoções;  
• Atualizar resultados no banco;  

Criar funções de pré-processamento:     

• Limpar e normalizar textos;  
• Detectar idioma e filtrar apenas comentários em português;  

Testar modelos de análise:    

• Aplicar testes de acurácia com dados rotulados;  
• Gerar relatórios de classificação e acurácia;  

**Pacote 4: Visualização de Resultados - Criar visualização no Streamlit:**  

• Desenvolver gráficos de polaridade e emoções;  
• Criar nuvem de palavras;  
• Implementar análise temporal;  

**Pacote 5: Documentação e Relatórios**     
 
Documentar o projeto:    

• Criar README no GitHub com as instruções de uso;  
• Detalhar a estrutura do banco de dados e o fluxo do programa;  

Preparar relatório para o TCC:    

• Explicar os métodos utilizados (coleta, análise, visualização);  
• Apresentar gráficos e insights obtidos;  
• Criar slide de apresentação final;  
 
**Pacote 6: Trabalhos Futuros - Planejar melhorias no projeto:**    

• Estender análise para outras palavras-chave ou idiomas;  
• Criar uma aplicação web completa para usuários finais.  

