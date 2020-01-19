FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

# set default port to 8080 as that is what firebase expects
ENV PORT 8080

COPY . .
CMD src/app.py