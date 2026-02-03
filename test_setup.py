#!/usr/bin/env python3
"""
Quick test to verify all files are correct before running Streamlit
"""

import os
from pathlib import Path

def test_files():
    """Test that all required files exist and have content"""

    print("🔍 Testing Rick & Morty Portal Setup...\n")

    base_dir = Path(__file__).parent

    # Test files
    files_to_check = {
        'AI_app.py': 350,  # minimum lines
        'assets/styles.css': 800,
        'assets/audio.js': 450,
    }

    all_good = True

    for file_path, min_lines in files_to_check.items():
        full_path = base_dir / file_path

        if not full_path.exists():
            print(f"❌ MISSING: {file_path}")
            all_good = False
            continue

        with open(full_path, 'r') as f:
            lines = len(f.readlines())

        if lines < min_lines:
            print(f"⚠️  WARNING: {file_path} has only {lines} lines (expected {min_lines}+)")
            all_good = False
        else:
            print(f"✅ OK: {file_path} ({lines} lines)")

    # Test specific content
    print("\n🔍 Checking specific features...\n")

    # Check audio.js has Rick voice
    with open(base_dir / 'assets/audio.js', 'r') as f:
        audio_content = f.read()

    if 'class RickVoice' in audio_content:
        print("✅ OK: Rick voice TTS found in audio.js")
    else:
        print("❌ MISSING: Rick voice TTS not found in audio.js")
        all_good = False

    if 'window.rickSpeakText' in audio_content:
        print("✅ OK: rickSpeakText function exposed")
    else:
        print("❌ MISSING: rickSpeakText function not exposed")
        all_good = False

    # Check AI_app.py has read aloud button
    with open(base_dir / 'AI_app.py', 'r') as f:
        app_content = f.read()

    if 'read-aloud-btn' in app_content:
        print("✅ OK: Read aloud button found in AI_app.py")
    else:
        print("❌ MISSING: Read aloud button not found in AI_app.py")
        all_good = False

    if 'sidebar-toggle-btn' in app_content:
        print("✅ OK: Sidebar toggle button found")
    else:
        print("❌ MISSING: Sidebar toggle button not found")
        all_good = False

    # Check character selection is OUTSIDE form
    if 'character_choice = st.selectbox' in app_content:
        # Find position of this line
        lines = app_content.split('\n')
        selectbox_line = None
        form_line = None

        for i, line in enumerate(lines):
            if 'character_choice = st.selectbox' in line:
                selectbox_line = i
            if 'form = st.form' in line:
                form_line = i

        if selectbox_line and form_line:
            if selectbox_line < form_line:
                print("✅ OK: Character selection is OUTSIDE form (correct!)")
            else:
                print("❌ ERROR: Character selection is INSIDE form (will not work!)")
                all_good = False

    # Check CSS has sidebar toggle animation
    with open(base_dir / 'assets/styles.css', 'r') as f:
        css_content = f.read()

    if '@keyframes pulseGlow' in css_content:
        print("✅ OK: pulseGlow animation found in CSS")
    else:
        print("❌ MISSING: pulseGlow animation not found in CSS")
        all_good = False

    if '.sidebar-toggle-visible' in css_content:
        print("✅ OK: .sidebar-toggle-visible class found in CSS")
    else:
        print("❌ MISSING: .sidebar-toggle-visible class not found in CSS")
        all_good = False

    print("\n" + "="*50)
    if all_good:
        print("✅ ALL TESTS PASSED! Ready to run Streamlit.")
        print("\nRun this command:")
        print("streamlit run AI_app.py")
    else:
        print("❌ SOME TESTS FAILED! Check errors above.")
        return 1

    print("="*50 + "\n")
    return 0

if __name__ == '__main__':
    exit(test_files())
