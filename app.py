import streamlit as st

def main():
    st.title("Hammad Ahmad Zafar")

    # Add a link to download the resume in PDF format
    st.subheader("Medical Scribe")
    st.markdown("[Click to Download Resume](resume.pdf)")
    
    # Display the PNG version of the resume for preview
    st.image("resume2.jpg", caption="Hammadahmadzafar471@gmail.com | +92-334-4555179", use_column_width=True)

if __name__ == "__main__":
    main()

