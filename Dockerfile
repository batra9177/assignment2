FROM python:3
WORKDIR /Elijah/Junk/python-docker
COPY Pipfile ./
RUN pip install --no-cache-dir pipenv && pipenv install
EXPOSE 5000
COPY *.py .
CMD [ "pipenv", "run", "python", "-m", "flask", "run", "--host=0.0.0.0" ]