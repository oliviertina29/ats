import streamlit as st
import requests

# Ajouter CSS personnalisé pour améliorer le style
st.markdown("""
    <style>
    .main {
        background-color: #e4e4ed;
    }
    .st-expander {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .st-expander-header {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 8px 8px 0 0;
        margin: -10px -10px 10px -10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 40px;
        width: 100%;
        margin-top: 10px;
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        border: 1px solid #dcdcdc;
        border-radius: 4px;
        padding: 8px;
    }
    .centered-title {
        text-align: center;
        color: #333;
        padding: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

API_URL = 'http://0.0.0.0:5000'

# Centrer le titre avec HTML
st.markdown("<h1 class='centered-title'>📋 Applicant Tracking System</h1>", unsafe_allow_html=True)

def add_candidate():
    with st.expander("➕ Add Candidate"): #, expanded=True
        st.markdown('<div class="st-expander-header">Add a New Candidate</div>', unsafe_allow_html=True)
        st.write("Complete the form below to add a new candidate to the system.")
        with st.form(key='add_candidate_form'):
            name = st.text_input("Name", key='add_name')
            email = st.text_input("Email", key='add_email')
            resume = st.text_area("Resume", key='add_resume')
            status = st.selectbox("Status", ["Applied", "Interviewed", "Hired", "Rejected"], key='add_status')
            submit_button = st.form_submit_button("Add Candidate")

            if submit_button:
                response = requests.post(f"{API_URL}/candidates", json={'name': name, 'email': email, 'resume': resume, 'status': status})
                if response.status_code == 201:
                    st.success(response.json().get('message', 'Candidate added successfully'))
                else:
                    st.error('Failed to add candidate')

def update_candidate():
    with st.expander("🔄 Update Candidate"):
        st.markdown('<div class="st-expander-header">Update Candidate Details</div>', unsafe_allow_html=True)
        st.write("Provide the candidate ID and updated details below.")
        candidate_id = st.number_input("Candidate ID", min_value=1, key='update_candidate_id')
        with st.form(key='update_candidate_form'):
            name = st.text_input("Name", key='update_name')
            email = st.text_input("Email", key='update_email')
            resume = st.text_area("Resume", key='update_resume')
            status = st.selectbox("Status", ["Applied", "Interviewed", "Hired", "Rejected"], key='update_status')
            update_button = st.form_submit_button("Update Candidate")

            if update_button:
                response = requests.put(f"{API_URL}/candidates/{candidate_id}", json={'name': name, 'email': email, 'resume': resume, 'status': status})
                if response.status_code == 200:
                    st.success(response.json().get('message', 'Candidate updated successfully'))
                else:
                    st.error('Failed to update candidate')

def delete_candidate():
    with st.expander("❌ Delete Candidate"):
        st.markdown('<div class="st-expander-header">Delete a Candidate</div>', unsafe_allow_html=True)
        st.write("Enter the candidate ID to delete the record.")
        candidate_id = st.number_input("Candidate ID", min_value=1, key='delete_candidate_id')
        delete_button = st.button("Delete Candidate")

        if delete_button:
            response = requests.delete(f"{API_URL}/candidates/{candidate_id}")
            if response.status_code == 200:
                st.success(response.json().get('message', 'Candidate deleted successfully'))
            else:
                st.error('Failed to delete candidate')

def view_candidates():
    with st.expander("👀 View Candidates"):
        st.markdown('<div class="st-expander-header">View All Candidates</div>', unsafe_allow_html=True)
        response = requests.get(f"{API_URL}/candidates")
        if response.status_code == 200:
            candidates = response.json()
            if candidates:
                st.write("List of Candidates:")
                for c in candidates:
                    st.write(f"ID: {c['id']}, Name: {c['name']}, Email: {c['email']}, Status: {c['status']}")
            else:
                st.write("No candidates available.")
        else:
            st.error('Failed to fetch candidates')

def match_candidates():
    with st.expander("🔍 Match Candidates with Job Description"):
        st.markdown('<div class="st-expander-header">Match Candidates</div>', unsafe_allow_html=True)
        job_description = st.text_area("Job Description", key='job_description')
        match_button = st.button("Match Candidates")

        if match_button:
            if job_description:
                response = requests.post(f"{API_URL}/match", json={'job_description': job_description})
                if response.status_code == 200:
                    matched_candidates = response.json()
                    if matched_candidates:
                        st.write("Matched Candidates (sorted by relevance):")
                        for mc in matched_candidates:
                            st.write(f"ID: {mc['id']}, Name: {mc['name']}, Email: {mc['email']}, Score: {mc['score']}")
                    else:
                        st.write("No matching candidates found.")
                else:
                    st.error('Failed to match candidates')
            else:
                st.error("Please provide a job description to match candidates.")

# Appel des fonctions pour rendre l'interface utilisateur
add_candidate()
update_candidate()
delete_candidate()
view_candidates()
match_candidates()
