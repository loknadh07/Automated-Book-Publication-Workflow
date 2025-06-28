#  Automated Book Publication Workflow

This project was developed as part of an internship assignment at Soft-Nerve. It automates the book publication workflow using scraping, AI editing, human feedback, and semantic search.

##  Features

- *Web Scraping**: Extract chapter content and screenshots from Wikisource using Playwright.
- *AI Writing & Reviewing**: Rewrite and refine chapters using LLMs (e.g., Gemini or OpenAI).
- *Human-in-the-Loop**: Supports multiple revision rounds by writers, reviewers, and editors.
- *Content Versioning**: Stores original, AI-generated, and final versions.
- *Semantic Search**: Uses ChromaDB and RL-based retrieval for intelligent paragraph-level queries.

##  Files

- `chapter1.txt` — Original scraped content  
- `chapter1_ai.txt` — AI-written version  
- `chapter1_final.txt` — Final human-reviewed version  
- `store_versions.py` — Store content in ChromaDB  
- `search_version.py` — Perform semantic search  
- `debug_check.py` — Inspect stored content chunks

##  How It Works

1. Scrape chapter from URL:  
   `https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1`
2. Rewrite using an AI model and save 3 versions.
3. Store all 3 versions in ChromaDB with sentence embeddings.
4. Ask questions using `search_version.py` to retrieve matching chunks.

##  Tech Stack

- Python
- Playwright
- ChromaDB
- LLM (e.g., Gemini/OpenAI)
- RL-based search (custom)

## Youtube Video
https://youtu.be/j_IffPw53rQ
