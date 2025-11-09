"""LLM client initialization utilities for multiple providers."""

from typing import Any
from dotenv import load_dotenv
import os

# Lazy imports to avoid requiring all providers to be installed
_openai_client = None
_anthropic_client = None
_mistral_client = None


def get_llm_client(provider: str = "openai") -> Any:
    """
    Initialize and return an LLM client for the specified provider.
    
    Loads environment variables from .env file and creates a client for the
    specified provider using the appropriate API key from environment variables.
    
    Args:
        provider: The LLM provider to use. Supported providers:
            - "openai" (requires OPENAI_API_KEY)
            - "anthropic" (requires ANTHROPIC_API_KEY)
            - "mistral" (requires MISTRAL_API_KEY)
    
    Returns:
        An initialized client instance for the specified provider.
        
    Raises:
        ValueError: If an unsupported provider is specified.
        RuntimeError: If the required API key is not found in environment variables.
    """
    load_dotenv()
    
    provider = provider.lower()
    
    if provider == "openai":
        return get_openai_client()
    elif provider == "anthropic":
        return get_anthropic_client()
    elif provider == "mistral":
        return get_mistral_client()
    else:
        raise ValueError(
            f"Unsupported provider: {provider}. "
            f"Supported providers: 'openai', 'anthropic', 'mistral'"
        )


def get_openai_client():
    """
    Initialize and return an OpenAI client using the API key from environment variables.
    
    Returns:
        OpenAI: An initialized OpenAI client instance.
        
    Raises:
        RuntimeError: If OPENAI_API_KEY is not found in environment variables.
    """
    global _openai_client
    
    if _openai_client is None:
        from openai import OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY not found in environment variables")
        _openai_client = OpenAI(api_key=api_key)
    
    return _openai_client


def get_anthropic_client():
    """
    Initialize and return an Anthropic client using the API key from environment variables.
    
    Returns:
        Anthropic: An initialized Anthropic client instance.
        
    Raises:
        RuntimeError: If ANTHROPIC_API_KEY is not found in environment variables.
    """
    global _anthropic_client
    
    if _anthropic_client is None:
        try:
            from anthropic import Anthropic
        except ImportError:
            raise RuntimeError(
                "Anthropic package not installed. Install it with: pip install anthropic"
            )
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY not found in environment variables")
        _anthropic_client = Anthropic(api_key=api_key)
    
    return _anthropic_client


def get_mistral_client():
    """
    Initialize and return a Mistral client using the API key from environment variables.
    
    Returns:
        Mistral: An initialized Mistral client instance.
        
    Raises:
        RuntimeError: If MISTRAL_API_KEY is not found in environment variables.
    """
    global _mistral_client
    
    if _mistral_client is None:
        try:
            from mistralai import Mistral
        except ImportError:
            raise RuntimeError(
                "Mistral package not installed. Install it with: pip install mistralai"
            )
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise RuntimeError("MISTRAL_API_KEY not found in environment variables")
        _mistral_client = Mistral(api_key=api_key)
    
    return _mistral_client


def call_llm(
    messages: list[dict[str, str]],
    model: str,
    provider: str = "openai",
    system_message: str | None = None,
    max_tokens: int = 250,
    temperature: float = 0.7,
) -> str:
    """
    Make a chat completion call to the specified LLM provider.
    
    This function abstracts away the differences between provider APIs, providing
    a unified interface for making LLM calls.
    
    Args:
        messages: List of message dictionaries with "role" and "content" keys.
                 Example: [{"role": "user", "content": "Hello"}]
        model: The model name to use (e.g., "gpt-4o-mini", "claude-3-haiku", "mistral-small").
        provider: The LLM provider to use ("openai", "anthropic", or "mistral").
                  Defaults to "openai".
        system_message: Optional system message. For Anthropic, this is passed separately.
        max_tokens: Maximum number of tokens to generate. Defaults to 250.
        temperature: Sampling temperature. Defaults to 0.7.
    
    Returns:
        The generated text response from the LLM.
        
    Raises:
        ValueError: If an unsupported provider is specified.
        RuntimeError: If the required API key is not found or package is not installed.
    """
    client = get_llm_client(provider=provider)
    provider = provider.lower()
    
    if provider == "openai":
        # Prepare messages for OpenAI
        openai_messages = []
        if system_message:
            openai_messages.append({"role": "system", "content": system_message})
        openai_messages.extend(messages)
        
        response = client.chat.completions.create(
            model=model,
            messages=openai_messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    
    elif provider == "anthropic":
        # Anthropic uses a separate system parameter
        anthropic_messages = [msg for msg in messages if msg["role"] != "system"]
        
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_message or "",
            messages=anthropic_messages
        )
        return response.content[0].text
    
    elif provider == "mistral":
        # Prepare messages for Mistral
        mistral_messages = []
        if system_message:
            mistral_messages.append({"role": "system", "content": system_message})
        mistral_messages.extend(messages)
        
        response = client.chat.complete(
            model=model,
            messages=mistral_messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content
    
    else:
        raise ValueError(f"Unsupported provider: {provider}")

