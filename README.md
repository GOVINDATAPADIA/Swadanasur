# The AI Culinary Journal 📖

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-ff69b4.svg)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An elegant, privacy-focused application that leverages local, open-source AI to generate personalized nutrition cookbooks based on your unique dietary needs, health goals, and taste preferences.

 
*(This is an example screenshot. You should replace the link with a screenshot of your own running application.)*

---

## ✨ About The Project

Tired of endlessly searching for recipes that fit your specific diet and goals? The AI Culinary Journal is your personal AI chef. It transforms your nutritional profile—including dietary style, allergies, health objectives, and favorite cuisines—into a beautifully formatted, ready-to-use digital cookbook.

Built with Python and Streamlit, this application runs entirely on your local machine, ensuring your health data remains 100% private. By using **Ollama** to serve a powerful open-source model like **Mistral**, we get all the benefits of generative AI with zero API costs and no rate limits.

### ✅ Key Features

-   **Truly Personalized:** Generates unique cookbooks based on your diet (Vegan, Keto, etc.), allergies, health goals (Weight Loss, Muscle Gain), and food preferences.
-   **100% Private:** Runs completely locally using Ollama. Your personal data never leaves your computer.
-   **Zero Cost:** No need for expensive API keys. The entire stack is built on free, open-source technology.
-   **Elegant UI:** A beautiful, responsive interface inspired by a rustic culinary journal, making meal planning a delightful experience.
-   **Instant & Downloadable:** Get a complete cookbook in seconds and download it as a `.txt` file for offline use.

---

## 🛠️ Technology Stack

-   **Frontend & Backend:** [Streamlit](https://streamlit.io/)
-   **AI Engine:** [Ollama](https://ollama.com/)
-   **AI Model:** [Mistral 7B](https://mistral.ai/) (or any other compatible model)
-   **HTTP Communication:** [Requests](https://requests.readthedocs.io/)
-   **Core Language:** [Python](https://www.python.org/)

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python** (version 3.8 or higher)
2.  **Git**
3.  **Ollama**: This is the most important part. Download and install it from the official website:
    -   [https://ollama.com/](https://ollama.com/)

### Installation & Setup

1.  **Clone the Repository**
    Open your terminal and clone this GitHub repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/ai-cookbook-app.git
    cd ai-cookbook-app
    ```

2.  **Create and Activate a Virtual Environment**
    It's best practice to keep project dependencies isolated.
    -   **On macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install Python Dependencies**
    Install all the required libraries from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download and Run the AI Model with Ollama**
    Open a **new, separate terminal window** and run the following command. This will download the Mistral model (a few GBs) and start the local AI server.
    ```bash
    ollama run mistral
    ```
    **Leave this terminal window open!** It is now your AI server.

---

## 🏃‍♀️ How to Use

With the setup complete, you can now run the application.

1.  Make sure your Ollama terminal from the previous step is still running.
2.  In your first terminal (with the virtual environment activated), run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
3.  Your web browser will automatically open a new tab with the application.
4.  Fill in your preferences in the form.
5.  Click the "Compose My Cookbook" button and watch the magic happen!

## 📂 Project Structure

```
ai_cookbook/
├── app.py             # The main Streamlit application script
├── background.jpeg    # The background image for the UI
├── requirements.txt   # List of Python dependencies for pip
└── README.md          # This file
```

## 📈 Future Improvements

-   [ ] **Meal Planning & Shopping Lists:** Generate a full week's meal plan and a corresponding shopping list.
-   [ ] **AI Image Generation:** Integrate a local image model to create a photo for each recipe.
-   [ ] **Save & Share Cookbooks:** Allow users to save cookbooks to a personal library.
-   [ ] **Enhanced File Support:** Add an option to download the cookbook as a formatted PDF.
-   [ ] **Nutritional Analysis:** Provide a detailed macronutrient and calorie breakdown for each recipe.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is distributed under the MIT License.

## 🙏 Acknowledgments

-   The teams behind **Streamlit** and **Ollama** for creating such powerful and accessible tools.
-   The **open-source community** for making projects like this possible.
