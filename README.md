# Dopamine Detox RAG App

This repository contains a **Retrieval-Augmented Generation (RAG)** application that uses the **Mistral 7B model** (sourced from [Ollama](https://ollama.com)) to answer questions based on content from a PDF book on **Dopamine Detox**. The app performs document embeddings, saves them locally using **Chroma DB**, and retrieves relevant information for querying.

---

## Features
- **Large Language Model**:
  - Powered by **Mistral 7B**, a compact yet powerful model with 7 billion parameters.
  - Locally hosted; the model size is approximately 4.2 GB.
- **Document Embedding and Retrieval**:
  - Extracts text from the provided PDF.
  - Splits and embeds the content for efficient retrieval.
  - Embeddings are persisted using **Chroma DB** for fast queries.
- **Efficient Querying**:
  - Uses the RAG paradigm to combine retrieval with generative AI for highly contextual answers.
- **Local Hosting**:
  - Fully self-contained, running locally on your system.

---

## Installation

### Prerequisites
1. **Python 3.8 or higher**.
2. **Pip** (Python package installer).
3. **Ollama CLI**:
   - Install from [Ollama](https://ollama.com) to manage the Mistral model locally.

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the **Mistral 7B model** via the Ollama CLI:
   ```bash
   ollama pull mistral:instruct
   ```

4. Place the **Dopamine Detox PDF** in the designated `Data/` folder.

5. Create a `.env` file and set the required environment variables:
   ```plaintext
   MISTRAL_API_KEY=<your_api_key>
   ```

---

## Usage

### Initial Embedding
Run the app to process the PDF and store embeddings locally:
```bash
python main.py
```
- This step reads the PDF, splits the text, embeds it, and saves the embeddings to the local Chroma DB.

### Querying
After embedding, the app enters a loop where you can query the model based on the document content:
```plaintext
PLEASE TYPE IN YOUR QUESTION BASED ON THE DOCUMENT TOPIC:
> What is dopamine detox?
```

The app retrieves relevant information from the embeddings and uses the Mistral model to generate a contextual answer.

---

## File Structure
```
.
├── main.py            # Main script for embedding and querying.
├── load_data.py       # Extracts and preprocesses text from PDFs.
├── embed_text.py      # Embeds and persists data to Chroma DB.
├── requirements.txt   # Required Python packages.
├── .env               # Environment variables.
├── Data/              # Folder for the Dopamine Detox PDF.
├── Chroma_DB/         # Local storage for embeddings.
```

---

## Technical Details

### Text Processing
- **PDF Parsing**: The `load_data.py` script extracts text from the PDF.
- **Text Splitting**: Long texts are split into smaller chunks for efficient embedding.

### Embeddings
- **Chroma DB**: Stores embeddings locally for fast retrieval.

### RAG Workflow
1. Retrieve relevant text chunks based on user queries.
2. Pass the retrieved chunks and user query as input to the Mistral model.
3. Generate a context-aware response.

---

## Example Queries
```plaintext
PLEASE TYPE IN YOUR QUESTION BASED ON THE DOCUMENT TOPIC:
> What is dopamine detox?

PLEASE TYPE IN YOUR QUESTION BASED ON THE DOCUMENT TOPIC:
> How does dopamine affect productivity?
```

---

## Requirements
### Python Libraries
- `langchain-core`
- `langchain-ollama`
- `python-dotenv`
- `chromadb`
- `PyPDF2`

### Tools
- **Ollama CLI** (for Mistral model management)

---

## Future Enhancements
- Add support for multiple document uploads.
- Optimize text chunking for more granular embeddings.
- Add a web interface for better accessibility.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- **Mistral Model**: Powered by [Ollama](https://ollama.com).
- **Chroma DB**: For embedding and retrieval storage.

---

Let me know if you need modifications or additional sections!
