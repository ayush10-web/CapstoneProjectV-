
## How to Run

### Backend (Flask)

1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

### Frontend (Streamlit)

1. Open a new terminal and navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

5. Open your browser and go to `http://localhost:8501` to see the chat interface.
