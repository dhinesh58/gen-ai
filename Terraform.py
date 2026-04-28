import os
from google import genai

API_KEY = os.getenv("GOOGLE_API_KEY") or "xxxxxxxxxxxxxxxxxxxxxxxx"
client = genai.Client(api_key=API_KEY)

# Show available models
print("Available models:")
models = list(client.models.list())
for idx, m in enumerate(models, start=1):
    print(f"{idx}. {m.name} — {m.supported_actions}")

# Ask user to pick a model (default = first one)
choice = input("\nEnter the number of the model you want to use (press Enter for default): ")
if choice.strip() == "":
    model_name = models[0].name
else:
    model_name = models[int(choice) - 1].name

PROMPT = """
Generate an optimized Terraform configuration for deploying {resource} in Azure.
Follow best practices:
- Use variables for reusable values (location, resource group, names).
- Apply tags for governance and cost tracking.
- Ensure security (e.g., enable HTTPS, restrict public access).
- Structure modules cleanly for scalability.
Return only the Terraform code between two lines for easy copy-paste.
"""

def generate_infra(resource):
    response = client.models.generate_content(
        model=model_name,
        contents=PROMPT.format(resource=resource)
    )
    return response.text

if __name__ == '__main__':
    resource = input("Enter the Azure resource (e.g., VM, AKS, Storage Account): ")
    config = generate_infra(resource)
    print("\nGenerated Terraform configuration:\n")
    print(config)
