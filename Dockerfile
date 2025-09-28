FROM python:3.11-slim
WORKDIR /app 
COPY . /app
# Update package lists and install AWS CLI
RUN apt update -y && apt install awscli -y 

RUN pip install -r requirements.txt 
CMD ["python3","app.py"]