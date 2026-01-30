# AgentCon Configuration Guide

## Quick Start - Choose Your Model Provider

### Option 1: OpenAI (Best quality, paid)
```bash
# .env
USE_OPENAI=true
USE_OLLAMA=false
OPENAI_API_KEY=your-key-here
OPENAI_MODEL=gpt-4o-mini  # or gpt-4o for better quality
```
✅ **Pros:** Full tool support, streaming, highest quality
⚠️ **Cost:** Pay per token

### Option 2: Ollama Local (Free, fast)
```bash
# .env
USE_OPENAI=false
USE_OLLAMA=true
OLLAMA_MODEL=gpt-oss:20b  # or other local models
```
✅ **Pros:** Free, local, complete answers, no API costs
⚠️ **Requirement:** Ollama running locally (`ollama serve`)

### Option 3: Foundry Local (On-premises)
```bash
# .env
USE_OPENAI=false
USE_OLLAMA=false
LOCAL_MODEL=gpt-oss-20b-generic-cpu:1
LOCAL_BASE_URL=http://127.0.0.1:56238/v1
```
✅ **Pros:** Enterprise-grade, local deployment
⚠️ **Requirement:** Microsoft Foundry service running

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `USE_OPENAI` | `false` | Enable OpenAI API |
| `USE_OLLAMA` | `false` | Enable Ollama local |
| `OPENAI_API_KEY` | (required) | Your OpenAI API key |
| `OPENAI_MODEL` | `gpt-4o-mini` | OpenAI model ID |
| `OLLAMA_BASE_URL` | `http://localhost:11434/v1` | Ollama endpoint |
| `OLLAMA_MODEL` | `gpt-oss:20b` | Ollama model name |
| `LOCAL_BASE_URL` | `http://127.0.0.1:56238/v1` | Foundry endpoint |
| `LOCAL_MODEL` | `gpt-oss-20b-generic-cpu:1` | Foundry model name |

## Running the Demo

```bash
# Run with current configuration
.venv\Scripts\python.exe agentcon_demo.py
```

The pipeline will:
1. 🔍 **Critique** your architecture (identify security issues)
2. 🔧 **Fix** it (provide recommendations)
3. 📊 **Visualize** it (generate Mermaid diagram)
4. 📝 **Generate IaC** (create Bicep code)

All outputs saved to `output/` folder.

## Recommended Setups

### Development (Free)
- **Model:** Ollama with gpt-oss:20b
- **Cost:** $0
- **Quality:** ⭐⭐⭐⭐ (complete, thorough answers)
- **Setup:** `ollama run gpt-oss:20b` then set `USE_OLLAMA=true`

### Production (Best Quality)
- **Model:** OpenAI gpt-4o
- **Cost:** ~$0.03-0.15 per run
- **Quality:** ⭐⭐⭐⭐⭐ (highest quality)
- **Setup:** Add OpenAI API key and set `USE_OPENAI=true`

### Enterprise (On-Prem)
- **Model:** Foundry gpt-oss-20b
- **Cost:** $0 (self-hosted)
- **Quality:** ⭐⭐⭐⭐ (good, local control)
- **Setup:** Point to Foundry service endpoint
