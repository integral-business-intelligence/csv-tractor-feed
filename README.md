# CSV Tractor Feed

A tool for humans to split text for upload into a vector database 

![image of tractor feed paper](https://raw.githubusercontent.com/integral-business-intelligence/csv-tractor-feed/refs/heads/main/Altair_Basic_Sign.jpg)

[Image Source: Wikipedia](https://en.wikipedia.org/wiki/Paul_Allen#Microsoft)

# Overview

CSV Tractor Feed is a simple but powerful Langflow component that treats each non-empty row in column A of a CSV file as a separate chunk for RAG systems, stopping at the first empty cell. This component enables business users to create precise, custom chunks without writing code.

**The core pattern of using a CSV's column A for custom chunks can be implemented in a few lines of code regardless of your preferred RAG pipeline setup - you can adapt this code to tools other than Langflow**

# Why Use CSV Tractor Feed?

Traditional text splitters often struggle with complex documents where different sections need different chunking approaches. CSV Row Splitter puts chunking control directly in users' hands by leveraging familiar spreadsheet tools:

- Fine-grained control: Create chunks of any size or type (paragraphs, sentences, bullet points, etc.)
- Mixed chunking strategies: Apply different chunking approaches to different parts of the same document
- No coding required: Use Excel or Google Sheets to prepare your chunks
- Perfect for subject matter experts: SMEs can directly influence chunking quality without developer intervention
- Simple integration: Fits easily into existing Langflow pipelines

# How It Works

- Prepare your CSV: Place each desired chunk as text in cells A1, A2, A3, etc. in Excel/Google Sheets
- Export as CSV: Save your spreadsheet as a CSV file
- Upload to Langflow: Use the File component to import the CSV
- Process with CSV Row Splitter: Connect the File output to this component
- Generate embeddings: Connect the Chunks output to your embedding model
- Store in vector database: Complete your RAG pipeline as usual

The component stops processing at the first empty cell in column A, treating each row as a separate chunk.

# Installation

- In the Langflow UI, add a generic custom component
- Click to select the component, click "<> Code", and replace the generic code with this script

![image from langflow](https://raw.githubusercontent.com/integral-business-intelligence/csv-tractor-feed/refs/heads/main/csv-tractor-feed.png)

# Limitations

- Only processes text from column A (ignores other columns)
- Stops at the first empty cell (intentional design)
- No metadata is automatically attached to chunks
- CSV must be properly formatted

# Use Cases

- Legal documents: Separate clauses and provisions with precise boundaries
- Medical content: Define exact chunk boundaries for clinical information
- Technical documentation: Control where API documentation gets split
- Academic papers: Keep mathematical formulas intact within chunks
- Compliance documents: Ensure regulatory text maintains proper context

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License

## Contact

dev@integralbi.ai

## Acknowledgments

- Langflow team

# About the name

Tractor feed, also known as pin-feed or continuous-form printing, is a method of feeding paper through a printer or other computer peripheral device. It was commonly used with dot-matrix printers and line printers in the past.

In a tractor feed system, the paper is fed through the printer using a series of perforated holes along the edges of the paper. These holes are engaged by sprockets or pins on the printer, which pull the paper through the device and ensure accurate alignment and positioning of the printed text or graphics.

The key features of tractor feed printing include:

- Continuous paper: The paper is supplied in a continuous roll or fanfold form, rather than individual sheets.

- Perforated edges: The paper has perforated edges with holes that align with the tractor feed mechanism in the printer.

- Precise alignment: The tractor feed mechanism ensures the paper is pulled through the printer in a straight and consistent manner, allowing for accurate printing.

- Continuous printing: Tractor feed printers can print continuously without the need to manually insert and remove individual sheets of paper.

Tractor feed printing was particularly useful in applications that required high-volume, continuous printing, such as in accounting, inventory management, and other business operations. However, with the rise of laser and inkjet printers that use individual sheets of paper, tractor feed printing has become less common in modern office environments.

We see CSV Tractor Feed as providing a similar function: methodically feeding text chunks from familiar spreadsheets into AI workflows with precision and control. It pairs perfectly with our [Chroma Auditor](https://github.com/integral-business-intelligence/chroma-auditor) tool, which enables users to export chunks to CSV, creating a complete roundtrip workflow where chunks become portable across AI systems via CSV: a format business users already know and trust.
