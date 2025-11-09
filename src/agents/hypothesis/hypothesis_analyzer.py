from ...utils import call_llm


def hypothesis_analyzer(
    refined_hypothesis: str,
    model: str = "gpt-4o-mini",
    provider: str = "openai"
) -> str:
    """
    Analyzes and provides constructive feedback on a refined hypothesis,
    focusing on its specificity, measurability, and experimental testability.

    Args:
        refined_hypothesis: The refined hypothesis to analyze.
        model: The model name to use (default: gpt-4o-mini).
        provider: The LLM provider ("openai", "anthropic", or "mistral").

    Returns:
        A concise reflection summarizing:
        - Strengths of the hypothesis
        - Weaknesses or ambiguities
        - Suggestions for improvement
    """

    prompt = f"""
    You are a Hypothesis Reflection Agent.

    Task:
    Critically evaluate the following refined hypothesis as if you are a peer reviewer
    preparing it for a real-world experiment.

    Refined hypothesis:
    "{refined_hypothesis}"

    Analyze it on the following criteria:
    1. **Clarity** – Is the hypothesis clearly stated and easy to understand?
    2. **Specificity** – Does it define measurable metrics, timeframes, or success conditions?
    3. **Testability** – Could it realistically be validated or falsified with an experiment?
    4. **Assumptions** – Are there any hidden assumptions or biases?
    5. **Actionability** – Can it guide a meaningful next experiment?

    Output:
    Provide a short, structured reflection in 3–5 paragraphs that includes:
    - A summary of the hypothesis quality
    - Two concrete strengths
    - Two areas to improve
    - One actionable suggestion for refinement or next steps.
    """

    return call_llm(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        provider=provider,
        system_message="You are a thoughtful and critical experiment design reviewer.",
        max_tokens=400,
        temperature=0.6
    )

