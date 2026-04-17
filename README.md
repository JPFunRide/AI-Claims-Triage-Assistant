# AI Claims Triage Assistant

## Problem
Insurance claims triage is often manual and time‑consuming. Adjusters must read through long claim descriptions and supporting documents to determine severity and next steps. This can lead to inconsistent decisions and delays.

## Solution
The **AI Claims Triage Assistant** uses Anthropic’s Claude model to analyze claim submissions and provide structured recommendations. It generates a severity classification, highlights key factors driving that classification and suggests follow‑up actions.

## Features
- **Severity classification** – classifies each claim as *Low*, *Medium* or *High* severity.
- **Key factors identification** – extracts important details that influence the severity assessment.
- **Action recommendations** – suggests actions for adjusters, such as further investigation, contacting the claimant or fast‑tracking.
- **Simple integration** – written in Python with JSON input/output for easy adoption.

## Tech Stack
- **Claude API (Anthropic)** for natural language analysis.
- **Python** for orchestration and script logic.
- **JSON** for input claim data.

## Example Input
```json
{
  "claim_id": "CLM123",
  "policy_number": "POL456",
  "claimant_name": "John Doe",
  "incident_date": "2025-06-15",
  "reported_date": "2025-06-16",
  "incident_type": "Water damage",
  "description": "Pipe burst causing significant water damage to property",
  "estimated_loss_amount": 100000,
  "location": "Dubai"
}
```

## Example Output
- **Claim Severity:** Medium
- **Key Factors:** High estimated loss, water damage severity, prompt reporting
- **Recommended Actions:** Send adjuster to inspect damage, coordinate with contractors, review policy coverage

## Why Claude?
Claude can process large amounts of unstructured text and generate consistent, structured responses. Its long context window and strong reasoning make it well‑suited for detailed insurance claims analysis.

## Future Improvements
- Integrate with insurance claim management systems for end‑to‑end automation.
- Support multiple languages and additional policy types.
- Add analytics dashboards for portfolio‑level insights.

## Author
JPFunRide
