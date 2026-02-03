# 🔥 RESTART INSTRUCTIES - LEES DIT EERST! 🔥

## WAAROM ZIE IK GEEN CHANGES?

Streamlit cached JavaScript en CSS agressief. Je MOET deze stappen volgen:

## STAP 1: Stop Streamlit VOLLEDIG

```bash
# In de terminal waar Streamlit draait:
# Druk op Ctrl+C
# Wacht tot je ziet: "Stopping..."
# Als het niet stopt, kill het proces:
pkill -f streamlit
```

## STAP 2: Clear Python Cache

```bash
cd /Volumes/Extreme_SSD/All_My_Files_DEC_2023/PROGRAMMEREN/APPS/RickAndMortyChat/rickandmorty_chat
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
rm -rf ~/.streamlit/cache
```

## STAP 3: Clear Browser Cache

### Chrome/Brave:
1. Open DevTools (Cmd+Option+I)
2. Right-click op de refresh button
3. Kies "Empty Cache and Hard Reload"

### Firefox:
1. Cmd+Shift+Delete
2. Vink "Cache" aan
3. Klik "Clear Now"

### Safari:
1. Cmd+Option+E (Clear Cache)
2. Dan Cmd+R (Refresh)

## STAP 4: Restart Streamlit met Clean Slate

```bash
cd /Volumes/Extreme_SSD/All_My_Files_DEC_2023/PROGRAMMEREN/APPS/RickAndMortyChat/rickandmorty_chat
streamlit run AI_app.py --server.port 8501 --server.headless true --browser.gatherUsageStats false --server.runOnSave true
```

## STAP 5: Open in PRIVATE/INCOGNITO Window

Dit zorgt ervoor dat er GEEN cached versie wordt geladen:

- Chrome/Brave: Cmd+Shift+N
- Firefox: Cmd+Shift+P
- Safari: Cmd+Shift+N

Ga naar: http://localhost:8501

## VERIFICATION CHECKLIST

Na restart, check dit:

### ✅ Audio Werkt:
- Open browser console (F12)
- Type: `window.portalAudio`
- Should see: `PortalAudioSystem {audioContext: AudioContext, ...}`
- Typ iets in een input field → Should hear typing sounds
- Klik "ACTIVATE PORTAL" → Should hear portal whoosh

### ✅ Sidebar Toggle Werkt:
- Klik op groene knop linksboven (☰)
- Sidebar should appear/disappear
- Button should animate (pulse glow)

### ✅ Custom Character Werkt:
- Selecteer "Andere..." in dropdown
- Custom input field should APPEAR
- Type een character → Should be enabled
- Selecteer een andere optie → Custom input should DISAPPEAR

### ✅ Select Options Styling:
- Open dropdown
- Options should have:
  - Font: Courier New (monospace)
  - Color: #00ff41 (neon green)
  - Background: #0a0e27 (dark blue)

### ✅ Read Aloud Werkt:
- Submit een vraag
- Wacht op antwoord
- Klik "RICK LEEST VOOR"
- Should hear Rick-like voice reading response

## ALS HET NOG STEEDS NIET WERKT:

### Debug Stap 1: Check Console Errors
```bash
# Open browser console (F12 → Console tab)
# Look for errors in RED
# Common issues:
# - "ReferenceError: portalAudio is not defined" → JavaScript didn't load
# - "Failed to load resource" → File path wrong
```

### Debug Stap 2: Verify Files Are Loaded
```bash
# In browser console:
window.portalAudio       # Should return object
window.rickSpeakText     # Should return function
window.togglePortalAudio # Should return function
```

### Debug Stap 3: Check Network Tab
```bash
# F12 → Network tab
# Refresh page
# Check if these are loaded:
# - styles.css (should be ~25KB)
# - audio.js content (should be ~15KB, embedded in HTML)
```

## LAATSTE RESORT: Nuclear Option

```bash
# Stop Streamlit
pkill -f streamlit

# Remove ALL Streamlit cache
rm -rf ~/.streamlit

# Clear browser storage
# Chrome: F12 → Application → Clear Storage → "Clear site data"

# Restart computer (clears all caches)
sudo reboot

# After reboot:
cd /Volumes/Extreme_SSD/All_My_Files_DEC_2023/PROGRAMMEREN/APPS/RickAndMortyChat/rickandmorty_chat
streamlit run AI_app.py
```

## WHAT WAS FIXED:

1. ✅ **Sidebar Toggle**: JavaScript event listener fixed, CSS animation added
2. ✅ **Select Options**: Enhanced CSS with proper font and colors
3. ✅ **Custom Character**: Moved OUTSIDE form so it updates immediately
4. ✅ **Audio System**: Changed from iframe to direct injection
5. ✅ **Read Aloud**: Added Rick-like voice with Web Speech API (FREE!)

## EXPECTED BEHAVIOR:

- **Audio**: Typing sounds, portal whoosh, glitch sounds during speech
- **Sidebar**: Animated button that toggles sidebar visibility
- **Custom Character**: Input appears ONLY when "Andere..." selected
- **Read Aloud**: Button appears after response, speaks with high pitch/fast rate
- **Select Options**: Courier New font, neon green text, dark background
