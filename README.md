# Codedex's Python Final Project

## Generate a Blog with OpenAI

This project is part of Codedex's final assignment to obtain certification.

### Track
- **Generate a Blog with OpenAI**

### Prerequisites
- **Python Fundamentals**

### Versions
- Python 3.10+
- `python-dotenv` 0.21.0+
- `openai` 1.0.0+

### Important Note
Make sure to add your own API key into a `.env` file.

### Description
Using OpenAI's API (Application Programming Interface), we will create a blog generator. This project reads the user's prompt and uses OpenAI's ChatGPT-3 to generate a paragraph about the given topic.

---

## Setup Instructions
1. **Clone the Repository**
    
    inside your terminal, cd into the desired working space:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. **Create a Virtual Enviorement**
    
    Type this into your console (make sure you're in the root of your working directory).
    ```sh
    python (or python3) -m venv venv

3. **Activate VENV**
    
    windows: 
    ```bash
    .\venv\Scripts\activate
    ```
    
    MacOS/Linux:
    ```sh
    source venv/bin/activate
    ```

4. **Install Dependencies**
    
    Type this into console:
    ```sh
    pip install -r requirements.txt
    ```

5. **Create .env File**

    At the root of your working project. Create a '.env' file and add your API key in a envioremental variable named 'API_KEY'.

    The project is working with that specific variable name and if a different name is used make sure to change the other variables to your new enviorement variable name.

**The installation of a venv is not necessary. However, it will make working with everything easier. Alternatively, you can just do *step 4* and *step 5*.**

