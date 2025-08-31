import streamlit as st
import requests
import json
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Swadanusar",
    page_icon="🌿",
    layout="wide",
)

# --- CUSTOM CSS FOR THE RUSTIC THEME ---

def add_bg_from_local(image_file):
    """
    Sets a local background image.
    """
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&display=swap');
        .stApp {{
            background-image: url(data:image/{"jpeg"};base64,{encoded_string}); /* <<< CHANGE #1: jpg -> jpeg */
            background-size: cover;
            background-attachment: fixed;
        }}
        [data-testid="stHeader"], [data-testid="stToolbar"] {{
            background: rgba(0,0,0,0);
        }}
        .block-container {{
            padding-top: 3rem;
            padding-bottom: 3rem;
        }}
        [data-testid="stVerticalBlock"] {{
            background-color: rgba(245, 245, 220, 0.85);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            border-radius: 20px;
            padding: 2rem;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        }}
        [data-testid="stSidebar"] > div:first-child {{
            background-color: #D2B48C;
            padding: 2rem;
            border-radius: 10px;
        }}
        h1, h2, h3, .stMarkdown, .stSelectbox, .stTextInput {{
            font-family: 'Merriweather', serif;
            color: #36454F;
        }}
        .stButton>button {{
            background-color: #228B22;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            border: 2px solid rgba(255, 255, 255, 0.5);
            font-weight: bold;
            font-family: 'Merriweather', serif;
            transition: all 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #3CB371;
            border-color: white;
        }}
        .stTextInput>div>div>input, .stSelectbox>div>div {{
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 5px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

try:
    add_bg_from_local('background.jpeg') # <<< CHANGE #2: jpg -> jpeg
except FileNotFoundError:
    st.warning("`background.jpeg` not found. Please add the background image to your project folder for the intended design.")


# --- OLLAMA API LOGIC (No changes here) ---
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def generate_cookbook_local(diet, allergies, goals, disliked_foods, cuisine_style):
    prompt = f"""
    You are a seasoned chef and nutritionist with a calm, reassuring tone. Create a personalized mini-cookbook based on the user's details.

    The cookbook should include:
    - An elegant title.
    - A brief, welcoming introduction.
    - 3 wholesome recipes: Breakfast, Lunch, and Dinner.

    User's Details:
    - Diet: {diet}
    - Allergies: {'None' if not allergies else ', '.join(allergies)}
    - Goal: {goals}
    - Dislikes: {'None' if not disliked_foods else disliked_foods}
    - Cuisine Style: {cuisine_style}

    For each recipe, provide: Recipe Title, a short Description, Ingredients (bulleted), Instructions (numbered), and a "Chef's Note" related to their health goal.

    Format the entire output in clean Markdown. Begin the response directly with the cookbook title.
    """
    payload = {"model": "mistral", "prompt": prompt, "stream": False}
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        return json.loads(response.text)['response']
    except requests.exceptions.ConnectionError:
        st.error("Connection Error: Could not connect to the Ollama server. Please ensure it is running.", icon="🚨")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}", icon="🚨")
        return None

# --- UI (No changes here) ---

with st.sidebar:
    st.header("🌿 About")
    st.markdown("This Culinary Journal uses a locally-run AI to craft recipes tailored to your unique tastes and nutritional goals. Every creation is private, personal, and designed just for you.")
    st.markdown("---")

st.title("Swadanusar 📖")
st.markdown("#### *Wholesome, personalized recipes, crafted by AI.*")
st.markdown("---")

with st.form("cookbook_generator_form"):
    st.header("Describe Your Culinary Preferences")

    col1, col2 = st.columns(2)
    with col1:
        diet = st.selectbox("Dietary Style:", ("None", "Vegetarian", "Vegan", "Keto", "Paleo", "Pescatarian"))
        allergies = st.multiselect("Allergies or Intolerances:", ["Gluten", "Dairy", "Nuts", "Soy", "Shellfish", "Eggs"])

    with col2:
        goals = st.selectbox("Primary Health Goal:", ("Weight Loss", "Muscle Gain", "Maintain Health", "Improve Energy"))
        cuisine_style = st.text_input("Preferred Cuisine (e.g., Mediterranean)")

    disliked_foods = st.text_input("Foods to Avoid:")
    
    st.markdown("")
    submitted = st.form_submit_button("🧑‍🍳 Compose My Cookbook")

if submitted:
    with st.spinner("Composing your recipes..."):
        cookbook_content = generate_cookbook_local(diet, allergies, goals, disliked_foods, cuisine_style)
        if cookbook_content:
            st.session_state['cookbook'] = cookbook_content
        else:
            if 'cookbook' in st.session_state:
                del st.session_state['cookbook']

if 'cookbook' in st.session_state:
    st.markdown("---")
    st.header("Your Personal Cookbook")
    st.markdown(st.session_state['cookbook'])
    
    st.download_button(
        label="Download Cookbook",
        data=st.session_state['cookbook'],
        file_name='my_culinary_journal.txt',
        mime='text/plain'
    )