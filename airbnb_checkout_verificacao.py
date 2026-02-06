import streamlit as st
import pandas as pd
from datetime import datetime
import os
from pathlib import Path


# ===============================
# CONFIGURAÇÃO INICIAL
# ===============================
st.set_page_config(page_title="Check-out Apartamento", layout="wide")

def carregar_css():
    with open("design.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carregar_css()

st.title("🧾 Check-out – Verificação do Apartamento")

os.makedirs("dados", exist_ok=True)
os.makedirs("fotos", exist_ok=True)

ARQUIVO_HISTORICO = "dados/historico_checkout.csv"


# ===============================
# FUNÇÕES
# ===============================

def checklist_itens(itens, key_base):
    selecionados = []
    for item in itens:
        key = f"{key_base}_{item}"
        if key not in st.session_state:
            st.session_state[key] = False

        if st.checkbox(item, key=key):
            selecionados.append(item)

    st.session_state[f"{key_base}_itens_verificados"] = selecionados


def salvar_nomes_fotos(fotos, key):
    if fotos:
        st.session_state[key] = ", ".join([f.name for f in fotos])
    return st.session_state.get(key, "")


def salvar_fotos_em_pasta(fotos, apartamento, data_verificacao):
    if not fotos:
        return ""
    
    # Pasta MM_AA
    pasta_mes = data_verificacao.strftime("%m_%y")
    pasta_destino = Path("fotos") / pasta_mes
    pasta_destino.mkdir(parents=True, exist_ok=True)

    caminhos = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    apt_nome = apartamento.replace(" ", "_")

    for i, foto in enumerate(fotos, start=1):
        extensao = Path(foto.name).suffix
        nome_arquivo = f"checkout_{apt_nome}_{timestamp}_{i}{extensao}"
        caminho_final = pasta_destino / nome_arquivo

        with open(caminho_final, "wb") as f:
            f.write(foto.getbuffer())

        caminhos.append(str(caminho_final))

    return " | ".join(caminhos)


def preview_fotos(fotos, titulo):
    if fotos:
        st.markdown(f"📸 **{titulo}**")
        for foto in fotos:
            st.image(foto, use_container_width=True)

# ===============================
# IDENTIFICAÇÃO
# ===============================
st.header("🔹 Identificação")
col1, col2 = st.columns(2)

with col1:
    st.date_input("Data da verificação", key="data_verificacao")

APARTAMENTOS = ["Citta Residence", "Vista Park"]

with col2:
    st.selectbox("Apartamento", APARTAMENTOS, key="apartamento")

# ===============================
# QUARTOS
# ===============================
itens_quarto_1 = [
    "Cama", "Colchão", "Armário", "Televisão", "Controle da TV",
    "Prateleiras" , "Ventilador", "Cortinas", "Paredes", "Chão",
    "Janela", "Iluminação"
]

st.divider()
st.header("🛏️ Quarto 1")
checklist_itens(itens_quarto_1, "q1")
st.text_area("Observações do quarto 1:", key="q1_obs")
fotos_q1 = st.file_uploader(
    "Fotos do quarto 1", ["jpg", "png", "jpeg"],
    accept_multiple_files=True, key="fotos_q1"
)
preview_fotos(fotos_q1, "Fotos – Quarto 1")
salvar_nomes_fotos(fotos_q1, "quarto1_fotos")


itens_quarto_2 = [
    "Cama", "Colchão", "Prateleiras", "Paredes" , "Ventilador",
    "Cortinas", "Janela", "Iluminação"
]

st.divider()
st.header("🛏️ Quarto 2")
checklist_itens(itens_quarto_2, "q2")
st.text_area("Observações do quarto 2:", key="q2_obs")
fotos_q2 = st.file_uploader(
    "Fotos do quarto 2", ["jpg", "png", "jpeg"],
    accept_multiple_files=True, key="fotos_q2"
)
preview_fotos(fotos_q2, "Fotos – Quarto 2")
salvar_nomes_fotos(fotos_q2, "quarto2_fotos")


# ===============================
# Sala
# ===============================
itens_sala = [
    "Sofá", "Capa do sofá", "Mesa", "Cadeiras da mesa", "Jogo americano",
    "Televisão", "Controles TV", "Rack TV", "Aparelho da Claro/net",
    "Aparelho Branco(Gateway)", "DVD's", "Cadeiras do balcão", "Vidro do Balcão",
    "Quadros", "Papel de parede", "Paredes", "Taco de sinuca",
    "Suporte taco de sinuca", "Cortina", "Chão", "Iluminação"
]

st.divider()
st.header("🛋️ Sala")
checklist_itens(itens_sala, "sala")
st.text_area("Observações da sala:", key="sala_obs")
fotos_sala = st.file_uploader(
    "Fotos da sala", ["jpg", "png", "jpeg"],
    accept_multiple_files=True, key="fotos_sala"
)
preview_fotos(fotos_sala, "Fotos – Sala")
salvar_nomes_fotos(fotos_sala, "sala_fotos")


# ===============================
# BANHEIROS
# ===============================
itens_banheiro_1 = [
    "Vaso sanitário", "Descarga", "Chuveiro", "Box", "Suporte xampu",
    "Suporte sabonete", "Dispenser sabonete", "Dispenser xampu e condicionador", 
    "Pia", "Espelho", "Toalha de banho", "Toalha de rosto", "Tapete",
    "Lixeira", "Paredes", "Chão", "Iluminação", "Exaustor"
]

st.divider()
st.header("🚿 Banheiro 1")
checklist_itens(itens_banheiro_1, "b1")
st.text_area("Observações do banheiro 1:", key="b1_obs")
fotos_b1 = st.file_uploader(
    "Fotos do banheiro 1", ["jpg", "png", "jpeg"],
    accept_multiple_files=True, key="fotos_b1"
)
preview_fotos(fotos_b1, "Fotos – Banheiro 1")
salvar_nomes_fotos(fotos_b1, "banheiro1_fotos")


itens_banheiro_2 = [
    "Vaso sanitário", "Descarga", "Chuveiro", "Box", "Suporte xampu",
    "Suporte sabonete", "Dispenser sabonete", "Dispenser xampu e condicionador", 
    "Pia", "Espelho", "Toalha de banho", "Toalha de rosto", "Tapete",
    "Lixeira", "Paredes", "Iluminação", "Exaustor"
]

st.divider()
st.header("🚿 Banheiro 2")
checklist_itens(itens_banheiro_2, "b2")
st.text_area("Observações do banheiro 2:", key="b2_obs")
fotos_b2 = st.file_uploader(
    "Fotos do banheiro 2", ["jpg", "png", "jpeg"],
    accept_multiple_files=True, key="fotos_b2"
)
preview_fotos(fotos_b2, "Fotos – Banheiro 2")
salvar_nomes_fotos(fotos_b2, "banheiro2_fotos")


itens_lavabo = [
    "Vaso sanitário", "Descarga",  "Dispenser sabonete", 
    "Pia", "Espelho", "Toalha de mão", "Lixeira", "Paredes",
    "Quadro", "Chão", "Iluminação", "Exaustor"
]

st.divider()
st.header("🚿 Lavabo")
checklist_itens(itens_lavabo, "lavabo")
st.text_area("Observações do lavabo:", key="lavabo_obs")
fotos_lavabo = st.file_uploader(
    "Fotos do lavabo", ["jpg", "png", "jpeg"],
    accept_multiple_files=True, key="fotos_lavabo"
)
preview_fotos(fotos_lavabo, "Fotos – Lavabo")
salvar_nomes_fotos(fotos_lavabo, "lavabo_fotos")

#=======================================================================
## Caso queira juntar tudo em um código só
# for i in [1, 2, 3]:
#     st.divider()
#     st.header(f"🛁 Banheiro {i}")
#     checklist_itens(itens_banheiro, f"ban{i}")
#     st.text_area(f"Observações do banheiro {i}:", key=f"ban{i}_obs")
#     fotos_ban = st.file_uploader(
#         f"Fotos do banheiro {i}", ["jpg", "png", "jpeg"],
#         accept_multiple_files=True, key=f"fotos_ban{i}"
#     )
#     preview_fotos(fotos_ban, f"Fotos – Banheiro {i}")
#     salvar_nomes_fotos(fotos_ban, f"banheiro{i}_fotos")
#=======================================================================


# ===============================
# COZINHA – CONTAGEM
# ===============================
st.divider()
st.header("🍽️ Cozinha – Contagem de Itens")

itens_contagem = [
    "facas", "garfos", "colheres", "colheres_cha",
    "copos", "xicaras", "pratos", "petisqueiras",
    "refratário_forno", "porta-mantimentos"
]

labels = [
    "facas", "garfos", "colheres", "colheres_cha",
    "copos", "xicaras", "pratos", "petisqueiras",
    "refratário_forno", "porta-mantimentos"
]

cols = st.columns(4)
for i, (k, label) in enumerate(zip(itens_contagem, labels)):
    with cols[i % 4]:
        st.number_input(label, min_value=0, key=k)


# ===============================
# PANELAS E FRIGIDEIRAS
# ===============================

st.divider()
st.header("🍳 Panelas e Frigideiras")

estados_panelas = [
    "Bom estado",
    "Riscada",
    "Cabo solto",
    "Amassada",
    "Muito queimada",
    "Inutilizável"
]

panelas = [
    ("panela_grande", "Panela grande"),
    ("panela_media", "Panela média"),
    ("panela_pequena", "Panela pequena"),
    ("frigideiras", "Frigideiras")
]

for key, nome in panelas:

    st.subheader(nome)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.number_input(
            "Quantidade",
            min_value=0,
            key=f"{key}_qtd"
        )

    with col2:
        st.multiselect(
            "Estado:",
            estados_panelas,
            placeholder="Selecione a opção",
            key=f"{key}_estado"
        )

#st.divider()
#st.header("📸 Fotos – Cozinha e Panelas")

fotos_cozinha = st.file_uploader(
    "Fotos da cozinha e panelas",
    ["jpg", "png", "jpeg"],
    accept_multiple_files=True,
    key="fotos_cozinha",
)

preview_fotos(fotos_cozinha, "Fotos – Cozinha / Panelas")

# ===============================
# FINALIZAÇÃO
# ===============================
st.divider()
st.header("✅ Finalização")
st.radio("Apartamento liberado?", ["Sim", "Não"], horizontal=True, key="liberado")
st.text_area("Observações finais", key="obs_finais")

# ===============================
# REGISTRO ATUAL
# ===============================
registro = {
    "Data": st.session_state.data_verificacao,
    "Apartamento": st.session_state.apartamento,
    "Q1 Itens": ", ".join(st.session_state.get("q1_itens_verificados", [])),
    "Q1 Obs": st.session_state.q1_obs,
    "Q2 Itens": ", ".join(st.session_state.get("q2_itens_verificados", [])),
    "Q2 Obs": st.session_state.q2_obs,
    "Liberado": st.session_state.liberado,
    "Panelas Estado": ", ".join(st.session_state.get("estado_panelas", [])),
    "Obs Finais": st.session_state.obs_finais,
    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

for k in itens_contagem:
    registro[k.capitalize()] = st.session_state.get(k, 0)

df_atual = pd.DataFrame([registro])

# ===============================
# HISTÓRICO + VALIDAÇÃO
# ===============================
if os.path.exists(ARQUIVO_HISTORICO):
    df_historico = pd.read_csv(ARQUIVO_HISTORICO)
    df_historico["Data"] = pd.to_datetime(df_historico["Data"]).dt.date
else:
    df_historico = pd.DataFrame()

st.divider()
st.subheader("🔎 Filtrar histórico")

col_f1, col_f2 = st.columns(2)

with col_f1:
    data_filtro = st.date_input(
        "Selecione a data",
        value=None,
        key="filtro_data"
    )

with col_f2:
    apt_filtro = st.selectbox(
        "Apartamento",
        ["Todos"] + sorted(df_historico["Apartamento"].unique().tolist())
        if not df_historico.empty else ["Todos"],
        key="filtro_apto"
    )

df_filtrado = df_historico.copy()

if data_filtro:
    df_filtrado = df_filtrado[df_filtrado["Data"] == data_filtro]

if apt_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Apartamento"] == apt_filtro]


duplicado = False
if not df_historico.empty:
    duplicado = (
        (df_historico["Data"] == st.session_state.data_verificacao) &
        (df_historico["Apartamento"] == st.session_state.apartamento)
    ).any()

# ===============================
# TABELA
# ===============================


st.divider()
st.header("📊 Histórico de Check-outs")

df_exibir = df_historico.copy()

# transformar caminho da foto em link clicável
if not df_exibir.empty and "Fotos" in df_exibir.columns:
    def criar_link(fotos):
        if pd.isna(fotos) or fotos == "":
            return ""
        primeira_foto = fotos.split(" | ")[0]
        return f"[📸 Ver foto]({primeira_foto})"

    df_exibir["Fotos"] = df_exibir["Fotos"].apply(criar_link)

if duplicado:
    st.error("⚠️ Já existe um check-out para este apartamento nesta data.")
    st.markdown(df_exibir.to_markdown(index=False), unsafe_allow_html=True)
else:
    df_preview = pd.concat([df_exibir, df_atual], ignore_index=True)
    st.markdown(df_preview.to_markdown(index=False), unsafe_allow_html=True)


# ===============================
# SALVAR
# ===============================
if st.button("💾 FINALIZAR E SALVAR CHECK-OUT", disabled=duplicado):

    # ---- salvar fotos ----
    fotos_salvas = []

    fotos_salvas.append(
        salvar_fotos_em_pasta(
            st.session_state.get("fotos_q1"),
            st.session_state.apartamento,
            st.session_state.data_verificacao
        )
    )

    fotos_salvas.append(
        salvar_fotos_em_pasta(
            st.session_state.get("fotos_q2"),
            st.session_state.apartamento,
            st.session_state.data_verificacao
        )
    )

    for i in [1, 2, 3]:
        fotos_salvas.append(
            salvar_fotos_em_pasta(
                st.session_state.get(f"fotos_ban{i}"),
                st.session_state.apartamento,
                st.session_state.data_verificacao
            )
        )

    # 👉 NOVO: fotos da cozinha / panelas
    fotos_salvas.append(
        salvar_fotos_em_pasta(
            st.session_state.get("fotos_cozinha"),
            st.session_state.apartamento,
            st.session_state.data_verificacao
        )
    )

    registro["Fotos"] = " | ".join([f for f in fotos_salvas if f])

    # ---- salvar CSV ----
    df_final = pd.DataFrame([registro])
    header = not os.path.exists(ARQUIVO_HISTORICO)

    df_final.to_csv(
        ARQUIVO_HISTORICO,
        mode="a",
        header=header,
        index=False
    )

    st.success("✅ Check-out salvo com fotos e histórico atualizado!")



# ===============================
# VISUALIZAÇÃO DE FOTOS
# ===============================

st.divider()
st.subheader("📸 Visualização de Fotos")

df_filtrado = df_historico.copy()

if df_filtrado.empty:
    st.info("Ainda não existem check-outs salvos.")
else:
    # garantir tipo data
    df_filtrado["Data"] = pd.to_datetime(df_filtrado["Data"])

    col1, col2 = st.columns(2)

    # --- filtro de data ---
    datas_disponiveis = sorted(df_filtrado["Data"].dt.date.unique())
    datas_opcoes = ["Selecione a data"] + datas_disponiveis

    with col1:
        data_selecionada = st.selectbox(
            "📅 Data",
            options=datas_opcoes,
            index=0
        )

    # --- filtro de apartamento ---
    if data_selecionada == "Selecione a data":
        apartamentos_opcoes = ["Selecione o apartamento"]
    else:
        apartamentos_disponiveis = (
            df_filtrado[df_filtrado["Data"].dt.date == data_selecionada]
            ["Apartamento"]
            .unique()
        )
        apartamentos_opcoes = ["Selecione o apartamento"] + list(apartamentos_disponiveis)

    with col2:
        apartamento_selecionado = st.selectbox(
            "🏢 Apartamento",
            options=apartamentos_opcoes,
            index=0
        )

    # --- só exibe fotos se ambos forem selecionados ---
    if (
        data_selecionada != "Selecione a data"
        and apartamento_selecionado != "Selecione o apartamento"
    ):
        registro_selecionado = df_filtrado[
            (df_filtrado["Data"].dt.date == data_selecionada) &
            (df_filtrado["Apartamento"] == apartamento_selecionado)
        ]

        if registro_selecionado.empty:
            st.info("Nenhuma foto encontrada para esse filtro.")
        else:
            fotos = registro_selecionado.iloc[0]["Fotos"]

            st.markdown(
                f"### 📅 Fotos do check-out — {apartamento_selecionado} ({data_selecionada})"
            )

            caminhos = fotos.split(" | ")

            for caminho in caminhos:
                if os.path.exists(caminho):
                    st.image(caminho, use_container_width=True)
                else:
                    st.warning(f"Arquivo não encontrado: {caminho}")

