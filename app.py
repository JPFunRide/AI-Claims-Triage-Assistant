import os
import json
import anthropic


def analyze_claim(claim_data):
    """Analyze an insurance claim using the Anthropic Claude model and return a structured response."""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    prompt = f"""
    Analyze the following insurance claim and provide:
    - Claim Severity (Low / Medium / High)
    - Key factors affecting severity
    - Recommended actions

    Claim Data:
    {json.dumps(claim_data, indent=2)}
    """
    # Send the prompt to Claude
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content


if __name__ == "__main__":
    # Load sample claim data from JSON file
    with open("sample_data/claim_example.json") as f:
        claim = json.load(f)
    result = analyze_claim(claim)
    print(result)
