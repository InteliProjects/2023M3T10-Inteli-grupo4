from flask import Flask, render_template, request, flash, redirect, url_for
import pandas as pd
import joblib
import os
from nbconvert import PythonExporter
import time

app = Flask(__name__)
app.secret_key = 'delfino'

caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_modelo = os.path.join(caminho_atual, '../notebooks/resultado_modelo_rf.pkl')

colunas_necessarias = ['Numero_Cotistas', 'Ativo', 'Ativo_Carteira',
       'Ativo_Direitos_Aquisicao',
       'Ativo_Direitos_Aquisicao_Creditos_Vencer_Adimplentes',
       'Ativo_Direitos_Aquisicao_Creditos_Vencer_Inadimplentes',
       'Ativo_Direitos_Aquisicao_Parcelas_Inadimplentes',
       'Ativo_Direitos_Aquisicao_Creditos_Inadimplentes',
       'Ativo_Direitos_Sem_Aquisicao',
       'Ativo_Direitos_Sem_Aquisicao_Creditos_Vencer_Adimplentes',
       'Ativo_Direitos_Sem_Aquisicao_Creditos_Vencer_Inadimplentes',
       'Ativo_Valores_Mobiliarios', 'Carteira', 'Patrimonio_Liquido',
       'Carteira_Direitos_Aquisicao_Inadimplentes', 'Valor_em_Risco',
       'Liquidez_curtoPrazo', 'Liquidez_medioPrazo', 'Liquidez_longoPrazo',
       'Fundo_Exclusivo_Não', 'Fundo_Exclusivo_Sim'
]

def converter_notebook_para_python():
    exporter = PythonExporter()
    (python_script, _) = exporter.from_filename('../notebooks/Destiny_resume.ipynb')
    return python_script

def executar_script_python():
    script = converter_notebook_para_python()
    exec(script)
    resultado = joblib.load(caminho_modelo)
    return resultado



@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/main', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        arquivo = request.files['arquivo']
        if arquivo.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(url_for('index'))
        
        try:
            df = pd.read_csv(arquivo)
        except pd.errors.ParserError as e:
            flash('Erro ao ler o arquivo CSV. Certifique-se de que o arquivo é válido.')
            return redirect(url_for('index'))


        colunas_existem = set(colunas_necessarias).issubset(set(df.columns))

        if colunas_existem:
            return redirect(url_for('upload'))
        else:
            flash('O arquivo não possui todas as colunas necessárias')
            return redirect(url_for('index'))

    return render_template('main.html', titulo='Modelo Preditivo')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        arquivo = request.files['arquivo']
        if arquivo.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(url_for('index'))

        df = pd.read_csv(arquivo)

        colunas_existem = set(colunas_necessarias).issubset(set(df.columns))

        if colunas_existem:
            resultado = executar_script_python()  
            joblib.dump(resultado, caminho_modelo)  
            return redirect(url_for('list'))  
        else:
            flash('O arquivo não possui todas as colunas necessárias')
            return redirect(url_for('index'))

    return render_template('upload.html', titulo='Processando Arquivo')

@app.route('/list', methods=['GET'])
def list():
    resultado = joblib.load(caminho_modelo)
    return render_template('list.html', titulo='list de Predições', predicoes=resultado)

if __name__ == '__main__':
    app.run(debug=True)
