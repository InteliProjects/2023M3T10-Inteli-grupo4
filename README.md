# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="documentos/outros/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# Destiny

## Delfino

## 🧑‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/bianca-borges-969586206/">Bianca Borges Lins</a>
- <a href="https://www.linkedin.com/in/breno-santos-0843131b8/">Breno Arthur Guimarães Santos</a>
- <a href="https://www.linkedin.com/in/breno-santana-4a1912228/">Breno Santana de Lima</a> 
- <a href="https://www.linkedin.com/in/bruna-brasil-alexandre-734055214/">Bruna Brasil Alexandre</a> 
- <a href="https://www.linkedin.com/in/joão-paulo-santos-872753264/">João Paulo Santos</a>
- <a href="https://www.linkedin.com/in/leandro-dos-santos-gomes/">Leandro dos Santos Gomes</a> 

## 🧑‍🏫 Professores:
### Orientador(a) 
- <a href="https://www.linkedin.com/in/marcelo-gonçalves-phd-a550652/">Marcelo Luiz do Amaral Gonçalves</a>
### Instrutores
- <a href="https://www.linkedin.com/in/egondaxbacher/">Egon F Daxbacher</a>
- <a href="https://www.linkedin.com/in/flaviomarquesazevedo/">Flavio Marques Azevedo</a> 
- <a href="https://www.linkedin.com/in/francisco-escobar/">Francisco Escobar</a> 
- <a href="https://www.linkedin.com/in/michele-bazana-de-souza-69b77763/">Michele Banzana de Souza</a>
- <a href="https://www.linkedin.com/in/ricardo-josé-missori/">Ricardo José Missori</a> 
- <a href="https://www.linkedin.com/in/victorbarq/">Laísa Ribeiro</a>

## 📝 Descrição


A Comissão de Valores Mobiliários (CVM) desempenha um papel crucial na fiscalização do mercado mobiliário, baseado em seus valores de transparência, proteção do investidor e desenvolvimento saudável do mercado de investimentos. Portanto, o projeto proposto visa resolver o desafio enfrentado pela CVM no que diz respeito à supervisão de Fundos de Investimento em Direitos Creditórios (FIDCs), que podem apresentar elevados níveis de inadimplência e possíveis irregularidades.

A solução proposta consiste no desenvolvimento de um modelo preditivo que utiliza dados relacionados aos FIDCs e seus créditos cedidos. Esse modelo tem como objetivo principal identificar potenciais riscos associados à provisão para eventuais perdas decorrentes da inadimplência dos créditos. Além disso, busca analisar e compreender os padrões e tendências presentes nesses dados, fornecendo insights à CVM para ação preventiva.

Em última análise, o projeto pretende auxiliar a CVM a tomar medidas proativas para minimizar riscos, preservar a integridade do mercado de capitais brasileiro e garantir a transparência e segurança para os investidores, cumprindo assim sua missão de supervisão eficaz do mercado mobiliário no país.

## 📁 Estrutura de pastas

Dentre os arquivos presentes na raiz do projeto, definem-se:

- <b>readme.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>documentos</b>: aqui estarão todos os documentos do projeto. Há também duas pastas denominadas <b>outros</b> onde estão presentes documentos complementares e <b>img</b> aqui estarão todas as imagens do projeto


- <b>notebooks</b>: todos os Jupyter Notebooks criados para desenvolvimento do projeto.

- <b>frontend</b>: todos os arquivos criados que fazem parte da interface (frontend) do projeto.

## 💻 Execução dos projetos

Este projeto foi desenvolvido no Visual Studio Code e deve ser executado no mesmo ambiente. Para iniciar o projeto, siga os passos abaixo:

1. **Instalação do Visual Studio (se ainda não estiver instalado):**
   - Se o Visual Studio não estiver instalado no seu sistema, faça o download e instale a versão apropriada para o seu sistema operacional a partir do site oficial do Visual Studio.

2. **Abertura do Jupyter Notebook:**
   - Abra o Visual Studio.

3. **Importando o Jupyter Notebook:**
   - No Visual Studio, clique em "File" (Arquivo) no menu superior e selecione "Open" (Abrir).
   - Navegue até o local onde o seu Jupyter Notebook está salvo (notebboks/Destiny_resume.ipynb) e selecione o arquivo.

4. **Instalação das Dependências:**
   - No Jupyter Notebook, procure e execute as células que instalam as bibliotecas necessárias. Elas devem estar comentadas como no exemplo abaixo:

    ```python
    # Instalando as bibliotecas 
    #%pip install Jupyter
    #%pip install pandas 
    #%pip install numpy
    #%pip install imblearn
    #%pip install lazypredict
    #%pip install scikit-learn
    ```

    Para executar esta célula e instalar as dependências, selecione tudo com Ctrl+A, depois com Ctrl+; com a célula selecionada, pressione Shift+Enter.

5. **Adição de Dados:**
   - Na pasta "dataset", adicione o informe mensal com as colunas do arquivo "nome_das_colunas.csv" com o nome "IM_semNP.csv".

6. **Executando Todas as Células:**
   - Após instalar todas as dependências e adicionar o arquivo, localize o botão "Run All" no menu superior do Jupyter Notebook e clique nele para executar todas as células do notebook.

7. **Execução do Modelo:**
   - Após a execução bem-sucedida, você pode encontrar o código para executar o modelo preditivo. Isso pode estar em uma célula específica rotulada como "Modelo Preditivo" ou algo semelhante.

**Resultados:**
Os resultados do modelo serão exibidos na pasta "dataset" no arquivo "resultado_modelo_rf.pkl".


## 🗃 Histórico de lançamentos

Neste tópico estão registrados os lançamentos ao longo do módulo.

