import streamlit as st
import pandas as pd
import numpy as np
import time

class StreamlitApp:
    """
    Uma classe para encapsular a lógica de um aplicativo Streamlit usando OOP.
    """
    def __init__(self):
        """
        Inicializa a aplicação Streamlit.
        Define as configurações da página e o título principal.
        """
        st.set_page_config(layout="wide", page_title="Streamlit App com OOP")
        st.title("Meu Projeto Streamlit com OOP")
        st.write("Este aplicativo demonstra como estruturar um projeto Streamlit usando Programação Orientada a Objetos.")
        st.divider()

    def display_text_elements(self):
        """
        Exibe uma seção de elementos de texto.
        """
        st.header("1. Elementos de Texto (via método da classe)")
        st.text("Este é um texto simples usando `st.text` dentro de um método de classe.")
        st.markdown("**Texto em negrito** usando `st.markdown`.")
        st.subheader("Subtítulo")
        st.caption("Legenda de exemplo.")
        st.code("print('Olá, OOP!')", language="python")
        st.latex(r"E=mc^2")
        st.divider()

    def display_input_widgets(self):
        """
        Exibe uma seção de widgets de entrada.
        """
        st.header("2. Widgets de Entrada (via método da classe)")
        
        if st.button("Clique-me (OOP)!"):
            st.write("Botão clicado dentro da classe!")

        name = st.text_input("Qual é o seu nome?", "Visitante")
        st.write(f"Olá, {name}!")

        age = st.slider("Qual é a sua idade?", 0, 100, 25)
        st.write(f"Você tem {age} anos.")

        options = ['Opção A', 'Opção B', 'Opção C']
        selected_option = st.selectbox("Escolha uma opção:", options)
        st.write(f"Você escolheu: {selected_option}")

        st.divider()

    def display_data_and_charts(self):
        """
        Exibe uma seção de dados e gráficos.
        """
        st.header("3. Exibição de Dados e Gráficos (via método da classe)")

        df = pd.DataFrame(
            np.random.rand(10, 2),
            columns=['col_a', 'col_b']
        )
        st.dataframe(df)

        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )
        st.line_chart(chart_data)
        st.divider()

    def display_status_elements(self):
        """
        Exibe uma seção de elementos de status.
        """
        st.header("4. Elementos de Status (via método da classe)")
        st.info("Esta é uma mensagem de informação da classe.")
        
        progress_text = "Carregando dados..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        st.success("Carregamento completo!")

        with st.spinner('Processando...'):
            time.sleep(2)
        st.success('Processamento concluído!')
        st.divider()

    def run(self):
        """
        Executa o aplicativo Streamlit, chamando todos os métodos de exibição.
        """
        self.display_text_elements()
        self.display_input_widgets()
        self.display_data_and_charts()
        self.display_status_elements()

# Ponto de entrada da aplicação
if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
