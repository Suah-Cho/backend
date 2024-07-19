FROM python:3.9
WORKDIR /
COPY . .
RUN pip install -r requirements.txt
ENV TEST_SLAK_URL="https://"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]