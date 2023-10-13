from PIL import Image
import os

# Caminho para o diretório contendo as imagens
caminho_diretorio = "img_male"

# Tamanho desejado para as imagens
tamanho = (224, 224)

# Loop para percorrer todas as imagens do diretório
for nome_arquivo in os.listdir(caminho_diretorio):
    if nome_arquivo.endswith(".jpg") or nome_arquivo.endswith(".jpeg") or nome_arquivo.endswith(".png"):
        # Abrir a imagem
        caminho_arquivo = os.path.join(caminho_diretorio, nome_arquivo)
        imagem = Image.open(caminho_arquivo)

        # Redimensionar para o tamanho desejado
        imagem_redimensionada = imagem.resize(tamanho)

        # Salvar a imagem redimensionada
        caminho_arquivo_redimensionado = os.path.join(caminho_diretorio, "redimensionado_" + nome_arquivo)
        imagem_redimensionada.save(caminho_arquivo_redimensionado)
