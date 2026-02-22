# Deploying to Vercel (Not Recommended)

⚠️ **Warning**: Vercel is not ideal for Django applications. Consider using Railway or Render instead.

## If you still want to use Vercel:

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy
```bash
vercel
```

### Step 4: Set Environment Variables
In Vercel dashboard, go to your project → Settings → Environment Variables:
- `SECRET_KEY` - Generate a new secret key
- `GENAI_API_KEY` - Your Google Gemini API key
- `DEBUG=False`
- `ALLOWED_HOSTS=your-app.vercel.app`

### Step 5: Important Limitations

1. **Database**: SQLite won't work on Vercel. You need to use an external database:
   - Use PostgreSQL (Railway, Supabase, or Neon)
   - Update DATABASES in settings.py

2. **Cold Starts**: Serverless functions have cold starts which can be slow

3. **File System**: Ephemeral file system - files won't persist

4. **Static Files**: May need special configuration

### Better Alternative: Railway

Railway is much better for Django:
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub"
4. Select your repository
5. Add environment variables
6. Deploy!

Railway automatically:
- Detects Django
- Sets up database
- Handles static files
- Provides persistent storage

Your app will be live in minutes!

