import streamlit as st
import PIL as Image


# Cria um dicionário com informações sobre as imagens
images = {
    "image1": {"name": "Imagem 1", "path": "/imagem1.JPG", "votes": 0},
    "image2": {"name": "Imagem 2", "path": "imagem2.JPG", "votes": 0},
    "image3": {"name": "Imagem 3", "path": "imagem3.JPG", "votes": 0},
    "image4": {"name": "Imagem 4", "path": "imagem4.JPG", "votes": 0},
    "image5": {"name": "Imagem 5", "path": "imagem5.JPG", "votes": 0},
    "image6": {"name": "Imagem 6", "path": "imagem6.PNG", "votes": 0},
    "image7": {"name": "Imagem 7", "path": "imagem7.JPG", "votes": 0},
    "image8": {"name": "Imagem 8", "path": "imagem8.JPG", "votes": 0},
    "image9": {"name": "Imagem 9", "path": "imagem9.mp4", "votes": 0},
    # Adicione aqui as demais imagens
}

# Definir a grade com 3 colunas e 8 linhas
col1, col2,col3 = st.columns(3)

# Exibe cada imagem em sua respectiva coluna
for i, image in enumerate(images):
    if i < 3:
        with col1:
            image_path = images[image]["path"]
            img = Image.open(image_path)
            st.image(img, width=200)
            if st.button("Votar na " + images[image]["name"]):
                images[image]["votes"] += 1
                st.write("A " + images[image]["name"] + " teve " + str(images[image]["votes"]) + " votos.")
    elif i < 6:
        with col2:
            image_path = images[image]["path"]
            img = Image.open(image_path)
            st.image(img, width=200)
            if st.button("Votar na " + images[image]["name"]):
                images[image]["votes"] += 1
                st.write("A " + images[image]["name"] + " teve " + str(images[image]["votes"]) + " votos.")
    else:
        with col3:
            image_path = images[image]["path"]
            img = Image.open(image_path)
            st.image(img, width=200)
            if st.button("Votar na " + images[image]["name"]):
                images[image]["votes"] += 1
                st.write("A " + images[image]["name"] + " teve " + str(images[image]["votes"]) + " votos.")
