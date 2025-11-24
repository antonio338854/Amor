import streamlit as st
import time
import random

# --- Configuração Visual (Romântica/Misteriosa) ---
st.set_page_config(page_title="Oráculo do Destino", page_icon="🔮", layout="centered")

# CSS para deixar o app com cara de "Mágica" e botões bonitos
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 25px;
        border: none;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    .stButton>button:hover {
        background-color: #ff1f1f;
    }
    h1 {
        color: #E91E63;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    .big-text {
        font-size: 22px;
        text-align: center;
        color: #333;
        font-weight: bold;
    }
    .resultado-card {
        padding: 20px;
        background-color: #FFF0F5;
        border-radius: 15px;
        border: 2px solid #E91E63;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Cabeçalho ---
st.title("🔮 O Oráculo da Conexão")
st.write("O algoritmo quântico que analisa a vibração dos nomes e das estrelas.")

# --- Entradas ---
col1, col2 = st.columns(2)
with col1:
    nome1 = st.text_input("Seu Nome")
    signo1 = st.selectbox("Seu Signo", ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"])

with col2:
    nome2 = st.text_input("Nome Dela(e)")
    signo2 = st.selectbox("Signo Dela(e)", ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"])

# --- Botão Mágico ---
if st.button("❤️ Calcular Nossa Sintonia"):
    if nome1 and nome2:
        # Efeito de suspense (MUITO IMPORTANTE para impressionar)
        barra = st.progress(0)
        status = st.empty()
        
        etapas = [
            "Conectando aos satélites do amor...",
            "Analisando numerologia dos nomes...",
            "Verificando alinhamento dos planetas...",
            "Consultando banco de dados do destino...",
            "Calculando probabilidades quânticas..."
        ]
        
        for i, etapa in enumerate(etapas):
            status.text(etapa)
            # Avança a barra
            time.sleep(0.7) # Tempo para dar suspense
            barra.progress((i + 1) * 20)
            
        status.empty()
        barra.empty()
        
        # --- A Lógica do Vovô (O Truque) ---
        # Gera sempre uma nota alta (entre 85% e 100%) para não passar vergonha
        # Mas usa os nomes para parecer aleatório, então se digitar o mesmo nome dá o mesmo número
        seed = len(nome1) + len(nome2) + len(signo1) + len(signo2)
        random.seed(seed) 
        compatibilidade = random.randint(86, 100)
        
        # Frases bonitas baseadas na porcentagem
        frases = [
            "Vocês têm uma energia cósmica rara! O universo conspira a favor.",
            "A química é inegável. Uma conexão que acontece uma vez a cada 100 anos.",
            "Almas que se reconhecem. A sintonia de vocês é de outro mundo!",
            "O match perfeito! As estrelas estão aplaudindo essa dupla."
        ]
        frase_escolhida = random.choice(frases)

        # --- O Grande Resultado ---
        st.balloons() # Solta balões na tela (Efeito WOW)
        
        st.markdown(f"""
        <div class="resultado-card">
            <h2>✨ Resultado Final ✨</h2>
            <h1 style='font-size: 60px;'>{compatibilidade}%</h1>
            <p class="big-text">{frase_escolhida}</p>
            <hr>
            <p style='color: gray; font-size: 14px;'>Análise: {signo1} com {signo2} gera uma fusão energética poderosa baseada na empatia e companheirismo.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Música (player fake só para dar clima) ou recomendação
        st.success(f"Dica do Oráculo: Convide {nome2} para sair hoje. A sorte está lançada! 🍀")

    else:
        st.warning("Ei, o Oráculo precisa dos dois nomes para trabalhar!")

st.markdown("---")
st.caption("Desenvolvido exclusivamente para analisar conexões reais.")
