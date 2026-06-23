# Secrets Management Guide

Complete guide for managing secrets across all deployment environments for AXCONTROL.

## Overview

This project uses a multi-layered secrets management approach to ensure security across different environments:

- **Local Development**: `.env` file (gitignored)
- **Docker**: `docker-compose.yml` with environment variables
- **GitHub Actions**: Repository secrets
- **Vercel**: Environment variables in project settings
- **Production**: Encrypted secrets with rotation support

## File Structure

```
axcontrol/
├── .env                          # Local development (gitignored)
├── .env.example                  # Template for new developers
├── .env.vercel                   # Vercel environment variables (gitignored)
├── docker-compose.yml            # Docker configuration
├── .github/workflows/
│   └── secrets-reference.md      # GitHub Actions secrets guide
└── docs/
    └── SECRETS-MANAGEMENT.md     # This file
```

## Local Development Setup

### 1. Initial Setup

```bash
# Copy the example file
cp .env.example .env

# Edit with your actual secrets
nano .env
```

### 2. Available Secrets

The `.env` file includes:

- **LLM Providers**: OpenAI, Claude, Gemini, Mistal, OpenRouter
- **GitHub**: PATs for different purposes (DAIOF, API, HyperAI)
- **Docker**: Organization access token
- **Monitoring**: Sentry, Grafana Cloud, Axiom
- **Database**: PostgreSQL connection string
- **Telegram**: Bot tokens
- **Other Services**: Notion, Postman, Linear, Vercel

### 3. Loading Environment Variables

```bash
# Using python-dotenv (automatic in config.py)
python main.py

# Manual loading
export $(cat .env | xargs)
python main.py
```

## Docker Deployment

### 1. Using Docker Compose

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f axcontrol

# Stop services
docker-compose down
```

### 2. Environment Variables in Docker

Docker Compose reads from `.env` file automatically. Secrets are passed as:

```yaml
environment:
  - OPENAI_API_KEY=${OPENAI_API_KEY}
  - DATABASE_URL=${DATABASE_URL}
```

### 3. Docker Secrets (Production)

For production Docker deployments, use Docker Secrets:

```bash
# Create secrets
echo "your-api-key" | docker secret create openai_api_key -

# Use in docker-compose.yml
secrets:
  openai_api_key:
    external: true
```

## GitHub Actions CI/CD

### 1. Setting Up Secrets

1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add each secret from `.github/workflows/secrets-reference.md`

### 2. Using Secrets in Workflows

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Build
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          echo "Building with API key"
```

### 3. Environment-Specific Secrets

Use GitHub Environments for different stages:

- **Development**: Secrets with `_DEV` suffix
- **Staging**: Secrets with `_STAGING` suffix
- **Production**: Secrets with `_PROD` suffix

### 4. Required GitHub Secrets

See `.github/workflows/secrets-reference.md` for complete list.

## Vercel Deployment

### 1. Setting Environment Variables

1. Go to Vercel project → Settings → Environment Variables
2. Add variables from `.env.vercel`
3. Select environment (Production, Preview, Development)

### 2. CLI Setup

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Set environment variables
vercel env add OPENAI_API_KEY production
vercel env add DATABASE_URL production
```

### 3. Automatic Deployment

Vercel automatically loads environment variables during deployment.

## Security Best Practices

### 1. Never Commit Secrets

All `.env*` files are in `.gitignore`. Never commit actual secrets.

### 2. Use Different Keys per Environment

- **Development**: Test keys with lower limits
- **Staging**: Pre-production keys
- **Production**: Full production keys

### 3. Regular Key Rotation

Rotate keys every 90 days:

```bash
# Generate new OpenAI key
# Update all environments
# Test before switching
# Delete old key after 7 days
```

### 4. Access Control

- Limit who can access secrets
- Use least privilege principle
- Audit access logs regularly

### 5. Backup Secrets

Store encrypted backups in password manager:

```bash
# Export to password manager
# Use Bitwarden, 1Password, or Doppler
# Include environment labels
```

## Secret Rotation Guide

### OpenAI API Key Rotation

1. Generate new key in OpenAI dashboard
2. Update `.env` locally
3. Update GitHub Actions secrets
4. Update Vercel environment variables
5. Update Docker secrets
6. Test all environments
7. Delete old key after 7 days

### GitHub PAT Rotation

1. Generate new PAT in GitHub Settings
2. Update `.env` and all CI/CD configs
3. Update any scripts using old PAT
4. Test authentication
5. Revoke old PAT

## Troubleshooting

### Secrets Not Loading

```bash
# Check file permissions
ls -la .env

# Verify .env exists
test -f .env && echo "Exists" || echo "Missing"

# Check pydantic-settings installation
pip show pydantic-settings
```

### Docker Secrets Issues

```bash
# Check docker-compose syntax
docker-compose config

# Verify environment variables
docker-compose config | grep OPENAI

# Check container environment
docker exec axcontrol env | grep OPENAI
```

### GitHub Actions Secrets

```bash
# List secrets (requires admin access)
gh secret list

# Add secret via CLI
gh secret set OPENAI_API_KEY
```

## Emergency Procedures

### Compromised Secret

1. **Immediate**: Revoke compromised key
2. **Generate**: Create new secret
3. **Update**: Change in all environments
4. **Test**: Verify functionality
5. **Audit**: Check access logs
6. **Document**: Record incident

### Lost Secret

1. **Check**: Password manager backup
2. **Regenerate**: Create new secret if needed
3. **Update**: All affected systems
4. **Notify**: Team members of change

## Monitoring

### Secret Usage Monitoring

- Track API key usage in provider dashboards
- Set up alerts for unusual activity
- Monitor GitHub Actions logs for secret exposure
- Review Vercel deployment logs

### Access Audits

- Regularly review who has access to secrets
- Audit GitHub repository collaborators
- Check Vercel team member access
- Review Docker registry permissions

## Compliance

### Data Protection

- Secrets contain sensitive data
- Follow GDPR/CCPA guidelines
- Implement data retention policies
- Document data processing activities

### SOC 2 / ISO 27001

- Maintain secret inventory
- Document secret lifecycle
- Implement access controls
- Regular security audits

## Support

For issues with secrets management:

1. Check this documentation first
2. Review `.github/workflows/secrets-reference.md`
3. Check provider documentation (OpenAI, GitHub, Vercel)
4. Contact team security lead for sensitive issues

## References

- [OpenAI API Keys](https://platform.openai.com/api-keys)
- [GitHub Actions Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Vercel Environment Variables](https://vercel.com/docs/projects/environment-variables)
- [Docker Secrets](https://docs.docker.com/engine/swarm/secrets/)
