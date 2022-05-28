FROM python:3.9-alpine

COPY handler.py /

EXPOSE 80

CMD ["python3", "handler.py"]