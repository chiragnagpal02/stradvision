import os
import streamlit as st

# Define the count_boxes function
def count_boxes(file_path):
    modified_content = []
    with open(file_path) as file:
        content = file.readlines()
    for i in content:
        modified_content.append(i.strip("\n"))
    total_count = 0
    for j in modified_content:
        if j.isdigit():
            total_count += int(j)

    return total_count

# Define the Streamlit app
def app():
    st.title("Stradvision Bounding Box Counting Tool")

    # Create a file uploader
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with open(os.path.join("temp", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Get the full file path
        file_path = os.path.abspath(os.path.join("temp", uploaded_file.name))

        # Display the file contents
        st.text("File contents:")
        file_contents = uploaded_file.read()
        st.code(file_contents)

        # Calculate the total count
        total_count = count_boxes(file_path)

        # Display the total count
        st.success(f"Total count: {total_count}")

        # Remove the temporary file
        os.remove(file_path)

# Run the app
if __name__ == "__main__":
    if not os.path.exists("temp"):
        os.makedirs("temp")
    app()