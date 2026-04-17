"""
Module providing a simple wrapper around the Anthropic Claude API.
Uses the configuration defined in config.py to instantiate a client and send prompts.
"""

from anthropic import Anthropic, APIError

from config import (
    ANTHROPIC_API_KEY,
    ANTHROPIC_MODEL,
    MAX_TOKENS,
    TEMPERATURE,
)


class ClaudeClient:
    """Thin wrapper around the Anthropic Claude API."""

    def __init__(self, api_key: str = ANTHROPIC_API_KEY) -> None:
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY is not set. Please set it in your environment or .env file.")
        self.client = Anthropic(api_key=api_key)

    def call_claude(
        self,
        prompt: str,
        model: str = ANTHROPIC_MODEL,
        max_tokens: int = MAX_TOKENS,
        temperature: float = TEMPERATURE,
    ) -> str:
        """Call Claude with the given prompt and return the response content."""
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content
        except APIError as err:
            # re-raise as runtime error with descriptive message
            raise RuntimeError(f"Claude API request failed: {err}")


# Create a module-level client instance for convenience
claude_client = ClaudeClient()
