from src.hypothesis_agent import hypothesis_agent
from src.hypothesis_analyzer import hypothesis_analyzer
from src.hypothesis_reviser import hypothesis_reviser  # optional, if you created it


def main():
    # --- Step 1: Input ---
    hypothesis = "Users who see personalized onboarding screens are more likely to upgrade."
    print("\n=== ORIGINAL HYPOTHESIS ===")
    print(hypothesis)

    # --- Step 2: Refinement ---
    refined = hypothesis_agent(hypothesis)
    print("\n=== REFINED HYPOTHESIS ===")
    print(refined)

    # --- Step 3: Reflection / Analysis ---
    reflection = hypothesis_analyzer(refined)
    print("\n=== ANALYZER FEEDBACK ===")
    print(reflection)

    # --- Step 4: Revision (optional improvement loop) ---
    revised = hypothesis_reviser(refined, reflection)
    print("\n=== REVISED HYPOTHESIS ===")
    print(revised)


if __name__ == "__main__":
    main()
