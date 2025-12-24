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
            image = cv2.imread(image_path)
            if image is None:
                return {'error': 'Could not read image', 'confidence': 0}
            
            # Perform OCR
            results = self.ocr.ocr(image, cls=True)
            
            # Extract text and confidence
            extracted_text = ""
            confidences = []
            
            for line in results:
                for word_info in line:
                    text = word_info
                    conf = word_info
                    extracted_text += text + " "
                    confidences.append(conf)
            
            avg_confidence = np.mean(confidences) if confidences else 0
            
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
