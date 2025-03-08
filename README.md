# MongoDB Atlas Vector Search with n8n 

## Overview

This project demonstrates how to integrate MongoDB Atlas Vector Search with n8n, using Hugging Face embeddings for a more accessible and scalable AI-powered search solution.

## Features

- Uses Hugging Face (sBAAI/bge-base-en-v1.5) for text embeddings
- Integrates with MongoDB Atlas Vector Search
- Queries data using n8n’s HTTP Request Node
- Fully automated AI-powered retrieval workflow

## Getting Started

### Prerequisites

- Python 3.x and pip (usually bundled with Python installation)
- Git installed on your machine
- Virtualenv (install using pip):
  ```bash
  pip install virtualenv

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/derejehinsermu/n8n-MongoDB-Vector-Search.git

2. **Create and Activate a Virtual Environment**
   
    Navigate to the root directory of the project and create a virtual environment named 'venv', then activate it:
    ```sh
    cd n8n-MongoDB-Vector-Search
    python -m venv venv  | virtualenv venv
    source venv/bin/activate
    ```
3. **Install Requirements**\
   
    While inside the virtual environment, install the project requirements:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Embedding API:**
   ```bash
   python app.py


## Contributing

Contributions are welcome! 

3. For any questions or support, please contact derejehinsermu2@gmail.com.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
