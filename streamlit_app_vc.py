import streamlit as st
import openai

# Initialize the OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Define a function to handle the chatbot response
def chatbot_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Define the Streamlit app
def main():
    st.title("Hinglish Chatbot")
        
    # Prompt the user to select their business type
    st.write("Please select your business type:")
    business_type_options = ("Kirana shop", "Mobile repair shop", "Beauty salon", "Food truck", "Others")
    business_type = st.selectbox("", business_type_options)

    if business_type == "Others":
        # Prompt the user to input their business type
        business_type = st.text_input("Please enter your business type:")

    # Prompt the user to input their business details in Hinglish
    st.write("Please provide some details about your business in Hinglish:")
    business_name = st.text_input("Business name")
    business_description = st.text_area("Business description")
    target_customers = st.text_area("Target customers")

    # Initialize the chat history
    chat_history = []
    counter = 1
    
    while True:
        # Ask the user a question in Hinglish and get the mentor's response in Hinglish
        question = st.text_input("Aap kya puchna chahte hain?")
        if question:
            prompt = "Hinglish mein jawaab dein: " + business_description + " " + target_customers + " " + question
            response = chatbot_response(prompt)

            # Display the mentor's response in Hinglish
            st.success("Mentor: " + response)

            # Store the conversation in the chat history
            chat_history.append((counter, "Microentrepreneur: " + question, "Mentor: " + response))
            counter += 1

        # Display chat history only if the conversation has started
        if chat_history:
            st.write("Chat History:")
            for chat in chat_history:
                st.write(chat[0])
                st.write(chat[1])
            
if __name__ == "__main__":
    main()
