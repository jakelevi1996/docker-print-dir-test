FROM python:3.6

# WORKDIR /app

COPY . .

CMD ["python", "printfs.py"]
