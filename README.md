# 31º Projeto Job Insights: 
<p align="center">
<img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/31-JobInsights.jpg?raw=true" alt="Header" />
<hr/>
<p align="center">
<a href="#project-description">Project Description</a> •
<a href="#in-this-project-i-learned-and-put-into-practice">Learning</a> •
<a href="#according-to-the-project-requirements-designated-by-trybe-i-learned-how-to">Requirements</a> •
<a href="#stacks">Stacks</a> •
<a href="#how-to-run-the-application">How to run the application</a>
</p>
<hr/>
<p align="center">
<a href="#descrição-do-projeto">Descrição do Projeto</a> •
<a href="#nesse-projeto-aprendi-e-coloquei-em-prática">Aprendizado</a> •
<a href="#de-acordo-com-os-requisitos-do-projeto-designados-pela-trybe-aprendi-como">Requisitos</a> •
<a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a> •
<a href="#como-rodar-a-aplicação">Rodar a Aplicação</a>
</p>
<hr/>

## Project Description
I completed this Computer Science project in Python during my learning period at Trybe, where I developed the implementation of functions for analyzing a dataset on jobs, which were extracted from the Glassdoor website and obtained (by Trybe) through Kaggle, a platform that provides datasets for data scientists.<br>

## In this project, I learned and put into practice:
- Use the Python interactive terminal  
- Use conditional and loop structures  
- Use Python's built-in functions  
- Use exception handling  
- Perform file manipulation  
- Write functions  
- Write tests with Pytest  
- Write my own modules and import them into other code  
<hr/>

## According to the project requirements designated by Trybe, I learned how to:
- ✅ Implement the `read` function
- ✅ Implement the `get_unique_job_types` function
- ✅ Implement the `get_unique_industries` function
- ✅ Implement the `filter_by_job_type` function
- ✅ Implement the `filter_by_industry` function
- ✅ Implement the `filter_by_salary_range` function
- ✅ Implement the `get_max_salary` function
- ✅ Implement the `get_min_salary` function
- ✅ Implement the `matches_salary_range` function
- ✅ Implement a test for the `count_occurrences` function
- ✅ Implement a test for the `read_brazilian_file` function
- ❌ Implement a test for the `sort_by` function
- ❌ Create the `/job` route receiving the `index` parameter
- ❌ Create the `view job` receiving the `index` parameter
- ❌ Implement `view job` so that it returns `status code 200` for valid jobs
- ❌ Implement `view job` to return the exact `HTML` of a job page

_*Note: In some projects, some requirements were not completed due to the accelerated pace of the course and not because I didn’t know how to do them. At the time, I just needed a little more time.*_

_*I haven’t decided yet if it’s better to leave it like this to demonstrate my progress during my learning, or if it would be better to complete the missing requirements from the course projects.*_

_*Feedback is welcome.*_

## Stacks
### BackEnd:
- Docker
- Python

<a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Docker2.png?raw=true" width="50" height="50" alt="Docker Icon" /></a><a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Python2.png?raw=true" width="50" height="50" alt="Python Icon" /></a>
<hr/>

## How to run the application?
### Local:
- Clone the repository: <br>
`git clone git@github.com:prtpj1/project-job-insights.git`
- Access the project folder: <br>
`cd project-job-insights`
- Create and activate the virtual environment: <br>
`python3 -m venv .venv && source .venv/bin/activate`
- Install the dependencies: <br>
`python3 -m pip install -r dev-requirements.txt`
- Access the Python terminal by typing: <br>
`python3`
- Inside the Python terminal, you can execute the functions, for example: <br>
`from src.jobs import read`
`read('src/jobs.csv')`

#### :whale: With Docker
- Confirm that Docker is running on your computer
- Clone the repository: <br>
`git clone git@github.com:prtpj1/project-job-insights.git`
- Access the project folder: <br>
`cd project-job-insights`
- Start the Docker container: <br>
`docker-compose up -d`
- Access the Docker container terminal: <br>
`docker exec -it project-job-insights-web-1 bash`
- Create and activate the virtual environment: <br>
`cd src`<br>
`python3 -m venv .venv && source .venv/bin/activate`
- Install the dependencies in the container terminal: <br>
`python3 -m pip install -r dev-requirements.txt`
- Access the Python terminal by typing: <br>
`python3`
- Inside the Python terminal, you can execute the functions, for example: <br>
`from src.jobs import read`
`read('src/jobs.csv')`
<hr/>
</br>
</br>

