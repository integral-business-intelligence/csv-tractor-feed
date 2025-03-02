from langflow.custom import Component
from langflow.io import HandleInput, Output
from langflow.schema import Data, DataFrame
import csv
import io
import logging

class CSVRowSplitterComponent(Component):
    display_name: str = "CSV Tractor Feed"
    description: str = "Treat each non-empty CSV row in column A as a chunk, stopping at first empty cell."
    icon = "scissors-line-dashed"
    name = "CSVRowSplitter"
    inputs = [
        HandleInput(
            name="data_input",
            display_name="CSV Data Input",
            info="CSV file to split by rows in column A",
            input_types=["Data"],
            required=True,
        )
    ]
    outputs = [
        Output(display_name="Chunks", name="chunks", method="split_rows"),
        Output(display_name="DataFrame", name="dataframe", method="as_dataframe"),
    ]

    def split_rows(self) -> list[Data]:
        chunks = []
        
        # Check if we have input data
        if not hasattr(self, 'data_input') or self.data_input is None:
            logging.warning("CSVRowSplitter: No data_input available")
            return chunks
        
        # Handle both single Data object and list of Data objects
        input_data = self.data_input
        if isinstance(input_data, list):
            if not input_data:
                return chunks
            input_data = input_data[0]
        
        if not isinstance(input_data, Data):
            logging.warning(f"CSVRowSplitter: Expected Data object, got {type(input_data)}")
            return chunks
            
        # Get the CSV content
        csv_text = input_data.text
        
        try:
            # Parse the CSV using csv module
            reader = csv.reader(io.StringIO(csv_text))
            
            for row_idx, row in enumerate(reader):
                # Check if row has data and first cell is not empty
                if not row or not row[0].strip():
                    logging.info(f"CSVRowSplitter: Empty cell at row {row_idx}, stopping")
                    break
                
                # Create a chunk with ONLY the text content from column A
                # No metadata at all
                chunk_text = row[0].strip()
                
                # Create a Data object with text only, no metadata
                chunks.append(Data(text=chunk_text))
                logging.info(f"CSVRowSplitter: Added chunk {len(chunks)}: '{chunk_text[:50]}...'")
                
            logging.info(f"CSVRowSplitter: Total chunks created: {len(chunks)}")
            
        except Exception as e:
            logging.error(f"CSVRowSplitter: Error parsing CSV: {str(e)}")
            import traceback
            logging.error(traceback.format_exc())
        
        return chunks

    def as_dataframe(self) -> DataFrame:
        return DataFrame(self.split_rows())
