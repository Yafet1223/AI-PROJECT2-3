# How to Run the Alternate Universe Project

## Step 1: Install Dependencies

Open PowerShell or Command Prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

If you prefer using a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Or (Windows Command Prompt)
venv\Scripts\activate

# Then install dependencies
pip install -r requirements.txt
```

## Step 2: Set Up API Key

1. Create a `.env` file in the project root directory (same level as `manage.py`)
2. Add your Google Gemini API key:
   ```
   GENAI_API_KEY=your_actual_api_key_here
   ```
3. Get your API key from: https://aistudio.google.com/apikey

## Step 3: Set Up Database

Run migrations to create the database:

```bash
python manage.py migrate
```

## Step 4: Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
```

## Step 5: Access the Application

1. Open your web browser
2. Go to: http://127.0.0.1:8000/
3. You'll see the login page
4. Click "Sign up here" to create a new account
5. After signing up/logging in, you'll see the AI chat interface

## Troubleshooting

- **Import errors**: Make sure all dependencies are installed (`pip install -r requirements.txt`)
- **API key errors**: Check that your `.env` file exists and has the correct `GENAI_API_KEY`
- **Database errors**: Run `python manage.py migrate` again
- **Port already in use**: Use `python manage.py runserver 8001` to use a different port

