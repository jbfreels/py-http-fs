FROM python:3.9-alpine

COPY handler.py /

CMD ["python3", "handler.py"]