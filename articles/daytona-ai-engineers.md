# Unleash AI Engineers in Daytona: Omni and Claude Step-by-Step Guide

AI-powered development tools are revolutionizing how we build software. Omni Engineer and Claude Engineer are two such tools, designed to assist developers by generating code, debugging, and performing various programming tasks. Combining these powerful AI engineers with Daytona's cloud-native development environment offers an unparalleled developer experience: instant setup, consistent environments, and seamless collaboration.

This article will guide you through setting up and using Omni Engineer and Claude Engineer within Daytona, demonstrating how to leverage their capabilities for your development workflows.

## What You'll Learn

*   How to add `devcontainer.json` files to Omni Engineer and Claude Engineer repositories.
*   How to create Daytona workspaces from these repositories.
*   How to configure necessary API keys within Daytona.
*   How to run and interact with Omni Engineer and Claude Engineer for specific tasks.

## Prerequisites

Before you begin, ensure you have:

1.  **GitHub Account**: To fork the repositories.
2.  **Daytona Account**: Access to the Daytona platform.
3.  **API Keys for AI Models**:
    *   **Omni Engineer**: Requires an `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, or `GROQ_API_KEY`.
    *   **Claude Engineer**: Requires an `ANTHROPIC_API_KEY` or `GROQ_API_KEY`.
    *   You can obtain these from OpenAI, Anthropic, or Groq respectively.

## Step 1: Fork the AI Engineer Repositories

To make changes and create Daytona workspaces, you'll first need to fork the original repositories to your GitHub account.

1.  Go to [Doriandarko/omni-engineer](https://github.com/Doriandarko/omni-engineer).
2.  Click the "Fork" button in the top-right corner.
3.  Repeat the process for [Doriandarko/claude-engineer](https://github.com/Doriandarko/claude-engineer).

You should now have `your-username/omni-engineer` and `your-username/claude-engineer` in your GitHub repositories.

## Step 2: Add `devcontainer.json` for Daytona Compatibility

Daytona leverages Dev Containers to provide a pre-configured development environment. By adding a `devcontainer.json` file, you tell Daytona (and other Dev Container-compatible tools) how to set up your workspace.

### For Omni Engineer

1.  Clone your forked `omni-engineer` repository locally:
    