_*Note: If you encounter any difficulties with the instructions and want to give feedback, send me a message*_

<hr/>

## Descrição do Projeto
Fiz este projeto de Ciência da Computação em Python durante meu período de aprendizagem na Trybe onde desenvolvi a implementação de funções para análises de um conjunto de dados sobre empregos, que foram extraídos do site Glassdoor e obtidos (pela Trybe) através do Kaggle, uma plataforma que disponibiliza conjuntos de dados para cientistas de dados.<br>

## Nesse projeto, aprendi e coloquei em prática:
- Utilizar o terminal interativo do Python
- Utilizar estruturas condicionais e de repetição
- Utilizar funções built-in do Python
- Utilizar tratamento de exceções
- Realizar a manipulação de arquivos
- Escrever funções
- Escrever testes com Pytest
- Escrever meus próprios módulos e importá-los em outros códigos 
<hr/>

## De acordo com os requisitos do projeto designados pela Trybe aprendi como:
- ✅ Implementar a função `read`
- ✅ Implementar a função `get_unique_job_types`
- ✅ Implementar a função `get_unique_industries`
- ✅ Implementar a função `filter_by_job_type`
- ✅ Implementar a função `filter_by_industry`
- ✅ Implementar a função `filter_by_salary_range`
- ✅ Implementar a função `get_max_salary`
- ✅ Implementar a função `get_min_salary`
- ✅ Implementar a função `matches_salary_range`
- ✅ Implementar um teste para a função `count_occurrences`
- ✅ Implementar um teste para a função `read_brazilian_file`
- ❌ Implementar um teste para a função `sort_by`
- ❌ Criar a `rota /job` recebendo o parâmetro `index`
- ❌ Criar a `view job` recebendo o parâmetro `index`
- ❌ Implementar `view job` para que ela retorne `status code 200` para jobs válidos
- ❌ Implementar `view job` de forma a retornar o `HTML` exato de uma página de job

_*OBS: Em alguns projetos alguns requisitos não foram feitos devido a dinâmica acelerada do curso e não por eu não saber como fazê-los. Na época eu apenas precisaria de um pouco mais de tempo.*_

_*Ainda não decidi se é melhor deixar desta forma para demonstrar o meu progresso durante meu aprendizado ou se seria melhor completar os requisitos que ficaram faltando nos projetos do curso.*_

_*Feedbacks são bem vindos.*_

<hr/>

## Tecnologias Utilizadas
### BackEnd:
- Docker
- Python

<a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Docker2.png?raw=true" width="50" height="50" alt="Docker Icon" /></a><a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Python2.png?raw=true" width="50" height="50" alt="Python Icon" /></a>
<hr/>

## Como rodar a aplicação?
#### Rodando localmente
- Clone o repositório: <br>
`git clone git@github.com:prtpj1/project-job-insights.git`
- Acesse a pasta do projeto: <br>
`cd project-job-insights`
- Crie e habilite o ambiente virtual: <br>
`python3 -m venv .venv && source .venv/bin/activate`
- Instale as dependências: <br>
`python3 -m pip install -r dev-requirements.txt`
- Acesse o terminal python digitando: <br>
`python3 `
- Dentro do terminal python você poderá executar as funções, por exemplo: <br>
`from src.jobs import read`
`read('src/jobs.csv')`

<hr/>

#### :whale: Rodando com Docker
- Confirme que o Docker está rodando no seu computador
- Clone o repositório: <br>
`git clone git@github.com:prtpj1/project-job-insights.git`
- Acesse a pasta do projeto: <br>
`cd project-job-insights`
- Suba o container para o Docker: <br>
`docker-compose up -d`
- Acesse o terminal do container no Docker: <br>
`docker exec -it project-job-insights-web-1 bash`
- Crie e habilite o ambiente virtual: <br>
`cd src`<br>
`python3 -m venv .venv && source .venv/bin/activate`
- No terminal do container instale as dependências: <br>
`python3 -m pip install -r dev-requirements.txt`
- Acesse o terminal python digitando: <br>
`python3 `
- Dentro do terminal python você poderá executar as funções, por exemplo: <br>
`from src.jobs import read`
`read('src/jobs.csv')`
<hr/>
</br>
</br>

_*OBS: Se tiver alguma dificuldade com as instruções e quiser dar um feedback me mande uma mensagem*_

<hr/>


