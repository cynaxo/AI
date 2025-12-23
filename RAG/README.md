# BINV3220 – Mini projet RAG (Retrieval Augmented Generation)

Ce dépôt contient une implémentation complète et fonctionnelle d’un pipeline **RAG** en Python,


L’objectif est de montrer toutes les étapes nécessaires pour enrichir un modèle de langage
à l’aide d’une base de connaissances externe.

---

## 🔍 Fonctionnalités

- Chargement de documents **PDF ou TXT**
- Découpage du texte en *chunks* avec chevauchement
- Calcul d’**embeddings sémantiques**
- Stockage et recherche vectorielle avec **FAISS**
- Construction d’un **prompt enrichi** prêt à être injecté dans un LLM

---

## 🧠 Pipeline RAG implémenté

1. Lecture du document
2. Chunking du texte
3. Calcul des embeddings
4. Indexation vectorielle (FAISS – similarité cosinus)
5. Recherche des passages les plus pertinents
6. Enrichissement du prompt utilisateur

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

## Environnement virtuel

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
# ou
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```


