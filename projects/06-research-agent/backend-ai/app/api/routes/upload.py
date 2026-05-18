import os

from fastapi import (
    APIRouter,
    UploadFile,
    File,
)

from app.rag.pdf_loader import (
    load_pdf,
)

from app.rag.chunker import (
    chunk_documents,
)

from app.rag.vector_store import (
    create_vector_store,
)

router = APIRouter()

UPLOAD_DIR = "uploaded_files"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True,
)

# -----------------------------------
# Upload PDF
# -----------------------------------


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename,
    )

    with open(
        file_path,
        "wb",
    ) as f:

        content = await file.read()

        f.write(content)

    # -----------------------------------
    # Load PDF
    # -----------------------------------

    documents = load_pdf(file_path)

    # -----------------------------------
    # Chunk
    # -----------------------------------

    chunks = chunk_documents(documents)

    # -----------------------------------
    # Store Embeddings
    # -----------------------------------

    # -----------------------------------
    # Validate Chunks
    # -----------------------------------

    if not chunks:

        return {
            "success": False,

            "message": "No text could be extracted from PDF.",
        }

    # -----------------------------------
    # Create Vector Store
    # -----------------------------------

    create_vector_store(chunks)

    return {
        "success": True,
        "message": "PDF uploaded successfully",
        "chunks": len(chunks),
    }
