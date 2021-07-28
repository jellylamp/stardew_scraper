FROM python:3.7
ENV PYTHONPATH "${PYTHONPATH}:."

# Change the stop signal to sigint to more quickly stop this container.
STOPSIGNAL SIGINT

COPY requirements.txt .
RUN pip install -r requirements.txt

# set default port to 8080 as that is what firebase expects
ENV PORT 8080

COPY . .
CMD src/app.py