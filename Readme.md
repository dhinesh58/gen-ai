# 🚀 GenAI for Terraform Automation (Azure)

This project demonstrates how Generative AI (Hosted LLMs and Local LLMs) can be used to generate Terraform code for Azure infrastructure.

---

## 📌 Overview

Generative AI can accelerate Infrastructure as Code (IaC) by:
- Generating Terraform templates
- Applying best practices (security, tagging, modularity)
- Reducing manual effort

---

## 🧠 Architecture

User → Prompt → GenAI (Hosted / Local) → Terraform Code → Azure Deployment

---

## 🤖 LLM Approaches

### 1. Hosted LLM (API-based)

Examples:
- Google Gemini
- OpenAI GPT

#### ✅ Pros:
- Easy to use
- High-quality output
- No setup required

#### ❌ Cons:
- API cost
- Data privacy concerns

---

### 2. Local LLM (Self-hosted)

Examples:
- Ollama
- LLaMA

#### ✅ Pros:
- Full data privacy
- No API dependency
- Customizable

#### ❌ Cons:
- Requires compute resources
- Setup complexity

---

## ⚙️ Example Prompt
Generate Terraform code for:
- Azure Virtual Machine
- NSG with inbound rules
- Tags and variables
- Managed Identity enabled

🚀 Project Setup
## Create Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Linux/MacOS

.\venv\Scripts\activate  # On Windows
## Install Dependencies

pip3 install google-genai
## Run the Application

python3 generate_terraform.py
