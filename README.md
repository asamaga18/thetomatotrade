# BitCamp 2025 Project

## Setup Instructions

### Backend Setup
1. Create a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `backend/.env` file with:
```
MONGODB_URL=your_mongodb_url
GOOGLE_CLIENT_ID=your_google_client_id
JWT_SECRET_KEY=your_jwt_secret
```

4. Start backend server:
```bash
# Windows (run commands separately)
cd backend
python -m uvicorn main:app --reload

# Mac/Linux
cd backend && python -m uvicorn main:app --reload
```

### Frontend Setup
1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start frontend server:
```bash
npm run dev
```

## Deployment
The project includes:
- `Procfile` for deployment platforms
- Production server (gunicorn)
- Environment variable handling
- CORS configuration

## Environment Variables Required
- `MONGODB_URL`: MongoDB Atlas connection string
- `GOOGLE_CLIENT_ID`: Google OAuth client ID
- `JWT_SECRET_KEY`: Secret key for JWT tokens
