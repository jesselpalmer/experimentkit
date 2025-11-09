# ExperimentKit

Open-source agentic infrastructure for planning, running, and evaluating product
experiments.

## Setup

1. Ensure that you have **Python 3.10+** installed.

```bash
python -V
```

2. (Recommended) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate     # On Windows: venv\Scripts\activate
```

3. Install all required libraries:

```bash
pip install -r requirements.txt
```

4. **Configure API Keys**

   ExperimentKit requires API keys from at least one LLM provider to
   function. Supported providers:

   - **OpenAI** (default) - Get your API key from
     [OpenAI Platform](https://platform.openai.com/api-keys)
   - **Anthropic** - Get your API key from
     [Anthropic Console](https://console.anthropic.com/)
   - **Mistral** - Get your API key from
     [Mistral AI Platform](https://console.mistral.ai/)

   Create a `.env` file in the project root directory:

   ```bash
   # .env file
   OPENAI_API_KEY=your_openai_api_key_here
   # ANTHROPIC_API_KEY=your_anthropic_api_key_here
   # MISTRAL_API_KEY=your_mistral_api_key_here
   ```

   **Note:** You only need to set the API key for the provider(s) you plan
   to use. The default provider is OpenAI. Uncomment and set the API keys
   for other providers if you want to use them.

   **Security:** Never commit your `.env` file to version control. It
   should already be in `.gitignore`.

5. (Optional) Link this environment to your IDE or Jupyter notebook:

```bash
python -m ipykernel install --user --name=.venv
```

## Usage

Once you have your API keys configured, you can run the example:

```bash
python main.py
```

This will run through the hypothesis refinement workflow:

1. Takes an original hypothesis
2. Refines it to be more specific and testable
3. Analyzes the refined hypothesis
4. Revises it based on the analysis feedback
