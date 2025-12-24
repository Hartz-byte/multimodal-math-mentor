import whisper
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class AudioProcessor:
    """Process audio files and convert to text using Whisper"""

    def __init__(self, model_name: str = "base"):
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
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
            result = self.model.transcribe(audio_path)
            
            return {
                'text': result['text'],
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
            'square root of': '√',
            'pi': 'π',
            'theta': 'θ',
            'alpha': 'α',
            'beta': 'β',
            'infinity': '∞',
            'approximately': '≈',
            'equals': '=',
            'greater than': '>',
            'less than': '<',
            'times': '×',
            'divided by': '÷',
            'to the power of': '^',
            'raised to': '^'
        }
        
        normalized = text.lower()
        for phrase, symbol in replacements.items():
            normalized = normalized.replace(phrase, symbol)
        
        return normalized
