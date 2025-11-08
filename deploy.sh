#!/bin/bash

echo "🚀 Deploying Payroll Data Structures Application to Docker..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Build and start the containers
echo "📦 Building and starting containers..."
docker-compose up --build -d

if [ $? -ne 0 ]; then
    echo "❌ Failed to build or start containers. Check the logs above."
    exit 1
fi

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 15

# Check if services are running
echo "🔍 Checking service status..."
docker-compose ps

# Test health endpoints
echo "🏥 Testing service health..."
curl -f http://localhost:8000/ > /dev/null 2>&1 && echo "✅ Web service is healthy" || echo "⚠️  Web service may not be ready yet"
curl -f http://localhost:5000/api/health > /dev/null 2>&1 && echo "✅ API service is healthy" || echo "⚠️  API service may not be ready yet"

# Display access information
echo ""
echo "✅ Deployment Complete!"
echo ""
echo "📊 Web Application: http://localhost:8000"
echo "🔧 Data Structures API: http://localhost:5000"
echo ""
echo "🌐 API Endpoints:"
echo "  - Stack Operations:"
echo "    • Push: http://localhost:5000/api/stack/push/item_name"
echo "    • Pop: http://localhost:5000/api/stack/pop"
echo "    • Peek: http://localhost:5000/api/stack/peek"
echo "    • Size: http://localhost:5000/api/stack/size"
echo "    • All: http://localhost:5000/api/stack/all"
echo ""
echo "  - Queue Operations:"
echo "    • Enqueue: http://localhost:5000/api/queue/enqueue/item_name"
echo "    • Dequeue: http://localhost:5000/api/queue/dequeue"
echo "    • Front: http://localhost:5000/api/queue/front"
echo "    • Size: http://localhost:5000/api/queue/size"
echo "    • All: http://localhost:5000/api/queue/all"
echo ""
echo "📋 Management Commands:"
echo "  • Stop: docker-compose down"
echo "  • Restart: docker-compose restart"
echo "  • Logs: docker-compose logs -f"
echo "  • Status: docker-compose ps"
echo ""
echo "🎯 Quick Test:"
echo "  • Stack test: curl http://localhost:5000/api/stack/push/test_item"
echo "  • Queue test: curl http://localhost:5000/api/queue/enqueue/test_item"