import requests
import streamlit as st


def buscar_letra(artista, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{artista}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra


st.image("https://i.imgur.com/SmktDIH.png")
# st.title("Letras de Música")
st.markdown("<h1 style='text-align: center;'>Letras de Músicas</h1>",
            unsafe_allow_html=True)

artista = st.text_input("Digite o nome do Artista: ", key="artista")
musica = st.text_input("Digite o nome da Música: ", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra = buscar_letra(artista, musica)
    if letra:
        st.success("Letra Disponível ✅")
        # st.text(letra)
        # Criação da moldura personalizada com degradê
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(to bottom right, #f0f0f0, #d9d9d9); /* Degradê de cinza claro para um cinza mais escuro */
                padding: 20px;
                border-radius: 10px;
                color: white;
                font-size: 18px;
                text-align: center;">
                <pre>{letra}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Não foi possível encontrar a Letra ❌")
