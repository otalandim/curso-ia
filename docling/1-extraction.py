from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("./2408.09869v5.pdf")
document = result.document

markdown_output = document.export_to_markdown()

print(markdown_output)
