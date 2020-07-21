FROM python:3.7.7

ENV DEBIAN_FRONTEND=noninteractive

# Install other dependencies
WORKDIR /code

COPY . .
RUN pip install -r requirements.txt

# Flask environment variables
ENV FLASK_APP=backend
ENV FLASK_ENV=production
EXPOSE 5000

CMD ["./scripts/runserver-prod.sh"]