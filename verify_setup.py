import sys

checks = {
    'Python 3.10+': sys.version_info >= (3, 10),
    'streamlit': False,
    'langchain': False,
    'chroma': False,
    'paddle': False,
    'whisper': False,
    'ollama': False
}

try:
    import streamlit; checks['streamlit'] = True
except: pass
try:
    import langchain; checks['langchain'] = True
except: pass
try:
    import chromadb; checks['chroma'] = True
except: pass
try:
    from paddleocr import PaddleOCR; checks['paddle'] = True
except: pass
try:
    import whisper; checks['whisper'] = True
except: pass
try:
    import ollama; checks['ollama'] = True
except: pass

print("\n✅ SETUP VERIFICATION")
for name, passed in checks.items():
    status = "✓" if passed else "✗"
    print(f"{status} {name}")

all_pass = all(checks.values())
if all_pass:
    print("\n🎉 All systems ready! Run: streamlit run app.py")
else:
    print("\n⚠️ Some checks failed. See errors above.")
