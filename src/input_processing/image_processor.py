import cv2
import numpy as np
from paddleocr import PaddleOCR
from typing import Tuple, Dict
import logging

logger = logging.getLogger(__name__)

class ImageProcessor:
    """Process images and extract text using PaddleOCR"""

    def __init__(self, use_gpu: bool = False):
        import torch
        self.use_gpu = use_gpu or torch.cuda.is_available()
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', device=('gpu' if self.use_gpu else 'cpu'))

    def process_image(self, image_path: str) -> Dict:
        """
        Process image and extract text
        
        Args:
            image_path: Path to image file
            
        Returns:
            {
                'text': extracted text,
                'confidence': average confidence,
                'raw_results': raw OCR output,
                'needs_review': if confidence low
            }
        """
        try:
            # Read image
            image_path_str = str(image_path)
            image = cv2.imread(image_path_str)
            if image is None:
                return {'error': 'Could not read image', 'confidence': 0}
            
            # Perform OCR
            results = self.ocr.ocr(image, cls=True)
            
            extracted_text = ""
            confidences = []
            
            # Results structure: [[ [box], (text, confidence) ], ... ] for single image
            # Sometimes wrapped in another list: [ [result_for_img] ]
            # PaddleOCR returns a list of result lists (one per image).
            if results and len(results) > 0:
                # Get result for the first (and only) image
                res = results[0]
                
                if res: # If text was detected
                    for line in res:
                        # line format: [box_coords, (text, confidence)]
                        # box_coords = line[0]
                        text_info = line[1]
                        
                        text = text_info[0]
                        conf = text_info[1]
                        
                        extracted_text += text + " "
                        confidences.append(conf)
            
            avg_confidence = np.mean(confidences) if confidences else 0
            
            if not extracted_text:
                return {'text': '', 'confidence': 0, 'needs_review': True, 'error': 'No text found'}

            return {
                'text': extracted_text.strip(),
                'confidence': avg_confidence,
                'raw_results': results,
                'needs_review': avg_confidence < 0.8
            }
            
        except Exception as e:
            logger.error(f"Image processing error: {str(e)}")
            return {'error': str(e), 'confidence': 0}

    def preprocess_image(self, image_path: str) -> str:
        """Preprocess image for better OCR (contrast, rotation)"""
        image = cv2.imread(image_path)
        
        # Increase contrast
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        l = clahe.apply(l)
        enhanced = cv2.merge([l,a,b])
        enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
        
        # Save preprocessed
        output_path = image_path.replace('.', '_enhanced.')
        cv2.imwrite(output_path, enhanced)
        
        return output_path
