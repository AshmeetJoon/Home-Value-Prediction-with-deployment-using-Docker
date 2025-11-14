# 1. Start with an official Python base image
# Using "slim" makes your final image smaller
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file first
# This helps Docker cache the installed packages
COPY requirements.txt .

# 4. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all your project files into the container
# This includes app.py, xgb_california_model.pkl, etc.
COPY . .

# 6. Expose the port your app will run on
# We chose port 8000 in the app.py (using gunicorn)
EXPOSE 8000

# 7. Define the command to run your app
# This is the corrected line:
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
