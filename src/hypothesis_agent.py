from .utils import call_llm

def hypothesis_agent(
    hypothesis: str, 
    model: str = "gpt-4o-mini", 
    provider: str = "openai"
) -> str:
    """
    Takes a hypothesis and returns a more specific, testable version of it
    using the specified model and provider.
    
    Args:
        hypothesis: The original hypothesis to refine.
        model: The model name to use (e.g., "gpt-4o-mini", "claude-3-haiku", "mistral-small").
        provider: The LLM provider to use ("openai", "anthropic", or "mistral").
                  Defaults to "openai".
    
    Returns:
        A refined, more specific and testable version of the hypothesis.
    """

    prompt = f"""
    You are a Hypothesis Refinement Agent.

    Task:
    Given the following hypothesis, rewrite it to make it more specific,
    measurable, and testable. Use clear metrics or conditions where possible.

    Original hypothesis:
    "{hypothesis}"

    Output:
    A single refined hypothesis that is concrete, falsifiable, and written
    in one or two sentences.
    """

    return call_llm(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        provider=provider,
        system_message="You are a helpful experiment design assistant.",
        max_tokens=250,
        temperature=0.7
    )
