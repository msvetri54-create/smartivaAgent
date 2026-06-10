import os
from openai import OpenAI

# Initialize the OpenAI client
# Ensure your OPENAI_API_KEY is set in your system environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class SmartivaAgent:
    """
    SmartivaAgent is an AI-powered assistant designed to help 
    software engineers refactor, document, and secure their code.
    """
    
    def __init__(self, model="gpt-4o"):
        self.model = model

    def _call_llm(self, prompt, code):
        """
        Private helper method to send tasks to the AI model.
        
        :param prompt: The instruction for the AI.
        :param code: The code snippet to be analyzed.
        :return: The AI's response as a string.
        """
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert AI software engineer."},
                {"role": "user", "content": f"{prompt}\n\nCode:\n{code}"}
            ]
        )
        return response.choices[0].message.content

    def refactor_code(self, code):
        """Analyzes code and suggests improvements for readability and performance."""
        prompt = "Analyze the following code and provide a refactored version that improves readability and performance."
        return self._call_llm(prompt, code)

    def generate_docs(self, code):
        """Generates professional docstrings for the provided code."""
        prompt = "Generate professional docstrings and documentation for the following code."
        return self._call_llm(prompt, code)

    def run_security_analysis(self, code):
        """Scans the code for potential security vulnerabilities."""
        prompt = "Identify any security vulnerabilities or bad practices in the following code."
        return self._call_llm(prompt, code)

# Main block to execute the agent
if __name__ == "__main__":
    # Instantiate the agent
    agent = SmartivaAgent()
    print("SmartivaAgent is now initialized and ready to assist!")
    
    # Example usage
    sample_code = "def add(a,b): return a+b"
    print("\n--- Refactoring Suggestion ---")
    print(agent.refactor_code(sample_code))
