FROM python:3.10-bullseye as builder

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app
RUN pip install --user -r requirements.txt


FROM python:3.10-slim-bullseye as release

ENV PYTHONUNBUFFERED 1
ENV PATH=/root/.local/bin:$PATH

COPY --from=builder /root/.local /root/.local
COPY . /app
WORKDIR app
EXPOSE 8501

CMD ["streamlit", "run", "src/app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
