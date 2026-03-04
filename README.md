# Clara Answers – Onboarding Automation Pipeline

## What This Builds
End-to-end pipeline: Demo Call Transcript → Account Memo JSON → Retell Agent Spec v1 → Onboarding Call → Updated Memo + Agent Spec v2 + Changelog

## Architecture
```
Transcript → LLM Extraction → Account Memo JSON (v1)
                                      ↓
                             Retell Agent Spec (v1)
                                      ↓
Onboarding Transcript → LLM Merge → Account Memo JSON (v2)
                                      ↓
                             Retell Agent Spec (v2) + Changelog
```

## Stack
- LLM: Groq API (llama-3.3-70b-versatile) — free tier
- Storage: JSON files versioned in GitHub
- Orchestration: Python pipeline (n8n architecture documented in /workflows)
- Cost: $0

## How to Run

### Option A: Google Colab (recommended)
1. Open `Clara_Pipeline.ipynb` in Google Colab
2. Set your GROQ_API_KEY in Cell 2
3. Run all cells in order

### Option B: Local
```bash
pip install groq
set GROQ_API_KEY=your_key_here   # Windows
python scripts/pipeline.py
```

## Adding New Accounts
Edit the `dataset` list in Cell 8 (Colab) or pipeline.py:
```python
dataset = [
    {
        "account_id": "ACC003",
        "demo_path": "mock_data/demo_ACC003.txt",
        "onboarding_path": "mock_data/onboarding_ACC003.txt"
    }
]
```
Drop transcript `.txt` files in `mock_data/` and re-run. Pipeline is idempotent.

## Output Structure
```
outputs/accounts/
├── ACC001/
│   ├── v1/account_memo.json       # Extracted from demo call
│   ├── v1/agent_spec.json         # Retell agent config v1
│   ├── v2/account_memo.json       # Updated after onboarding
│   ├── v2/agent_spec.json         # Retell agent config v2
│   ├── changelog.json             # Machine-readable diff
│   └── changelog.md               # Human-readable diff table
└── ACC002/
    └── ...
```

## Retell Manual Import (Free Tier)
1. Create account at retell.ai
2. Agents → Create Agent
3. Copy `system_prompt` from `v2/agent_spec.json` into prompt editor
4. Set transfer numbers from `key_variables`
5. Save and test

## Known Limitations
| Limitation | Production Fix |
|---|---|
| No audio transcription | Add Whisper step before extraction |
| File storage | Replace with Supabase |
| Task log is local JSON | Replace with Asana API |
| Retell import is manual | Use Retell API on paid plan |

## Zero-Cost Compliance
All components use free tiers. Total spend: $0.
