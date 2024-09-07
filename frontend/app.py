import streamlit as st
import requests
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="ATS - Applicant Tracking System", layout="wide", page_icon="📋")

# CSS personnalisé amélioré
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    .main {
        background-color: #f8f9fa;
        padding: 2rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .centered-title {
        text-align: center;
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        padding: 1rem;
        background-color: #ecf0f1;
        border-radius: 10px;
    }
    .subheader {
        color: #34495e;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #3498db;
    }
    .st-expander {
        background-color: #ffffff;
        border: none;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    .st-expander-header {
        font-size: 1.2rem;
        font-weight: bold;
        color: #2c3e50;
        background-color: #ecf0f1;
        padding: 1rem;
        border-radius: 10px 10px 0 0;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background-color: #2980b9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        padding: 0.5rem;
        font-size: 1rem;
    }
    .dataframe {
        font-size: 0.9rem;
        border-collapse: separate;
        border-spacing: 0;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        overflow: hidden;
    }
    .dataframe th {
        background-color: #f2f2f2;
        font-weight: bold;
        text-align: left;
        padding: 12px;
    }
    .dataframe td {
        padding: 12px;
        border-top: 1px solid #e0e0e0;
    }
    .stAlert {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

API_URL = 'http://0.0.0.0:5000'

# Titre centré
st.markdown("<h1 class='centered-title'>📋 Applicant Tracking System</h1>", unsafe_allow_html=True)

# Barre latérale pour la navigation
with st.sidebar:
    st.image("https://your-logo-url.com/logo.png", width=200)  # Remplacez par l'URL de votre logo
    st.markdown("## Navigation")
    page = st.radio("", ["Dashboard", "Add Candidate", "Update Candidate", "View Candidates", "Match Candidates"])

def dashboard():
    st.markdown("<h2 class='subheader'>Dashboard</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    # Ces valeurs devraient être récupérées depuis votre API
    with col1:
        st.metric("Total Candidates", "100")
    with col2:
        st.metric("Applied", "50")
    with col3:
        st.metric("Interviewed", "30")
    with col4:
        st.metric("Hired", "20")
    
    st.markdown("<h3>Recent Activities</h3>", unsafe_allow_html=True)
    # Ici, vous pouvez ajouter un tableau ou une liste des activités récentes

def add_candidate():
    st.markdown("<h2 class='subheader'>Add a New Candidate</h2>", unsafe_allow_html=True)
    with st.form(key='add_candidate_form'):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name", key='add_name')
            email = st.text_input("Email", key='add_email')
        with col2:
            status = st.selectbox("Status", ["Applied", "Interviewed", "Hired", "Rejected"], key='add_status')
        resume = st.text_area("Resume", key='add_resume')
        submit_button = st.form_submit_button("Add Candidate")

        if submit_button:
            if name and email and resume:
                response = requests.post(f"{API_URL}/candidates", json={'name': name, 'email': email, 'resume': resume, 'status': status})
                if response.status_code == 201:
                    st.success(response.json().get('message', 'Candidate added successfully'))
                else:
                    st.error('Failed to add candidate')
            else:
                st.warning("Please fill in all fields.")

def update_candidate():
    st.markdown("<h2 class='subheader'>Update Candidate Details</h2>", unsafe_allow_html=True)
    candidate_id = st.number_input("Candidate ID", min_value=1, key='update_candidate_id')
    
    if st.button("Fetch Candidate Data"):
        response = requests.get(f"{API_URL}/candidates/{candidate_id}")
        if response.status_code == 200:
            candidate = response.json()
            with st.form(key='update_candidate_form'):
                col1, col2 = st.columns(2)
                with col1:
                    name = st.text_input("Name", value=candidate['name'], key='update_name')
                    email = st.text_input("Email", value=candidate['email'], key='update_email')
                with col2:
                    status = st.selectbox("Status", ["Applied", "Interviewed", "Hired", "Rejected"], index=["Applied", "Interviewed", "Hired", "Rejected"].index(candidate['status']), key='update_status')
                resume = st.text_area("Resume", value=candidate['resume'], key='update_resume')
                update_button = st.form_submit_button("Update Candidate")

                if update_button:
                    response = requests.put(f"{API_URL}/candidates/{candidate_id}", json={'name': name, 'email': email, 'resume': resume, 'status': status})
                    if response.status_code == 200:
                        st.success(response.json().get('message', 'Candidate updated successfully'))
                    else:
                        st.error('Failed to update candidate')
        else:
            st.error('Failed to fetch candidate details')

def view_candidates():
    st.markdown("<h2 class='subheader'>View All Candidates</h2>", unsafe_allow_html=True)
    response = requests.get(f"{API_URL}/candidates")
    if response.status_code == 200:
        candidates = response.json()
        if candidates:
            df = pd.DataFrame(candidates)
            st.dataframe(df[['id', 'name', 'email', 'status']], use_container_width=True)
            
            # Ajout d'un graphique
            st.markdown("<h3>Candidate Status Distribution</h3>", unsafe_allow_html=True)
            status_counts = df['status'].value_counts()
            st.bar_chart(status_counts)
        else:
            st.info("No candidates available.")
    else:
        st.error('Failed to fetch candidates')

def match_candidates():
    st.markdown("<h2 class='subheader'>Match Candidates with Job Description</h2>", unsafe_allow_html=True)
    job_description = st.text_area("Job Description", key='job_description')
    match_button = st.button("Match Candidates")

    if match_button:
        if job_description:
            with st.spinner('Matching candidates...'):
                response = requests.post(f"{API_URL}/match", json={'job_description': job_description})
                if response.status_code == 200:
                    matched_candidates = response.json()
                    if matched_candidates:
                        df = pd.DataFrame(matched_candidates)
                        st.dataframe(df[['id', 'name', 'email', 'score']].sort_values('score', ascending=False), use_container_width=True)
                        
                        # Ajout d'un graphique
                        st.markdown("<h3>Top 5 Candidates by Match Score</h3>", unsafe_allow_html=True)
                        top_5 = df.nlargest(5, 'score')
                        st.bar_chart(top_5.set_index('name')['score'])
                    else:
                        st.info("No matching candidates found.")
                else:
                    st.error('Failed to match candidates')
        else:
            st.warning("Please provide a job description to match candidates.")

# Affichage de la page sélectionnée
if page == "Dashboard":
    dashboard()
elif page == "Add Candidate":
    add_candidate()
elif page == "Update Candidate":
    update_candidate()
elif page == "View Candidates":
    view_candidates()
elif page == "Match Candidates":
    match_candidates()
