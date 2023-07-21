import os
import subprocess
import simpleaudio as sa
import json

DATA_PATH = 'path/to/audio/files' 
METADATA_FILE = 'metadata.json'

metadata = []

current_index = 0
if os.path.exists(METADATA_FILE):
  with open(METADATA_FILE) as f:
    metadata = json.load(f)
    current_index = len(metadata)

for filename in os.listdir(DATA_PATH)[current_index:]:
  filepath = os.path.join(DATA_PATH, filename)

  print(f"Now playing: {filename}")
  
  # Play audio 
  wave_obj = sa.WaveObject.from_wave_file(filepath)
  play_obj = wave_obj.play()
  play_obj.wait_done()

  # Prompt for description
  desc = input("Enter comma-separated descriptive keywords: ")

  # Save metadata
  metadata.append({
    'file': filename,
    'description': desc
  })

  # Write updated metadata
  with open(METADATA_FILE, 'w') as f:
    json.dump(metadata, f)

print("Metadata collection complete!")
