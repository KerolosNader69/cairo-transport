# Vercel Deployment Guide for Cairo Transport

This guide will help you deploy the Cairo Transport application to Vercel.

## Prerequisites

1. A [Vercel account](https://vercel.com/signup)
2. [Vercel CLI](https://vercel.com/docs/cli) installed (optional but recommended)
3. Git repository with your code

## Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push your code to GitHub/GitLab/Bitbucket**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Import Project to Vercel**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New" → "Project"
   - Import your Git repository
   - Vercel will auto-detect the configuration

3. **Configure Build Settings**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Output Directory**: `frontend/dist`
   - **Install Command**: `pip install -r requirements.txt`

4. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete
   - Your app will be live at `https://your-project.vercel.app`

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy from project root**
   ```bash
   vercel
   ```

4. **Follow the prompts**
   - Link to existing project or create new one
   - Confirm settings
   - Deploy

5. **Deploy to production**
   ```bash
   vercel --prod
   ```

## Important Notes

### Backend Considerations

- The FastAPI backend runs as a serverless function on Vercel
- SQLite database will be ephemeral (resets on each deployment)
- For persistent data, consider using:
  - Vercel Postgres
  - Supabase
  - PlanetScale
  - Any external database service

### Frontend Configuration

- The frontend is built as a static site
- API calls are proxied through Vercel's routing
- All `/api/*` routes are handled by the Python backend

### Environment Variables

If you need environment variables:

1. Go to your project settings in Vercel Dashboard
2. Navigate to "Environment Variables"
3. Add any required variables

### Database Persistence (Optional)

To use a persistent database instead of SQLite:

1. Set up an external database (e.g., PostgreSQL on Vercel/Supabase)
2. Update `cairo_transport/database.py` to use the external database
3. Add database connection string as environment variable
4. Update `requirements.txt` to include database driver (e.g., `psycopg2-binary`)

## Troubleshooting

### 500 Error on Network Data Load

If you see "Failed to load network data: Request failed with status code 500":
- This was caused by double `/api/` prefix in routes
- Fixed by removing `/api/` prefix from FastAPI routes in `Cairo-Transport-main/api.py`
- Vercel routing adds the `/api/` prefix automatically via `vercel.json`
- The serverless handler is now in `api/index.py` which imports the FastAPI app

### Build Fails

- Check build logs in Vercel Dashboard
- Ensure all dependencies are in `requirements.txt` and `frontend/package.json`
- Verify Python version compatibility (Vercel uses Python 3.9 by default)

### API Routes Not Working

- Verify `vercel.json` routing configuration
- Check that API endpoints start with `/api/`
- Review function logs in Vercel Dashboard

### Frontend Not Loading

- Ensure `frontend/dist` directory is being created during build
- Check that `index.html` exists in the output directory
- Verify Vite build configuration in `frontend/vite.config.ts`

## Custom Domain

To add a custom domain:

1. Go to your project in Vercel Dashboard
2. Navigate to "Settings" → "Domains"
3. Add your domain and follow DNS configuration instructions

## Monitoring

- View deployment logs in Vercel Dashboard
- Monitor function execution and errors
- Set up alerts for failed deployments

## Local Development

Continue using the existing development workflow:

```bash
# Backend
python api.py

# Frontend (in another terminal)
cd frontend
npm run dev
```

## Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Vercel CLI Reference](https://vercel.com/docs/cli)
