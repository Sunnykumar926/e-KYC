
from sqlalchemy import text,select

import streamlit as st

import pandas as pd


# Initialize connection.
conn = st.connection('mysql', type='sql')

def insert_records(text_info):
    with conn.session as s:

        s.execute(
            text('INSERT INTO users (id, name, father_name, dob, id_type, embedding) VALUES (:id, :name, :father_name, :dob, :id_type, :embedding);'),
            {
                'id': text_info['ID'],
                'name': text_info['Name'],
                'father_name': text_info["Father's Name"],
                'dob': text_info['DOB'],  # Make sure this is formatted as a string 'YYYY-MM-DD'
                'id_type': text_info['ID Type'],
                'embedding': str(text_info['Embedding'])
            }
            )
        s.commit()


def fetch_record(text_info):

    df = pd.DataFrame(conn.query('SELECT * from users;', ttl=600))
    return df


def check_duplicacy(text_info):

    is_duplicate = False
    df = fetch_record(text_info)
    df = df[df['id'] == text_info['ID']] 
    if df.shape[0] > 0:
        is_duplicate = True
    return is_duplicate

