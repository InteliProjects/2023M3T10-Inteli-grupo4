# Documentação Modelo Preditivo - Inteli

## Destiny
### Delfino
#### Bianca Borges, Breno Santos, Breno Santana, Bruna Brasil, João Paulo, Leandro Gomes

## Sumário
[1. Introdução](#c1)

[2. Objetivos e Justificativa](#c2)

[3. Metodologia](#c3)

[4. Desenvolvimento e Resultados](#c4)

[5. Conclusões e Recomendações](#c5)

[6. Referências](#c6)

[Anexos](#attachments)

## <a name="c1"></a>1. Introdução
 &emsp;A CVM desempenha um papel fundamental como o órgão responsável pela fiscalização do mercado mobiliário em todo o território nacional, entre os seus principais valores encontra-se: transparência, proteção do investidor e desenvolvimento saudável do mercado de investimentos.  A empresa tem como principais funções o estabelecimento de normas, fiscalização de ações de empresas, educação de investidores e análise do mercado voltada a detecção de fraudes e irregularidades em diversos setores. No entanto, a CVM tem enfrentado desafios na previsão de  FIDCs (Fundos de Investimento em Direitos Creditórios) com elevados níveis de inadimplência e possíveis irregularidades, o que dificulta o comprimento de suas funções nessa área de valores mobiliários em ascensão.

### 1.1 Compreensão do Problema
#### 1.1.1 Contexto da indústria 

 &emsp;A Comissão de Valores Mobiliários(CVM) é uma autarquia, criada em 07 de Dezembro de 1976, vinculada ao ministério da Fazenda. Sua função é o controle e fiscalização do mercado de valores mobiliários no Brasil. Ela é a principal instituição que cuida da segurança dos investidores e da integridade e transparência do mercado financeiro brasileiro. A comissão é uma entidade reguladora, e não exatamente uma empresa ou orgazinação no sentido tradicional de competição entre empresas. Entretanto, existem outras entidades e órgãos que também exercem funções regulatórias e fiscais no mercado financeiro brasileiro, embora não sejam exatamentes concorrentes da CVM. Alguns desses órgãos são o Banco Central do Brasil (BCB), Superintendência de Seguros Privados (SUSEP) e o próprio Ministério da Fazenda. 

 &emsp;O modelo de negócio da CVM é essencialmente regulatório e fiscalizatório. A comissão estabelece regulamentos e regras que regem a emissão, negociação e a divulgação de informações sobre valores mobiliários.  Ela monitora as atividades das empresas emissoras, intermediários financeiros, gestores de fundos e todos os participantes do mercado de capitais. A CVM também é responsável por aprovar ofertas públicas de válores mobiliários, garantindo que os investidores possuam acesso a informações adequadas e relevantes antes de investir.

 &emsp;Com o avanço tecnológico, o mercado financeiro está evoluindo, como a adoção de plataforma digitais de investimentos, negociação algorítimica e a crecente das fintechs. A supervisão e a regulamentação dessas novas tendências viraram um desafio para a CVM, que precisa se adaptar e acompanhar às mudanças que a tecnologia traz.

 &emsp;Além disso, a globalização dos mercados financeiros exige uma maior cooperação entre os órgãos reguladores internacionais para previnir atividades ilegais. A CVM necessita estar alinhada com as normas internacionais e participar dos esforços de supervisão global para garantir a integridade do mercado financeiro.

 &emsp;O surgimento de novos ativos financeiros, como derivativos e criptomoedas, também exigem uma abordagem regulatória mais flexível e adaptável para garantir a estabilidade do mercado e a proteção dos investidores. 

 &emsp;Em conclusão, a Comissão de Valores Mobiliários é uma entidade reguladora e fiscalizadora do mercado de capitais do Brasil, que garante sua saúde e promove a segurança dos investidores. Com os avanços tecnológicos novos instrumento financeiros surgiram e a CVM vem se adaptando a essas mudanças.


#### 1.1.2 - 5 forças de porter

 &emsp;A análise das Cinco Forças de Porter busca analisar o cenário de uma empresa com relação ao mercado que está inserida, portanti na Figura 1 encontra-se a análise realizada pelo grupo sobre a CVM. Neste contexto, a análise é importante para que a empresa possa compreender melhor a dinâmica competitiva que enfrenta e possa desenvolver estratégias eficazes para se destacar no mercado. As Cinco Forças de Porter englobam a ameaça de novos entrantes, o poder de negociação dos fornecedores, o poder de negociação dos clientes, a ameaça de produtos substitutos e a intensidade da rivalidade entre os concorrentes existentes. Ao examinar cada uma dessas forças, a empresa pode identificar pontos de vantagem competitiva, áreas de vulnerabilidade e oportunidades de diferenciação.

 &emsp;No caso específico da análise da CVM (Comissão de Valores Mobiliários), a aplicação das Cinco Forças de Porter pode ajudar a entender como fatores como regulamentações, o poder das instituições financeiras, a influência dos investidores e a disponibilidade de alternativas de investimento podem impactar a atuação da CVM no mercado. Isso possibilita que a CVM tome decisões informadas para melhorar sua eficácia na supervisão e regulação do mercado de valores mobiliários.

 &emsp;Além disso, a análise das Cinco Forças também contribui para a identificação de possíveis mudanças no ambiente competitivo e permite que a empresa antecipe movimentos estratégicos de concorrentes, ajustando seu próprio planejamento de acordo. Em última análise, a análise das Cinco Forças de Porter fornece uma estrutura sólida para avaliar o posicionamento da empresa no mercado e tomar medidas proativas para garantir sua sustentabilidade e sucesso a longo prazo.

<center> Figura 1 - Cinco Forças de Porter </center>

![Forças](outros/5forcas.png)
<center> Fonte: Autoria própria </center>
      
 &emsp;A partir da imagem acima, são feitos os seguintes parágrafos:

#### Rivalidade entre concorrentes existentes:

&emsp;A Comissão de Valores Mobiliários é uma autarquia federal, responsável por fiscalizar e regularizar o mercado de valores mobiliários brasileiro, portanto ao enquadrar-se como um órgão governamental, ainda que com autonomia administrativa, a CVM não é considerada uma "empresa" e não tem concorrentes ou competidores. Porém, assim como essa instituição, existem outras entidades que exercem funções semelhantes como o Banco Central do Brasil(BCB), a Superintendência de Seguros Privados(SUSEP) e o ministério da Fazenda, mas eles não competem entre si, pois estes agentes atuam em conjunto para o crescimento da economia brasileira.

#### Ameaça de novos entrantes

&emsp;Devido à natureza regulatória e governamental da CVM, a ameaça de novos entrantes no mercado não se aplica da mesma forma que em indústrias comerciais ou empresas comuns. Sua função primordial é supervisionar e controlar o mercado de valores mobiliários para garantir transparência e integridade, tendo em vista que essa função de autoridade exclusiva, a entrada de novos órgãos reguladores não é uma preocupação relevante.

#### Ameaças de Produtos e Substitutos

&emsp;A comissão é uma entidade federal e não uma empresa, ela não oferece nenhum produto e sua função é única: supervisar as atividades do mercado de capitais, regulamentar as operações financeiras e promover a transparência e confiança nos mercados. Dessa forma, por se tratar de um órgão soberano nacional, não há ameaças de produtos substitutos

#### Poder de Barganha dos Clientes

&emsp;O conceito de "poder de barganha dos clientes" não se aplica diretamente à Comissão de Valores Mobiliários (CVM) devido à sua natureza regulatória e ao papel que desempenha no mercado financeiro. Os investidores e participantes do mercado não têm influência direta sobre os termos e regulamentos estabelecidos pela CVM. Em vez disso, é a própria CVM que exerce um papel ativo na proteção dos investidores e na manutenção da integridade do mercado.


#### Poder de Barganha dos Fornecedores

&emsp;A principio é importante ressaltar que a CVM não opera da mesma maneira que empresas comerciais tradicionais, e sua natureza como órgão regulador do governo pode impactar como o conceito de "poder de barganha dos fornecedores" é aplicado. Neste contexto, a organização pode ter contratos com prestadores de serviços, como empresas de tecnologia, consultorias jurídicas ou outras entidades que ajudem na operação da comissão. A relação com esses fornecedores pode envolver negociações contratuais, ela faz isso com base nas necessidades operacionais e regulatórias, visando cumprir suas obrigações de supervisão e regulamentação, ao invés de serem diretamente comparáveis ao poder de barganha de fornecedores em um ambiente de mercado comercial tradicional.


## <a name="c2"></a>2. Objetivos e Justificativa
### 2.1 Objetivos
&emsp;Desenvolver um modelo preditivo que auxilie a CVM (Comissão de Valores Mobiliários) na supervisão de FIDCs, identificando potenciais riscos relacionados à provisão para eventuais perdas decorrentes da inadimplência dos créditos cedidos. Como objetivos mais especificos temos que analisar e compreender os padrões e tendências dos dados relacionados aos FIDCs e seus créditos cedidos. Também, fornecer insights à CVM para atuação preventiva, minimizando riscos e preservando a integridade do mercado de capitais brasileiro.

### 2.2 Proposta de solução
&emsp;Nossa proposta é criar um modelo preditivo que utilize técnicas avançadas de Machine Learning e análise de dados. Este modelo será treinado com dados históricos relacionados aos FIDCs e seus créditos cedidos, permitindo identificar e prever riscos associados à inadimplência e à provisão insuficiente. O modelo será capaz de alertar a CVM sobre potenciais problemas, permitindo intervenções tempestivas e evitando consequências negativas para o mercado e seus investidores.

### 2.3 Justificativa
&emsp;A implementação deste modelo preditivo é essencial no contexto atual do mercado de capitais brasileiro, especialmente com a abertura dos FIDCs para investidores de varejo. A capacidade de prever e identificar riscos relacionados à provisão para perdas é crucial para manter a confiança dos investidores e a estabilidade do mercado. Nossa proposta oferece uma solução personalizada e adaptada às especificidades dos FIDCs, diferenciando-se por sua precisão, adaptabilidade e foco na prevenção. Os benefícios incluem a proteção dos investidores, a preservação da integridade do mercado e o fortalecimento da atuação da CVM como órgão regulador.


## <a name="c3"></a>3. Descrição da Solução 
### 3.1 Qual é o problema a ser resolvido

&emsp;Nos FIDCs (Fundo de Investimento em Direitos Creditórios), um dos principais desafios é a gestão apropriada de provisões para eventuais perdas, originadas majoritariamente da inadimplência dos créditos cedidos. Para preservar a justiça entre os cotistas e a confiabilidade do fundo, que em última instancia garantem a confiabilidade da econômica brasileira, por isso é papel da CVM como, órgão supervisor nacional, uma forma de prever e estimar perdas futuras com precisão. A ausência de uma provisão adequada, ou a insuficiência da provisão estabelecida, pode resultar em uma transferência de riqueza não intencional entre cotistas. Essa transferência acontece quando alguns investidores, ao resgatarem suas cotas antes da materialização de uma grande perda no fundo, acabam por obter rentabilidades desproporcionalmente elevadas em comparação com aqueles que permanecem no fundo, e experimentam uma desvalorização das suas cotas.

### 3.2 Qual a solução proposta (visão de negócios)

&emsp;A solução proposta visa abordar a problemática da provisão inadequada em FIDCs por meio da implementação de um modelo preditivo. Esse modelo, alimentado por técnicas de machine learning e análise de dados históricos, tem o objetivo de antecipar e estimar possíveis perdas futuras com precisão. Com esse instrumento, a CVM poderá alertar os administradores do fundo para poderem provisionar recursos de forma mais eficaz, reduzindo o risco de transferência não intencional de riqueza entre os cotistas e fortalecendo, assim, a confiança e a higidez do mercado de capitais brasileiro. Complementando, essa solução contribuirá para uma gestão mais transparente e eficiente dos fundos, beneficiando toda a cadeia de stakeholders envolvida.

### 3.3 Como a solução proposta deverá ser utilizada

&emsp;A solução proposta, um modelo preditivo para antecipar e estimar possíveis perdas futuras em FIDCs, deverá ser integrada ao sistema da CVM.

### 3.4 Benefícios trazidos pela solução proposta

&emsp;A implementação do modelo preditivo para a gestão de provisões em FIDCs não somente aborda um problema crítico no setor, mas também introduz uma série de benefícios tangíveis, tais como o fortalecimento da confiança no mercado. Uma gestão mais transparente e eficaz das provisões contribui para fortalecer a confiança dos investidores e stakeholders no mercado de capitais brasileiro. Outro benefício seria a redução de riscos, pois, ao antecipar possíveis cenários de perda, a solução permite ações proativas que minimizam riscos associados à volatilidade do mercado e mudanças no ambiente econômico.

### 3.5 Critério de Sucesso e Medida de Avaliação

&emsp;Taxa de Acurácia do Modelo: Esta será a medida principal e refere-se à porcentagem de vezes que o modelo prevê corretamente as perdas dentro de uma margem aceitável de erro. Uma alta taxa de acurácia indicará que o modelo é confiável e eficaz em suas previsões.



## <a name="c3"></a>3.6 Metodologia

&emsp;Durante o processo de elaboração da solução, utilizamos como metodologia o CRISP-DM (Cross-Industry Standard Process of Data Mining) que é um modelo utilizado para o desenvolvimento de projeto de data mining e machine learning. Tal metodologia divide o processo em seis etapas principais, já que visa uma abordagem estruturada e eficaz para a solução do problema. No contexto da criação do Destiny a metodologia CRISP-DM foi utilizada da seguinte forma:

* &emsp;Entendimento do Negócio:
Durante essa etapa é necessário desenvolver uma profunda análise da estrutura do mercado de créditos no Brasil, sendo mais específico, direito creditórios (modelo praticado por FIDCs) e dos desafios que a CVM enfrenta em tal setor.

* &emsp;Entendimento dos Dados:
Pelo fato dos dados terem sido fornecidos pela CVM, o subprocesso de avaliar e identificar os fornecedores dos Dados foi poupado. Com isso passamos a avaliar a qualidade dos dados e projetar possíveis relações mais simples.

* &emsp;Preparação do Dados:
Nesse processo os dados foram tratados, limpos e preparados para o teste de relações e hipóteses. Com esse entendimento você separa as colunas que são relevantes para o modelo e começa a trabalhar sobre elas.

* &emsp;Modelagem:com os dados preparados: Através de um do grupo consenso é escolhido entre diferentes algoritmos e técnicas a mais adequada para criar um modelo mais preciso para prever os riscos associados à provisão para perda em FIDCs

&emsp;Ao longo de todas essas etapas, a metodologia CRISP-DM serviu como um guia, garantindo uma abordagem sistemática e estruturada para o desenvolvimento do projeto.


## <a name="c4"></a>4. Desenvolvimento e Resultados


#### 4.1.2. Análise SWOT 
&emsp;Nesta seção realiza-se a análise SWOT, que tem como objetivo avaliar a situação da empresa no mercado de maneira geral. Logo, para realizar essa proposta, analisam-se fatores externos e internos do negócio, isto é, condições que são controláveis pela empresa ou não.

&emsp;Ademais, são avaliadas internamente ao contexto da empresa as “Forças” (“Strenghts”; características destacáveis em comparação a concorrência da empresa e que são positivas para a atuação) e “Fraquezas” (“Weaknesses”; elementos que são pontos de melhoria ou não são contemplados como deveriam, podem influenciar negativamente a atividade empresarial), por outro lado, o contexto externo é avaliado por meio das “Oportunidades” (“Opportunities”; cenários que possibilitam obter melhor desempenho, maior lucratividade ou crescimento graças a um conjunto de fatores externos favoráveis) e “Ameaças” (“Threats”; são os contextos externos desfavoráveis que colocam em risco a atuação da empresa da maneira mais eficiente possível).

&emsp;Neste contexto, a empresa a ser analisada é a Comissão de Valores Mobiliários(CVM), definida como uma autarquia federal — nos parágrafos abaixo aborda-se esse termo — que atua na regulamentação do Mercado de Valores no Brasil. Além disso, o principal objetivo da empresa é “defender os interesses do investidor, especialmente o acionista minoritário, e o mercado de valores mobiliários em geral”. Logo, segundo o GOV.BR, a CVM valoriza:

- &emsp;Valorização permanente do corpo funcional, com foco na sua capacitação, comprometimento, motivação e meritocracia;
- &emsp;Ambiente de trabalho que preze a coordenação, cooperação e constante diálogo entre as diferentes áreas e níveis hierárquicos;
- &emsp;Educação financeira como instrumento essencial para o fortalecimento do mercado de capitais;
- &emsp;Atuação coordenada com instituições públicas e privadas, nacionais e internacionais, na busca de maior eficiência das atividades de regulação, registro, supervisão, fiscalização, sanção e educação;
- &emsp;Atuação técnica, independente, célere e transparente, pautada pela ética, eficiência, equilíbrio e segurança jurídica das decisões;
- &emsp;Atuação regulatória com foco no atendimento das necessidades do mercado e sua evolução, em consonância com padrões internacionais, e pautada na participação da sociedade, inclusive por meio das audiências públicas;
- &emsp;Atuação pautada na proteção do investidor, na exigência de ampla divulgação de informação, no monitoramento dos riscos de mercado e na estabilidade financeira, inclusive com o apoio da autorregulação.

&emsp;Portanto, entre esses princípios, destaca-se o compromisso com a justiça no mercado, a proteção do investidor e a busca contínua por contribuir positivamente para a sociedade. Na figura 2 está representada a análise SWOT da empresa CVM:

<center> Figura 2: Análise SWOT da CVM </center

![swot](outros/swot_delfino.png)

<center> Fonte: Autoria própria </center>

&emsp;Nos parágrafos a seguir, discorre-se sobre a análise SWOT com detalhamentos importantes para a compreensão do resumo apresentado na imagem acima.

**Forças:**

#### Transparência para o público

&emsp;A CVM é uma entidade federal que regularmente compartilha relatórios públicos contendo informações relevantes, como salários dos servidores, demonstrativos financeiros de empresas de capital aberto, ofertas públicas e decisões sobre penalidades. Essa abordagem de transparência é altamente benéfica para o público em geral, transmitindo confiança e credibilidade tanto para pequenos investidores quanto para grandes empresas.

#### Experiência

&emsp;A Comissão de Valores Mobiliários atua há 47 anos no mercado, isso contribui para que a empresa tenha experiência no setor que opera. Logo, a sua extensa base de dados acumulada neste período facilita a identificação de padrões e tendências significativas no mercado, essa capacidade desempenha um papel crucial na tomada de decisões e na supervisão de maneira eficaz. Logo, a longevidade da empresa é um fator positivo, pois promove aprendizados e confiança para tomar as melhores decisões com base no que é justo.

#### Planejamento estratégico

&emsp;De acordo com informações do site GOV.BR, a CVM revisa e atualiza suas diretrizes estratégicas a cada cinco anos. Essa prática é essencial para o setor em que a empresa atua, dada a natureza em constante evolução do mercado de investimentos, seja devido a avanços tecnológicos ou a mudanças globais como crises econômicas ou conflitos internacionais. Manter um planejamento estratégico contínuo é crucial para definir as ações, prioridades e se adaptar às transformações globais de maneira eficaz.


**Fraquezas:**

#### Sobrecarga de fundos para supervisionar

&emsp;A organização enfrenta o desafio de supervisionar uma vasta gama de mais de 24 mil fundos de investimento e atender às necessidades de cerca de 5 milhões de investidores ativos na bolsa de valores. Toda essa atividade ocorre em um ambiente caracterizado por mudanças e flutuações diárias no mercado. Esse cenário complexo gera um volume significativo de dados, exigindo um esforço substancial por parte da empresa para manter a supervisão efetiva e atualizada. Se a empresa não investir em tecnologias avançadas para automatizar processos, analisar dados em tempo real e tomar decisões baseadas em informações precisas, poderá enfrentar dificuldades em manter uma supervisão eficaz.

#### Insuficiência de funcionários

&emsp;A Comissão de Valores Mobiliários (CVM) enfrenta um desafio significativo em relação à quantidade de funcionários disponíveis. A admissão de novos colaboradores ocorre por meio de um concurso público, um processo burocrático em comparação com as contratações convencionais. Essa abordagem, gerenciada pelo governo, limita a autonomia da empresa. O próprio presidente da CVM reconheceu a necessidade de um aumento substancial no número de servidores, destacando que seriam necessários "duas a três vezes mais" do que o contingente atual. Dado que os funcionários são fundamentais para a operação adequada de qualquer organização, a escassez de recursos humanos representa um risco potencial para a CVM.

#### Método de provisão não eficiente

&emsp;No momento, a empresa depende de um processo manual para lidar com a provisão de inadimplências, o que consome o tempo de funcionários especializados que poderia ser poupado ao introduzir um sistema automatizado, como uma inteligência artificial (IA). A falta de automação nessas tarefas específicas e, de certo modo, repetitivas, é um aspecto que precisa ser aprimorado, pois, ao implementar tecnologias como IA, a CVM poderia otimizar esses métodos, aumentar a eficiência da operação e contribuir para o alcance dos seus objetivos de forma mais eficaz.

**Oportunidades:**

#### Confiança do público

&emsp;Com mais de 45 anos de experiência no mercado, a Comissão de Valores Mobiliários conquistou a confiança dos pequenos investidores como um órgão regulador imparcial. Quando ocorrem situações delicadas, como o caso do escândalo da empresa americanas, os investidores de menor porte confiam na CVM para iniciar investigações. Esse exemplo ilustra a importância da confiança do público na atuação da CVM, já que a falta desse respaldo pode prejudicar o desempenho de empresas estatais.

#### Adoção de inteligências artificiais

&emsp;CVM tem como missão principal a proteção dos investidores. Ao incorporar tecnologias de inteligência artificial (IA) em suas operações, a CVM pode proporcionar diversos benefícios significativos aos investidores. Isso inclui a ampliação da segurança digital, reduzindo as vulnerabilidades e riscos associados às transações financeiras online. Além disso, a adoção de IA pode agilizar consideravelmente o processamento das provisões de inadimplência, permitindo uma resposta mais rápida e eficiente em casos de violações das regras.

#### Concentração de dinheiro em investimentos

&emsp;O cenário atual revela um montante considerável de aproximadamente 25 trilhões de reais em ativos, fundos de investimento, ações e títulos. Esse capital substancial apresenta uma oportunidade significativa para impulsionar o crescimento econômico do Brasil. Através de uma gestão inteligente e eficaz desses recursos, a CVM pode contribuir para a alocação eficiente de investimentos, fomentando o desenvolvimento de setores-chave da economia e estimulando a geração de empregos e a inovação.

&emsp;A utilização responsável deste potencial financeiro não apenas beneficia investidores individuais, mas também pode desempenhar um papel crucial na transformação positiva da economia brasileira como um todo. Ao direcionar esses recursos para investimentos produtivos e estratégicos, a CVM tem a capacidade de desencadear um impacto significativo no crescimento econômico sustentável do país.


**Ameaças:**

#### Rotatividade de cargos

&emsp;A CVM é uma entidade federal, o que implica que alguns cargos da empresa sejam preenchidos por indicação do atual presidente da república, esse fator acaba mudando a gestão da empresa a cada quatro anos, interrompendo o fluxo contínuo da liderança da empresa. Esse cenário pode ser visto como uma potencial ameaça para a CVM, uma vez que a alternância de cargos de alto escalão pode criar períodos de vulnerabilidade, tendo em vista que durante essas transições, a estabilidade e a coesão na execução das operações podem ser comprometidas. Portanto, embora a CVM seja uma entidade federal e sujeita a mudanças políticas, é importante considerar as implicações dessa dinâmica na manutenção da integridade e eficácia de suas operações de supervisão e regulamentação.

#### Orçamento baixo

&emsp;A CVM enfrenta um problema relacionado ao seu orçamento, tendo em vista que ele é o mesmo há treze anos, isso implica que a empresa tenha orçamento de 25 milhões para financiar operações que fiscalizam 25 trilhões. Essa disparidade entre o orçamento e a escala das operações da CVM coloca em risco sua capacidade de cumprir adequadamente sua missão de regulamentar e proteger o mercado de valores mobiliários. Neste cenário, a ameaça está na possibilidade de que recursos financeiros inadequados possam limitar a efetividade da CVM, permitindo que atividades inadequadas ou fraudulentas escapem da devida supervisão.

#### Desafios de Fraudes e Integridade

&emsp;Apesar de serem ocorrências infrequentes, o cenário das fraudes representa um desafio para a Comissão de Valores Mobiliários (CVM). Algumas empresas, embora em casos raros, conseguem perpetrar fraudes ao apresentar informações ou dados falsos à CVM, resultando em prejuízos para o mercado. Um exemplo notório é o caso da empresa americanas, que apresentou alegações de "problemas contábeis" que totalizaram 20 bilhões de reais. Essas fraudes têm o potencial de minar a integridade do mercado financeiro, afetando a confiança dos investidores e prejudicando a equidade e a transparência que a CVM busca promover. Quando empresas apresentam informações enganosas ou falsas, podem influenciar decisões de investimento e distorcer a avaliação precisa das condições de mercado.


#### 4.1.3. Planejamento Geral da Solução

&emsp;Para desenvolver a nossa solução, contamos com o acesso à base de dados dos fundos sobre a supervisão da Comissão de Valores Mobiliários (CVM). Utilizamos essa fonte de informações como base para criar um modelo preditivo que visa analisar e antecipar o comportamento dos fundos de investimento. Para alcançar esse objetivo, adotamos uma abordagem que envolve o cálculo da tabela de Valor em Risco. Através dessa métrica, conseguimos avaliar e quantificar o potencial de perda em diferentes cenários de mercado, proporcionando uma visão mais completa e realista do estado dos fundos.

&emsp;O nosso modelo preditivo utiliza dados históricos dos fundos, incluindo seu desempenho passado e comportamento em diferentes condições de mercado. Com base nesses dados, empregamos um modelo de classificação, que categoriza os fundos em duas principais classes: saudáveis e em risco. A grande vantagem do nosso sistema é a sua capacidade de automatizar esse processo de classificação, o que torna o trabalho do analista mais eficiente e ágil. Ao receber uma lista dos fundos considerados em estado de risco, o analista pode tomar ações preventivas de forma proativa. Essas ações podem variar desde a reavaliação das estratégias de investimento até o alerta de possíveis problemas aos investidores.

&emsp;Em última análise, nosso objetivo é aprimorar a abordagem da CVM em relação à supervisão dos fundos de investimento. Em vez de depender principalmente de análises reativas após o surgimento de problemas, estamos possibilitando uma mudança para uma abordagem preventiva, que visa evitar potenciais crises e proteger os investidores e o mercado financeiro como um todo.

#### 4.1.4. Value Proposition Canvas

&emsp;O Value Proposition Canvas (ou Canvas Proposta de Valor) é uma ferramenta que auxilia a entender as necessidades, dores, expectativas e tarefas do cliente, e também como um produto se enquadra e pode ajudar a resolver esses problemas. No modelo, estão presentes os seguintes tópicos:

- &emsp;Segmento do cliente: dores, ganhos e tarefas do cliente;

- &emsp;Proposta de valor: Criadores de ganhos, produtos e serviços e aliviam as dores.

&emsp;Na imagem abaixo, está anexado o Value Proposition Canvas desenvolvido especificamente para o projeto descrito neste documento. 

<center> Figura 3 - Value Proposition Canvas </center>

![Canvas](outros/value_proposition_canvas.png)
<center> Fonte: Autoria Própria </center>

&emsp;A seguir, segue a explicação de cada um dos tópicos resumidos na figura:

- &emsp;Tarefas do cliente: Definimos como algumas das atuais tarefas realizadas pela CVM analisar os possíveis riscos de inadimplência e fraudes por meio de análise de dados de maneira não automatizada, e acionar os clientes caso o FIDIC esteja em risco. Visto isso, o projeto citado visa simplificar a execução destas tarefas.

- &emsp;Dores do cliente: As dores são as dificuldades que o parceiro enfrenta atualmente ao realizar as tarefas citadas, como, por exemplo, dificuldade de alertar os investidores sobre possíveis riscos de inadimplência e a desproporcionalidade de dados sobrecarregando o analista. Com o projeto entregue, espera-se que seja um avanço facilitador tanto para a aumentar a eficiência de estudo de possíveis riscos aos investidores quanto para diminuir a sobrecarga nos analistas.

- &emsp;Ganhos do cliente: Com a implementação do projeto, planeja-se que seja possível a previsão automatizada dos riscos nos investimentos em FIDICS, redução do tempo de análise e descoberta de fraudes e a automatização do processo de análise, deixando os analistas menos sobrecarregados.

- &emsp;Produtos e serviços do projeto: O projeto oferece um modelo preditivo de acompanhamento de inadimplência em fundos de investimentos em direitos creditórios.

- &emsp;Criadores de ganhos do projeto: Para que sejam entregues os ganhos esperados pelo parceiro, o projeto será contemplado com o poder de análise de fundos automatizada, visto que a IA será treinada para minimizar possíveis riscos para os investidores.

- &emsp;Aliviador de dores do projeto: O aliviador de dores é o antecessor do ganho. São as características do projeto que vão fazer com que o cliente tenha seu problema resolvido. Dentre os citados na imagem, está a automatização da análise de fundos e a capacidade de previsão da IA que será treinada.



#### 4.1.5. Matriz de Riscos

&emsp;A matriz de riscos desempenha um papel crucial neste projeto, pois ela abrange tanto as principais preocupações relacionadas a uma variedade de problemas que podem surgir, quanto os cenários mais favoráveis que podem se concretizar. A figura a seguir condensa esses cenários de forma sucinta:

<center> Figura 4 - Matriz de Riscos </center>

![Matriz](outros/matriz_de_riscos.png)
<center> Fonte: Autoria própria </center>

&emsp;Logo, a partir deste panorama geral, os parágrafos a seguir abordam cada tópico individualmente.

- &emsp;Dados mal tratados: Esse é um risco que pode afetar muito o treinamento da máquina, uma vez que ela depende  dos dados apresentados de uma forma adequada para um bom aprendizado. Uma forma de evitar esse risco é tratando bem os dados, excluindo colunas inúteis, linhas com valores nulos e transformando colunas com tipos de dados "string" em tipos que facilitam o aprendizado da IA, como inteiros.

- &emsp;A IA estar viciada pelos dados da pandemia:
Durante a pandemia os números de inadimplências aumentaram, o que pode influenciar no resultado da predição da maquiná. Uma maneira de lidar com esse risco é excluir a parte dos dados referentes a época da pandemia.

- &emsp;Dados insuficientes para treinar a IA: Com dados insuficientes, a maquiná não terá um treinamento adequado para realizar suas  predições com exatidão. Uma possível solução para prevenir esse risco, seria solicitar uma maior quantidade de dados com a CVM, para que seja suficiente para o treinamento do modelo preditivo.

- &emsp;IA não ter uma boa acurácia: Há o risco baixo de a Inteligência Artificial não ter uma boa acurácia. Porém, esse risco pode ser facilmente evitado, ao utilizar vários modelos de aprendizagem de maquiná e estudar qual se encaixa melhor para o contexto do problema.

- &emsp;O cliente implementar o projeto em seu sistema: Esse risco representa uma oportunidade. Com um modelo que prevê os riscos de inadimplência, há altas hipóteses da CVM utilizar a solução em suas funções de fiscalização.

- &emsp;Facilitar o trabalho dos analistas: Com uma ferramenta que avalia riscos de um fundo de direitos creditórios, os analistas da CVM terão um auxílio para acompanhar a situação dos FIDCs, o que consequentemente facilitara seu trabalho.

- &emsp;Reconhecimento da mídia pela solução feita: Esse é um risco de uma oportunidade. Em posse de um bom modelo preditivo em mãos, a CVM pode divulgar sua nova ferramenta para a mídia, em geral, trazendo reconhecimento para o grupo que realizou o projeto.


- &emsp;Através da solução a CVM identificar fraudes nos fundos:  Esse risco representa uma oportunidade. A CVM utilizando o modelo preditivo, pode notar irregularidades constantes em fundos e caso investigue, pode ser que fraudes sejam encontradas.

#### 4.1.6. Personas

&emsp;As personas desempenham um papel essencial no desenvolvimento do projeto, pois, aproximam o produto do usuário final. Elas oferecem uma representação humanizada do público-alvo, enriquecendo o processo de desenvolvimento. Nesse contexto, a persona criada pelo grupo está apresentada na Figura 5 abaixo:

<center> Figura 5 - Persona </center>

![Persona](outros/persona_delfino.png)
<center> Fonte: Autoria Própria </center>

&emsp;Nos parágrafos subsequentes, são destacados os principais detalhes pessoais da persona:

**Andre Alves**

**Idade:** 37

**Gênero:** Masculino

**Localização:** Rio de Janeiro - Barra da Tijuca

**Carreira:**

&emsp;André Alves é um analista de mercado financeiro com formação em economia e mestrado em finanças. Atualmente, ele desempenha um papel fundamental na CVM, analisando produtos financeiros, regulamentações e divulgações de empresas.

**Personalidade:**

&emsp;Nos momentos de lazer, André aprecia passar tempo com seu filho de 6 anos e sua esposa. Além disso, ele cultiva o hábito de colecionar moedas antigas, uma paixão que herdou de seu pai. Nos finais de semana, ele costuma frequentar bares na região com seus amigos para se desconectar.

**Desafios:**

&emsp;André enfrenta os desafios decorrentes da constante evolução do mercado financeiro, especialmente no que diz respeito aos FIDCs com níveis elevados de inadimplência. Lidar com essas situações requerem uma profunda compreensão da economia, das regulamentações e a habilidade de antecipar cenários complexos.

**Metas:**

&emsp;André nutre o desejo de se tornar uma autoridade no campo da regulamentação financeira e deseja contribuir ainda mais para a missão da CVM.

&emsp;Nesse sentido, a persona de André Alves é uma ferramenta valiosa para guiar o desenvolvimento do projeto, mantendo as necessidades e aspirações do usuário final em foco durante todo o processo.

#### 4.1.7. Jornadas do Usuário

&emsp;Uma jornada do usuário é uma representação, seja visual ou narrativa, das etapas que um indivíduo atravessa ao interagir com um produto, serviço, marca ou empresa. No âmbito deste projeto, essa ferramenta delineia a experiência completa do usuário, desde o momento em que ele identifica a necessidade de analisar um FIDC até a conclusão da utilização do nosso modelo preditivo. A figura a seguir ilustra esse processo.

<center> Figura 6 - Jornada do Usuário </center>

![Jornada](outros/mapa_do_usuario.jpg)
<center> Fonte - Autoria Própria </center>

&emsp;Essa jornada do usuário não apenas mapeia as interações tangíveis, mas também captura as emoções e necessidades que surgem ao longo do caminho. Compreender essa jornada de ponta a ponta nos permite otimizar cada ponto de contato, oferecendo uma experiência mais alinhada e satisfatória. Ao focar em atender às expectativas e desejos do usuário em todas as fases, podemos criar um impacto positivo e duradouro em sua jornada global com nosso produto.

#### 4.1.8 Política de Privacidade
Política de Privacidade

&emsp;A Inteli, pessoa jurídica de direito privado, com sede na Av. Prof. Almeida Prado, 520 - Butantã, São Paulo, inscrita no CNPJ/MF sob o nº 28.226.170/0001-08 (“Lojista” ou “nós”) leva a sua privacidade a sério e zela pela segurança e proteção de dados de todos os seus clientes, parceiros, fornecedores e usuários (“Usuários” ou “você”) do modelo preditivo e qualquer outro site.

&emsp;Esta Política de Privacidade (“Política de Privacidade”) destina-se a informá-lo sobre o modo como nós utilizamos e divulgamos informações coletadas em suas visitas ao nosso modelo preditivo e em mensagens que trocamos com você (“Comunicações”).

&emsp;AO ACESSAR O MODELO PREDITIVO, ENVIAR COMUNICAÇÕES OU FORNECER QUALQUER TIPO DE DADO SENSÍVEL, VOCÊ DECLARA ESTAR CIENTE E DE ACORDO COM ESTA POLÍTICA DE PRIVACIDADE, A QUAL DESCREVE AS FINALIDADES E FORMAS DE TRATAMENTO DE SEUS DADOS SENSÍVEIS QUE VOCÊ DISPONIBILIZAR NO MODELO PREDITIVO.

&emsp;Esta Política de Privacidade fornece uma visão geral de nossas práticas de privacidade e das escolhas que você pode fazer, bem como direitos que você pode exercer em relação aos Dados Sensíveis tratados por nós.

&emsp;Caso você nos envie Dados Sensíveis referentes a outras pessoas físicas, você declara ter a competência para fazê-lo e declara ter obtido o consentimento necessário para autorizar o uso de tais informações nos termos desta Política de Privacidade.

**Definições**

Para os fins desta Política de Privacidade:

&emsp;“Dados Pessoais” significa qualquer informação que, direta ou indiretamente, identifique ou possa identificar uma pessoa natural, como, por exemplo, nome, CPF, data de nascimento, endereço IP, dentre outros;

&emsp;“Dados Sensíveis” significa qualquer informação que seja possível identificar informações sobre a natureza dos investimentos analisados como, por exemplo, nome do fundo, CNPJ do administrador, CNPJ do fundo, dentre outros dados;

&emsp;“Dados Pessoais Sensíveis” significa qualquer informação que revele, em relação a uma pessoa natural, origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico;

&emsp;“Tratamento de Dados Sensíveis” significa qualquer operação efetuada no âmbito dos Dados Sensíveis, por meio de meios automáticos ou não, tal como a recolha, gravação, organização, estruturação, armazenamento, adaptação ou alteração, recuperação, consulta, utilização, divulgação por transmissão, disseminação ou, alternativamente, disponibilização, harmonização ou associação, restrição, eliminação ou destruição. Também é considerado Tratamento de Dados Sensíveis qualquer outra operação prevista nos termos da legislação aplicável;

&emsp;“Leis de Proteção de Dados” significa todas as disposições legais que regulam o Tratamento de Dados Pessoais, incluindo, porém, sem se limitar, a Lei nº 13.709/18, Lei Geral de Proteção de Dados Pessoais (“LGPD”).

**Uso de Dados Pessoais**

&emsp;Coletamos e usamos Dados Sensíveis quando você estiver adquirindo informações no modelo preditivo, personalizando e melhorando sua experiência.
Exemplos de como usamos os dados incluem:

- &emsp;Incrementar os dados para treino do nosso modelo preditivo;

- &emsp;Para enviar informações que acreditamos ser do seu interesse;

&emsp;Além disso, os Dados Sensíveis fornecidos também podem ser utilizados na forma que julgarmos necessária ou adequada: (a) nos termos das Leis de Proteção de Dados; (b) para atender exigências de processo judicial; (c) para cumprir decisão judicial, decisão regulatória ou decisão de autoridades competentes, incluindo autoridades fora do país de residência; (d) para proteger nossas operações; (e) para proteger direitos, privacidade, segurança nosso, seus ou de terceiros; (f) para detectar e prevenir fraude; (g) permitir-nos usar as ações disponíveis ou limitar danos que venhamos a sofrer; (h) de outros modos permitidos por lei.

&emsp;O NOSSO MODELO SE DESTINA A ANALISTAS DA CVM E PEDIMOS QUE OUTRAS PESSOAS NÃO NOS FORNEÇA QUALQUER DADO PESSOAL E SENSÍVEL.

**Não fornecimento de Dados Sensíveis**

&emsp;Você não é obrigado a compartilhar os Dados Sensíveis que solicitamos, no entanto, se você optar por não os compartilhar, em alguns casos, não poderemos fornecer a você acesso completo, alguns recursos especializados ou ser capaz de prestar a assistência necessária, ou, ainda, viabilizar a entrega do produto ou prestar o serviço contratado por você.

**Dados coletados**

&emsp;O público em geral poderá navegar pelo modelo preditivo sem necessidade de qualquer cadastro e envio de Dados Pessoais. No entanto, algumas das funcionalidades do modelo poderão depender do envio de Dados Sensíveis como viabilizar a entrega dos resultados das análises feitas pelo modelo preditivo.

&emsp;No contato ao modelo preditivo, nós podemos coletar:
Informações que você envia. Informações que você envia via formulário
Na navegação geral no modelo preditivo, nós poderemos coletar:

&emsp;Dados anônimos ou agregados. Durante nossas operações, aplicamos um processo de desidentificação ou pseudo minimização aos seus dados para que seja razoavelmente improvável que você identifique você através do uso desses dados com a tecnologia disponível;

&emsp;Outras informações que podemos coletar. Outras informações que não revelem especificamente a sua identidade ou que não são diretamente relacionadas a um indivíduo, tais como informações sobre os FIDCs analisados.

&emsp;Forma de coleta automática de Dados Sensíveis
Quando você visita o modelo, ela pode armazenar e se aprimorar com as informações anteriormente computadas e elas são usadas principalmente para que o modelo funcione como você espera. As informações geralmente não o identificam diretamente.

&emsp;Você pode, a qualquer momento, requerer: (i) confirmação de que seus Dados Sensíveis estão sendo tratados; (ii) correções a dados incompletos, inexatos ou desatualizados; (iii) anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade com o disposto em lei; (v) eliminação de Dados Pessoais tratados com seu consentimento, na medida do permitido em lei; e (ix) revogação do consentimento. Os seus pedidos serão tratados com especial cuidado de forma a que possamos assegurar a eficácia dos seus direitos. Poderá lhe ser pedido que faça prova da sua identidade de modo a assegurar que a partilha dos Dados Pessoais é apenas feita com o seu titular.

&emsp;Você deverá ter em mente que, em certos casos (por exemplo, devido a requisitos legais), o seu pedido poderá não ser imediatamente satisfeito, além de que nós poderemos não conseguir atendê-lo por conta de cumprimento de obrigações legais. Segurança dos Dado Sensíveis
Buscamos adotar as medidas técnicas e organizacionais previstas pelas Leis de Proteção de Dados adequadas para proteção dos Dados Sensíveis na nossa organização. Infelizmente, nenhuma transmissão ou sistema de armazenamento de dados tem a garantia de serem 100% seguros. Caso tenha motivos para acreditar que sua interação conosco tenha deixado de ser segura (por exemplo, caso acredite que a segurança de qualquer uma de suas contas foi comprometida), favor nos notificar imediatamente.

&emsp;Atualizações desta Política de Privacidade
Se modificarmos nossa Política de Privacidade, publicaremos o novo texto com a data de revisão atualizada. Podemos alterar esta Política de Privacidade a qualquer momento. Caso haja alteração significativa nos termos desta Política de Privacidade, podemos informá-lo por meio das informações de contato que tivermos em nosso banco de dados ou por meio de notificação em nosso modelo.
Recordamos que nós temos como compromisso não tratar os seus Dados Sensíveis de forma incompatível com os objetivos descritos acima, exceto se de outra forma requerido por lei ou ordem judicial.

&emsp;Sua utilização do modelo preditivo após as alterações significam que aceitou as Políticas de Privacidade revisadas. Caso, após a leitura da versão revisada, você não esteja de acordo com seus termos, favor encerrar o acesso ao modelo.


### 4.2. Compreensão dos Dados

#### 4.2.1. Exploração de dados

&emsp;Após o recebimento dos dados, conduzimos um processo de tratamento e modelagem que resultou nas seguintes características para o treinamento do modelo preditivo:

'SK_Documento' - Dado Numérico

'CNPJ_Administrador' - Dado Numérico

'Nome_Administrador' - Dado Numérico

'Fundo_Exclusivo' - Dado Categórico

'Cotistas_Vinculados_Interesse' - Dado Categórico

'Ativo' - Dado Numérico

'Ativo_Disponibilidades'- Dado Numérico

'Ativo_Carteira' - Dado Numérico

'Ativo_Carteira' - Dado Numérico

'Ativo_Direitos_Aquisicao' - Dado Numérico

'Ativo_Direitos_Aquisicao_Creditos_Vencer_Adimplentes' - Dado Numérico

'Ativo_Direitos_Aquisicao_Creditos_Inadimplentes' - Dado Numérico

'Ativo_Direitos_Aquisicao_Creditos_Acoes_Judiciais' - Dado Numérico

'Ativo_Direitos_Sem_Aquisicao' - Dado Numérico

'Ativo_Direitos_Sem_Aquisicao_Creditos_Vencer_Adimplentes' - Dado Numérico

'Ativo_Direitos_Sem_Aquisicao_Creditos_Vencer_Inadimplentes' - Dado Numérico

'Ativo_Cotas_FIDC' - Dado Numérico

'Ativo_Posicao_Derivativos' - Dado Numérico

'Ativo_Valores_Mobiliarios' - Dado Numérico

'Patrimonio_Liquido' - Dado Numérico

'Liquidez_Ate_30_Dias' - Dado Numérico

'Liquidez_Ate_60_Dias' - Dado Numérico

'Liquidez_Ate_90_Dias' - Dado Numérico

'Liquidez_Ate_180_Dias' - Dado Numérico

'Liquidez_Ate_360_Dias' - Dado Numérico

'Liquidez_Acima_360_Dias' - Dado Numérico

'Carteira' - Dado Numérico

'Carteira_Comercial' - Dado Numérico 

'Carteira_Servicos' - Dado Numérico 

'Carteira_Financeiro' - Dado Numérico

'Carteira_Mercado_Imobiliario' - Dado Numérico

'Prazo_Conversao_Cotas' - Dado Numérico

'Ativo_Direitos_Aquisicao_Parcelas_Inadimplentes' - Dado Numérico

'Ativo_Direitos_Aquisicao_Creditos_Inadimplentes' - Dado Numérico

'Ativo_Direitos_Sem_Aquisicao_Provisao_Reducao' - Dado Numérico

'Ativo_Direitos_Aquisicao_Provisao_Reducao' - Dado Numérico

&emsp;Todas essas colunas desempenharão um papel crucial no desenvolvimento do modelo preditivo, visando maximizar sua eficácia no projeto. Além da análise dessas características, também elaboramos gráficos, como exemplificado na Figura (número), e uma matriz de calor (Figura número), que revela as relações entre as diversas colunas escolhidas. Esse conjunto de características e análises visa assegurar que nosso modelo seja robusto e capaz de fornecer previsões precisas, impulsionando assim a qualidade e a utilidade do projeto como um todo.

<center> Figura 7 - Patrimonio Liquido e Créditos Inadimplentes </center>

![Patrimonio Liquido e Créditos Inadimplentes](outros/patrimonio_liquido_e_inadimplentes.png)
<center> Fonte: Autoria Própria </center>

&emsp;Nesta representação gráfica, o eixo horizontal retrata os valores de créditos inadimplentes, enquanto o eixo vertical apresenta os diferentes níveis de patrimônio líquido. A análise desse gráfico proporciona insights sobre como a inadimplência se relaciona com o patrimônio líquido, ajudando a identificar possíveis padrões ou tendências.

<center> Figura 8 - Patrimonio Liquido e Créditos Adimplentes </center>

![Patrimonio Liquido e Créditos Adimplentes](outros/patrimonio_liquido_e_adimplentes.png)
<center> Fonte: Autoria Própria </center>


&emsp;Este gráfico visualiza a conexão entre o patrimônio líquido e os créditos adimplentes. Similar à figura anterior, o eixo horizontal representa os créditos adimplentes, enquanto o eixo vertical destaca os vários níveis de patrimônio líquido. A análise desse gráfico permite entender como os créditos em dia estão relacionados com o patrimônio líquido, auxiliando na compreensão da interação entre essas variáveis. Além disso, comparar a inadimplência com a adimplência foi um fator considerado ao escolher essa variável, pois ambas são opostas.

<center> Figura 9 - Mapa de calor das variáveis escolhidas </center>

![Mapa de calor](outros/mapa_de_calor.png)
<center> Fonte: Autoria Própria </center>

&emsp;Essa imagem exibe uma matriz de calor que visualmente apresenta as relações entre as variáveis escolhidas. Cada célula da matriz é colorida conforme a força da correlação entre duas variáveis. Cores mais intensas indicam correlações mais fortes, enquanto cores mais claras indicam correlações mais fracas. O mapa de calor é uma ferramenta poderosa para identificar padrões de interdependência entre variáveis, contribuindo para a seleção final das características no modelo preditivo.


#### 4.2.1.1 Análise Descritiva

&emsp;A Análise Descritiva desempenha um papel fundamental na etapa inicial do processo de análise dos dados fornecidos. Ela emprega métodos de Estatística Descritiva para estruturar, resumir e elucidar aspectos significativos do conjunto de características examinadas. Essa fase é de importância crucial no desenvolvimento e na compreensão de modelos preditivos, pois envolve a exploração e interpretação dos dados antes da construção de um modelo. Isso possibilita aos analistas identificar padrões, identificar valores discrepantes (outliers) e obter insights valiosos.

&emsp;A figura abaixo, intitulada "Figura 10 - Análise Descritiva", encapsula essa análise referente às 32 colunas selecionadas e detalhadas no tópico anterior (4.2.1). Ela apresenta os principais indicadores estatísticos de cada coluna, como moda, média, mediana, desvio padrão, valor mínimo e valor máximo.

<center> Figura 10 - Análise Descritiva </center>

![Análise Descritiva](outros/Análise.descritiva2_page-0001.jpg)
<center> Fonte: Autoria Própria </center>

&emsp;Através dessa análise gráfica, começamos a vislumbrar padrões estatísticos que podem nos fornecer uma compreensão mais profunda dos dados. Essa análise crítica das estatísticas descritivas é um passo crucial para alicerçar a construção subsequente de um modelo preditivo confiável e informado.

#### 4.2.2. Pré-processamento dos dados
**Passos:**

1. &emsp;Primeiramente, importamos os dados para um notebook com o mesmo estilo do Google Colab e Jupyter Notebook. Em seguida, lemos esses dados com a função "read_csv" da biblioteca pandas, que será utilizada na maior parte do tratamento desses dados.

2. &emsp;Logo após a importação dos dados, iniciamos o processo de tratamento dos mesmos. Primeiramente, removemos todas as linhas que possuíam informações faltantes e excluímos todas as linhas duplicadas, a fim de obtermos uma visão mais clara dos dados.

3. &emsp;Posteriormente, tentamos identificar e separar as principais colunas dentre as 321 fornecidas. Para isso, contamos com a ajuda do chat GPT, que foi informado detalhadamente sobre o contexto do trabalho, embora não tenhamos compartilhado os dados sensíveis. Essa abordagem nos permitiu filtrar de maneira eficaz as colunas a serem utilizadas.

4. &emsp;Com esse procedimento, obtivemos dois conjuntos de dados parcialmente tratados. Assim, agrupamos todos os dados de um dos datasets que possuíam o mesmo "SK_Documento".

5. &emsp;Após a etapa de agrupamento, combinamos os dois datasets em um único conjunto. No entanto, realizamos essa fusão de forma unilateral, pois um dos datasets era consideravelmente maior que o outro. Assim, apenas incluímos os dados do dataset maior que correspondiam aos dados do dataset menor.

6. &emsp;Uma vez que tínhamos um único conjunto de dados, finalizamos o processo de filtragem, removendo as colunas que não seriam utilizadas, como por exemplo "Nome_Administrador" e outras.

7. &emsp;Continuando, realizamos a transformação das variáveis categóricas em numéricas por meio do método "get_dummies" disponibilizado pela biblioteca pandas.

8. &emsp;Com o intuito de encontrar novas features que se relacionassem com a Inadimplencia e o Patrimônio Líquido, foram realizados testes por meio do orange e do python, com isso encontramos um conjunto de novas features para serem adicionadas e, além disso, removemos as que não haviam relações significativas com estas variáveis chave.

#### 4.2.3. Hipóteses

&emsp;Nesta seção, será feita uma análise exploratória dos dados para a formulação de hipóteses sobre seus relacionamentos e sobre o funcionamento do mercado dos Fundos de Direitos Creditórios (FIDCs).

&emsp;Utilizando a biblioteca Matplotlib e a Seaborn do Python para a geração de gráficos, aplicamos uma matriz de correlação sobre as colunas. Isso demonstra, através de números de 0 a 1, o nível de correlação entre elas.

&emsp;Durante a análise, percebemos um alto nível de relação entre a coluna de liquidez acima de 360 dias e aquela que representa a inadimplência. A hipótese é que, se os devedores adiarem cada vez mais seu pagamento, há um risco elevado de ocorrer inadimplência. Essa hipótese é reforçada com a visualização do gráfico de correlação, onde é observada uma correlação de 0.6. Se o valor de uma das colunas cresce, há uma tendência de a outra também crescer.

&emsp;Outra observação que pode ser feita na matriz é o alto nível de correlação entre a carteira financeira e a inadimplência. A carteira financeira refere-se ao conjunto de ativos financeiros nos quais o fundo investe, como ações, títulos de renda fixa, derivativos, entre outros. No entanto, a relação entre inadimplência e a carteira pode estar principalmente ligada aos ativos de renda fixa, como títulos corporativos, títulos públicos, debêntures, etc. Quando um emissor de títulos enfrenta dificuldades financeiras e não consegue honrar seus compromissos de pagamento aos detentores de títulos, ocorre a inadimplência. Isso explicaria o nível de correlação de 0.8 entre essas colunas.

&emsp;Uma última hipótese é que os valores da provisão aumentam com os valores de créditos inadimplentes a vencer. A lógica é simples: se os devedores não cumprirem seus compromissos financeiros, o fundo precisa se preparar para garantir o dinheiro dos outros cotistas, aumentando assim a provisão. Para essa análise, foi utilizado o software Orange, gerando um gráfico de dispersão entre as variáveis "provisão" e "inadimplência". Ao observar a relação entre as colunas, percebe-se uma proporcionalidade entre as duas, reforçando assim essa teoria.

### 4.3. Preparação dos Dados e Modelagem

&emsp;A preparação dos dados envolve a limpeza, transformação e organização dos dados brutos para torná-los adequados para análise. A partir disso, os algoritmos são aplicados aos dados preparados para extrair insights e tomar decisões informadas. Durante o projeto, todas essas etapas foram cuidadosamente atendidas, garantindo que os dados estejam prontos para aplicação.

&emsp;Após a preparação dos dados, foi avaliada diversas abordagens de modelagem, considerando diferentes tipos de algoritmos. Após uma análise minuciosa, o modelo ideal que atenderia plenamente ao escopo do projeto seria o modelo supervisionado. O mesmo foi escolhido devido à natureza dos dados disponíveis e aos objetivos do projeto, visto que envolve a previsão inadimplência com base nas características específicas dos próprios fundos FIDCS.

&emsp;Com a escolha do modelo supervisionado, procedeu-se à divisão dos dados em conjuntos de treinamento e teste, sendo 70% dos dados limpos para treinamento e 30% para teste, para garantir que o modelo fosse treinado em uma parte dos dados e avaliado em outra parte independente. Isso ajudou a evitar problemas de overfitting e a avaliar o desempenho do modelo de forma mais precisa.

&emsp;Por fim, o algorítimo candidato para o projeto foi o Random Forest, que é um método de aprendizado de maquiná usado tanto para tarefas de classificação quanto para de regressão. Ele é uma extensão do algoritmo de árvore de decisão que combina múltiplas árvores de decisão para tomar decisões mais precisas e robustas.
A escolha  foi realizada comparando o resultado da acurácia com outros algoritmos usando o erro quadrático médio, uma métrica que descreve a margem de erro do modelo. Observamos que o Random Forest possui uma precisão maior que os outros algoritmos supervisionados. Um dos modelos testados  foi o KNN, que obteve um erro quadrático de 0,0021.

<center> Acurácia do knn </center>

![KNN Acuracia](outros/KNNAcuracia.png)
<center> Fonte: Autoria Própria </center>


&emsp;Porém mesmo com um número bem baixo, o Random Forest alcançou uma margem de erro muito menor, o que o torna mais adequado para o desenvolvimento do projeto.

<center> Acurácia do Random Forest </center>

![Random Forest Acuracia](outros/RandomForestAcuracia.png)
<center> Fonte: Autoria Própria </center>

Link para o notebook
<a href="https://github.com/2023M3T10-Inteli/grupo4/blob/main/notebooks/Destiny/Destiny2.0.ipynb" target="_blank"Random forest></a>

### 4.4. Comparação de Modelos

### Escolha da Métrica e Justificativa

&emsp;Durante o desenvolvimento dos modelos preditivos nos deparamos com um problema para a escolha das métricas dos modelos que foi o overfitting. O overfitting, em português "sobreajuste", é um conceito importante no aprendizado de máquina e na estatística que ocorre quando um modelo de machine learning se ajusta excessivamente aos dados de treinamento. Isso significa que o modelo se torna muito complexo e captura não apenas os padrões genuínos presentes nos dados, mas também o ruído e as flutuações aleatórias que podem estar presentes nos dados de treinamento. No nosso caso o overfitting foi causado pela falta de balanceamento das classes, possuindo muito mais casos de fundos “saudáveis” do que os considerados de risco. Este overfitting não permite definir as melhores métricas para o nosso modelo de maneira concreta, porém podemos escolher duas métricas baseado no tipo de modelo que estamos trabalhando.

### Métricas de Avaliação do Modelo

&emsp;As métricas escolhidas para avaliar o desempenho do modelo foram:


#### Acurácia
&emsp;A acurácia é uma métrica apropriada para modelos de classificação, pois mede a proporção de predições corretas em relação ao total de predições realizadas. No contexto deste projeto, o objetivo é identificar corretamente os clusters aos quais os fundos de investimento pertencem. A acurácia proporciona uma visão clara e direta da eficácia do modelo nesse sentido.

#### F1 Score
&emsp;O F1 Score é uma métrica que combina precisão e recall. Precisão é a proporção de verdadeiros positivos em relação ao total de classificações positivas feitas pelo modelo, enquanto recall é a proporção de verdadeiros positivos em relação ao total de instâncias que realmente são positivas. O F1 Score é a média harmônica entre precisão e recall e é particularmente útil quando há um desequilíbrio significativo entre as classes.

#### Recall Score
&emsp;O Recall Score mede a habilidade do modelo em identificar corretamente todas as instâncias que pertencem a uma classe. É especialmente importante em cenários onde identificar falsos negativos é crítico, como em aplicações médicas ou de segurança.

&emsp;Essas métricas oferecem uma compreensão mais abrangente do desempenho do modelo, complementando a informação proporcionada pela acurácia.


### Modelos Otimizados 

#### Modelos Apresentados e Suas Métricas

&emsp;Foram apresentados três modelos para a classificação dos fundos de investimento:

1. **Random Forest Classifier**

- Número de Estimadores: 100
- Critério de Divisão: Gini
- Profundidade Máxima das Árvores: Não especificada
- Acurácia: 100%
- F1 Score : 1.0

&emsp;Justificativa: O Random Forest é um algoritmo robusto e versátil que geralmente produz resultados confiáveis em tarefas de classificação. A seleção de 100 estimadores foi baseada em experimentação preliminar e resultou em bom desempenho.

2. **K-Nearest Neighbors (KNN)**

- Número de Vizinhos: 49
- Métrica de Distância: Euclidiana
- Acurácia:100%
- f1 score: 1.0

&emsp;Justificativa: O KNN é um método baseado em instâncias que pode ser eficaz para problemas de classificação. A escolha de 49 vizinhos foi baseada em experimentação prévia e demonstrou resultados aceitáveis.

3. **K-means**

- Número de Clusters (K): 2
- Acurácia: 100%

&emsp;Justificativa: O K-means é um algoritmo de aprendizado não supervisionado amplamente utilizado para agrupamento de dados. Foi aplicado neste contexto para identificar naturalmente clusters nos fundos de investimento com base na taxa de inadimplência. A escolha de 2 clusters foi feita com base em considerações teóricas sobre o problema.

&emsp;Este modelo, embora não seja um classificador como os anteriores, é valioso para revelar padrões intrínsecos nos dados que podem ser úteis para análises futuras.


#### Otimização dos Modelos 

&emsp;Ambos os modelos foram balanceados utilizando a técnica de SMOTE (Synthetic Minority Over-sampling Technique) para lidar com o desbalanceamento dos dados. O SMOTE gera dados sintéticos para a classe minoritária, melhorando assim a capacidade do modelo de generalizar para essa classe. Porém, não utilizamos nenhum modelo de otimização de hiperparâmetros porque os dados estavam em overfitting.

#### Clareza no Texto e Integração com o Código 

&emsp;O código foi organizado de forma clara e está devidamente comentado para facilitar a compreensão. Além disso, a explicação dos modelos e suas justificativas estão bem integradas com a implementação no Colab, permitindo uma compreensão completa do processo.

### Definição do Modelo Escolhido e Justificativa 

&emsp;O modelo escolhido para a classificação dos fundos de investimento foi o Random Forest Classifier. Esta escolha foi baseada na sua alta flexibilidade, capacidade de lidar com variáveis categóricas, e performance satisfatória obtida durante os experimentos. A acurácia e o f1-score ponderado obtidos foram de 100% e 100, respectivamente.


### 4.5. Avaliação

### Descrição da Situação dos Modelos Preditivos

&emsp;Durante o desenvolvimento do projeto, identificamos um problema de overfitting nos dados. Isso significa que o modelo se ajustou de forma excessiva aos dados de treinamento específicos, o que resultou em um desempenho comprometido ao lidar com novos conjuntos de dados. Em outras palavras, devido à predominância de dados iguais a zero e a uma escassez de dados diferentes, o modelo tende a classificar novos dados como zero em vez de outros valores. Por isso, não conseguimos selecionar um modelo preditivo neste momento. Logo, para trabalhar com um modelo preditivo no caso apresentado pela empresa seriam necessárias modificações no banco de dados.

&emsp;Porém, em uma situação hipotética na qual haja a disponibilidade de um conjunto de dados mais apropriado e bem preparado, o modelo que seria considerado para a aplicação seria o Random Forest Classifier. Esta escolha se basearia nas seguintes razões:

1. **Robustez e Desempenho:** 

&emsp;O Random Forest se destaca por sua robustez e habilidade de lidar com conjuntos de dados complexos e relações não-lineares. Em tarefas de classificação de fundos de investimento, isso é particularmente crucial. Esses dados muitas vezes apresentam interações e padrões que não são facilmente discerníveis por métodos de modelagem mais simples. O Random Forest consegue capturar essas nuances devido à sua capacidade de considerar múltiplas combinações de variáveis de forma simultânea.

&emsp;Além disso, o Random Forest se beneficia da agregação de múltiplas árvores de decisão, o que reduz o impacto de overfitting e aumenta a estabilidade das previsões. Outros modelos podem ser mais susceptíveis a superajuste quando confrontados com dados complexos e variáveis interconectadas.

&emsp;Por esses motivos, observamos que o Random Forest demonstra um desempenho notavelmente superior em comparação aos outros modelos em nossa análise. Isso se traduz em uma capacidade mais efetiva de classificar corretamente os fundos de investimento, mesmo em situações desafiadoras e com dados menos estruturados.

2. **Acurácia Elevada:** 

&emsp;Embora o overfitting tenha impactado a capacidade de avaliar a acurácia com precisão, ao considerarmos o contexto dos dados, é razoável supor que o modelo Random Forest (RF) demonstraria uma acurácia notavelmente alta durante a fase experimental. Isso se deve à sua notável capacidade de classificar com precisão os fundos de investimento em clusters.

&emsp;Portanto, mesmo na ausência de parâmetros de avaliação ideais devido ao overfitting, podemos ter uma confiança substancial na capacidade do modelo RF de tomar decisões precisas em um contexto com dados bem elaborados e representativos. Isso se traduz em uma alta confiança na capacidade do modelo de classificar corretamente os fundos de investimento em clusters, fornecendo assim um recurso valioso para a tomada de decisões

3. **F1 Score e Recall Score**: 

&emsp;Além da avaliação da acurácia, decidimos utilizar o F1 Score e o Recall Score para fornecer uma visão mais abrangente do desempenho do modelo. Em uma situação hipotética, onde o modelo Random Forest (RF) é empregado, há motivos substanciais para acreditar que ele apresentaria resultados notáveis nessas métricas.

&emsp;O F1 Score é uma medida que combina precisão e recall, sendo particularmente relevante em situações onde identificar falsos positivos e falsos negativos é crítico. Dada a capacidade do RF em lidar com dados complexos e não-lineares, ele é altamente eficaz na minimização desses erros.

&emsp;O Recall Score, por sua vez, foca na capacidade do modelo de identificar corretamente os verdadeiros positivos, o que é essencial em cenários onde a identificação de todos os casos relevantes é crucial. O RF, com sua habilidade de considerar múltiplas combinações de variáveis simultaneamente, é especialmente competente nessa tarefa.

&emsp;Portanto, ao avaliar o RF com base nessas métricas em um contexto com dados bem estruturados e representativos, há uma forte indicação de que ele apresentaria um desempenho impressionante. Essas métricas reforçam a confiabilidade do modelo na identificação precisa dos clusters, proporcionando assim uma ferramenta valiosa para a tomada de decisões em tal situação hipotética.

4. **Facilidade de Interpretação**: 

&emsp;O modelo Random Forest (RF) destaca-se pela sua capacidade de fornecer interpretações claras das decisões tomadas. Esta característica é fundamental em situações onde a transparência e a explicabilidade são requisitos críticos.

&emsp;A interpretabilidade do RF deriva da forma como ele combina múltiplas árvores de decisão para chegar a uma predição final. Cada árvore individual pode ser entendida como uma sequência de regras de decisão, tornando mais acessível compreender como o modelo chega a uma conclusão. Além disso, é possível quantificar a importância relativa de cada variável na tomada de decisão, fornecendo insights valiosos sobre quais fatores influenciam mais fortemente as previsões.

&emsp;Portanto, em uma situação hipotética em que o RF fosse empregado, teríamos razões sólidas para acreditar que ele proporcionaria uma interpretação clara e acessível das decisões do modelo. Isso seria particularmente valioso em contextos onde a compreensão do raciocínio por trás das previsões é de extrema importância.

### Plano de Contingência para Falhas nas Predições

&emsp;Dado que não foi possível selecionar um modelo preditivo devido ao overfitting nos dados, um plano de contingência se torna menos relevante e apenas hipotético nesta etapa. No entanto, ainda é importante considerar medidas para lidar com futuras situações similares. Abaixo, sugerimos um plano de contingência para lidar com uma situação hipotética na qual não ocorreu o overfitting mas, ainda assim, o modelo esta realizando predições equivocadas:

#### Passo 1: Análise Detalhada dos Dados

- &emsp;Realizar uma análise minuciosa dos dados utilizados no treinamento do modelo.
- &emsp;Identificar possíveis inconsistências ou desbalanceamentos que possam estar afetando as predições.

#### Passo 2: Reavaliação do Modelo

- &emsp;Considerar a possibilidade de reavaliar o modelo atual e reentrená-lo com um conjunto de dados mais abrangente ou ajustado.
- &emsp;Explorar a viabilidade de utilizar um conjunto de dados mais atualizado, caso esteja disponível.

#### Passo 3: Exploração de Outros Modelos
- &emsp;Avaliar a aplicação de diferentes algoritmos de aprendizado de máquina que possam ser mais adequados ao contexto e aos dados disponíveis.

#### Passo 4: Implementação de Melhorias Incrementais
- &emsp;Realizar ajustes nos hiperparâmetros do modelo atual para melhorar o desempenho e a precisão das predições.

#### Passo 5: Monitoramento Contínuo
- &emsp;Estabelecer um processo de monitoramento constante das predições do modelo, identificando rapidamente quaisquer desvios ou problemas de desempenho.

#### Passo 6: Feedback Iterativo
- &emsp;Estabelecer um ciclo de feedback entre a equipe responsável pelo modelo e os especialistas no domínio, visando aprimorar continuamente as predições.

&emsp;Lembrando que este plano de contingência é hipotético, uma vez que, no momento, o overfitting está impactando a seleção do modelo. Contudo, ao considerar cenários futuros, estas etapas fornecem um guia valioso para lidar com predições equivocadas em situações onde overfitting não seja um fator relevante.

&emsp;Além disso, também sugerimos um plano de contigência para lidar com o problema atual que é o overfitting:

### Plano de Contingência para Lidar com Overfitting

#### 1. **Avaliação Constante dos Dados:**
- &emsp;Mantenha uma vigilância constante sobre a qualidade dos dados. Estabeleça procedimentos regulares de revisão e limpeza para identificar e corrigir possíveis fontes de overfitting.

#### 2. **Aumento do Tamanho do Conjunto de Dados:**
- &emsp;Quando possível, procure aumentar o tamanho do conjunto de dados de treinamento. Isso pode ajudar a reduzir a tendência ao overfitting, permitindo que o modelo aprenda padrões mais representativos.

#### 3. **Implementação de Regularização:**
- &emsp;Considere a aplicação de técnicas de regularização, como L1 (Lasso) ou L2 (Ridge), em modelos mais complexos. Isso pode ajudar a reduzir a complexidade do modelo e mitigar o overfitting.

#### 4. **Validação Cruzada Adequada:**
- &emsp;Utilize técnicas de validação cruzada, como K-fold cross-validation, para avaliar o desempenho do modelo em diferentes conjuntos de dados. Isso ajuda a garantir que o modelo não esteja superajustando a um conjunto de dados específico.

#### 5. **Seleção de Atributos Significativos:**
- &emsp;Analise os atributos utilizados no modelo e verifique se todos são realmente relevantes. A remoção de atributos menos informativos pode ajudar a reduzir a complexidade do modelo e prevenir o overfitting.

#### 6. **Monitoramento Contínuo e Retreinamento:**
- &emsp;Estabeleça um processo de monitoramento contínuo da performance do modelo. Se sinais de overfitting forem detectados, reajauste e retreinamento devem ser realizados.

#### 7. **Exploração de Modelos Alternativos:**
- &emsp;Considere a exploração de modelos mais simples ou técnicas de aprendizado de máquina mais robustas para cenários onde o overfitting é uma preocupação significativa.

&emsp;Este plano de contingência visa proporcionar uma estrutura para lidar com o overfitting em projetos futuros, garantindo que a qualidade do modelo não seja comprometida por viéses nos dados.

### Explicabilidade do Modelo e Verificação de Hipóteses

&emsp;A explicabilidade do modelo é crucial para estabelecer confiança com os stakeholders. No caso do modelo Random Forest, podemos analisar a importância relativa de cada variável na tomada de decisão do modelo. Isso pode ser visualizado através de gráficos de barras ou tabelas que destacam as features mais influentes.

&emsp;Além disso, as hipóteses subjacentes ao modelo podem ser verificadas através de testes de significância estatística e análise de correlações entre as variáveis.

### Visualizações de Dados

## <a name="c5"></a>5. Conclusões e Recomendações

&emsp;Durante o processo de análise e desenvolvimento do modelo preditivo focado no acompanhamento de provisionamento em FIDCs em colaboração com a CVM, nos deparamos com desafios significativos relacionados à qualidade e integridade dos dados fornecidos.

#### Desafios Encontrados:

1. **Inconsistências nos Dados:** Muitas colunas na base de dados estavam zeradas ou continham informações incompletas, o que afetou a eficácia e a precisão do nosso modelo.

2. **Overfitting:** Devido às incoerências na base de dados, nosso modelo sofreu de overfitting, tornando-se excessivamente adaptado aos dados de treinamento. Isso limitou a capacidade do modelo de fazer previsões generalizadas e precisas em dados não vistos.

#### Expectativas em um Cenário Ideal:

&emsp;Se tivéssemos acesso a uma base de dados mais coerente e completa, nossas expectativas e conclusões seriam:

1. **Concentração de Cedentes e Risco Associado:** FIDCs altamente concentrados em poucos cedentes tenderiam a um risco maior de provisionamento inadequado.

2. **Atividades de Gestão de Créditos e Risco Associado:** FIDCs que participam regularmente de recompras, substituições ou renegociações de créditos apresentariam padrões de risco distintos.

3. **Dinâmica dos Créditos:** A inadimplência e o VR entre DCs com e sem riscos se comportariam de forma diferente, necessitando de análise e gestão separadas.

#### Recomendações:

1. **Revisão e Limpeza dos Dados:** Antes de qualquer tentativa futura de modelagem ou análise, é crucial que a base de dados seja revisada e limpa para garantir sua integridade.

2. **Monitoramento Contínuo em Base Limpa:** Uma vez que a base esteja em condições adequadas, a criação de um painel de controle para monitorar regularmente os indicadores-chave é essencial.

3. **Comunicação Transparente:** Informar aos stakeholders sobre os desafios encontrados na base de dados atual e a importância de manter registros precisos para futuras análises.

&emsp;Em resumo, enquanto o atual conjunto de dados limitou nossa capacidade de alcançar conclusões concretas, acreditamos firmemente no potencial do projeto e nas conclusões que poderíamos alcançar em um cenário ideal. É essencial que a qualidade dos dados seja priorizada para garantir análises futuras mais precisas e benéficas.



### Sugestões para Melhorar a Governança de Dados

#### Melhoria do Banco de Dados para Potencializar o Modelo Preditivo

&emsp;Os resultados do modelo preditivo apontam para a necessidade de aprimoramentos na governança de dados, porque ao executar o modelo preditivo foram encontrados dados em Overfitting, isto é, para o modelo é muito difícil sugerir que um fundo de investimeno não está saudável. Para maximizar a eficácia do modelo e garantir decisões mais precisas e confiáveis, é essencial implementar as seguintes sugestões:

1. **Aprimoramento da Qualidade dos Dados:**
- &emsp;Realize uma revisão abrangente dos dados disponíveis. Identifique e corrija inconsistências, valores ausentes e possíveis outliers que possam afetar a performance do modelo.

2. **Atualização e Enriquecimento dos Dados:**
- &emsp;Mantenha o banco de dados atualizado com as informações mais recentes. Considere também a possibilidade de enriquecer os dados com fontes externas confiáveis para aumentar a precisão das previsões.

3. **Padronização e Normalização:**
- &emsp;Garanta que os dados estejam padronizados e normalizados de acordo com as melhores práticas da indústria. Isso facilitará a interpretação e a utilização pelo modelo preditivo.

4. **Validação e Auditoria de Dados:**
- &emsp;Implemente processos de validação e auditoria de dados para assegurar a integridade e a consistência das informações armazenadas no banco de dados.

5. **Estabelecimento de Metadados Claros:**
- &emsp;Documente e descreva de forma clara os metadados associados aos dados. Isso facilitará a compreensão e a utilização adequada das informações pelos usuários.

6. **Treinamento e Conscientização da Equipe:**
- &emsp;Ofereça treinamento e conscientização sobre a importância da governança de dados e a influência direta que isso tem na eficácia do modelo preditivo.

7. **Avaliação de Impacto nas Decisões de Negócio:**
- &emsp;Estude como as decisões baseadas nas previsões do modelo afetam o negócio e aprimore os processos de implementação das recomendações.

&emsp;A implementação dessas sugestões não apenas melhorará a qualidade dos dados, mas também aumentará a confiabilidade e a precisão das previsões geradas pelo modelo preditivo.

### Discussão sobre a Explicabilidade do Modelo RF:

&emsp;O modelo Random Forest (RF) possui uma boa capacidade de explicabilidade. Isso significa que é possível compreender como o modelo toma suas decisões. Ele opera através de múltiplas árvores de decisão, o que facilita a interpretação das features mais importantes para as previsões. Além disso, a contribuição de cada variável pode ser quantificada, fornecendo insights sobre quais fatores mais influenciam as predições.

### Verificação de Aceitação ou Refutação de Hipóteses:

&emsp;Em um caso hipotético, para aceitar ou refutar as hipóteses, seriam utilizadas métricas de avaliação de desempenho do modelo, como acurácia, F1 Score e Recall Score. Essas métricas seriam comparadas com os critérios de aceitação previamente estabelecidos para determinar se o modelo atende aos objetivos do projeto.

### Principais Resultados do Projeto:

&emsp;Os principais resultados do projeto indicam que, mesmo com a presença de overfitting nos dados, o modelo Random Forest demonstrou capacidade promissora em lidar com complexidades e não-linearidades nos dados de fundos de investimento. Além disso, a interpretabilidade do modelo o torna uma escolha valiosa em cenários onde transparência e explicabilidade são cruciais.

### Recomendações Formais:

&emsp;Recomendamos que o modelo Random Forest seja considerado como uma opção viável para a classificação de fundos de investimento. No entanto, é importante abordar o overfitting nos dados através de estratégias de regularização ou obtenção de um conjunto de dados mais representativo.

### Recomendações Éticas e Estratégicas:

&emsp;Dado o impacto das decisões do modelo, é crucial tratar as pessoas potencialmente afetadas de maneira estratégica e ética. Sugerimos a implementação de um processo de feedback contínuo com especialistas no domínio para garantir que o modelo esteja alinhado com as necessidades e valores da organização. Além disso, considerar a criação de um manual de usuário detalhado para garantir o uso adequado e ético do modelo.

### Anexos:

Recomendamos a inclusão de um manual de usuário mais detalhado como anexo, fornecendo orientações específicas sobre como interpretar e utilizar o modelo de forma eficaz e ética. Isso contribuirá para a transparência e a responsabilidade no uso do modelo preditivo.

## <a name="c6"></a>6. Referências

fontes:

https://app.uff.br/riuff;/handle/1/2393 - Acesso em 7 de Agosto de 2023

https://blog.toroinvestimentos.com.br/investimentos/cvm-comissao-de-valores-mobiliarios#:~:text=Os%20valores%20da%20CVM&text=Veja%2C%20logo%20abaixo%2C%20as%20principais,fortalecer%20o%20mercado%20de%20capitais. - Acesso em 7 de agosto de 2023

https://www.gov.br/cvm/pt-br/acesso-a-informacao-cvm/servidores/remuneracao - Acesso em 15 de Agosto de 2023

https://www.gov.br/cvm/pt-br/acesso-a-informacao-cvm/institucional/sobre-a-cvm - Acesso em 12 de Agosto de 2023

https://endeavor.org.br/estrategia-e-gestao/entenda-matriz-swot/?gclid=Cj0KCQjwrMKmBhCJARIsAHuEAPR8-d7NK9rhZ8_WykH8wDfsx4kPpVcGV1w3Gid2zLuq_siOdMGi5zgaAj_fEALw_wcB - Acesso em 21 de agosto de 2023

https://www.gov.br/cvm/pt-br/acesso-a-informacao-cvm/acoes-e-programas/plano-estrategico - Acesso em 17 de Setembro de 2023 

https://blocktrends.com.br/cvm-tem-orcamento-de-r25-milhoes-para-fiscalizar-r25-trilhoes/ - Acesso em 12 de Setembro de 2023

https://braziljournal.com/play/preciso-de-duas-a-tres-vezes-mais-servidores-diz-presidente-da-cvm/ - Acesso em 25 de agosto de 2023

https://www.poder360.com.br/brasil/governo-lula-fara-1a-indicacao-a-cvm-apos-renuncia-de-diretor/

https://valor.globo.com/financas/noticia/2023/07/25/acordo-entre-cvm-e-b3-educacao-mira-inclusao-financeira.ghtml - Acesso em 8 de Setembro de 2023

https://www.gov.br/cvm/pt-br/acesso-a-informacao-cvm/acoes-e-programas/plano-estrategico/planejamento_estrategico_cvm_2013_2023.pdf - Acesso em 1 de Setembro de 2023

https://www.cnnbrasil.com.br/economia/minoritarios-denunciam-americanas-a-cvm-e-pedem-investigacao-sobre-pwc/ - Acesso em 27 de Setembro de 2023




## <a name="attachments"></a> Anexos

Vídeo de utilização do modelo: https://youtu.be/4NcCQyeQT1w
