<!-- HNG Internship Backend Projects -->

# HNG Internship Backend Projects

This repository contains two backend projects completed during my HNG Internship:

1. **Stage 0**: Public API for Basic Information
2. **Stage 1**: Number Classification API

---

## Stage 0: Public API for Basic Information

### Task Description
Develop a public API that returns the following information in JSON format:
- Your registered email address (used to register on the HNG12 Slack workspace).
- The current datetime as an ISO 8601 formatted timestamp.
- The GitHub URL of the project's codebase.

### API Endpoint
**Endpoint:** `/api/info`

**Response Format:**
```json
{
  "slack_email": "your-email@example.com",
  "current_datetime": "2025-02-13T12:00:00Z",
  "github_repo": "https://github.com/dideey/hngx-stage-0"
}
```

### How to Run Locally
```sh
# Clone the repo locally
git clone https://github.com/dideey/hngx-stage-0.git

# Navigate to the repo
cd stage0

# Create a virtual environment
python3 -m venv venv 

# Activate venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Run the local server
python3 manage.py runserver
```

[Navigate to the endpoint](http://127.0.0.1/api/api/)

[The API documentation](https://documenter.getpostman.com/view/36596982/2sAYX2PjbU)

## Backlink to Chosen Tech Stack
[Python Developers - HNG](https://hng.tech/hire/python-developers)

---

## Stage 1: Number Classification API

### Task Description
Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

### API Endpoint
**Endpoint:** `/api/number/{number}`

**Response Format:**
```json
{
  "number": 42,
  "is_even": true,
  "is_prime": false,
  "square_root": 6.48,
  "fun_fact": "42 is the answer to life, the universe, and everything!"
}
```

### How to Run Locally
```sh
# Clone the repo locally
git clone https://github.com/dideey/hngx-stage-0.git

# Navigate to the repo
cd stage1

# Create a virtual environment
python3 -m venv venv 

# Activate venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Run the local server
python3 manage.py runserver
```

[Navigate to the endpoint](http://127.0.0.1/api/number/42)

[The API documentation](https://documenter.getpostman.com/view/36596982/2sAYX2PjbU)

## Backlink to Chosen Tech Stack
[Python Developers - HNG](https://hng.tech/hire/python-developers)

### Resources
- [Fun Fact API](http://numbersapi.com/#42)
- [Parity in Mathematics](https://en.wikipedia.org/wiki/Parity_(mathematics))

---

## Contributing
Feel free to fork this repository and submit pull requests if you have improvements!

## License
This project is licensed under the MIT License.

---

## Contact
For any inquiries, reach out via email: [ndwarubradley@gmail.com](mailto:ndwarubradley@gmail.com).

