"""
Module containing functions to validate insurance claims, calculate severity scores,
classify claim severity levels, and generate summary recommendations.

The scoring logic here is simplistic and meant for demonstration purposes. In a real
application you should develop more robust models or rules based on historical data
and domain expertise.
"""

from typing import Any, Dict, List
from datetime import datetime

# Required fields that must be present in the claim submission
REQUIRED_FIELDS: List[str] = [
    "claim_id",
    "policy_number",
    "claimant_name",
    "incident_date",
    "reported_date",
    "incident_type",
    "description",
    "estimated_loss_amount",
    "location",
]

def validate_claim(claim_data: Dict[str, Any]) -> None:
    """Validate that all required fields exist in the claim data."""
    missing = [field for field in REQUIRED_FIELDS if field not in claim_data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")


def calculate_severity_score(claim_data: Dict[str, Any]) -> float:
    """Compute a severity score for a claim based on simple heuristics."""
    score = 0.0

    # Score based on estimated loss amount
    loss = float(claim_data.get("estimated_loss_amount", 0))
    if loss > 500_000:
        score += 3.0
    elif loss > 100_000:
        score += 2.0
    elif loss > 10_000:
        score += 1.0

    # Score based on delay between incident and report dates
    try:
        incident_date = datetime.fromisoformat(claim_data.get("incident_date"))
        reported_date = datetime.fromisoformat(claim_data.get("reported_date"))
        days_delay = (reported_date - incident_date).days
        if days_delay > 30:
            score += 2.0
        elif days_delay > 7:
            score += 1.0
    except Exception:
        # If date parsing fails, ignore delay scoring
        pass

    # Score based on incident type
    incident_type = claim_data.get("incident_type", "").lower()
    if incident_type in {"fire", "injury", "liability"}:
        score += 2.0
    elif incident_type in {"theft", "water damage", "burst pipe"}:
        score += 1.0

    return score


def classify_claim_severity(score: float) -> str:
    """Classify the claim severity based on the severity score."""
    if score >= 5.0:
        return "High"
    elif score >= 3.0:
        return "Medium"
    else:
        return "Low"


def generate_claim_summary(claim_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate the claim, compute its severity, and assemble recommendations."""
    validate_claim(claim_data)
    score = calculate_severity_score(claim_data)
    severity = classify_claim_severity(score)

    recommendations: List[str] = []
    if severity == "High":
        recommendations.append("Assign a senior adjuster immediately.")
        recommendations.append("Initiate an on-site investigation.")
    elif severity == "Medium":
        recommendations.append("Request additional documentation and statements.")
        recommendations.append("Review policy coverage details and prior claims history.")
    else:
        recommendations.append("Proceed with standard claim processing procedures.")
        recommendations.append("Monitor for potential fraud indicators as you process the claim.")

    return {
        "severity": severity,
        "score": score,
        "recommendations": recommendations,
    }
