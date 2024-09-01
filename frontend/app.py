import streamlit as st
import requests

API_URL = 'http://127.0.0.1:5000/candidates'

st.title("Applicant Tracking System")

def add_candidate():
    with st.expander("Add Candidate"):
        with st.form(key='add_candidate_form'):
            name = st.text_input("Name", key='add_name')
            email = st.text_input("Email", key='add_email')
            resume = st.text_area("Resume", key='add_resume')
            status = st.selectbox("Status", ["Applied", "Interviewed", "Hired", "Rejected"], key='add_status')
            submit_button = st.form_submit_button("Add Candidate")

            if submit_button:
                response = requests.post(API_URL, json={'name': name, 'email': email, 'resume': resume, 'status': status})
                if response.status_code == 201:
                    st.success(response.json().get('message', 'Candidate added successfully'))
                else:
                    st.error('Failed to add candidate')

def update_candidate():
    with st.expander("Update Candidate"):
        candidate_id = st.number_input("Candidate ID", min_value=1, key='update_candidate_id')
        with st.form(key='update_candidate_form'):
            name = st.text_input("Name", key='update_name')
            email = st.text_input("Email", key='update_email')
            resume = st.text_area("Resume", key='update_resume')
            status = st.selectbox("Status", ["Applied", "Interviewed", "Hired", "Rejected"], key='update_status')
            update_button = st.form_submit_button("Update Candidate")

            if update_button:
                response = requests.put(f'{API_URL}/{candidate_id}', json={'name': name, 'email': email, 'resume': resume, 'status': status})
                if response.status_code == 200:
                    st.success(response.json().get('message', 'Candidate updated successfully'))
                else:
                    st.error('Failed to update candidate')

def delete_candidate():
    with st.expander("Delete Candidate"):
        candidate_id = st.number_input("Candidate ID", min_value=1, key='delete_candidate_id')
        delete_button = st.button("Delete Candidate")

        if delete_button:
            response = requests.delete(f'{API_URL}/{candidate_id}')
            if response.status_code == 200:
                st.success(response.json().get('message', 'Candidate deleted successfully'))
            else:
                st.error('Failed to delete candidate')

def view_candidates():
    with st.expander("View Candidates"):
        response = requests.get(API_URL)
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

# Call functions to render UI
add_candidate()
update_candidate()
delete_candidate()
view_candidates()
