FROM python:3.9


ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE library_project.settings

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint for the container
ENTRYPOINT ["/app/entrypoint.sh"]