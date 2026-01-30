#!/usr/bin/env python
import os
from dotenv import load_dotenv

load_dotenv()

print("Configuration:")
print(f"  USE_OPENAI={os.getenv('USE_OPENAI')}")
print(f"  USE_OLLAMA={os.getenv('USE_OLLAMA')}")
print(f"  USE_FOUNDRY_LOCAL={os.getenv('USE_FOUNDRY_LOCAL')}")
print(f"  OPENAI_MODEL={os.getenv('OPENAI_MODEL')}")
print(f"  OLLAMA_MODEL={os.getenv('OLLAMA_MODEL')}")
print(f"  LOCAL_MODEL={os.getenv('LOCAL_MODEL')}")
