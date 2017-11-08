FROM python:3

RUN ls
# Bundle app source
COPY  target/dist/houseTemperature-1.0.0/dist/houseTemperature-1.0.0-py3-none-any.whl /src/houseTemperature-1.0.0-py3-none-any.whl


# Install app dependencies
RUN pip install src/houseTemperature-1.0.0-py3-none-any.whl

run ls

EXPOSE 5000
CMD ["python", "-m","houseTemperature.run"]