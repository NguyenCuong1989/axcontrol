# GitHub Actions Secrets Configuration

This document lists all secrets that need to be configured in GitHub repository settings for CI/CD workflows.

## Required Secrets for GitHub Actions

Add these secrets in: Repository Settings → Secrets and variables → Actions → New repository secret

### LLM & AI Services
- `OPENAI_API_KEY` - (Get from OpenAI dashboard)
- `CLAUDE_API_KEY` - (Get from Anthropic dashboard)
- `GEMINI_API_KEY` - (Get from Google AI Studio)
- `MISTRAL_API_KEY` - (Get from Mistral AI dashboard)

### GitHub Integration
- `GITHUB_PAT` - (Generate in GitHub Settings → Developer settings → Personal access tokens)
- `GITHUB_PAT_DAIOF` - (Generate for DAIOF integration)
- `GITHUB_PAT_API` - (Generate for API access)
- `GITHUB_PAT_HYPERAI` - (Generate for HyperAI ecosystem)

### Docker
- `DOCKER_USERNAME` - (Your Docker Hub username)
- `DOCKER_PASSWORD` - (Docker Hub access token)
- `DOCKER_ORG` - (Your Docker organization)

### Monitoring
- `SENTRY_DSN` - (Get from Sentry project settings)
- `GCLOUD_RW_API_KEY` - (Get from Grafana Cloud)

### Deployment
- `VERCEL_TOKEN` - (Get from Vercel account settings)
- `VERCEL_ORG_ID` - (Get from Vercel dashboard)
- `VERCEL_PROJECT_ID` - (Get from Vercel dashboard)

### Database
- `DATABASE_URL` - (Your PostgreSQL connection string)

### Telegram (if using bots)
- `TELEGRAM_BOT_TOKEN_FINALAI` - (Get from BotFather)

## Setup Instructions

1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret" for each secret above
3. Paste the value and save
4. Ensure secrets are not exposed in logs (use GitHub Actions secret masking)

## Environment-Specific Secrets

For different environments (dev/staging/prod), use GitHub Environments:

### Development
- Use secrets with `_DEV` suffix
- Lower rate limits, test data

### Staging
- Use secrets with `_STAGING` suffix  
- Pre-production testing

### Production
- Use secrets with `_PROD` suffix
- Full production keys, monitoring enabled
