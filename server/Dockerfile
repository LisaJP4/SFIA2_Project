FROM python:latest
WORKDIR /server
COPY . .
RUN pip install flask requests flask_sqlalchemy pymysql
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]