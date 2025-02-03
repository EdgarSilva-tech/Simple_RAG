This project is a minimal Retrieval-Augmented Generation (RAG) system that allows users to ask a question about the Attention is All you need paper, retrieve relevant text snippets(paragraphs), and generate an answer using a language model.

The system is built using FastAPI, Chroma (for embeddings & retrieval), and a generative AI model, GPT 4o-mini. The entire service is containerized with Docker and can be launched with a single script - start.sh. Before running this script, it's necessary to have an OpenAI API key defined in the environment as such: export OPENAI_API_KEY='API_KEY', this API key for safety reasons will only be injected at runtime.

How to use the API:
We can make a JSON request to ask a question using curl like the following example:
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"question": "How does the Attention mecanism work?"}' \
     http://localhost:8000/ask

Or use the using the Swagger UI by going to localhost:8000/docs and clicking on the try it out button after expanding the POST section and making a question on the request body's designated field.

Brief code explanation:
The embeddings.py reads the Attention is All you need paper pdf file, splits the document into paragraphs and then embeds them using OpenAI embeddings, these embeddings are then stored into Chroma in order to be able to do a similarity search that will return the 3 most relevant paragraphs to answer the question.
The model_integration.py file implements a chat model from OpenAI that will answer the question based on the question itself and the most relevant snippets return by the embeddings.py file. The main.py file will expose an endpoint (ask) that will use the logic of the previously mentioned files to answer a question.

Future improvements:
In the future, obvious improvements that could be made are: create a proper frontend for FastAPI using a HTML file and Jinja templates for integration, for the Langchain portion of the project next steps could include the integration of the LangSmith for monitoring and evaluation and the integration of LangGraph for orchestration.

Deployment strategy:
To deploy the container on Azure, it's necessary to create a Azure Container Registery for the safe storage of our image, after connecting to the Azure Container Registery, we can tag and push the image to the registry. Then, the image can be deployed using Azure Container Instances, now we can retrieve a public IP address that can be used to make API calls similarly to the example above using curl by substituting the localhost address by this public IP address. Using the Azure Container Registery we can also use a more scalable solution in Azure Kubernetes Service, in this solutions we will need to create a Kubernetes cluster, connect to it and then follow the above steps to create a Container Registry and push the image to the registry. The final steps are creating the required YAML files (deployment and service) and applying them, after this we get an external IP address that can be used to make API calls by replacing the localhost address as the previous solutions does similarly with the Container Instances public IP address.