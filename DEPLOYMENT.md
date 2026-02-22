# Deployment Guide for Alternate Universe

## ⚠️ Important Note About Vercel

**Vercel is NOT recommended for Django applications** because:
- Vercel is optimized for serverless functions and static sites
- Django requires persistent connections and WSGI servers
- Database (SQLite) won't persist on Vercel's serverless platform
- Complex setup with limitations

## ✅ Recommended Platforms (Better for Django)

### Option 1: Railway (Easiest & Recommended) ⭐
- Free tier available
- Automatic deployments from GitHub
- Easy Django setup
- PostgreSQL database included

### Option 2: Render
- Free tier available
- Good Django support
- Easy setup

### Option 3: PythonAnywhere
- Free tier available
- Specifically designed for Python apps
- Very easy Django deployment

---

## 🚀 Option 1: Deploy to Railway (Recommended)

### Step 1: Prepare Your Project

1. **Update settings.py for production** (already done in settings.py)
2. **Create a Procfile** (for Railway)
3. **Update requirements.txt** (already exists)

### Step 2: Create Railway Configuration

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect Django and deploy!

### Step 3: Set Environment Variables

In Railway dashboard, add these environment variables:
- `SECRET_KEY` - Generate a new secret key
- `GENAI_API_KEY` - Your Google Gemini API key
- `DEBUG=False`
- `ALLOWED_HOSTS=your-app-name.railway.app`

### Step 4: Database Setup

Railway will automatically set up a PostgreSQL database. You'll need to:
1. Add PostgreSQL service in Railway
2. Update DATABASES in settings.py to use PostgreSQL

---

## 🌐 Option 2: Deploy to Render

### Step 1: Create render.yaml

Already created in the project root.

### Step 2: Deploy

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Render will use the render.yaml configuration

---

## 📦 Option 3: Deploy to Vercel (Not Recommended)

If you still want to use Vercel, follow these steps:

### Step 1: Install Vercel CLI
```bash
npm i -g vercel
```

### Step 2: Create vercel.json
Already created in project root.

### Step 3: Deploy
```bash
vercel
```

**Limitations:**
- SQLite database won't work (need external database)
- Cold starts can be slow
- Some Django features may not work
- Need to use serverless-friendly database

---

## 🔧 Required Setup for Production

### 1. Update settings.py for Production

Key changes needed:
- Set DEBUG = False
- Add ALLOWED_HOSTS
- Use environment variables for secrets
- Configure static files
- Use PostgreSQL instead of SQLite

### 2. Environment Variables

Create a `.env` file (or set in hosting platform):
```
SECRET_KEY=your-secret-key-here
GENAI_API_KEY=your-gemini-api-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

### 3. Static Files

For production, you'll need to:
- Run `python manage.py collectstatic`
- Configure static file serving

---

## 🎯 Quick Start: Railway Deployment

1. **Push your code to GitHub**
2. **Go to railway.app and sign up**
3. **Click "New Project" → "Deploy from GitHub"**
4. **Select your repository**
5. **Add environment variables**
6. **Deploy!**

Railway will automatically:
- Detect Django
- Install dependencies
- Run migrations
- Deploy your app

Your app will be live at: `https://your-app-name.railway.app`

---

## 📝 Next Steps

1. Choose a platform (Railway recommended)
2. Push code to GitHub
3. Follow platform-specific deployment steps
4. Set environment variables
5. Configure database (if needed)
6. Deploy!

