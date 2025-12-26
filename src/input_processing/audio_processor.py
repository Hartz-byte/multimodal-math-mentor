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
        # Use regex patterns for more flexible matching
        import re
        
        replacements = [
            (r'\s+is equal to\s+', '='),
            (r'\s+equal to\s+', '='),
            (r'\s+equals\s+', '='),
            (r'\s+plus\s+', '+'),
            (r'\s+minus\s+', '-'),
            (r'\s+multiplied by\s+', '*'),
            (r'\s+divided by\s+', '/'),
            (r'\s+over\s+', '/'),
            (r'\s+times\s+', '*'),
            (r'\s+square root of\s+', '√'),
            (r'\s+pi\s+', 'π'),
            
            # Powers - Order matters! Specific phrases first
            (r'\s+to the power of\s+', '^'),
            (r'\s+raised to\s+', '^'),
            
            # "squared" and "square" handling
            # "x squared" -> "x²"
            # "x square" -> "x²"
            # Warning: "square root" is already handled above, so we must be careful not to break it.
            # "root" is distinct.
            (r'(\w+)\s+squared', r'\1²'),
            (r'(\w+)\s+square(?! root)', r'\1²'), # Negative lookahead to avoid "square root"
            
            (r'(\w+)\s+cubed', r'\1³'),
            (r'(\w+)\s+cube', r'\1³'),
        ]
        
        normalized = text
        for pattern, replacement in replacements:
            normalized = re.sub(pattern, replacement, normalized, flags=re.IGNORECASE)
            
        # Cleanup
        normalized = normalized.replace(" =", "=").replace(" +", "+").replace(" -", "-")
        
        return normalized.strip()
