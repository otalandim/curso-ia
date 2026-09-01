from docling.chunking import HierarchicalChunker
from docling.document_converter import DocumentConverter

converter = DocumentConverter()

result = converter.convert("./2408.09869v5.pdf")
document = result.document

chunker = HierarchicalChunker()
chunks = list(chunker.chunk(document))

chunks
print(chunks[4].text)
