import requests
import io
import PyPDF2

def process_pdf_from_url(file_url):
    """
    Reads a PDF from a URL, checks if it's text-based, and passes the content to get_score for analysis.

    Args:
        file_url (str): The URL of the PDF file.

    Returns:
        dict or None: The AI-generated results (score, summary) if successful, or None if the PDF isn't text-based or an error occurs.
    """
    try:
        # 1. Fetch PDF from URL
        response = requests.get(file_url)
        response.raise_for_status()  # Raise an exception for bad responses

        # 2. Read PDF Content (Without Downloading)
        with io.BytesIO(response.content) as file:  
            reader = PyPDF2.PdfReader(file)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extract_text()
    
        # 3. Check if Text-Based
        if not pdf_text.strip():
            print("Error: The PDF does not contain extractable text.")
            return None


        return pdf_text
    except Exception as e:
        print(f"Error processing PDF from URL: {e}")
        return None
