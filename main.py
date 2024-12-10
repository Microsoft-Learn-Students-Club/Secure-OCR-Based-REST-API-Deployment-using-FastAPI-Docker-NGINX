import re
import fitz
from fastapi.responses import JSONResponse
import os
import requests
from dotenv import load_dotenv
from PIL import Image
import pytesseract
import requests
from fastapi import FastAPI, UploadFile, File, Request, Depends, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
from PIL import Image

app = FastAPI()
load_dotenv()

# middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setting up Tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
# pytesseract.pytesseract.tesseract_cmd = os.getenv('Tesseract')

# Define a function to extract text from a single page of the PDF
def extract_text_from_page(page):
    # Extract text from a specific page
    return page.get_text("text")

def get_api_key(request: Request):
    api_key = request.headers.get('X-API-Key') or request.query_params.get('api_key')
    # print(f"Received API key: {api_key}")
    correct_api_keys = os.getenv("API_KEY").split(',')
    # print(correct_api_keys)
    if api_key not in correct_api_keys:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")
    return api_key

def preprocess_image_for_ocr(image):
    # Step 1: Increase Image Resolution (upscale)
    image = image.resize((int(image.width * 1.5), int(image.height * 1.5)), Image.Resampling.LANCZOS)

    # Convert to a format compatible with OpenCV for further processing
    open_cv_image = np.array(image)
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)

    processed_image = Image.fromarray(open_cv_image)
    return processed_image


# Define a function to extract codes based on the fixed pattern
def extract_codes_from_text(text):
    # Regex pattern for codes like AC1-21-02-15-3, AC1-21-02-15-12, etc.
    # pattern = r'[A-Z]{2}\d-\d{2}-\d{2}-\d{1,2}-\d{1,2}'
    pattern = r'[A-Z]{2,5}\d{1,9}-\d{1,5}-\d{1,5}-\d{1,5}-\d{1,3}'
    codes = re.findall(pattern, text)
    return codes


# extracting codes using ocr
def extract_codes_from_image(page):
    pix = page.get_pixmap()  
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    preprocessed_img = preprocess_image_for_ocr(img)
    text = pytesseract.image_to_string(preprocessed_img)
    # print(text)  
    return text


# function to check if the pdf has images or text
def check_pdf (doc):
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        if page.get_text("text").strip(): 
            return False
    return True

# API route 
@app.post('/ocr')
async def extract(url: str = None, api_key: str = Depends(get_api_key)):
    temp_pdf = 'temp.pdf'
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP request errors
        with open(temp_pdf, "wb") as f:
            f.write(response.content)  # Write the downloaded content to a file
    except Exception as e:
        return JSONResponse(content={"error": f"Failed to download PDF from URL. Error: {str(e)}"})


    # Open the PDF document
    doc = fitz.open(temp_pdf)


    # Empty list to collect all the codes along with page nos
    codes_with_page_no = []

    contains_image = check_pdf(doc)

    # Loop through each page in the PDF
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)

        if contains_image:
            text = extract_codes_from_image(page)
        else:    
        # Extract text from the current page
            text = extract_text_from_page(page)
        # Extract codes from the current page's text
        codes = extract_codes_from_text(text)
        code = codes[0] if codes else None
        # Print the result for each page
        if code:
            parts = code.split('-')
            certificate_id = parts[0]  
            document_id = parts[1]        
            sequence = parts[-3] 
            page_number = parts[-1]   
            total_pages = parts[-2]       
            
            codes_with_page_no.append({
                "certificate_id": certificate_id,
                "document_id": document_id,
                "sequence": sequence,
                "total_pages": total_pages,
                "page_number": page_number
                })
        else:
            # Pages with no codes found
            codes_with_page_no.append({
                "certificate_id": None,
                "document_id": None,
                "sequence": None,
                "total_pages": None,
                "page_number": None
            })


    # closing the pdf
    doc.close()

    # Clean up the temporary file
    os.remove(temp_pdf)   

    if codes_with_page_no:
        return JSONResponse(content={"extracted_data": codes_with_page_no})
    else:
        return {'message' : 'NO CODES FOUND'}

if __name__=='__main__' :
    uvicorn.run(app, host = '127.0.0.1', port = 80)
    
