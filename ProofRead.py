import openai

def proofread_report(report):
    # Set up your OpenAI API key
    openai.api_key = 'YOUR_API_KEY'
    
    # Define the parameters for the completion
    prompt = "Proofread the following report:\n\n" + report + "\n\n====="
    temperature = 0.7
    max_tokens = 100
    
    # Request the proofreading from OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    # Extract and return the proofread text
    return response.choices[0].text.strip()

# Example usage
report_text = """
Introduction:
This is a consultation report for patient John Doe.
The patient presented with symptoms of coughing and wheezing.
Assessment:
Upon examination, it was found that the patient has a history of asthma.
The patient also reported exposure to dust and pollen.
Plan:
Prescribe an inhaler to manage the symptoms.
Advise the patient to avoid triggers such as dust and pollen.
"""

proofread_text = proofread_report(report_text)
print(proofread_text)
