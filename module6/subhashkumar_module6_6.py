# subhashkumar_module6_6.py

#make UI using streamlit to interact with LLM to get user question then store the result in pydantic format ( "name", "time", "number") where these information is given by user and only one of them is mandatory then store it in SQL db.    

import streamlit as st
import sqlite3
from typing import Optional
from pydantic import BaseModel, ValidationError
from langchain_ollama import ChatOllama


# =========================================================
# 1. Pydantic model
# =========================================================

class UserInformation(BaseModel):
    name: Optional[str] = None
    time: Optional[str] = None
    number: Optional[int] = None


# =========================================================
# 2. Database setup
# =========================================================

DB_NAME = "user_information.db"


def create_database():
    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_information (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            time TEXT,
            number INTEGER
        )
    """)

    connection.commit()
    connection.close()


def save_to_database(data: UserInformation):

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO user_information
        (name, time, number)
        VALUES (?, ?, ?)
    """, (
        data.name,
        data.time,
        data.number
    ))

    connection.commit()
    connection.close()


def get_previous_records():

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, time, number
        FROM user_information
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records


# =========================================================
# 3. LLM
# =========================================================

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# =========================================================
# 4. Ask LLM to extract information
# =========================================================

def extract_information(user_question):

    prompt = f"""
You are an information extraction assistant.

Extract the following information from the user's message:

1. name
2. time
3. number

Rules:

- name should be a person's name if provided.
- time should contain a time such as 10:30 AM, 14:00, etc.
- number should be an integer if a number is provided.
- If information is not provided, use null.
- Return ONLY valid JSON.
- Do not add explanations.

JSON format:

{{
    "name": null,
    "time": null,
    "number": null
}}

User message:

{user_question}
"""

    response = llm.invoke(prompt)

    return response.content


# =========================================================
# 5. Streamlit UI
# =========================================================

st.set_page_config(
    page_title="Information Agent",
    page_icon="🤖"
)

st.title("🤖 Information Extraction Agent")

st.write(
    "Enter information in natural language. "
    "The LLM will extract name, time and number."
)


# Create database when application starts
create_database()


# =========================================================
# User input
# =========================================================

question = st.text_input(
    "Enter your information",
    placeholder="Example: My name is John and the number is 25"
)


if st.button("Process"):

    if not question.strip():

        st.warning("Please enter some information.")

    else:

        try:

            # -------------------------------------------------
            # Send question to LLM
            # -------------------------------------------------

            llm_response = extract_information(question)

            st.subheader("LLM Response")

            st.code(llm_response)


            # -------------------------------------------------
            # Convert JSON response to Python dictionary
            # -------------------------------------------------

            import json

            data = json.loads(llm_response)


            # -------------------------------------------------
            # Convert dictionary to Pydantic object
            # -------------------------------------------------

            user_data = UserInformation(**data)


            # -------------------------------------------------
            # Check that at least ONE field is provided
            # -------------------------------------------------

            if (
                user_data.name is None
                and user_data.time is None
                and user_data.number is None
            ):

                st.error(
                    "At least one of name, time or number "
                    "must be provided."
                )

            else:

                # ---------------------------------------------
                # Display validated Pydantic object
                # ---------------------------------------------

                st.subheader("Pydantic Object")

                st.json(user_data.model_dump())


                # ---------------------------------------------
                # Save to database
                # ---------------------------------------------

                save_to_database(user_data)

                st.success(
                    "Information validated and saved to database."
                )


        except json.JSONDecodeError:

            st.error(
                "The LLM did not return valid JSON."
            )

        except ValidationError as e:

            st.error(
                f"Pydantic validation failed: {e}"
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )


# =========================================================
# Display previous records
# =========================================================

st.divider()

st.subheader("Previous Records")

records = get_previous_records()

if records:

    st.dataframe(
        records,
        column_config={
            "0": "ID",
            "1": "Name",
            "2": "Time",
            "3": "Number"
        }
    )

else:

    st.info("No records found.")