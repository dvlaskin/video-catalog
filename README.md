# Video catalog

## Description

The simple video catalog template website. You can add categories for video, and add video files using the built-in Django admin page. The thumbnails for video files are created automatically when the video is uploaded to the site. The Django doesn't allow you to rewind the video, for this feature use nginx as revers-proxy serves. All setting for docker-compose file that run application and nginx already done and you can find the file in the repo. 

## Installation

To set up and run this project locally, you'll need to have Docker installed. 

Follow local development:

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd <project-directory>/src
```

3. Create virtual environment
```bash
python -m venv .venv
```

4. Activate virtual environment
```bash
source venv/bin/activate
```

5. Install requirements
```bash
pip install -r requirements.txt
```

6. Apply the database migrations:

```bash
python manage.py migrate
```

7. Create admin user:

```bash
python manage.py createsuperuser
```

8. Run the application
```bash
python manage.py runserver
```

For run in docker:
```bash
docker-compose up -d
```

## Usage
Once the Docker container is running, you can access the application at http://localhost:8000.

## Project Structure
This project has the following structure:

- src/: This directory contains the Django application.
    - approot/: This directory contains the Django project settings.
    - mainapp/: This directory contains the video catalog app.
    - static/:  This directory contains static files for the Django application.
- nginx/: This directory contains the Nginx configuration files.
- Dockerfile: This file is used to build the Docker image for the Django application.
- docker-compose.yml: This file is used to define and run the Docker application.

## Contributing
Contributions are welcome! Please read the contributing guidelines before getting started.

## License
This project is licensed under the terms of the MIT license.