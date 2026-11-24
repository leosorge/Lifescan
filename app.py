import streamlit as st

st.set_page_config(
    page_title="Lifescan",
    page_icon="🧬",
    layout="wide"
)

st.title("Lifescan")
st.markdown("### Cronologie di personaggi ispirate al Ma-Yi")
st.info("Simulazione narrativa. I profili sono predefiniti. Le cronologie non forniscono diagnosi, prognosi o indicazioni terapeutiche.")

# Sidebar for Character Selection & Input
st.sidebar.header("🎛️ Anagrafica e Biometria Personaggio")
nome = st.sidebar.text_input("Nome Personaggio", "Marco Valeri")
eta = st.sidebar.slider("Età Attuale", 18, 90, 44)
sesso = st.sidebar.selectbox("Sesso", ["M", "F"])
altezza = st.sidebar.number_input("Altezza (cm)", 140, 210, 182)
peso = st.sidebar.number_input("Peso (kg)", 40, 150, 74)
whr = st.sidebar.slider("WHR (Rapporto Vita/Fianchi)", 0.65, 1.20, 0.87, 0.01)

archetipo = st.sidebar.selectbox("Archetipo Principale (Wu Xing / Ma-Yi)", [
    "Tipo Legno (Mu Xing)",
    "Tipo Fuoco (Huo Xing)",
    "Tipo Terra (Tu Xing)",
    "Tipo Metallo (Jin Xing)",
    "Tipo Acqua (Shui Xing)"
])

# Dati simulati per i 5 archetipi con cronologia e medicina retrodatata
profili_db = {
    "Tipo Legno (Mu Xing)": {
        "asse": "Legno (Fegato/Colecisti)",
        "san_ting": "Regione Media (Sopracciglia/Naso) affilata, arcate sopraccigliari marcate",
        "segni": ["Tensione glabellare (Palazzo del Sigillo)", "Sub-ittero/rossore sclerale"],
        "fasi": {
            "<5 anni": "Ereditarietà energetica stabile, svezzamento precoce con sensibilità ai latticini e tendenza a coliche gassose.",
            "5-20 anni": "Infanzia e adolescenza con crescita rapida, reattività nervosa, irritabilità e sensibilità epato-biliare sotto stress scolastico.",
            "21-45 anni": "Piena attività lavorativa competitiva, stasi del Qi del Fegato, accumulo iniziale di grasso epatico e alterazione degli acidi biliari.",
            "46-65 anni (Medicina Retrodatata)": "Intervento a 48 anni: Protocollo di drenaggio biliare mirato, riduzione dell'iperinsulinemia e antiossidanti epatici per bloccare la fibrosi.",
            "46-65 anni (Crisi Critica)": "Crisi a 50-52 anni: Rischio di epatocarcinoma iniziale o colangiocarcinoma su base di steatosi cronica non trattata, oppure crisi ipertensiva acuta con colica biliare severa.",
            "66+ anni": "Mantenimento dell'elasticità tendinea e controllo pressorio costante per prevenire eventi vascolari e fibrosi epatica senile."
        }
    },
    "Tipo Fuoco (Huo Xing)": {
        "asse": "Fuoco (Cuore/Circolazione)",
        "san_ting": "Regione Media con zigomi pronunciati e punta del naso reattiva",
        "segni": ["Micro-teleangectasie zigomatiche/nasali", "Rossore alla punta del naso"],
        "fasi": {
            "<5 anni": "Costituzione vivace, riflessi pronti, sonno leggero e rapida reattività agli stimoli ambientali e termici.",
            "5-20 anni": "Adolescenza dinamica ma con tendenza a tachicardie emotive e dispersione energetica nello studio.",
            "21-45 anni": "Vita relazionale e lavorativa intensa, sovraccarico miocardico progressivo e aumento iniziale della viscosità ematica.",
            "46-65 anni (Medicina Retrodatata)": "Intervento a 48 anni: Terapia chelante o antiaggregante preventiva, controllo rigoroso della viscosità ematica e rivascolarizzazione laser endovascolare.",
            "46-65 anni (Crisi Critica)": "Crisi a 49-53 anni: Elevato rischio di infarto miocardico acuto o ischemia coronarica silente per aumento delle resistenze vascolari e cristalli di colesterolo.",
            "66+ anni": "Protezione rigorosa del microcircolo coronarico e cerebrale; gestione clinica dello stress ossidativo senile."
        }
    },
    "Tipo Terra (Tu Xing)": {
        "asse": "Terra (Milza/Stomaco)",
        "san_ting": "Regione Media (Naso carnoso, zigomi pieni) dominante",
        "segni": ["Borse sub-oculari pronunciate", "Gonfiore periorale"],
        "fasi": {
            "<5 anni": "Difficoltà nello svezzamento, tendenza al ristagno linfatico, adenoidi ingrossate e accumulo di muco infantile.",
            "5-20 anni": "Sensibilità gastrica, stanchezza post-prandiale e rallentamento del transito intestinale.",
            "21-45 anni": "Consolidamento della sindrome metabolica, dislipidemia mista, obesità androide e rallentamento della peristalsi.",
            "46-65 anni (Medicina Retrodatata)": "Intervento a 53-56 anni: Intervento bariatrico o metabolico aggressivo, dieta chetogenica ciclica e regolarizzazione della peristalsi intestinale.",
            "46-65 anni (Crisi Critica)": "Crisi a 55-58 anni: Rischio di adenocarcinoma gastrico o del colon-retto favorito da stasi cronica e iperinsulinismo, associato a ictus ischemico.",
            "66+ anni": "Gestione rigorosa del sovraccarico cardiovascolare e articolare legato al peso; riattivazione del metabolismo basale."
        }
    },
    "Tipo Metallo (Jin Xing)": {
        "asse": "Metallo (Polmone/Crasso)",
        "san_ting": "Regione Superiore e Media ben definite, lineamenti scolpiti",
        "segni": ["Pallore cutaneo", "Secchezza epidermica e solchi naso-labiali marcati"],
        "fasi": {
            "<5 anni": "Bronchi reattivi, tendenza a tracheiti ricorrenti e ipersensibilità delle mucose respiratorie.",
            "5-20 anni": "Crescita longilinea, spiccata attitudine analitica ma vulnerabilità alle infezioni delle alte vie aeree.",
            "21-45 anni": "Rigore professionale, ridotta capacità vitale polmonare e ipossia tissutale cronica (bassa PaCO2).",
            "46-65 anni (Medicina Retrodatata)": "Intervento a 50-54 anni: Applicazione di OME (Ossigenoterapia Molecolare Espansa), ginnastica respiratoria diaframmatica profonda e immunomodulazione mucosa.",
            "46-65 anni (Crisi Critica)": "Crisi a 52-56 anni: Rischio di carcinoma broncogeno o insufficienza respiratoria grave da fibrosi polmonare e stasi mucosale.",
            "66+ anni": "Preservazione della funzione ventilatoria e della barriera immunitaria mucosale contro le patologie degenerative senili."
        }
    },
    "Tipo Acqua (Shui Xing)": {
        "asse": "Acqua (Rene/Vescica)",
        "san_ting": "Regione Inferiore (Mento/Mandibola) solida ma soggetta a ristagno",
        "segni": ["Occhiaie scure profonde", "Perdita di tono sottomentoniero"],
        "fasi": {
            "<5 anni": "Ereditarietà renale delicata, fragilità ossea e sensibilità accentuata alle basse temperature.",
            "5-20 anni": "Sviluppo scheletrico disarmonico, affaticamento precoce e consumo della riserva energetica di fondo.",
            "21-45 anni": "Usura progressiva del Jing renale, iperuricemia persistente, proteinuria e prime calcificazioni tissutali.",
            "46-65 anni (Medicina Retrodatata)": "Intervento a 58-61 anni: Terapia alcalinizzante profonda, chelazione dell'acido urico, blocco della proteinuria con ACE-inibitori metabolici e laserterapia prostatica.",
            "46-65 anni (Crisi Critica)": "Crisi a 60-63 anni: Rischio di insufficienza renale cronica terminale, leucemia mieloide secondaria a tossicità midollare o carcinoma prostatico/vescicale.",
            "66+ anni": "Tutela rigorosa dell'integrità scheletrica, della funzione renale residua e prevenzione delle patologie reumatiche invalidanti."
        }
    }
}

