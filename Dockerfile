FROM python:3.8.5

ENV DEBIAN_FRONTEND=noninteractive

# Install other dependencies
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Flask environment variables
ENV FLASK_APP=risotto
ENV FLASK_ENV=production
EXPOSE 5000

CMD ["./scripts/runserver-prod.sh"]