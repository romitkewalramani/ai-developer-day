#!/bin/bash
# Quick start script for workshop participants (optional - VS Code handles this automatically)

set -e

echo "🚀 Starting Workshop Dev Container..."

# Start containers
docker compose up -d

echo ""
echo "✅ Container is running!"
echo ""
echo "📝 Next steps:"
echo "   1. Open this project in Cursor"
echo "   2. Press F1 and select 'Dev Containers: Reopen in Container'"
echo "   3. Clone your repos into /workspace or subdirectories"
echo ""
echo "🔍 Container status:"
docker compose ps