# 🚀 Quick Deployment Guide

## ⭐ Recommended: Railway (Easiest)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/alternate-universe.git
git push -u origin main
```

### 2. Deploy on Railway
1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway auto-detects Django! ✨

### 3. Add Environment Variables
In Railway dashboard → Variables tab:
```
SECRET_KEY=your-secret-key-here
GENAI_API_KEY=your-gemini-api-key
DEBUG=False
```

### 4. Add Database (Optional)
- Click "+ New" → "Database" → "PostgreSQL"
- Railway automatically connects it

### 5. Deploy!
Railway will automatically:
- Install dependencies
- Run migrations
- Start your app

**Your app is live!** 🎉

---

## 🌐 Alternative: Render

### 1. Push to GitHub (same as above)

### 2. Deploy on Render
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your repository
5. Render uses the `render.yaml` file automatically

### 3. Set Environment Variables
In Render dashboard:
```
SECRET_KEY=your-secret-key
GENAI_API_KEY=your-api-key
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
```

### 4. Deploy!
Render will build and deploy automatically.

---

## ⚠️ Vercel (Not Recommended)

If you must use Vercel:

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Deploy
```bash
vercel
```

### 3. Set Environment Variables
In Vercel dashboard → Settings → Environment Variables

### ⚠️ Important Notes:
- **SQLite won't work** - Need external database (PostgreSQL)
- **Cold starts** can be slow
- **File system is ephemeral**
- Consider Railway or Render instead!

---

## 🔑 Generate Secret Key

For production, generate a secure secret key:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Use this as your `SECRET_KEY` environment variable.

---

## 📝 Checklist Before Deploying

- [ ] Push code to GitHub
- [ ] Set `DEBUG=False` in environment variables
- [ ] Generate and set `SECRET_KEY`
- [ ] Set `GENAI_API_KEY`
- [ ] Set `ALLOWED_HOSTS` to your domain
- [ ] Test locally with `DEBUG=False`
- [ ] Deploy!

---

## 🎯 Recommended: Railway

**Why Railway?**
- ✅ Free tier available
- ✅ Automatic Django detection
- ✅ Easy database setup
- ✅ Automatic deployments
- ✅ Simple configuration
- ✅ Great for Django apps

**Get started in 5 minutes!**

1. Push to GitHub
2. Go to railway.app
3. Deploy from GitHub
4. Add environment variables
5. Done! 🚀

