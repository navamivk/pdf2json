# pdf2json
Convert resume PDFs into a structured JSON format using the OpenAI API.

## Installation

1. Clone the repository
2. Create a virtual environment and activate it.
3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory with your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

Run the script with the following command, providing the path to the input resume PDF and the directory to store the output JSON file:

```bash
python main.py path_to_resume.pdf output_directory_path
