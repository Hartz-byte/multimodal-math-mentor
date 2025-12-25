import whisper
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class AudioProcessor:
    """Process audio files and convert to text using Whisper"""

    def __init__(self, model_name: str = "base"):
        import torch
        # device = "cuda" if torch.cuda.is_available() else "cpu"
        device = "cpu"
        self.model = whisper.load_model(model_name, device=device)

    def process_audio(self, audio_path: str) -> Dict:
        """
        Process audio file and extract text
        
        Args:
            audio_path: Path to audio file
            
        Returns:
            {
                'text': transcribed text,
                'confidence': confidence score,
                'language': detected language
            }
        """
        try:
            result = self.model.transcribe(str(audio_path))
            
            # Normalize math text
            final_text = self.normalize_math_phrases(result['text'])
            
            return {
                'text': final_text,
                'confidence': result.get('confidence', 0.9),
                'language': result['language'],
                'raw_result': result
            }
            
        except Exception as e:
            logger.error(f"Audio processing error: {str(e)}")
            return {'error': str(e), 'confidence': 0}

    def normalize_math_phrases(self, text: str) -> str:
        """Convert spoken math phrases to mathematical notation"""
        replacements = {
            ' is equal to ': '=',
            ' equal to ': '=',
            ' equals ': '=',
            ' plus ': '+',
            ' minus ': '-',
            ' multiplied by ': '*',
            ' divided by ': '/',
            ' over ': '/',
            ' square root of ': '√',
            ' pi ': 'π',
            ' theta ': 'θ',
            ' alpha ': 'α',
            ' beta ': 'β',
            ' infinity ': '∞',
            ' approximately ': '≈',
            ' greater than ': '>',
            ' less than ': '<',
            ' times ': '*',
            ' to the power of ': '^',
            ' raised to ': '^',
            ' squared': '^2',
            ' cubed': '^3'
        }
        
        # Simple case-insensitive replacement
        # Note: simplistic, might replace non-math usage, but fine for math context
        normalized = text
        for phrase, symbol in replacements.items():
            # efficient case-insensitive replace?
            # re.sub(phrase, symbol, normalized, flags=re.IGNORECASE) is better
            import re
            normalized = re.sub(phrase, symbol, normalized, flags=re.IGNORECASE)
        
        return normalized.strip()
