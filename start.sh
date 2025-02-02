#!/bin/bash

if [ -z "$OPENAI_API_KEY" ]; then
  echo "ERROR: OPENAI_API_KEY is not set in the environment!"
  echo "Please run: export OPENAI_API_KEY='your-api-key-here' and try again."
  exit 1
fi

echo "Building the Docker image..."
docker build -t ai-test .

echo "Running the Docker container..."
docker run -d -p 8000:8000 --name ai-test-container -e OPENAI_API_KEY="$OPENAI_API_KEY" ai-test

echo "Container is running on http://localhost:8000"