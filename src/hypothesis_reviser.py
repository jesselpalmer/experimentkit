from .utils import call_llm

def hypothesis_reviser(original: str, reflection: str, model="gpt-4o-mini", provider="openai"):
    """
    Incorporates analyzer feedback into a new, improved hypothesis.
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
