from ...utils import call_llm


def hypothesis_reviser(
    original: str,
    reflection: str,
    model: str = "gpt-4o-mini",
    provider: str = "openai"
) -> str:
    """
    Incorporates analyzer feedback into a new, improved hypothesis.
    
    Args:
        original: The original hypothesis that was refined.
        reflection: The feedback/reflection from the analyzer.
        model: The model name to use (default: gpt-4o-mini).
        provider: The LLM provider to use ("openai", "anthropic", or "mistral").
                  Defaults to "openai".
    
    Returns:
        A revised hypothesis that integrates the reflection feedback.
    """
    prompt = f"""
    You are a Hypothesis Revision Agent.

    Original hypothesis:
    "{original}"

    Reflection feedback:
    "{reflection}"

    Task:
    Produce one revised hypothesis that integrates the reflection feedback
    while remaining specific, measurable, and testable.
    """

    return call_llm(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        provider=provider,
        system_message="You are a precise experiment improvement agent.",
        max_tokens=250,
        temperature=0.7
    )

