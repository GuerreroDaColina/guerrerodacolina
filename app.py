from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina_imagens')
def pagina_imagens():
    return render_template('pagina_imagens.html')

@app.route('/nova_pagina/<int:contador>')
def nova_pagina(contador):
    imagens = {
        1: {'nome': 'Imagem 1', 'arquivo': 'caldeiraria.png', 'texto': 'Escreva alguma coisa aqui'},
        2: {'nome': 'Imagem 2', 'arquivo': 'serralheria.png', 'texto': 'Texto da imagem 2'},
        3: {'nome': 'Imagem 3', 'arquivo': 'vidraçaria.jpg', 'texto': 'Texto da imagem 3'},
        4: {'nome': 'Imagem 4', 'arquivo': 'imagem2.jpg', 'texto': 'Escreva alguma coisa aqui'},
        5: {'nome': 'Imagem 5', 'arquivo': 'imagem3.jpg', 'texto': 'Texto da imagem 4'},
        6: {'nome': 'Imagem 6', 'arquivo': 'imagem4.png', 'texto': 'Texto da imagem 5'},
    }    
    imagem = imagens.get(contador)

    if imagem:
        return render_template('nova_pagina.html', imagem=imagem)
    else:
        return render_template('pagina_imagens.html')

@app.route('/outra_pagina/<int:contador>')
def outra_pagina(contador):
    outras_imagens = {
        1: {'nome': 'Imagem 1', 'arquivo': 'outra_imagem1.png', 'texto': 'Texto da imagem 1'},
        2: {'nome': 'Imagem 2', 'arquivo': 'outra_serralheria.png', 'texto': 'Texto da imagem 2'},
        3: {'nome': 'Imagem 3', 'arquivo': 'outra_vidraçaria.jpg', 'texto': 'Texto da imagem 3'},
        4: {'nome': 'Imagem 4', 'arquivo': 'outra_imagem2.png', 'texto': 'Texto da imagem 4'},
        5: {'nome': 'Imagem 5', 'arquivo': 'outra_imagem3.png', 'texto': 'Texto da imagem 5'},
        6: {'nome': 'Imagem 6', 'arquivo': 'outra_imagem4.png', 'texto': 'Texto da imagem 6'},
    }    
    imagem = outras_imagens.get(contador)

    if imagem:
        return render_template('outra_pagina.html', imagem=imagem)
    else:
        return render_template('pagina_imagens.html')

if __name__ == '__main__':
    app.run()