# =============================================================================
# BINV3220 – Retrieval Augmented Generation (RAG)
# -----------------------------------------------------------------------------
# Description:
#   Implémentation complète d’un pipeline RAG (Retrieval Augmented Generation)
#   permettant d’enrichir une question utilisateur à l’aide d’un contexte
#   extrait dynamiquement depuis un document externe (PDF ou TXT).
#
#   Le pipeline inclut :
#     - le chargement et le prétraitement de documents,
#     - le découpage en chunks avec chevauchement,
#     - le calcul d’embeddings sémantiques,
#     - l’indexation et la recherche vectorielle avec FAISS,
#     - la construction d’un prompt enrichi prêt à être injecté dans un LLM.
#
# Contexte académique:
#   Projet réalisé dans le cadre du cours BINV3220 – Retrieval Augmented Generation.
#
# Author:
#   cynaxo 
#
# =============================================================================


from typing import List, Tuple
import pathlib

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader


# ======================================================
# Lecture de documents
# ======================================================

def read_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def read_pdf(path: str) -> str:
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)


def load_document(path: str) -> str:
    ext = pathlib.Path(path).suffix.lower()
    if ext == ".txt":
        return read_txt(path)
    elif ext == ".pdf":
        return read_pdf(path)
    else:
        raise ValueError("Format non supporté (.txt ou .pdf)")


# ======================================================
# Chunking
# ======================================================

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    assert chunk_size > 0 and 0 <= overlap < chunk_size
    chunks = []
    start = 0
    step = chunk_size - overlap

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += step

    return chunks


# ======================================================
# Index RAG (FAISS + embeddings)
# ======================================================

class RAGIndex:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks: List[str] = []

    def build(self, chunks: List[str]):
        embeddings = self.model.encode(chunks).astype("float32")
        faiss.normalize_L2(embeddings)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(embeddings)

        self.chunks = chunks

    def search(self, query: str, k: int = 3) -> List[Tuple[str, float, int]]:
        query_embedding = self.model.encode([query]).astype("float32")
        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(query_embedding, k)

        results = []
        for idx, score in zip(indices[0], scores[0]):
            results.append((self.chunks[idx], float(score), idx))

        return results


# ======================================================
# Construction du prompt enrichi
# ======================================================

def build_rag_prompt(
    query: str,
    hits: List[Tuple[str, float, int]],
    min_score: float = 0.0
) -> str:
    selected_chunks = [
        text for text, score, _ in hits if score >= min_score
    ]

    context = "\n\n".join(selected_chunks)

    prompt = (
        "Contexte (extraits pertinents) :\n"
        f"{context}\n\n"
        "Question :\n"
        f"{query}\n\n"
        "Instruction : Réponds de manière factuelle et concise, "
        "en t'appuyant uniquement sur le contexte."
    )

    return prompt


# ======================================================
# Exécution complète
# ======================================================

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage : python rag_pipeline.py <document.pdf|document.txt>")
        sys.exit(1)

    document_path = sys.argv[1]

    print("▶ Chargement du document...")
    text = load_document(document_path)

    print("▶ Découpage en chunks...")
    chunks = chunk_text(text)

    print("▶ Création de l’index vectoriel...")
    rag = RAGIndex()
    rag.build(chunks)

    question = "What is the date of birth of Adrien Foucart?"

    print("▶ Recherche des passages pertinents...")
    hits = rag.search(question, k=3)

    enriched_prompt = build_rag_prompt(question, hits)

    print("\n" + "=" * 80)
    print("PROMPT ENRICHI")
    print("=" * 80)
    print(enriched_prompt)
