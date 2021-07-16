FROM python:3.7
WORKDIR ./service3
RUN pip install Flask
COPY app.py .
EXPOSE 5003
ENTRYPOINT ["python3", "app.py"]