* 1.0.0 - 06/10/2023
    * Protótipo final do projeto
* 0.8.4 - 06/10/2023
    * Adição do video de execução do modelo
* 0.8.3 - 05/10/2023
    * Documentação finalizada
* 0.8.2 - 03/10/2023
    * Aperfeiçoamento da documentação
* 0.8.1 - 03/10/2023
    * Atualização do Jupyter Notebook
* 0.8.0 - 02/10/2023
    * Adição de comentários no código
* 0.7.8 - 27/09/2023
    * Atualização do Jupyter Notebook
* 0.7.7 - 27/09/2023
    * Atualização do front end
* 0.7.6 - 26/09/2023
    * Atualização do Jupyter Notebook
* 0.7.5 - 25/09/2023
    * Revisão da documentação
* 0.7.4 - 25/09/2023
    * Atualização da documentação
* 0.7.3 - 21/09/2023
    * Construção do front end
* 0.7.2 - 20/09/2023
    * Atualização do Jupyter Notebook
* 0.7.1 - 20/09/2023
    * Criação da pasta "frontend"
* 0.7.0 - 19/09/2023
    * Atualização do Jupyter Notebook
* 0.6.11 - 15/09/2023
    * Atualização do histórico de lançamentos do ReadMe
* 0.6.10 - 13/09/2023
    * Atualização do Jupyter Notebook
* 0.6.9 - 12/09/2023
    * Atualização do Jupyter Notebook
* 0.6.8 - 08/09/2023
    * Atualização do Jupyter Notebook
* 0.6.7 - 08/09/2023
    * Correção do link da seção 4.3
* 0.6.6 - 07/09/2023
    * Revisão da documentação
* 0.6.5 - 06/09/2023
    * Revisão da documentação
* 0.6.4 - 05/09/2023
    * Revisão da documentação
* 0.6.3 - 05/09/2023
    * Atualização da seção 4.3
* 0.6.2 - 05/09/2023
    * Preenchimento da seção 4.3
* 0.6.1 - 04/09/2023
    * Atualização do Jupyter Notebook
* 0.6.0 - 28/08/2023
    * Preenchimento das seções 2 (completa) e 3.6
* 0.5.11 - 27/08/2023
    * Atualização da seção 4.2.1.1
* 0.5.10 - 24/08/2023
    * Preenchimento da seção 4.2.3
* 0.5.10 - 24/08/2023
    * Revisão da documentação e adição de gráficos
* 0.5.9 - 24/08/2023
    * Atualização do Jupyter Notebook
* 0.5.8 - 24/08/2023
    * Atualização da seção 4.2.1
* 0.5.7 - 24/08/2023
    * Atualização do ReadMe
* 0.5.6 - 23/08/2023
    * Adição de códigos no Jupyter Notebook
* 0.5.5 - 23/08/2023
    * Atualização da seção 4.1.7
* 0.5.4 - 22/08/2023
    * Preenchimento da seção 4.2.1.1
* 0.5.3- 21/08/2023
    * Preenchimento da seção 4.2.1
* 0.5.1 - 21/08/2023
    * Correção do link das imagens
* 0.5.0 - 17/08/2023
    * Preenchimento da seção 4.2.2
* 0.4.7 - 13/08/2023
    * Atualização seção 1.1.2
* 0.4.6 - 11/08/2023
    * Preenchimento da seção 3.1, 3.2, 3.3, 3.4, 3.5
* 0.4.5 - 11/08/2023
    * Preenchimento da seção 4.1.7
* 0.4.4 - 10/08/2023
    * Preenchimento da seção 4.1.4
* 0.4.3 - 10/08/2023
    * Preenchimento da seção 4.1.5
* 0.4.2 - 10/08/2023
    * Preenchimento da seção 4.1.8
* 0.4.1 - 09/08/2023
    * Preenchimento da seção 4.1.6 
* 0.4.0 - 09/08/2023
    * Criação da pasta "img" para armazenar imagens
* 0.3.2 - 08/08/2023
    * Criação da introdução da documentação
* 0.3.1 - 07/08/2023
    * Preenchimento da seção  1.1.1
* 0.3.0 - 07/08/2023
    * Preenchimento da seção 1.1.2
* 0.2.2 - 07/08/2023
    * Atualização de nomenclaturas da solução e do grupo (código do módulo permanece inalterado).
* 0.2.1 - 25/01/2022
    * Atualização de documentos (código do módulo permanece inalterado).
* 0.2.0 - 15/01/2022
    * Remove `setDefaultXYZ()`
    * Adiciona `init()`
* 0.1.1 - 11/01/2022
    * Crash quando chama `baz()`
* 0.1.0 - 10/01/2022
    * O primeiro lançamento adequado
    * Renomeia `foo()` para `bar()`
* 0.0.1 - 01/01/2022
    * Trabalho em andamento

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Spidus/Teste_Final_1">DELFINO</a> by <a href="https://github.com/2023M3T10-Inteli">Inteli</a>, <a href="https://www.linkedin.com/in/bianca-borges-969586206/">Bianca Borges Lins, </a><a href="https://www.linkedin.com/in/breno-santos-0843131b8/">Breno Arthur Guimarães Santos, </a><a href="https://www.linkedin.com/in/breno-santana-4a1912228/">Breno Santana de Lima, </a><a href="https://www.linkedin.com/in/bruna-brasil-alexandre-734055214/">Bruna Brasil Alexandre, </a><a href="https://www.linkedin.com/in/joão-paulo-santos-872753264/">João Paulo Santos e </a><a href="https://www.linkedin.com/in/leandro-dos-santos-gomes/">Leandro dos Santos Gomes</a>  is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
