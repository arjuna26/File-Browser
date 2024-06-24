## Ngrok Configuration Guide

### HTTPS Tunneling

Ngrok is a tool that creates secure tunnels to localhost, exposing local servers behind NATs and firewalls to the public internet over secure tunnels. When you run Ngrok, it creates a secure tunnel to your local server, allowing external users to access your local web server securely. Ngrok encrypts all traffic over the tunnel using TLS/SSL, making it secure against eavesdropping and tampering.

### Setting up an Ngrok Account and Creating a Free Domain

To use Ngrok, you need to sign up for an account on the Ngrok website. Follow these steps:

1. Go to [Ngrok](https://ngrok.com/) and sign up for an account.
2. After signing up, log in to your Ngrok account.
3. Once logged in, you can create a permanent domain by going to the [Domains](https://dashboard.ngrok.com/cloud-edge/domains) section of your Ngrok dashboard. Follow the instructions to set up your free domain.

## Credentials

### Creating config.py

To set up your credentials and the command to start the ngrok tunnel, you can create a `config.py` file in the same repository as the provided code. Here's how to create the `config.py` file:

1. Create a new file named `config.py` in your repository.
2. Add the following content to `config.py`:

```python
# config.py

NGROK_COMMAND = [
    "ngrok", "http", "--scheme=https", "https://localhost:5000",
    "--domain=your-free-domain.ngrok.io"
]

USERNAME = ' '
PASSWORD = ' '
```

Don't forget to replace `your-free-domain.ngrok.io` with your Ngrok domain obtained above. Note this ngrok tunnel will be redirecting requests from `localhost:5000`, feel free to change the port as needed.
