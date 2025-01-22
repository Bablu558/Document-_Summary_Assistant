
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from PyPDF2 import PdfReader
# from pdf2image import convert_from_path
# from PIL import Image
# import pytesseract

# # Set Tesseract path (Windows के लिए)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Set Poppler path (Windows के लिए)
# POPPLER_PATH = r'C:\Users\kushw\Release-24.08.0-0\poppler-24.08.0\Library\bin'

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']

#         # Save the uploaded file
#         fs = FileSystemStorage()
#         file_name = fs.save(uploaded_file.name, uploaded_file)
#         file_path = fs.path(file_name)
#         file_url = fs.url(file_name)

#         # Text extraction logic
#         extracted_text = ""
#         if uploaded_file.name.endswith('.pdf'):
#             try:
#                 # Try extracting text using PyPDF2
#                 reader = PdfReader(file_path)
#                 for page in reader.pages:
#                     extracted_text += page.extract_text()

#                 # If PyPDF2 fails or extracted text is empty, use OCR
#                 if not extracted_text.strip():
#                     images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
#                     for image in images:
#                         extracted_text += pytesseract.image_to_string(image)

#             except Exception as e:
#                 return render(request, 'uploader/upload.html', {'error': f"PDF processing failed: {str(e)}"})

#         elif uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#             try:
#                 # Extract text from image
#                 image = Image.open(file_path)
#                 extracted_text = pytesseract.image_to_string(image)
#             except Exception as e:
#                 return render(request, 'uploader/upload.html', {'error': f"Image processing failed: {str(e)}"})

#         # Summarize text (basic example)
#         summary = extracted_text[:500] + '...' if len(extracted_text) > 500 else extracted_text

#         return render(request, 'uploader/result.html', {'summary': summary, 'file_url': file_url})

#     return render(request, 'uploader/upload.html')






# 2nd time 
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from PyPDF2 import PdfReader
# from pdf2image import convert_from_path
# from PIL import Image
# import pytesseract
# from django.contrib import messages  # Import messages framework

# # Set Tesseract path (Windows के लिए)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Set Poppler path (Windows के लिए)
# POPPLER_PATH = r'C:\Users\kushw\Release-24.08.0-0\poppler-24.08.0\Library\bin'

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']

#         # Check for valid file formats
#         valid_formats = ['.pdf', '.png', '.jpg', '.jpeg']
#         file_extension = uploaded_file.name.split('.')[-1].lower()

#         if file_extension not in [ext.lstrip('.') for ext in valid_formats]:
#             # Invalid file format error
#             messages.error(request, "Invalid file format. Please upload a PDF or an image (PNG, JPG, JPEG).")
#             return render(request, 'uploader/upload.html')

#         # Save the uploaded file
#         fs = FileSystemStorage()
#         file_name = fs.save(uploaded_file.name, uploaded_file)
#         file_path = fs.path(file_name)
#         file_url = fs.url(file_name)

#         # Text extraction logic
#         extracted_text = ""
#         try:
#             if uploaded_file.name.endswith('.pdf'):
#                 # Try extracting text using PyPDF2
#                 reader = PdfReader(file_path)
#                 for page in reader.pages:
#                     extracted_text += page.extract_text()

#                 # If PyPDF2 fails or extracted text is empty, use OCR
#                 if not extracted_text.strip():
#                     images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
#                     for image in images:
#                         extracted_text += pytesseract.image_to_string(image)

#             elif uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')): 
#                 # Extract text from image
#                 image = Image.open(file_path)
#                 extracted_text = pytesseract.image_to_string(image)

#         except Exception as e:
#             # Catch any errors during file processing
#             messages.error(request, f"An error occurred while processing the file: {str(e)}")
#             return render(request, 'uploader/upload.html')

#         # Handle case if no text was extracted
#         if not extracted_text.strip():
#             messages.warning(request, "No text could be extracted from the file. Please ensure the file contains readable text.")
#             return render(request, 'uploader/upload.html')

#         # Summarize text (basic example)
#         summary = extracted_text[:500] + '...' if len(extracted_text) > 500 else extracted_text

#         # Provide the summary and file URL to the user
#         return render(request, 'uploader/result.html', {'summary': summary, 'file_url': file_url})

#     return render(request, 'uploader/upload.html')




# 3rd

# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from PyPDF2 import PdfReader
# from pdf2image import convert_from_path
# from PIL import Image
# import pytesseract

# # Set Tesseract path (Windows के लिए)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Set Poppler path (Windows के लिए)
# POPPLER_PATH = r'C:\Users\kushw\Release-24.08.0-0\poppler-24.08.0\Library\bin'

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         uploaded_file = request.FILES['file']

#         # Check file type
#         if not uploaded_file.name.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')):
#             return render(request, 'uploader/upload.html', {'error': 'Invalid file format. Please upload a PDF or image file (PNG, JPG, JPEG).'})

#         # Save the uploaded file
#         fs = FileSystemStorage()
#         file_name = fs.save(uploaded_file.name, uploaded_file)
#         file_path = fs.path(file_name)
#         file_url = fs.url(file_name)

#         # Text extraction logic
#         extracted_text = ""
#         if uploaded_file.name.endswith('.pdf'):
#             try:
#                 # Try extracting text using PyPDF2
#                 reader = PdfReader(file_path)
#                 for page in reader.pages:
#                     extracted_text += page.extract_text()

#                 # If PyPDF2 fails or extracted text is empty, use OCR
#                 if not extracted_text.strip():
#                     images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
#                     for image in images:
#                         extracted_text += pytesseract.image_to_string(image)

#             except Exception as e:
#                 return render(request, 'uploader/upload.html', {'error': f"PDF processing failed: {str(e)}"})

#         elif uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#             try:
#                 # Extract text from image
#                 image = Image.open(file_path)
#                 extracted_text = pytesseract.image_to_string(image)
#             except Exception as e:
#                 return render(request, 'uploader/upload.html', {'error': f"Image processing failed: {str(e)}"})

#         # Summarize text (basic example)
#         summary = extracted_text[:500] + '...' if len(extracted_text) > 500 else extracted_text

#         return render(request, 'uploader/result.html', {'summary': summary, 'file_url': file_url})

#     return render(request, 'uploader/upload.html')





# option for length working final night end with this code befor start work today 19


# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from PyPDF2 import PdfReader
# from pdf2image import convert_from_path
# from PIL import Image
# import pytesseract

# # Set Tesseract path (Windows के लिए)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Set Poppler path (Windows के लिए)
# POPPLER_PATH = r'C:\Users\kushw\Release-24.08.0-0\poppler-24.08.0\Library\bin'

# def upload_file(request):
#     error_message = "" 
#     if request.method == 'POST' and request.FILES.get('file'):
#         uploaded_file = request.FILES['file']
#         if not uploaded_file.name.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')):
#             error_message = 'Invalid file format. Please upload a PDF or image file (PNG, JPG, JPEG).45'
#             return render(request, 'uploader/upload.html', {'error': error_message})
        
#         # Save the uploaded file
#         fs = FileSystemStorage()
#         file_name = fs.save(uploaded_file.name, uploaded_file)
#         file_path = fs.path(file_name)
#         file_url = fs.url(file_name)

#         # Text extraction logic
#         extracted_text = ""
#         if uploaded_file.name.endswith('.pdf'):
#             try:
#                 # Try extracting text using PyPDF2
#                 reader = PdfReader(file_path)
#                 for page in reader.pages:
#                     extracted_text += page.extract_text()

#                 # If PyPDF2 fails or extracted text is empty, use OCR
#                 if not extracted_text.strip():
#                     images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
#                     for image in images:
#                         extracted_text += pytesseract.image_to_string(image)

#             except Exception as e:
#                 return render(request, 'uploader/upload.html', {'error': f"PDF processing failed: {str(e)}"})

#         elif uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#             try:
#                 # Extract text from image
#                 image = Image.open(file_path)
#                 extracted_text = pytesseract.image_to_string(image)
#             except Exception as e:
#                 return render(request, 'uploader/upload.html', {'error': f"Image processing failed: {str(e)}"})

#         # Get the summary length from the form
#         summary_length = request.POST.get('summary_length', 'medium')

#         # Generate the summary based on the selected length
#         if summary_length == 'short':
#             summary = extracted_text[:200] + '...' if len(extracted_text) > 200 else extracted_text
#         elif summary_length == 'long':
#             summary = extracted_text[:1000] + '...' if len(extracted_text) > 1000 else extracted_text
#         else:
#             summary = extracted_text[:500] + '...' if len(extracted_text) > 500 else extracted_text

