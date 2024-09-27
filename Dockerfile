FROM python:3.10.11

WORKDIR /my_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=hello.py

# Command to run your application
CMD ["flask", "run", "--host=0.0.0.0"]
