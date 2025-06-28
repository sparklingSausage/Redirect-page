# Redirect-page
Simple page to keep track of your public/private/dns domains
This repository is not actively maintained, tho if you encounter a bug feel free to open a new issue

### What you'll need
- Basic understanding of Docker

### Structure
- Installation using [Docker](#Docker)
- Installation using [Python](#Python)


#### Docker
Run it using the [Docker Compose](docker-compose.yml)
```
services:
  domain-manager:
    container_name: domain-manager
    image: sparklingsausage/redirect:latest
    ports:
      - "5000:5000"
    volumes:
      - /path/to/domains.json:/app/domains.json
```

#### Python
Download the [python file](app.py) and install all [requirements](requirements.txt) using pip.
Run the it using python

```
python app.py
```

#### Screenshots
Outdated, gonna update soon
![](/screenshot.png?raw=true "Image of the UI")
