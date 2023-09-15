FROM python:3.8.2

COPY consum.py .

RUN pip install confluent-kafka 

CMD ["python", "consum.py"]
