#!/bin/bash
echo "🚀 Setting up WagonX AI Agents..."

# Copy environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file"
    echo "⚠️  Please edit .env with your API keys"
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo "🌐 Run: python -m uvicorn backend.main:app --reload"