profilo_attivo = profili_db[archetipo]
bmi = round(peso / ((altezza / 100) ** 2), 1)

# Main Dashboard Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📊 Profilo Biometrico & Costituzionale")
    st.info(f"**Soggetto:** {nome} ({eta} anni, {sesso})\n"
            f"**Biometria:** {altezza} cm, {peso} kg (BMI: {bmi}, WHR: {whr})\n"
            f"**Costituzione Ma-Yi:** {archetipo}\n"
            f"**Asse Energetico:** {profilo_attivo['asse']}")
    
    st.markdown("### 🔍 Tratti del profilo predefinito")
    for segno in profilo_attivo['segni']:
        st.write(f"- {segno}")
        
    st.markdown("### 🧬 San Ting (Analisi Zonale)")
    st.write(profilo_attivo['san_ting'])

with col2:
    st.markdown("### ⏳ Cronologia immaginaria")
    
    fasi_ordine = [
        ("<5 anni", "👶 Infanzia (<5 anni)"),
        ("5-20 anni", "🧒 Giovinezza (5-20 anni)"),
        ("21-45 anni", "🧑 Età Adulta (21-45 anni)"),
        ("46-65 anni (Medicina Retrodatata)", "🛡️ Intervento ipotizzato nella storia"),
        ("46-65 anni (Crisi Critica)", "⚠️ Evento ipotizzato nella storia"),
        ("66+ anni", "👴 Senescenza e Longevità (66+ anni)")
    ]
    
    for key, label in fasi_ordine:
        desc = profilo_attivo['fasi'][key]
        st.markdown(f"**{label}**\n\n{desc}")
