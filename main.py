from src.agents import (
    hypothesis_refiner,
    hypothesis_analyzer,
    hypothesis_reviser,
)


def main():
    # --- Step 1: Input ---
    hypothesis = "Users who see personalized onboarding screens are more likely to upgrade."
    print("\n=== ORIGINAL HYPOTHESIS ===")
    print(hypothesis)

    # --- Step 2: Refinement ---
    refined = hypothesis_refiner(hypothesis)
    print("\n=== REFINED HYPOTHESIS ===")
    print(refined)

    # --- Step 3: Reflection / Analysis ---
    reflection = hypothesis_analyzer(refined)
    print("\n=== ANALYZER FEEDBACK ===")
    print(reflection)

    # --- Step 4: Revision ---
    revised = hypothesis_reviser(refined, reflection)
    print("\n=== REVISED HYPOTHESIS ===")
    print(revised)


if __name__ == "__main__":
    main()
