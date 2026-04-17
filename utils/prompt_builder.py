"""
Utility functions for constructing prompts from template files and data.
"""

import json
from pathlib import Path
from typing import Any, Dict, List

def load_template(template_path: str) -> str:
    """Load a prompt template from the given file path."""
    path = Path(template_path)
    return path.read_text(encoding="utf-8")

def build_prompt(template: str, data: Dict[str, Any], severity: str, recommendations: List[str]) -> str:
    """
    Fill a prompt template with claim data, a severity classification, and recommendations.

    The template should contain placeholders {data}, {severity}, and {recommendations}.
    The data dictionary will be formatted as pretty JSON.
    Recommendations will be formatted as a bulleted list.
    """
    formatted_data = json.dumps(data, indent=2)
    formatted_recs = "\n".join(f"- {rec}" for rec in recommendations)
    return template.format(data=formatted_data, severity=severity, recommendations=formatted_recs)