#         # Return the summary and file URL to the user
#         return render(request, 'uploader/result.html', {'summary': summary, 'file_url': file_url})

#     return render(request, 'uploader/upload.html', {'error': error_message})
   
   
   
   
   
   
   
   
#    without error 



from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set Poppler path (Windows)
POPPLER_PATH = r'C:\Users\kushw\Release-24.08.0-0\poppler-24.08.0\Library\bin'

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        # Save the uploaded file
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(file_name)
        file_url = fs.url(file_name)

        # Text extraction logic
        extracted_text = ""
        if uploaded_file.name.endswith('.pdf'):
            reader = PdfReader(file_path)
            for page in reader.pages:
                extracted_text += page.extract_text() or ""
            
            if not extracted_text.strip():
                images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
                for image in images:
                    extracted_text += pytesseract.image_to_string(image)

        elif uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(file_path)
            extracted_text = pytesseract.image_to_string(image)

        # Get the summary length from the form
        summary_length = request.POST.get('summary_length', 'medium')

        # Generate the summary based on the selected length
        if summary_length == 'short':
            summary = extracted_text[:200] + '...' if len(extracted_text) > 200 else extracted_text
        elif summary_length == 'long':
            summary = extracted_text[:1000] + '...' if len(extracted_text) > 1000 else extracted_text
        else:
            summary = extracted_text[:500] + '...' if len(extracted_text) > 500 else extracted_text

        # Return the summary and file URL to the user
        return render(request, 'uploader/upload.html', {'summary': summary, 'file_url': file_url})

    return render(request, 'uploader/upload.html') 




# fresh add error handling thing no need change other file 



### views.py
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from django.contrib import messages
# from PyPDF2 import PdfReader
# from pdf2image import convert_from_path
# from PIL import Image, UnidentifiedImageError
# import pytesseract

# # Set Tesseract path (Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Set Poppler path (Windows)
# POPPLER_PATH = r'C:\Users\kushw\Release-24.08.0-0\poppler-24.08.0\Library\bin'

# def upload_file(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         uploaded_file = request.FILES['file']

#         if uploaded_file.size == 0:
#             messages.error(request, "The uploaded file is empty. Please upload a valid file.")
#             return render(request, 'uploader/upload.html')

#         # Validate file extension
#         allowed_extensions = ['.pdf', '.png', '.jpg', '.jpeg']
#         if not any(uploaded_file.name.lower().endswith(ext) for ext in allowed_extensions):
#             messages.error(request, "Unsupported file type. Please upload a PDF or image file.")
#             return render(request, 'uploader/upload.html')

#         # Save the uploaded file
#         fs = FileSystemStorage()
#         file_name = fs.save(uploaded_file.name, uploaded_file)
#         file_path = fs.path(file_name)
#         file_url = fs.url(file_name)

#         extracted_text = ""
#         try:
#             if uploaded_file.name.endswith('.pdf'):
#                 reader = PdfReader(file_path)
#                 for page in reader.pages:
#                     extracted_text += page.extract_text() or ""
                
#                 if not extracted_text.strip():
#                     images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
#                     for image in images:
#                         extracted_text += pytesseract.image_to_string(image)

#             elif uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#                 try:
#                     image = Image.open(file_path)
#                     extracted_text = pytesseract.image_to_string(image)
#                 except UnidentifiedImageError:
#                     messages.error(request, "Unable to process the uploaded image. Please try a different file.")
#                     return render(request, 'uploader/upload.html')
#         except Exception as e:
#             messages.error(request, f"An error occurred while processing the file: {str(e)}")
#             return render(request, 'uploader/upload.html')

#         # Get the summary length from the form
#         summary_length = request.POST.get('summary_length', 'medium')

#         # Generate the summary based on the selected length
#         if summary_length == 'short':
#             summary = extracted_text[:200] + '...' if len(extracted_text) > 200 else extracted_text
#         elif summary_length == 'long':
#             summary = extracted_text[:1000] + '...' if len(extracted_text) > 1000 else extracted_text
#         else:
#             summary = extracted_text[:500] + '...' if len(extracted_text) > 500 else extracted_text

#         # Return the summary and file URL to the user
#         return render(request, 'uploader/result.html', {'summary': summary, 'file_url': file_url})

#     return render(request, 'uploader/upload.html')












