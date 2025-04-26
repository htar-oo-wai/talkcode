# TalkCode

**TalkCode** is an interactive intelligent knowledge base that helps you understand and improve complex codebases. It uses `tree-sitter` to parse code into structured syntax trees, generates embeddings using LLMs, stores them in FAISS, and allows intelligent querying using graph and semantic search.

https://tree-sitter.github.io/tree-sitter/ for parsing codebase

## Features

- Parses codebase into an AST using **Tree-sitter**
- Builds code graphs (functions, classes, calls, inheritance, etc.)
- Generates semantic embeddings for code segments
- Stores embeddings in **FAISS** for efficient vector search
- Enables both structural and semantic search over your code
- Supports Retrieval-Augmented Generation (RAG) for high-quality query responses

## How it Works

### 1. Parse the Codebase
- Use Tree-sitter to generate an AST
- Extract entities: classes, methods, functions, variables
- Construct a code graph: nodes (entities), edges (relations)

### 2. Generate Code Embeddings
- Use models like OpenAI or CodeBERT for embedding generation
- Each embedding captures the semantic meaning of code sections
- Metadata includes function/class names and relationships

### 3. Store in FAISS
- Vector storage of embeddings
- Metadata links embeddings to code entities and graph data

### 4. Query the Codebase
- **Graph Traversal**: e.g., “Find all functions calling `authService`”
- **Semantic Search**: e.g., “Find code related to user authentication”
- **Combined**: Narrow down with graph → refine with FAISS

### 5. Use RAG for Better Responses
- Retrieval-Augmented Generation merges graph + embedding context
- Generates answers with reasoning and code references

## Installation

```bash
git clone https://github.com/swaroop325/talkcode.git
cd talkcode
chmod +x setup.sh
bash setup.sh
